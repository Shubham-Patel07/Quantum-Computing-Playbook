# Quantum Computing Lab

Qiskit notebooks for the M.Tech quantum computing lab. The experiments start with single-qubit gates and entanglement, then cover quantum teleportation, superdense coding and quantum error correction.

## Experiments

| # | Experiment | What it shows | Inputs |
|---|---|---|---|
| 0.1 | [First Circuit](0_Basics/0_1_FirstCircuit) | X gate, statevector, measurement | apply X? (`y` / `n`) |
| 0.2 | [Single-Qubit Gates](0_Basics/0_2_SingleQubitGates) | H, X, Y, Z, S, T, S†, T†, I: one cell per gate | none |
| 0.3 | [Superposition & Measurement](0_Basics/0_3_Superposition_Measurement) | Ry(θ) superposition and the Born rule | angle θ, shots |
| 0.4 | [Bell States](0_Basics/0_4_BellStates) | the four entangled Bell states Φ+, Φ−, Ψ+, Ψ− | none |
| 1 | [Quantum Teleportation](1_Teleportation) | send a qubit state using a Bell pair + 2 classical bits | Alice's measurement |
| 2 | [Superdense Coding](2_SuperDenseCoding) | send 2 classical bits using 1 qubit | 2-bit message |
| 3.1 | [Bit-Flip Code](3_ErrorCorrection/3_1_BitFlip.ipynb) | 3-qubit code that corrects an X error | α, β, error qubit |
| 3.2 | [Phase-Flip Code](3_ErrorCorrection/3_2_PhaseFlip.ipynb) | 3-qubit code that corrects a Z error | α, β, error qubit |
| 3.3 | [Shor 9-Qubit Code](3_ErrorCorrection/3_3_Shor9Bit_BitFlip_PhaseFlip.ipynb) | corrects any single-qubit error (X, Z or Y) | α, β, X-error qubit, Z-error qubit |

Each notebook starts with a short description of the experiment.

## Setup

Requires **Python 3.11 or newer**.

```bash
pip install qiskit qiskit_aer pylatexenc matplotlib jupyter
jupyter notebook
```

## Running a notebook

1. Open the notebook and run the cells in order (**Run All**).
2. If it asks for inputs, type them in the box under the cell and press Enter.
3. The cell after each circuit saves the circuit diagram as a PNG in the same folder.

### Inputs to try

| Notebook | Example inputs | Expected result |
|---|---|---|
| 0.1 First Circuit | `y` | all 1024 shots measure `1` |
| 0.3 Superposition | θ = `60`, shots = `1024` | P(0) ≈ 0.75, P(1) ≈ 0.25 |
| 1 Teleportation | `01` | Bob applies X; fidelity = 1.0, *Teleportation successful!* |
| 2 Superdense Coding | `11` | Z and X activated; Bob decoded `11`, *Correct: True* |
| 3.1 Bit-Flip | a = `0.8`, b = `0.6`, error qubit = `2` | error detected in q[2], X applied to q[2], state recovered |
| 3.2 Phase-Flip | a = `0.8`, b = `0.6`, error qubit = `2` | syndrome `10`, Z applied to q[2], state recovered |
| 3.3 Shor Code | α = `0.8`, β = `0.6`, X error = `2`, Z error = `6` | fidelity = 1.0, *QUANTUM ERROR CORRECTION SUCCESSFUL!* |

Amplitudes are normalized automatically and can be complex (e.g. `0.6j`). In the Shor code, press Enter without a number to skip that error. Use the same qubit for X and Z to make a Y error.

## Folder structure

```
0_Basics/
├── 0_1_FirstCircuit/               notebook + circuit PNG
├── 0_2_SingleQubitGates/           notebook + one PNG per gate
├── 0_3_Superposition_Measurement/  notebook + circuit PNG
└── 0_4_BellStates/                 notebook + one PNG per Bell state
1_Teleportation/                    notebook + circuit PNG
2_SuperDenseCoding/                 notebook + circuit PNG
3_ErrorCorrection/                  bit-flip, phase-flip and Shor notebooks + their PNGs
```

## Notes

- **Bit order:** Qiskit is little-endian. In a result like `'10'`, the right-most bit belongs to qubit 0, so counts read as `c1 c0`.
- **Simulator:** all experiments run on the local Qiskit Aer simulator; no IBM Quantum account is needed.

## License

[MIT](LICENSE)
