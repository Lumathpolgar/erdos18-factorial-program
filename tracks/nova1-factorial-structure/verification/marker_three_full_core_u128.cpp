#include <algorithm>
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/rational.hpp>
#include <cstdint>
#include <cstdlib>
#include <functional>
#include <iostream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

using boost::multiprecision::cpp_int;
using Rational = boost::rational<cpp_int>;
using U128 = unsigned __int128;

struct AuditError : std::runtime_error {
    using std::runtime_error::runtime_error;
};

static std::string to_string_u128(U128 x) {
    if (x == 0) return "0";
    std::string s;
    while (x > 0) {
        s.push_back(char('0' + unsigned(x % 10)));
        x /= 10;
    }
    std::reverse(s.begin(), s.end());
    return s;
}

static U128 parse_u128(const std::string& s) {
    U128 x = 0;
    for (char c : s) {
        if (c < '0' || c > '9') throw AuditError("invalid decimal integer");
        U128 digit = U128(c - '0');
        U128 next = x * 10 + digit;
        if (next < x) throw AuditError("u128 overflow");
        x = next;
    }
    return x;
}

static unsigned bit_length(U128 x) {
    unsigned bits = 0;
    while (x) {
        ++bits;
        x >>= 1;
    }
    return bits;
}

static cpp_int ceil_rational(const Rational& x) {
    cpp_int q = x.numerator() / x.denominator();
    if (x.numerator() % x.denominator() != 0) ++q;
    return q;
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
        partial += power / cpp_int(2 * j + 1);
        power *= z2;
    }
    Rational lower = cpp_int(2) * partial;
    Rational tail = cpp_int(2) * power /
        (cpp_int(2 * terms + 1) * (Rational(1) - z2));
    return {lower, lower + tail};
}

static std::pair<int, int> certified_log_parameters(int n) {
    const int term_options[] = {8, 12, 16, 24, 32, 48, 64, 96};
    int exponent = 0;
    while ((1 << (exponent + 1)) <= n) ++exponent;
    int scale = 1 << exponent;

    for (int terms : term_options) {
        auto ln2 = atanh_log_bounds(2, 1, terms);
        auto ratio = atanh_log_bounds(n, scale, terms);
        Rational lower = cpp_int(exponent) * ln2.first + ratio.first;
        Rational upper = cpp_int(exponent) * ln2.second + ratio.second;
        cpp_int r_lo = ceil_rational(cpp_int(4) * lower);
        cpp_int r_hi = ceil_rational(cpp_int(4) * upper);
        cpp_int m_lo = ceil_rational(cpp_int(16) * lower * lower);
        cpp_int m_hi = ceil_rational(cpp_int(16) * upper * upper);
        if (r_lo == r_hi && m_lo == m_hi) {
            return {r_lo.convert_to<int>(), m_lo.convert_to<int>()};
        }
    }
    throw AuditError("could not certify logarithmic parameters");
}

static std::vector<int> primes_up_to(int n) {
    std::vector<bool> sieve(n + 1, true);
    sieve[0] = false;
    sieve[1] = false;
    for (int p = 2; p * p <= n; ++p) {
        if (!sieve[p]) continue;
        for (int q = p * p; q <= n; q += p) sieve[q] = false;
    }
    std::vector<int> primes;
    for (int p = 2; p <= n; ++p) {
        if (sieve[p]) primes.push_back(p);
    }
    return primes;
}

static int factorial_valuation(int n, int p) {
    int total = 0;
    while (n) {
        n /= p;
        total += n;
    }
    return total;
}

static cpp_int factorial(int n) {
    cpp_int value = 1;
    for (int k = 2; k <= n; ++k) value *= k;
    return value;
}

static cpp_int integer_sqrt(const cpp_int& n) {
    if (n < 0) throw AuditError("negative square-root input");
    if (n == 0) return 0;
    unsigned shift = (boost::multiprecision::msb(n) + 2) / 2;
    cpp_int x = cpp_int(1) << shift;
    while (true) {
        cpp_int y = (x + n / x) / 2;
        if (y >= x) return x;
        x = y;
    }
}

struct LayerRow {
    int t;
    U128 scale;
    U128 core_bound;
    U128 threshold;
    U128 connected_max;
    U128 endpoint;
    std::size_t connected_count;
    bool blocked;
    U128 left_core;
    U128 right_core;
    U128 blocking_gap;
};

int main(int argc, char** argv) {
    try {
        int n = 46;
        std::size_t max_values = 100000000;
        for (int i = 1; i < argc; ++i) {
            std::string arg = argv[i];
            if (arg == "--n" && i + 1 < argc) {
                n = std::stoi(argv[++i]);
            } else if (arg == "--max-values" && i + 1 < argc) {
                max_values = std::stoull(argv[++i]);
            } else {
                throw AuditError(
                    "usage: marker_three_full_core_u128 --n N [--max-values K]"
                );
            }
        }
        if (n < 12 || n > 50) {
            throw AuditError("certified u128 verifier range is 12<=n<=50");
        }

        auto [r, M] = certified_log_parameters(n);
        int v2 = factorial_valuation(n, 2);
        cpp_int X_big = integer_sqrt(factorial(n));
        cpp_int Y_big = X_big / 3;
        std::string Y_text = Y_big.convert_to<std::string>();
        if (Y_text.size() > 38) {
            throw AuditError("quotient endpoint exceeds u128 range");
        }
        U128 Y = parse_u128(Y_text);
        U128 W = ((U128(1) << r) - 3) / 3;

        std::vector<std::pair<int, int>> prime_exponents;
        cpp_int total_divisor_count = 1;
        for (int p : primes_up_to(n)) {
            if (p == 2) continue;
            int e = factorial_valuation(n, p) - (p == 3 ? 1 : 0);
            if (e < 0) throw AuditError("reserved factor 3 unavailable");
            if (e > 0) {
                prime_exponents.push_back({p, e});
                total_divisor_count *= (e + 1);
            }
        }

        std::vector<U128> cores;
        std::size_t reserve_count = max_values;
        if (total_divisor_count <= cpp_int(max_values)) {
            reserve_count = total_divisor_count.convert_to<std::size_t>();
        }
        cores.reserve(reserve_count);

        bool limit_exceeded = false;
        std::function<void(std::size_t, U128)> generate =
            [&](std::size_t index, U128 value) {
                if (limit_exceeded) return;
                if (index == prime_exponents.size()) {
                    if (cores.size() >= max_values) {
                        limit_exceeded = true;
                        return;
                    }
                    cores.push_back(value);
                    return;
                }
                int p = prime_exponents[index].first;
                int e = prime_exponents[index].second;
                U128 current = value;
                for (int a = 0; a <= e; ++a) {
                    generate(index + 1, current);
                    if (limit_exceeded || a == e || current > Y / U128(p)) break;
                    current *= U128(p);
                }
            };

        generate(0, U128(1));
        if (limit_exceeded) {
            throw AuditError("truncated core count exceeds --max-values");
        }
        std::sort(cores.begin(), cores.end());
        if (std::adjacent_find(cores.begin(), cores.end()) != cores.end()) {
            throw AuditError("duplicate core generated");
        }

        int legal_layers = std::min({M, v2 + 1, int(bit_length(Y))});
        U128 E = 0;
        std::vector<LayerRow> rows;
        for (int t = 1; t <= legal_layers; ++t) {
            U128 scale = U128(1) << (t - 1);
            U128 bound = Y / scale;
            auto menu_end = std::upper_bound(cores.begin(), cores.end(), bound);
            U128 threshold = (E + W + 1) / scale;
            U128 previous = 0;
            U128 connected_max = 0;
            std::size_t connected_count = 0;
            bool blocked = false;
            U128 right = 0;
            U128 gap = 0;

            for (auto it = cores.begin(); it != menu_end; ++it) {
                U128 core = *it;
                U128 current_gap = core - previous;
                if (current_gap <= threshold) {
                    connected_max = core;
                    previous = core;
                    ++connected_count;
                } else {
                    blocked = true;
                    right = core;
                    gap = current_gap;
                    break;
                }
            }

            E += scale * connected_max;
            rows.push_back({
                t,
                scale,
                bound,
                threshold,
                connected_max,
                E,
                connected_count,
                blocked,
                previous,
                right,
                gap,
            });
            if (E + W >= Y) break;
        }

        U128 occupied = E + W;
        std::cout << "schema=nova1.marker-three-full-core-u128.v1\n";
        std::cout << "result_class=finite certificate\n";
        std::cout << "n=" << n << "\n";
        std::cout << "r=" << r << "\n";
        std::cout << "M=" << M << "\n";
        std::cout << "v2_factorial=" << v2 << "\n";
        std::cout << "Y=" << to_string_u128(Y) << "\n";
        std::cout << "W=" << to_string_u128(W) << "\n";
        std::cout << "total_odd_core_divisor_count="
                  << total_divisor_count << "\n";
        std::cout << "truncated_generated_core_count="
                  << cores.size() << "\n";
        std::cout << "layers_used=" << rows.size() << "\n";

        for (const auto& row : rows) {
            std::cout << "layer=" << row.t
                      << ",scale=" << to_string_u128(row.scale)
                      << ",core_bound=" << to_string_u128(row.core_bound)
                      << ",gap_threshold=" << to_string_u128(row.threshold)
                      << ",connected_max_core=" << to_string_u128(row.connected_max)
                      << ",connected_count=" << row.connected_count
                      << ",carrier_endpoint=" << to_string_u128(row.endpoint);
            if (row.blocked) {
                std::cout << ",first_blocking_left="
                          << to_string_u128(row.left_core)
                          << ",first_blocking_right="
                          << to_string_u128(row.right_core)
                          << ",first_blocking_gap="
                          << to_string_u128(row.blocking_gap);
            } else {
                std::cout << ",first_blocking_gap=NONE";
            }
            std::cout << "\n";
        }

        std::cout << "carrier_endpoint=" << to_string_u128(E) << "\n";
        std::cout << "occupied_through=" << to_string_u128(occupied) << "\n";
        std::cout << "margin="
                  << (occupied >= Y
                          ? to_string_u128(occupied - Y)
                          : "-" + to_string_u128(Y - occupied))
                  << "\n";
        std::cout << "reaches_full_endpoint="
                  << (occupied >= Y ? "true" : "false") << "\n";
        return occupied >= Y ? 0 : 2;
    } catch (const std::exception& exc) {
        std::cerr << "FAIL: " << exc.what() << "\n";
        return 1;
    }
}
