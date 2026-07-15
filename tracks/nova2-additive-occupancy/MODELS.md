# Nova 2 Additive Model Registry

## Model A: Rainbow convolution

Status: `OPEN`

Choose at most one divisor from each labeled layer and study the support and local mass of the resulting convolution. Required inputs include layer supports, collision rules, gcd, moments, and correction radius.

## Model B: Exponentially tilted convolution

Status: `OPEN`

For each target `x`, tilt layer measures so the total mean is near `x`. Required proof obligations:

- uniform existence of the tilt;
- variance lower and upper bounds;
- lattice compatibility;
- local mass lower bound in the target window;
- deterministic conversion from positive mass to a valid representation.

## Model C: Restricted sumset growth

Status: `OPEN`

Use additive-combinatorial growth of labeled or restricted sumsets. Required proof obligations:

- no hidden modular obstruction;
- quantitative interval or window inclusion;
- compatibility with one-per-layer or bounded-per-packet restrictions;
- final term count.

## Model D: Hybrid coarse-to-local occupancy

Status: `OPEN`

Use a global sumset for coarse placement and a disjoint correction family for local completion. The coarse and correction term sets must be numerically disjoint.

## Model evaluation fields

For every model record:

1. frozen layer input;
2. support range;
3. term budget;
4. expected number of profiles;
5. collision multiplicity;
6. lattice span;
7. variance or entropy;
8. window width;
9. endpoint behavior;
10. exact missing theorem.
