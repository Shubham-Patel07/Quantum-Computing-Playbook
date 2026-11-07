# Lab 07 — 3-Qubit Phase-Flip Code

## Aim
To protect a qubit against a single phase-flip ($Z$) error by encoding it in the Hadamard basis, detecting the error through $X$-type parity checks, correcting it, and recovering the original state with fidelity 1.

## Theory
A phase-flip $Z$ maps $|1\rangle \to -|1\rangle$. No classical code has an equivalent error. But in the Hadamard basis it acts like a bit flip:

$$Z|+\rangle = |-\rangle, \qquad Z|-\rangle = |+\rangle .$$

So we use the bit-flip code from Lab 06 with every qubit rotated by $H$.

**Encoding.**

$$\alpha|0\rangle + \beta|1\rangle \xrightarrow{\text{CNOTs}} \alpha|000\rangle + \beta|111\rangle \xrightarrow{H^{\otimes3}} \alpha|{+}{+}{+}\rangle + \beta|{-}{-}{-}\rangle .$$

**Syndrome extraction.** The checks become $X_0X_1$ and $X_1X_2$. To measure one, the circuit rotates the two qubits with $H$, collects their $Z$-parity on an ancilla with CNOTs, and rotates back with $H$.

| Error | $X_0X_1$ → `c[0]` | $X_1X_2$ → `c[1]` | Syndrome `c1 c0` | Correction |
|---|---|---|---|---|
| none | 0 | 0 | 00 | — |
| $Z_0$ | 1 | 0 | 01 | $Z$ on `q[0]` |
| $Z_1$ | 1 | 1 | 11 | $Z$ on `q[1]` |
| $Z_2$ | 0 | 1 | 10 | $Z$ on `q[2]` |

**Decoding.** Apply $H^{\otimes3}$ and then the reverse CNOTs. The recovered state is in `q[0]`.

**Limitation.** This code corrects one $Z$ error but not $X$ errors. Lab 08 (Shor code) combines both codes.

## Circuit diagram
![Phase-flip code circuit](circuit.png)

## Procedure
1. Open `lab.ipynb` and set `ALPHA`, `BETA` and `ERROR_QUBIT` (0, 1, 2 or `None`).
2. Run all cells.
3. Note the measured syndrome, the qubit that was corrected, and the recovered state.
4. The verification cell repeats the run for every error position.

## Parameters to try
- `ERROR_QUBIT` = `None`, `0`, `1`, `2`
- `(ALPHA, BETA)` = `(1, 1)`, `(1, -1)`, `(0.8, 0.6)`, `(1, 1j)`
- Extra exercise: replace the injected `Z` with an `X`. What syndrome do you get? Is the state recovered?

## Expected output
```
Injected error: Z on q[2]
Syndrome (c1 c0): 10

Error detection result:
Phase-flip error detected at q[2].
Z gate applied to q[2] for correction.

Original state : (+0.8000)|0> + (+0.6000)|1>
Recovered state: (+0.8000)|0> + (+0.6000)|1>
Fidelity       : 1.0
```

## Observations
| S.No | α | β | Error qubit | Syndrome (c1 c0) | Corrected qubit | Recovered state | Fidelity |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | | | |

## Result
Each single phase-flip error was found by the $X$-parity syndrome and corrected with a $Z$ gate, and the input state was recovered with fidelity 1.

## Viva questions
1. Why is a phase-flip invisible to the bit-flip code's $Z_iZ_j$ checks?
2. Show that $HZH = X$ and explain how this links the two codes.
3. Why do we sandwich the CNOTs between $H$ gates when extracting the syndrome?
4. What are the stabilizer generators of this code?
5. Why does an $X$ error on one qubit of $\alpha|{+}{+}{+}\rangle + \beta|{-}{-}{-}\rangle$ go undetected?
