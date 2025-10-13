# QuantumTask2-ComplexAmplitudes
Two-qubit state preparation using complex amplitudes
Task 2:

Your goal is to implement a routine that prepares a two-qubit quantum state given a set of complex amplitudes. The solution should be written from scratch, without relying on high-level quantum libraries (e.g., Qiskit’s initialize, PennyLane’s state preparation templates, etc.). Instead, focus on constructing the state manually using fundamental concepts such as normalization, tensor products, and matrix–vector representations of quantum states and gates.
Requirements

Input: A list or array of four complex amplitudes [a0, a1, a2, a3] that define the desired two-qubit state.
   - Ensure that the state is normalized:
     |a0|^2 + |a1|^2 + |a2|^2 + |a3|^2 = 1

   - If the input is not normalized, include a normalization step.
A representation of the two-qubit quantum state vector, for example as a NumPy array:
     |ψ⟩ = a0|00⟩ + a1|01⟩ + a2|10⟩ + a3|11⟩
 
 - Do not use quantum-specific state preparation functions from libraries.
4. Testing:
   - Write unit tests that check:
     - Normalization is enforced.
     - The output vector has the correct dimension (4 for two qubits).

Stretch Goal
Generalize the implementation to support a three-qubit state given 8 amplitudes.
