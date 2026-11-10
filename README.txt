QUANTUM COMPUTING LAB
=====================

Install
-------
pip install qiskit qiskit_aer pylatexenc matplotlib

Run
---
Open a notebook in Jupyter and run the cells in order.
Each notebook asks for its inputs (amplitudes, error qubit, message, ...)
when the first cell runs. The second cell saves the circuit diagram as a PNG.

Experiments
-----------
0_Basics/
  0_1_FirstCircuit               X gate, statevector, measurement
  0_2_SingleQubitGates           single-qubit gates (I, X, Y, Z, H, S, T, SX, RX, RY, RZ, P, U) and the Bloch sphere
  0_3_Superposition_Measurement  Ry(theta) superposition and the Born rule
  0_4_BellStates                 circuits for the four Bell states (Phi+, Phi-, Psi+, Psi-)

1_Teleportation/
  1_Teleportation                teleport alpha|0> + beta|1> using a Bell pair

2_SuperDenseCoding/
  2_SuperDenseCoding             send 2 classical bits using 1 qubit

3_ErrorCorrection/
  3_1_BitFlip                    3-qubit bit-flip code (X errors)
  3_2_PhaseFlip                  3-qubit phase-flip code (Z errors)
  3_3_Shor9Bit_BitFlip_PhaseFlip Shor 9-qubit code (X, Z and Y errors)
