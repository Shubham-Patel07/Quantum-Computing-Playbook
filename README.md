# Quantum Computing Lab Playbook

Hands-on quantum computing labs in [Qiskit](https://www.ibm.com/quantum/qiskit). The labs start with single qubits and end with full quantum error correction. Every lab has a runnable notebook, a lab sheet you can print, and a built-in check that the results match theory.

## Labs

| # | Lab | Topics | Qubits |
|---|---|---|---|
| 00 | [Setup and First Circuit](labs/00_setup_and_first_circuit) | environment check, X gate, statevector, shots | 1 |
| 01 | [Single-Qubit Gates](labs/01_single_qubit_gates) | X, Y, Z, H, S, T, rotations, Bloch sphere, gate identities | 7 |
| 02 | [Superposition and Measurement](labs/02_superposition_measurement) | Born rule, shot noise ∝ 1/√N, measurement basis | 1 |
| 03 | [Entanglement and Bell States](labs/03_entanglement_bell_states) | four Bell states, reduced states, ZZ/XX correlations | 2 |
| 04 | [Quantum Teleportation](labs/04_quantum_teleportation) | Bell measurement, classical feed-forward, fidelity | 3 |
| 05 | [Superdense Coding](labs/05_superdense_coding) | 2 classical bits per qubit, Bell-basis decoding | 2 |
| 06 | [Bit-Flip Code](labs/06_bit_flip_code) | 3-qubit repetition code, syndrome measurement | 5 |
| 07 | [Phase-Flip Code](labs/07_phase_flip_code) | Hadamard-basis encoding, X-type stabilizers | 5 |
| 08 | [Shor 9-Qubit Code](labs/08_shor_9_qubit_code) | concatenated code, corrects any single-qubit X/Y/Z error | 17 |

Do the labs in order: 00–03 build the foundations, 04–05 use entanglement as a resource, and 06–08 protect quantum information against errors.

## Setup

Requires **Python 3.11 or newer**.

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Open any `labs/*/lab.ipynb` in JupyterLab or VS Code and run all cells.

## How each lab is organized

```
labs/NN_topic/
├── lab.ipynb     # the experiment
├── README.md     # the lab sheet
└── circuit.png   # circuit diagram (regenerated whenever the notebook runs)
```

**Notebooks** follow the same layout every time:
1. **Parameters cell.** Change the inputs here (amplitudes, error positions, messages, angles). Nothing asks for typed input, so a notebook always runs top to bottom.
2. **Build → simulate → explain.** Each step is a separate, labelled cell.
3. **Verification cell.** `assert`s that the results match theory, usually across *every* case (all measurement outcomes, all messages, all error positions).

**Lab sheets** have the same sections every time: Aim · Theory · Circuit diagram · Procedure · Parameters to try · Expected output · Observations table · Result · Viva questions.

## Shared helpers

[`common/qlab.py`](common/qlab.py) holds code that the notebooks share: `normalize`, `format_amplitude` / `format_state`, `print_sparse_state`, `get_snapshot`, `qubit_state`, `fidelity`, `save_circuit`.

## Testing

```bash
pytest
```

This runs every notebook in a fresh kernel with [nbmake](https://github.com/treebeardtech/nbmake), so all the verification cells are checked. The whole suite takes about 30 s.

## Conventions

- **Bit ordering:** Qiskit is little-endian. Qubit 0 is the *rightmost* character of a bitstring, and statevector index = $\sum_k q_k 2^k$.
- **Resets:** after measurement, ancillas and unused data qubits are reset and labelled *"Available for Reuse"* in the circuit diagrams.
- **Known issue:** qiskit-aer 0.18 segfaults on `StatePreparation(...).inverse()`. Lab 04 appends the explicit adjoint as a `UnitaryGate` instead.

## License

[MIT](LICENSE)
