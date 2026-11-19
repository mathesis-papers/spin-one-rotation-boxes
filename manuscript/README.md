# Answering the finite-outcome spin-one question

This package contains a proof that every normalized family of nonnegative
degree-two trigonometric polynomials has one pure qutrit realization. It
answers the question at the end of §IV.B.3, p. 17, of Aloy, Galley, Jones,
Ludescher and Müller, arXiv:2312.09278v2 (§IV.2.3 in the arXiv HTML;
§4.2.3 in the journal).
The binary equality was already proved by those authors in the preprint
of December 14, 2023, published in 2024.
The same question is repeated in §VII, p. 27. The note also proves
dimension-three optimality, a fixed-state obstruction, the exact spin-one
positive-Gram feasibility consequence and the dimension boundary of reversal
averaging. Its lower-spin corollary reproves the source's existing equalities.

## Contents

- `note.tex`: statement, complete proof and coverage table; `note.pdf` is
  distributed separately.
- `verify.py`: exact matrix identities, every nonempty coordinate support,
  and the complete stated finite Gram catalog.
- `verify_scalar.py`: exact factorization and Gram identities for the scalar lemma.
- `verify_corollaries.py`: exact lower-spin formulas, frequency obstructions
  and the positive degree-three normalization example.
- `verification.txt`: expected output of those three programs, in that order.
- `metadata.json`: scientific metadata, creators, license and pinned proof source.

## Build

Build `note.tex` with **Tectonic 0.17.0**:

```sh
tectonic note.tex
```

Alternatively, use an up-to-date TeX distribution and run
`pdflatex note.tex` twice. The bibliography is included in `note.tex`;
no external figures, bibliography database or BibTeX invocation is needed.

## Exact checks

Use Python 3 with SymPy 1.14.0:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install sympy==1.14.0
.venv/bin/python verify.py
.venv/bin/python verify_scalar.py
.venv/bin/python verify_corollaries.py
```

All three programs end with `ALL_CHECKS_OK`. The three-outcome catalog contains
5,984 multisets, of which 91 have constant nonzero sum polynomial. The
four-outcome catalog contains 52,360 multisets, with 575 such families.
They use rank-one factors in `{0, 1, -1, i, -i}^3` modulo global unit phase,
including zero and repeated factors. Exact positivity, support and measurement
normalization hold for every accepted family. All seven nonempty coordinate
supports are checked symbolically, including supports more general than the
balanced outer populations needed by the theorem.

The universal theorem, positivity argument for scalar polynomials, and
six corollaries have written proofs. The pinned Lean
declaration `D5.S3.Quantum.Measurement.RotationBoxes.SpinOneRotationBoxes.result`
states equality of the independently defined quantum and general correlation
predicates for every finite outcome type of cardinality at least three.
The source is the file `D5/S3/Quantum/Measurement/RotationBoxes/SpinOneRotationBoxes.lean`
at commit `4b14c77599edfd8a52c0a7926d038f4121ca7db1`, linked from the note
and `metadata.json`. The pure-state balanced-population form and the
one-outcome case are covered by the written argument. The finite catalog
illustrates the normalization identities; it does not exhaust real families.

## Authors and license

Haobo Ma — ChronoAI Pte Ltd, Singapore.

Wenlin Zhang — National University of Singapore; ChronoAI Pte Ltd, Singapore.

CC BY 4.0 (`cc-by-4.0`).
