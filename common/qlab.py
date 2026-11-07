"""Shared helpers for the Quantum Computing Lab Playbook notebooks."""

from pathlib import Path

import numpy as np
from qiskit import transpile
from qiskit.quantum_info import Statevector, state_fidelity


def normalize(alpha, beta):
    """Return (alpha, beta) scaled so that |alpha|^2 + |beta|^2 = 1."""
    alpha, beta = complex(alpha), complex(beta)
    norm = np.sqrt(abs(alpha) ** 2 + abs(beta) ** 2)

    if np.isclose(norm, 0):
        raise ValueError("Input state cannot have both amplitudes zero.")

    return alpha / norm, beta / norm


def format_amplitude(value, digits=4):
    """Format a complex amplitude compactly, e.g. +0.6000 or +0.6000 - 0.8000j."""
    real, imag = value.real, value.imag

    if abs(imag) < 1e-8:
        return f"{real:+.{digits}f}"

    if abs(real) < 1e-8:
        return f"{imag:+.{digits}f}j"

    sign = "+" if imag >= 0 else "-"
    return f"{real:+.{digits}f} {sign} {abs(imag):.{digits}f}j"


def format_state(alpha, beta, digits=4):
    """Format a single-qubit state as (alpha)|0> + (beta)|1>."""
    return (f"({format_amplitude(alpha, digits)})|0> + "
            f"({format_amplitude(beta, digits)})|1>")


def print_sparse_state(title, state, n_bits):
    """Print the non-zero amplitudes of a statevector over its lowest n_bits qubits.

    Basis labels are printed in Qiskit (little-endian) order: q[n-1] ... q[0].
    """
    print("\n" + "=" * 55)
    print(title)
    print("=" * 55)
    print(f"Basis states are displayed in q{n_bits - 1}...q0 order:\n")

    mask = (1 << n_bits) - 1
    for index, amplitude in enumerate(np.asarray(state)):
        if abs(amplitude) > 1e-8:
            bits = format(index & mask, f"0{n_bits}b")
            print(f"({format_amplitude(amplitude)}) |{bits}>")


def get_snapshot(circuit, label, backend):
    """Simulate a copy of `circuit` and return its statevector at this point.

    The copy keeps the save instruction out of the circuit being built.
    """
    probe = circuit.copy()
    probe.save_statevector(label=label)

    compiled = transpile(probe, backend, optimization_level=0)
    result = backend.run(compiled, shots=1).result()

    return Statevector(result.data(0)[label])


def qubit_state(state, qubit=0):
    """Extract the single-qubit state of `qubit` when all other qubits are |0>.

    Returns normalized (alpha, beta).
    """
    data = np.asarray(state)
    alpha = data[0]
    beta = data[1 << qubit]
    return normalize(alpha, beta)


def fidelity(input_state, output_state):
    """Fidelity |<psi_in|psi_out>|^2 between two pure states (vectors or Statevectors)."""
    return state_fidelity(Statevector(np.asarray(input_state)),
                          Statevector(np.asarray(output_state)))


def save_circuit(qc, path, **draw_kwargs):
    """Draw `qc` with matplotlib and save it as a high-resolution PNG."""
    draw_kwargs.setdefault("fold", -1)
    fig = qc.draw(output="mpl", **draw_kwargs)
    fig.savefig(Path(path), dpi=300, bbox_inches="tight")
    return fig
