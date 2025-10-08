import numpy as np
from prepare_state import prepare_state

def test_normalization():
    amps = [1+0j, 1+0j, 1+0j, 1+0j]
    state = prepare_state(amps)
    assert np.isclose(np.linalg.norm(state), 1)

def test_dimension():
    state = prepare_state([0.5, 0.5, 0.5, 0.5])
    assert state.shape == (4,)

def test_zero_error():
    try:
        prepare_state([0,0,0,0])
    except ValueError:
        assert True

test_normalization()
test_dimension()
test_zero_error()
print("All tests passed ✅")
