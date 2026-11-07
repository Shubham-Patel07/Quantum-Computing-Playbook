# Lab 08 — Shor 9-Qubit Code

## Aim
To implement Shor's 9-qubit code, which corrects **any** single-qubit error ($X$, $Z$ or $Y$). The lab injects bit-flip and phase-flip errors, measures the bit-flip and phase-flip syndromes, corrects the errors, and checks that the original state comes back with fidelity 1.

## Theory
The Shor code *concatenates* the two 3-qubit codes:
- **Outer layer: phase-flip code (Lab 07).** One logical qubit is spread over three blocks.
- **Inner layer: bit-flip code (Lab 06).** Each block is a 3-qubit repetition code.

$$|0_L\rangle = \frac{(|000\rangle + |111\rangle)^{\otimes 3}}{2\sqrt2}, \qquad
|1_L\rangle = \frac{(|000\rangle - |111\rangle)^{\otimes 3}}{2\sqrt2}.$$

**Bit-flip correction (per block).** Six ancillas measure $Z_iZ_{i+1}$ and $Z_{i+1}Z_{i+2}$ in each block, giving the syndromes `s0`, `s1`, `s2`:

| Flipped qubit in block | Local syndrome |
|---|---|
| first (q0 / q3 / q6) | 01 |
| middle (q1 / q4 / q7) | 11 |
| last (q2 / q5 / q8) | 10 |

**Phase-flip correction (between blocks).** A $Z$ on any qubit of a block flips that block's sign ($|000\rangle + |111\rangle \leftrightarrow |000\rangle - |111\rangle$). Two ancillas measure the 6-qubit stabilizers $X_0\cdots X_5$ and $X_3\cdots X_8$, giving the syndrome `p`:

| Block with phase error | `p` | Correction |
|---|---|---|
| none | 00 | — |
| 1 (q0–q2) | 01 | $Z$ on `q[0]` |
| 2 (q3–q5) | 11 | $Z$ on `q[3]` |
| 3 (q6–q8) | 10 | $Z$ on `q[6]` |

Every qubit in a block has the same effect on its sign, so one $Z$ on the block leader is enough. This is an example of *degeneracy*.

**Y errors.** $Y = iXZ$, so a $Y$ error triggers both syndromes and both corrections are applied. Set `X_ERROR == Z_ERROR` to see this.

**Discretization of errors.** Any single-qubit error is a combination of $I, X, Y, Z$. Measuring the syndrome forces the error to become one of these, so correcting $X$ and $Z$ is enough to correct *every* single-qubit error.

## Circuit diagram
![Shor code circuit](circuit.png)

## Procedure
1. Open `lab.ipynb` and set `ALPHA`, `BETA`, `X_ERROR` and `Z_ERROR` (qubit 0–8 or `None`).
2. Run all cells.
3. **Stage 1/2** print the encoded state and the state after the error, over the 9 data qubits.
4. Compare the measured syndromes with the expected ones, and the recovered state with the original.
5. The verification cell runs all 100 combinations of X and Z error positions.

## Parameters to try
| `X_ERROR` | `Z_ERROR` | Case |
|---|---|---|
| `None` | `None` | no error |
| `4` | `None` | bit-flip only |
| `None` | `7` | phase-flip only |
| `2` | `6` | X and Z on different blocks |
| `5` | `5` | Y error on q5 |
| `0` | `2` | X and Z on the same block |

## Expected output (`X_ERROR = 2`, `Z_ERROR = 6`)
```
SYNDROME RESULTS
Measured (p s2 s1 s0): 10 00 00 10
Block 1 (s0): measured 10, expected 10
Block 2 (s1): measured 00, expected 00
Block 3 (s2): measured 00, expected 00
Phase (p)    : measured 10, expected 10

SHOR CODE RESULTS
Original quantum state : (+0.8000)|0> + (+0.6000)|1>
Recovered quantum state: (+0.8000)|0> + (+0.6000)|1>
Fidelity: 1.0

100 / 100 error combinations corrected with fidelity 1.
```

## Observations
| S.No | α | β | X error | Z error | s0 | s1 | s2 | p | Corrections applied | Fidelity |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | | | |
| 2 | | | | | | | | | | |
| 3 | | | | | | | | | | |
| 4 | | | | | | | | | | |

## Result
The Shor code detected and corrected every single-qubit $X$, $Z$ and $Y$ error, and the input state was recovered with fidelity 1 in all 100 error configurations.

## Viva questions
1. How many physical qubits does the Shor code use per logical qubit, and what are its $[[n, k, d]]$ parameters?
2. Why is a $Z$ error on `q[7]` corrected by applying $Z$ to `q[6]`?
3. Why does correcting only $X$ and $Z$ errors also correct an arbitrary single-qubit rotation?
4. What happens with two $X$ errors in the *same* block? In *different* blocks?
5. Write down all 8 stabilizer generators of the Shor code.
6. Does an $X$ error change the phase syndrome `p`? Explain using the commutation of $X_i$ with the $X$-type stabilizers.
7. How does the Shor code compare with the 7-qubit Steane code and the 5-qubit perfect code?
