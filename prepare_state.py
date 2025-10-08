import numpy as np

def prepare_state(amplitudes):
    amplitudes = np.array(amplitudes, dtype=complex)
    if len(amplitudes) != 4:
        raise ValueError("Need exactly 4 amplitudes for two qubits.")

    norm = np.linalg.norm(amplitudes)
    if norm == 0:
        raise ValueError("Amplitudes cannot all be zero.")
    
    amplitudes /= norm  # normalize
    return amplitudes
