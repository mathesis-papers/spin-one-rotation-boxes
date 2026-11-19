"""Exact identities for the scalar Gram construction in Lemma 2."""
import sympy

constant, cosine_one, sine_one, cosine_two, sine_two = sympy.symbols(
    'constant cosine_one sine_one cosine_two sine_two', real=True)
cosine, sine = sympy.symbols('cosine sine', real=True)
polynomial = (constant + cosine_one*cosine + sine_one*sine
              + cosine_two*(2*cosine**2-1) + 2*sine_two*sine*cosine)
factored = ((1-cosine)*(constant-cosine_two
                       - 2*cosine_two*cosine - 2*sine_two*sine))
stationary = polynomial.subs({cosine_one: -constant-cosine_two,
                             sine_one: -2*sine_two})
assert sympy.expand(stationary-factored) == 0

linear_constant, linear_cosine, linear_sine = sympy.symbols(
    'linear_constant linear_cosine linear_sine', real=True)
phase = sympy.Symbol('phase', nonzero=True)
small_gram = sympy.Matrix([
    [linear_constant, linear_cosine-sympy.I*linear_sine],
    [linear_cosine+sympy.I*linear_sine, linear_constant]])/2
difference = sympy.Matrix([[1, -1, 0], [0, 1, -1]])
gram = difference.T*small_gram*difference/2
vector = sympy.Matrix([1, phase, phase**2])
adjoint = sympy.Matrix([[1, 1/phase, 1/phase**2]])
evaluated = (adjoint*gram*vector)[0]
expected = ((1-(phase+1/phase)/2)
            *(linear_constant + linear_cosine*(phase+1/phase)/2
              + linear_sine*(phase-1/phase)/(2*sympy.I)))
assert sympy.simplify(evaluated-expected) == 0
radius = sympy.Symbol('radius', real=True)
characteristic = (radius*sympy.eye(2)-small_gram).det()
assert sympy.expand(characteristic
                    - ((radius-linear_constant/2)**2
                       - (linear_cosine**2+linear_sine**2)/4)) == 0
print('SCALAR_FACTOR_OK: stationary minimum gives the exact degree-two factor')
print('SCALAR_GRAM_OK: the displayed 3-by-3 matrix has the required Laurent polynomial')
print('SCALAR_SPECTRUM_OK: the degree-one Gram eigenvalue formula is exact')
print('SCOPE: algebraic identities; existence of the minimum and positivity follow from Lemma 2')
print('ALL_CHECKS_OK')
