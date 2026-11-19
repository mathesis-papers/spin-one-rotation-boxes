"""Exact algebra for the lower-spin, dimension and normalization corollaries."""
from itertools import combinations, combinations_with_replacement

import sympy

phase = sympy.Symbol('phase', nonzero=True)
constant, cosine, sine = sympy.symbols('constant cosine sine', real=True)
effect = sympy.Matrix([
    [constant, cosine - sympy.I * sine],
    [cosine + sympy.I * sine, constant],
])
vector = sympy.Matrix([1, phase])
adjoint = sympy.Matrix([[1, 1 / phase]])
expected = (constant + cosine * (phase + 1 / phase) / 2
            + sine * (phase - 1 / phase) / (2 * sympy.I))
assert sympy.expand((adjoint * effect * vector)[0] / 2 - expected) == 0
assert sympy.expand(effect.det() - (constant**2 - cosine**2 - sine**2)) == 0
assert effect.subs({constant: 1, cosine: 0, sine: 0}) == sympy.eye(2)
print('LOWER_SPIN_OK: fixed equatorial-qubit Born formula, determinant and normalized effect sum')

positive_frequencies = {1, 2}
for dimension in (1, 2):
    for labels in combinations_with_replacement((-1, 0, 1), dimension):
        differences = {abs(first - second) for first in labels for second in labels}
        assert not positive_frequencies.issubset(differences)
probability = sympy.Rational(1, 2) + (phase + 1 / phase + phase**2 + 1 / phase**2) / 16
assert sympy.expand(probability).coeff(phase, 1) == sympy.Rational(1, 16)
assert sympy.expand(probability).coeff(phase, 2) == sympy.Rational(1, 16)
print('DIMENSION_OK: every one- or two-dimensional spin-one spectrum misses a required frequency')

outer_left, middle, outer_right = sympy.symbols('outer_left middle outer_right', real=True)
overlap = -sympy.I * outer_left + middle + sympy.I * outer_right
assert sympy.re(overlap) == middle
population = sympy.Symbol('population', real=True)
assert sympy.expand(overlap.subs({outer_left: population, middle: 1 - 2 * population,
                                outer_right: population})) == 1 - 2 * population
coherence = sympy.Symbol('coherence')
supported_state = sympy.Matrix([
    [outer_left, 0, coherence],
    [0, 0, 0],
    [sympy.conjugate(coherence), 0, outer_right],
])
rotation = sympy.diag(1 / phase, 1, phase)
inverse_rotation = sympy.diag(phase, 1, 1 / phase)
free_entries = sympy.symbols('effect_entry_0:9')
free_effect = sympy.Matrix(3, 3, free_entries)
born = sympy.expand(sympy.trace(rotation * supported_state * inverse_rotation * free_effect))
assert born.coeff(phase, 1) == 0 and born.coeff(phase, -1) == 0
print('FIXED_STATE_OK: orthogonal quarter-turn forces zero middle population and no first harmonic')

reversal = sympy.zeros(4)
for index in range(4):
    reversal[index, 3 - index] = 1
normalized_gram = sympy.eye(4) / 4 + sympy.Matrix([
    [0, 1, 0, 0],
    [1, 0, -2, 0],
    [0, -2, 0, 1],
    [0, 0, 1, 0],
]) / 16
assert reversal * normalized_gram.T * reversal == normalized_gram
assert normalized_gram != sympy.diag(*normalized_gram.diagonal())
degree_three_vector = sympy.Matrix([phase**index for index in range(4)])
degree_three_adjoint = sympy.Matrix([[phase**(-index) for index in range(4)]])
assert sympy.expand((degree_three_adjoint * normalized_gram * degree_three_vector)[0]) == 1
for size in range(1, 5):
    for coordinates in combinations(range(4), size):
        assert normalized_gram.extract(coordinates, coordinates).det() > 0
for index in range(4):
    row_sum = sum(abs(normalized_gram[index, column]) for column in range(4) if column != index)
    assert normalized_gram[index, index] - row_sum >= sympy.Rational(1, 16)
print('DEGREE_THREE_OK: normalized reversal-invariant nondiagonal matrix; all 15 principal minors positive')
print('SCOPE: symbolic identities and finite frequency/support checks; the corollaries have written proofs')
print('ALL_CHECKS_OK')
