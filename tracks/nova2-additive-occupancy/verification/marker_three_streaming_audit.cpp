// Exact bounded-memory streaming carrier audit for N1-CON-003.
//
// The program enumerates odd cores u with 3u | n! in increasing numerical
// order without materializing the complete divisor list. It records only
// prefix checkpoints and record-breaking consecutive gaps, then replays the
// N2-ADD-120 connected-core recursion exactly.

#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <queue>
#include <stdexcept>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

#include <boost/multiprecision/cpp_int.hpp>
#include <boost/rational.hpp>

using boost::multiprecision::cpp_int;
using Rational = boost::rational<cpp_int>;
using u128 = unsigned __int128;
using u64 = std::uint64_t;

namespace {

constexpr const char* kSchema = "nova2.marker-three-streaming-audit.v1";
constexpr const char* kNova1Commit = "ebb47ba436af554366d0f285119a769f31f9e561";

struct AuditError : std::runtime_error {
  using std::runtime_error::runtime_error;
};

std::string to_decimal(u128 value) {
  if (value == 0) return "0";
  std::string out;
  while (value > 0) {
    out.push_back(static_cast<char>('0' + value % 10));
    value /= 10;
  }
  std::reverse(out.begin(), out.end());
  return out;
}

u128 parse_u128(const std::string& text) {
  u128 value = 0;
  for (char ch : text) {
    if (ch < '0' || ch > '9') throw AuditError("invalid decimal integer");
    value = value * 10 + static_cast<unsigned>(ch - '0');
  }
  return value;
}

int ceil_rational(const Rational& value) {
  cpp_int quotient = value.numerator() / value.denominator();
  cpp_int remainder = value.numerator() % value.denominator();
  if (remainder != 0 && value.numerator() > 0) ++quotient;
  return quotient.convert_to<int>();
}

std::pair<Rational, Rational> atanh_log_bounds(
    int numerator, int denominator, int terms) {
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

std::pair<Rational, Rational> natural_log_bounds(int n, int terms) {
  if (n < 1) throw AuditError("n must be positive");
  if (n == 1) return {Rational(0), Rational(0)};
  int exponent = 0;
  while ((1LL << (exponent + 1)) <= n) ++exponent;
  int scale = 1 << exponent;
  auto [ln2_lower, ln2_upper] = atanh_log_bounds(2, 1, terms);
  auto [ratio_lower, ratio_upper] = atanh_log_bounds(n, scale, terms);
  return {
      Rational(exponent) * ln2_lower + ratio_lower,
      Rational(exponent) * ln2_upper + ratio_upper,
  };
}

std::pair<int, int> certified_log_parameters(int n) {
  for (int terms : {8, 12, 16, 24, 32, 48, 64, 96}) {
    auto [lower, upper] = natural_log_bounds(n, terms);
    int r_lower = ceil_rational(Rational(4) * lower);
    int r_upper = ceil_rational(Rational(4) * upper);
    int m_lower = ceil_rational(Rational(16) * lower * lower);
    int m_upper = ceil_rational(Rational(16) * upper * upper);
    if (r_lower == r_upper && m_lower == m_upper) {
      return {r_lower, m_lower};
    }
  }
  throw AuditError("could not certify r_n and M_n");
}

std::vector<int> primes_up_to(int n) {
  std::vector<bool> prime(n + 1, true);
  if (n >= 0) prime[0] = false;
  if (n >= 1) prime[1] = false;
  std::vector<int> out;
  for (int p = 2; p <= n; ++p) {
    if (!prime[p]) continue;
    out.push_back(p);
    if (static_cast<long long>(p) * p <= n) {
      for (int multiple = p * p; multiple <= n; multiple += p) {
        prime[multiple] = false;
      }
    }
  }
  return out;
}

int factorial_valuation(int n, int p) {
  int total = 0;
  while (n > 0) {
    n /= p;
    total += n;
  }
  return total;
}

cpp_int factorial_value(int n) {
  cpp_int value = 1;
  for (int k = 2; k <= n; ++k) value *= k;
  return value;
}

cpp_int integer_sqrt(const cpp_int& value) {
  if (value < 0) throw AuditError("integer square root of negative value");
  if (value == 0) return 0;
  cpp_int low = 0;
  cpp_int high =
      cpp_int(1) << ((boost::multiprecision::msb(value) + 2) / 2 + 1);
  while (low + 1 < high) {
    cpp_int middle = (low + high) / 2;
    if (middle * middle <= value) {
      low = middle;
    } else {
      high = middle;
    }
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

FactorData odd_core_factor_data(int n) {
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
        std::numeric_limits<u64>::max() /
            static_cast<u64>(exponent + 1)) {
      throw AuditError("odd-core divisor count exceeds uint64 range");
    }
    data.divisor_count *= static_cast<u64>(exponent + 1);
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
};

struct StreamSummary {
  u64 emitted_count = 0;
  u128 final_value = 0;
  std::size_t maximum_frontier = 0;
  std::vector<GapRecord> record_gaps;
  std::vector<u64> counts_at_bounds;
  std::vector<u128> last_values_at_bounds;
};

StreamSummary stream_odd_cores(
    const FactorData& factors,
    u128 maximum_bound,
    const std::vector<u128>& requested_bounds,
    std::size_t frontier_cap) {
  std::vector<std::pair<u128, std::size_t>> ordered_bounds;
  ordered_bounds.reserve(requested_bounds.size());
  for (std::size_t index = 0; index < requested_bounds.size(); ++index) {
    ordered_bounds.push_back({requested_bounds[index], index});
  }
  std::sort(ordered_bounds.begin(), ordered_bounds.end());

  StreamSummary summary;
  summary.counts_at_bounds.resize(requested_bounds.size(), 0);
  summary.last_values_at_bounds.resize(requested_bounds.size(), 0);

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
      std::size_t original_index = ordered_bounds[bound_index].second;
      summary.counts_at_bounds[original_index] = summary.emitted_count;
      summary.last_values_at_bounds[original_index] = previous;
      ++bound_index;
    }

    u128 gap = node.value - previous;
    if (gap > largest_gap) {
      largest_gap = gap;
      summary.record_gaps.push_back({gap, previous, node.value});
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
          static_cast<u64>(factors.exponents[index] + 1));
      if (exponent >= factors.exponents[index]) continue;
      unsigned prime = static_cast<unsigned>(factors.primes[index]);
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
    std::size_t original_index = ordered_bounds[bound_index].second;
    summary.counts_at_bounds[original_index] = summary.emitted_count;
    summary.last_values_at_bounds[original_index] = previous;
    ++bound_index;
  }

  summary.final_value = previous;
  return summary;
}

struct CarrierRow {
  int layer;
  u128 scale;
  u128 core_bound;
  u64 menu_size;
  u128 gap_threshold;
  u128 connected_max_core;
  u128 carrier_endpoint;
  bool has_blocking_gap;
  GapRecord blocking_gap{};
};

struct AuditResult {
  int n;
  int r;
  int M;
  int v2_factorial;
  int legal_layer_count;
  u128 X;
  u128 Y;
  u128 W;
  u64 odd_core_divisor_count;
  StreamSummary stream;
  std::vector<CarrierRow> rows;
  u128 carrier_endpoint;
  u128 occupied_through;
};

AuditResult audit_n(int n, std::size_t frontier_cap) {
  if (n < 3) throw AuditError("n must be at least 3");
  auto [r, M] = certified_log_parameters(n);
  FactorData factors = odd_core_factor_data(n);
  if (r - 1 > factors.v2_factorial) {
    throw AuditError("binary correction palette is not legal");
  }

  cpp_int factorial = factorial_value(n);
  cpp_int x_big = integer_sqrt(factorial);
  cpp_int y_big = x_big / 3;
  std::string x_text = x_big.convert_to<std::string>();
  std::string y_text = y_big.convert_to<std::string>();
  if (x_text.size() > 38 || y_text.size() > 38) {
    throw AuditError("endpoint exceeds unsigned 128-bit audit range");
  }
  u128 X = parse_u128(x_text);
  u128 Y = parse_u128(y_text);
  u128 W = ((static_cast<u128>(1) << r) - 3) / 3;

  int y_bit_length = boost::multiprecision::msb(y_big) + 1;
  int legal_layer_count =
      std::min({M, factors.v2_factorial + 1, y_bit_length});
  std::vector<u128> bounds;
  bounds.reserve(legal_layer_count);
  for (int layer = 1; layer <= legal_layer_count; ++layer) {
    bounds.push_back(Y >> (layer - 1));
  }

  StreamSummary stream =
      stream_odd_cores(factors, Y, bounds, frontier_cap);

  u128 carrier_endpoint = 0;
  std::vector<CarrierRow> rows;
  for (int layer = 1; layer <= legal_layer_count; ++layer) {
    u128 scale = static_cast<u128>(1) << (layer - 1);
    u128 gap_threshold = (carrier_endpoint + W + 1) / scale;
    u128 core_bound = bounds[layer - 1];

    auto iterator = std::upper_bound(
        stream.record_gaps.begin(), stream.record_gaps.end(), gap_threshold,
        [](u128 threshold, const GapRecord& record) {
          return threshold < record.gap;
        });

    bool blocked =
        iterator != stream.record_gaps.end() && iterator->right <= core_bound;
    u128 connected_max =
        blocked ? iterator->left : stream.last_values_at_bounds[layer - 1];
    carrier_endpoint += scale * connected_max;
    rows.push_back({
        layer,
        scale,
        core_bound,
        stream.counts_at_bounds[layer - 1],
        gap_threshold,
        connected_max,
        carrier_endpoint,
        blocked,
        blocked ? *iterator : GapRecord{},
    });
    if (carrier_endpoint + W >= Y) break;
  }

  return {
      n,
      r,
      M,
      factors.v2_factorial,
      legal_layer_count,
      X,
      Y,
      W,
      factors.divisor_count,
      std::move(stream),
      std::move(rows),
      carrier_endpoint,
      carrier_endpoint + W,
  };
}

void print_json(const AuditResult& result) {
  std::cout << "{\n";
  std::cout << "  \"schema\": \"" << kSchema << "\",\n";
  std::cout << "  \"result_id\": \"N2-FIN-203\",\n";
  std::cout << "  \"result_class\": \"finite certificate\",\n";
  std::cout << "  \"source\": {\n";
  std::cout
      << "    \"repository\": \"Lumathpolgar/erdos18-factorial-program\",\n";
  std::cout << "    \"nova1_branch\": \"nova/factorial-structure\",\n";
  std::cout << "    \"nova1_commit\": \"" << kNova1Commit << "\",\n";
  std::cout << "    \"nova1_construction\": \"N1-CON-003\",\n";
  std::cout << "    \"nova2_theorems\": [\"N2-ADD-119\", "
               "\"N2-ADD-120\", \"N2-ADD-121\"]\n";
  std::cout << "  },\n";
  std::cout << "  \"n\": " << result.n << ",\n";
  std::cout << "  \"r\": " << result.r << ",\n";
  std::cout << "  \"M\": " << result.M << ",\n";
  std::cout << "  \"v2_factorial\": " << result.v2_factorial << ",\n";
  std::cout << "  \"legal_layer_count\": " << result.legal_layer_count
            << ",\n";
  std::cout << "  \"X\": " << to_decimal(result.X) << ",\n";
  std::cout << "  \"Y\": " << to_decimal(result.Y) << ",\n";
  std::cout << "  \"W\": " << to_decimal(result.W) << ",\n";
  std::cout << "  \"odd_core_divisor_count\": "
            << result.odd_core_divisor_count << ",\n";
  std::cout << "  \"stream\": {\n";
  std::cout << "    \"emitted_count_through_Y\": "
            << result.stream.emitted_count << ",\n";
  std::cout << "    \"final_value_through_Y\": "
            << to_decimal(result.stream.final_value) << ",\n";
  std::cout << "    \"record_gap_count\": "
            << result.stream.record_gaps.size() << ",\n";
  std::cout << "    \"maximum_frontier\": "
            << result.stream.maximum_frontier << "\n";
  std::cout << "  },\n";
  std::cout << "  \"layers_used\": " << result.rows.size() << ",\n";
  std::cout << "  \"carrier_endpoint\": "
            << to_decimal(result.carrier_endpoint) << ",\n";
  std::cout << "  \"occupied_through\": "
            << to_decimal(result.occupied_through) << ",\n";
  if (result.occupied_through >= result.Y) {
    std::cout << "  \"margin\": "
              << to_decimal(result.occupied_through - result.Y) << ",\n";
    std::cout << "  \"deficit\": 0,\n";
  } else {
    std::cout << "  \"margin\": 0,\n";
    std::cout << "  \"deficit\": "
              << to_decimal(result.Y - result.occupied_through) << ",\n";
  }
  std::cout << "  \"reaches_full_endpoint\": "
            << (result.occupied_through >= result.Y ? "true" : "false")
            << ",\n";
  std::cout << "  \"term_bound\": " << result.r + result.rows.size()
            << ",\n";
  std::cout << "  \"rows\": [\n";
  for (std::size_t index = 0; index < result.rows.size(); ++index) {
    const CarrierRow& row = result.rows[index];
    std::cout << "    {\n";
    std::cout << "      \"t\": " << row.layer << ",\n";
    std::cout << "      \"scale\": " << to_decimal(row.scale) << ",\n";
    std::cout << "      \"core_bound\": " << to_decimal(row.core_bound)
              << ",\n";
    std::cout << "      \"menu_size\": " << row.menu_size << ",\n";
    std::cout << "      \"gap_threshold\": "
              << to_decimal(row.gap_threshold) << ",\n";
    std::cout << "      \"connected_max_core\": "
              << to_decimal(row.connected_max_core) << ",\n";
    std::cout << "      \"carrier_endpoint\": "
              << to_decimal(row.carrier_endpoint) << ",\n";
    if (row.has_blocking_gap) {
      std::cout << "      \"first_blocking_gap\": {\n";
      std::cout << "        \"left_core\": "
                << to_decimal(row.blocking_gap.left) << ",\n";
      std::cout << "        \"right_core\": "
                << to_decimal(row.blocking_gap.right) << ",\n";
      std::cout << "        \"gap\": " << to_decimal(row.blocking_gap.gap)
                << "\n";
      std::cout << "      }\n";
    } else {
      std::cout << "      \"first_blocking_gap\": null\n";
    }
    std::cout << "    }"
              << (index + 1 == result.rows.size() ? "\n" : ",\n");
  }
  std::cout << "  ]\n";
  std::cout << "}\n";
}

}  // namespace

int main(int argc, char** argv) {
  int n = 46;
  std::size_t frontier_cap = 5'000'000;
  for (int index = 1; index < argc; ++index) {
    std::string argument = argv[index];
    if (argument == "--n" && index + 1 < argc) {
      n = std::stoi(argv[++index]);
    } else if (argument == "--frontier-cap" && index + 1 < argc) {
      frontier_cap =
          static_cast<std::size_t>(std::stoull(argv[++index]));
    } else {
      std::cerr << "unknown or incomplete argument: " << argument << "\n";
      return 2;
    }
  }

  try {
    AuditResult result = audit_n(n, frontier_cap);
    print_json(result);
    return 0;
  } catch (const std::bad_alloc&) {
    std::cerr
        << "{\"status\":\"FAIL\",\"classification\":\"resource limit\","
           "\"error\":\"memory allocation failed\"}\n";
    return 1;
  } catch (const AuditError& error) {
    std::cerr
        << "{\"status\":\"FAIL\",\"classification\":\"audit error\","
           "\"error\":\""
        << error.what() << "\"}\n";
    return 1;
  }
}
