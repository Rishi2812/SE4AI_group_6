import pytest
from unittest.mock import MagicMock
import random
from ezr import *
#pytest test_file.py

@pytest.fixture
def mock_data():
    mock_data = MagicMock()
    mock_data.rows = list(range(100))  # Mock data with 100 rows
    return mock_data

def guess(N, d):
    some = random.choices(d.rows, k=N)
    return d.clone().adds(some).chebyshevs().rows
def test_dumb_list_length(mock_data):
    for N in (20, 30, 40, 50):
        d = mock_data
        dumb = [guess(N, d) for _ in range(20)]
        dumb = [d.chebyshev(lst[0]) for lst in dumb]
        assert len(dumb) == 20, f"dumb list length is not 20 for N={N}"

def test_smart_list_length(mock_data):
    for N in (20, 30, 40, 50):
        d = mock_data
        smart = [d.shuffle().activeLearning() for _ in range(20)]
        smart = [d.chebyshev(lst[0]) for lst in smart]
        assert len(smart) == 20, f"smart list length is not 20 for N={N}"