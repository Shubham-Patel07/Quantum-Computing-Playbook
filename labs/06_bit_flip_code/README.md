# Lab 06 — 3-Qubit Bit-Flip Code

## Aim
To encode a qubit into the 3-qubit repetition code, inject a single bit-flip ($X$) error, find where it happened with syndrome measurement, correct it, and recover the original state with fidelity 1.

## Theory
**Encoding.** Two CNOTs spread the state over three qubits:

$$\alpha|0\rangle + \beta|1\rangle \;\longrightarrow\; \alpha|000\rangle + \beta|111\rangle .$$

This is *not* cloning. The result is an entangled state, not $|\psi\rangle^{\otimes 3}$.

**Error.** An $X$ on qubit $k$ flips that bit in both branches, for example $X_1:\ \alpha|010\rangle + \beta|101\rangle$.

**Syndrome extraction.** Two ancillas measure the parities $Z_0Z_1$ and $Z_1Z_2$. These checks say whether neighbouring qubits agree, without revealing $\alpha$ or $\beta$, so the superposition survives the measurement.

| Error | $Z_0Z_1$ → `c[0]` | $Z_1Z_2$ → `c[1]` | Syndrome `c1 c0` | Correction |
|---|---|---|---|---|
| none | 0 | 0 | 00 | — |
| $X_0$ | 1 | 0 | 01 | $X$ on `q[0]` |
| $X_1$ | 1 | 1 | 11 | $X$ on `q[1]` |
| $X_2$ | 0 | 1 | 10 | $X$ on `q[2]` |

**Decoding.** The two CNOTs are applied again in reverse order. This returns $|\psi\rangle$ to `q[0]` and leaves `q[1]`, `q[2]` in $|0\rangle$.

**Limitation.** The code corrects at most one bit-flip. It gives no protection against phase-flip ($Z$) errors (see Lab 07).

## Circuit diagram
![Bit-flip code circuit](circuit.png)

## Procedure
1. Open `lab.ipynb` and set `ALPHA`, `BETA` and `ERROR_QUBIT` (0, 1, 2 or `None`) in the **Parameters** cell.
2. Run all cells.
3. Note the measured syndrome, the qubit that was corrected, and the recovered state.
4. The verification cell repeats the run for every error position.

## Parameters to try
- `ERROR_QUBIT` = `None`, `0`, `1`, `2`
- `(ALPHA, BETA)` = `(1, 0)`, `(0, 1)`, `(1, 1)`, `(0.8, 0.6)`, `(1, 1j)`
- Extra exercise: edit the circuit to inject errors on *two* qubits and observe how the code fails.

## Expected output
```
Injected error: X on q[2]
Syndrome (c1 c0): 10

Error detection result:
Error detected in q[2].
X gate applied to q[2].

Original state : (+0.8000)|0> + (+0.6000)|1>
Recovered state: (+0.8000)|0> + (+0.6000)|1>
Fidelity       : 1.0

error on None | syndrome 00 | fidelity 1.000000
error on    0 | syndrome 01 | fidelity 1.000000
error on    1 | syndrome 11 | fidelity 1.000000
error on    2 | syndrome 10 | fidelity 1.000000
```

## Observations
| S.No | α | β | Error qubit | Syndrome (c1 c0) | Corrected qubit | Recovered state | Fidelity |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | | | |

## Result
Each single bit-flip error was located correctly by its syndrome and corrected, and the input state was recovered with fidelity 1.

## Viva questions
1. Why doesn't measuring the syndrome collapse the encoded superposition?
2. Why is encoding with CNOTs not a violation of the no-cloning theorem?
3. What happens with two bit-flip errors? Which wrong correction is applied?
4. Why can't this code detect a $Z$ error?
5. If each qubit flips independently with probability $p$, show that the logical error rate is $3p^2 - 2p^3$. When does encoding help?
6. Why are the ancillas reset after measurement?
