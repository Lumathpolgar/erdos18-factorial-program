// Exact streaming connected-prefix audit for N1-CON-003.
//
// This independently reconstructs Nova 2 theorem N2-ADD-121 and stores
// record-gap left counts so that both the connected maximum u_t^* and the
// connected-prefix cardinality K_t are recovered exactly.

#include <algorithm>
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/rational.hpp>
#include <cstdint>
#include <iostream>
#include <limits>
#include <queue>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

using boost::multiprecision::cpp_int;
using Rational = boost::rational<cpp_int>;
using u128 = unsigned __int128;
using u64 = std::uint64_t;

struct AuditError : std::runtime_error {
    using std::runtime_error::runtime_error;
};

static std::string decimal(u128 value) {
    if (value == 0) return "0";
    std::string out;
    while (value > 0) {
        out.push_back(static_cast<char>('0' + unsigned(value % 10)));
        value /= 10;
    }
    std::reverse(out.begin(), out.end());
    return out;
}

static u128 parse_u128(const std::string& text) {
    u128 value = 0;
    for (char ch : text) {
        if (ch < '0' || ch > '9') throw AuditError("invalid decimal integer");
        u128 old = value;
        value = value * 10 + unsigned(ch - '0');
        if (value < old) throw AuditError("unsigned 128-bit overflow");
    }
    return value;
}

static int ceil_rational(const Rational& value) {
    cpp_int quotient = value.numerator() / value.denominator();
    if (value.numerator() % value.denominator() != 0 && value.numerator() > 0) {
        ++quotient;
    }
    return quotient.convert_to<int>();
}

static std::pair<Rational, Rational> atanh_log_bounds(
    int numerator,
    int denominator,
    int terms
) {
    if (numerator < denominator || numerator > 2 * denominator) {
        throw AuditError("log ratio must lie in [1,2]");
    }
    if (numerator == denominator) return {Rational(0), Rational(0)};
    Rational z(cpp_int(numerator - denominator), cpp_int(numerator + denominator));
    Rational z2 = z * z;
    Rational power = z;
    Rational partial(0);
    for (int j = 0; j < terms; ++j) {
        partial += power / Rational(2 * j + 1);
        power *= z2;
    }
    Rational lower = 2 * partial;
    Rational tail =
        2 * power / (Rational(2 * terms + 1) * (Rational(1) - z2));
    return {lower, lower + tail};
}

static std::pair<int, int> certified_log_parameters(int n) {
    int exponent = 0;
    while ((1LL << (exponent + 1)) <= n) ++exponent;
    int scale = 1 << exponent;
    for (int terms : {8, 12, 16, 24, 32, 48, 64, 96}) {
        auto ln2 = atanh_log_bounds(2, 1, terms);
        auto ratio = atanh_log_bounds(n, scale, terms);
        Rational lower = Rational(exponent) * ln2.first + ratio.first;
        Rational upper = Rational(exponent) * ln2.second + ratio.second;
        int r_lower = ceil_rational(Rational(4) * lower);
        int r_upper = ceil_rational(Rational(4) * upper);
        int m_lower = ceil_rational(Rational(16) * lower * lower);
        int m_upper = ceil_rational(Rational(16) * upper * upper);
        if (r_lower == r_upper && m_lower == m_upper) {
            return {r_lower, m_lower};
        }
    }
    throw AuditError("could not certify logarithmic parameters");
}

static std::vector<int> primes_up_to(int n) {
    std::vector<bool> is_prime(n + 1, true);
    is_prime[0] = false;
    is_prime[1] = false;
    std::vector<int> primes;
    for (int p = 2; p <= n; ++p) {
        if (!is_prime[p]) continue;
        primes.push_back(p);
        if (1LL * p * p <= n) {
            for (int q = p * p; q <= n; q += p) is_prime[q] = false;
        }
    }
    return primes;
}

static int factorial_valuation(int n, int p) {
    int total = 0;
    while (n > 0) {
        n /= p;
        total += n;
    }
    return total;
}

static cpp_int factorial_value(int n) {
    cpp_int value = 1;
    for (int k = 2; k <= n; ++k) value *= k;
    return value;
}

static cpp_int integer_sqrt(const cpp_int& value) {
    cpp_int low = 0;
    cpp_int high = cpp_int(1) << ((boost::multiprecision::msb(value) + 2) / 2 + 1);
    while (low + 1 < high) {
        cpp_int middle = (low + high) / 2;
        if (middle * middle <= value) low = middle;
        else high = middle;
    }
    return low;
}

struct FactorData {
    std::vector<int> primes;
    std::vector<int> exponents;
    std::vector<u64> strides;
    u64 divisor_count = 1;
    int v2_factorial = 0;
};

static FactorData odd_core_factor_data(int n) {
    FactorData data;
    for (int p : primes_up_to(n)) {
        int exponent = factorial_valuation(n, p);
        if (p == 2) {
            data.v2_factorial = exponent;
            continue;
        }
        if (p == 3) --exponent;
        if (exponent <= 0) continue;
        data.primes.push_back(p);
        data.exponents.push_back(exponent);
        data.strides.push_back(data.divisor_count);
        if (data.divisor_count >
            std::numeric_limits<u64>::max() / u64(exponent + 1)) {
            throw AuditError("odd-core divisor count exceeds uint64 range");
        }
        data.divisor_count *= u64(exponent + 1);
    }
    return data;
}

struct HeapNode {
    u128 value;
    u64 exponent_code;
    std::uint8_t largest_nonzero_index;
};

struct HeapGreater {
    bool operator()(const HeapNode& left, const HeapNode& right) const {
        if (left.value != right.value) return left.value > right.value;
        if (left.exponent_code != right.exponent_code) {
            return left.exponent_code > right.exponent_code;
        }
        return left.largest_nonzero_index > right.largest_nonzero_index;
    }
};

struct GapRecord {
    u128 gap;
    u128 left;
    u128 right;
    u64 left_count;
};

struct StreamSummary {
    u64 emitted_count = 0;
    u128 final_value = 0;
    std::size_t maximum_frontier = 0;
    std::vector<GapRecord> record_gaps;
    std::vector<u64> counts_at_bounds;
    std::vector<u128> last_values_at_bounds;
};

static StreamSummary stream_odd_cores(
    const FactorData& factors,
    u128 maximum_bound,
    const std::vector<u128>& requested_bounds,
    std::size_t frontier_cap
) {
    std::vector<std::pair<u128, std::size_t>> ordered_bounds;
    for (std::size_t index = 0; index < requested_bounds.size(); ++index) {
        ordered_bounds.push_back({requested_bounds[index], index});
    }
    std::sort(ordered_bounds.begin(), ordered_bounds.end());

    StreamSummary summary;
    summary.counts_at_bounds.assign(requested_bounds.size(), 0);
    summary.last_values_at_bounds.assign(requested_bounds.size(), 0);

    std::priority_queue<HeapNode, std::vector<HeapNode>, HeapGreater> frontier;
    frontier.push({1, 0, std::numeric_limits<std::uint8_t>::max()});
    summary.maximum_frontier = 1;

    u128 previous = 0;
    u128 largest_gap = 0;
    std::size_t bound_index = 0;

    while (!frontier.empty()) {
        HeapNode node = frontier.top();
        frontier.pop();
        if (node.value > maximum_bound) break;

        while (bound_index < ordered_bounds.size() &&
               ordered_bounds[bound_index].first < node.value) {
            std::size_t original = ordered_bounds[bound_index].second;
            summary.counts_at_bounds[original] = summary.emitted_count;
            summary.last_values_at_bounds[original] = previous;
            ++bound_index;
        }

        u128 gap = node.value - previous;
        if (gap > largest_gap) {
            largest_gap = gap;
            summary.record_gaps.push_back(
                {gap, previous, node.value, summary.emitted_count}
            );
        }

        previous = node.value;
        ++summary.emitted_count;

        int start_index =
            node.largest_nonzero_index ==
                    std::numeric_limits<std::uint8_t>::max()
                ? 0
                : static_cast<int>(node.largest_nonzero_index);

        for (int index = start_index;
             index < static_cast<int>(factors.primes.size()); ++index) {
            int exponent = static_cast<int>(
                (node.exponent_code / factors.strides[index]) %
                u64(factors.exponents[index] + 1)
            );
            if (exponent >= factors.exponents[index]) continue;
            unsigned prime = unsigned(factors.primes[index]);
            if (node.value > maximum_bound / prime) continue;
            frontier.push({
                node.value * prime,
                node.exponent_code + factors.strides[index],
                static_cast<std::uint8_t>(index),
            });
        }

        summary.maximum_frontier =
            std::max(summary.maximum_frontier, frontier.size());
        if (summary.maximum_frontier > frontier_cap) {
            throw AuditError("stream frontier exceeded declared cap");
        }
    }

    while (bound_index < ordered_bounds.size()) {
        std::size_t original = ordered_bounds[bound_index].second;
        summary.counts_at_bounds[original] = summary.emitted_count;
        summary.last_values_at_bounds[original] = previous;
        ++bound_index;
    }
    summary.final_value = previous;
    return summary;
}

int main(int argc, char** argv) {
    try {
        int n = 51;
        std::size_t frontier_cap = 30'000'000;
        if (argc > 1) n = std::stoi(argv[1]);
        if (argc > 2) frontier_cap = std::stoull(argv[2]);

        auto [r, M] = certified_log_parameters(n);
        FactorData factors = odd_core_factor_data(n);
        cpp_int X_big = integer_sqrt(factorial_value(n));
        cpp_int Y_big = X_big / 3;
        std::string Y_text = Y_big.convert_to<std::string>();
        if (Y_text.size() > 38) throw AuditError("quotient endpoint exceeds u128");
        u128 Y = parse_u128(Y_text);
        u128 W = ((u128(1) << r) - 3) / 3;

        int bit_length = boost::multiprecision::msb(Y_big) + 1;
        int legal_layers = std::min({M, factors.v2_factorial + 1, bit_length});
        std::vector<u128> bounds;
        for (int t = 1; t <= legal_layers; ++t) bounds.push_back(Y >> (t - 1));

        StreamSummary stream =
            stream_odd_cores(factors, Y, bounds, frontier_cap);

        u128 endpoint = 0;
        int used = 0;
        std::cout << "schema=nova1.marker-three-streaming-prefix-u128.v1\n";
        std::cout << "result_class=finite certificate\n";
        std::cout << "n=" << n << "\n";
        std::cout << "r=" << r << "\n";
        std::cout << "M=" << M << "\n";
        std::cout << "v2_factorial=" << factors.v2_factorial << "\n";
        std::cout << "Y=" << decimal(Y) << "\n";
        std::cout << "W=" << decimal(W) << "\n";
        std::cout << "total_odd_core_divisor_count="
                  << factors.divisor_count << "\n";
        std::cout << "emitted_count_through_Y=" << stream.emitted_count << "\n";
        std::cout << "final_value_through_Y=" << decimal(stream.final_value) << "\n";
        std::cout << "record_gap_count=" << stream.record_gaps.size() << "\n";
        std::cout << "maximum_frontier=" << stream.maximum_frontier << "\n";

        for (int t = 1; t <= legal_layers; ++t) {
            u128 scale = u128(1) << (t - 1);
            u128 threshold = (endpoint + W + 1) / scale;
            u128 bound = bounds[t - 1];
            auto iterator = std::upper_bound(
                stream.record_gaps.begin(),
                stream.record_gaps.end(),
                threshold,
                [](u128 value, const GapRecord& record) {
                    return value < record.gap;
                }
            );
            bool blocked =
                iterator != stream.record_gaps.end() && iterator->right <= bound;
            u128 connected_max =
                blocked ? iterator->left : stream.last_values_at_bounds[t - 1];
            u64 connected_count =
                blocked ? iterator->left_count : stream.counts_at_bounds[t - 1];
            endpoint += scale * connected_max;
            ++used;

            std::cout << "layer=" << t
                      << ",scale=" << decimal(scale)
                      << ",core_bound=" << decimal(bound)
                      << ",menu_size=" << stream.counts_at_bounds[t - 1]
                      << ",gap_threshold=" << decimal(threshold)
                      << ",connected_max_core=" << decimal(connected_max)
                      << ",connected_count=" << connected_count
                      << ",carrier_endpoint=" << decimal(endpoint);
            if (blocked) {
                std::cout << ",first_blocking_left=" << decimal(iterator->left)
                          << ",first_blocking_right=" << decimal(iterator->right)
                          << ",first_blocking_gap=" << decimal(iterator->gap);
            } else {
                std::cout << ",first_blocking_gap=NONE";
            }
            std::cout << "\n";
            if (endpoint + W >= Y) break;
        }

        u128 occupied = endpoint + W;
        std::cout << "layers_used=" << used << "\n";
        std::cout << "carrier_endpoint=" << decimal(endpoint) << "\n";
        std::cout << "occupied_through=" << decimal(occupied) << "\n";
        std::cout << "margin="
                  << (occupied >= Y
                          ? decimal(occupied - Y)
                          : std::string("-") + decimal(Y - occupied))
                  << "\n";
        std::cout << "reaches_full_endpoint="
                  << (occupied >= Y ? "true" : "false") << "\n";
        std::cout << "term_bound=" << r + used << "\n";
        return occupied >= Y ? 0 : 2;
    } catch (const std::bad_alloc&) {
        std::cerr << "FAIL: memory allocation failed\n";
        return 1;
    } catch (const std::exception& error) {
        std::cerr << "FAIL: " << error.what() << "\n";
        return 1;
    }
}
