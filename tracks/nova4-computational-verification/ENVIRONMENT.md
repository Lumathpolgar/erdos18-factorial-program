# Nova 4 Environment

Date: 2026-07-15

Result class: `exact finite theorem audit`

## Runtime

```text
Python: 3.13.5
Implementation: CPython
Platform: Linux 4.4.0 x86_64 with glibc 2.41
Arithmetic: Python arbitrary-precision integers
External runtime dependencies: none
```

The implementation and complete test suite use only the Python standard library.

## Deterministic setup

From the repository root:

```bash
cd tracks/nova4-computational-verification
python3 --version
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

Generate the published exact dataset and representation certificates:

```bash
PYTHONPATH=src python3 src/replay.py generate-dataset \
  --n-min 1 \
  --n-max 13 \
  --output data/factorial_half_range_profiles_n1_n13.json \
  --certificate-dir certificates
```

Verify every representation certificate without trusting producer metadata:

```bash
PYTHONPATH=src python3 src/replay.py verify-tree certificates
```

Recompute and verify the complete dataset:

```bash
PYTHONPATH=src python3 src/replay.py verify-dataset \
  data/factorial_half_range_profiles_n1_n13.json
```

Verify one certificate:

```bash
PYTHONPATH=src python3 src/replay.py verify \
  certificates/n8_target155_optimal.json
```

## Determinism

- Prime generation is deterministic.
- Divisor generation is sorted and deterministic.
- Dynamic programming tie breaking is deterministic.
- Certificate JSON is canonicalized with sorted keys and sorted numerical terms.
- Dataset JSON uses stable separators and sorted keys.
- No randomized procedure is used in this checkpoint.
- No solver status, cached sum, or cached term count is trusted.

## Fail-closed behavior

Malformed JSON, wrong schemas, noninteger arithmetic fields, nonpositive terms, illegal divisors, duplicate numerical values, wrong sums, exceeded term bounds, invalid target ranges, checksum mismatches, or independent-method disagreements cause a nonzero replay result.

Timeouts and external process termination are reported as `unknown due to resource limits`, never as a false statement.

## Clean-room limitation

The container had no working network path for a local Git clone and no installed GitHub CLI. Repository reads and writes therefore use the connected GitHub application, while all code execution occurs in the local clean directory. This does not change the branch policy or arithmetic verification standard.
