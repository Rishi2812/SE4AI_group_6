import pytest
from unittest.mock import MagicMock
from extend import *
#pytest test_file.py
from typing import List, Dict, Type, Callable, Generator


@pytest.fixture
def mock_data():
    mock_data = MagicMock()
    mock_data.rows = list(range(100))
    return mock_data

# Are smart and dumb lists the right length (i.e. N). if not, why not?
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

# Does chebyshevs().rows[0] return the top item in that sort?
def test_chebyshevs_rows():
    the.train = "/workspaces/ezr/data/test_data/test_extend_file.csv"
    data_instance = DATA().adds(csv(the.train))
    assert 12999 == data_instance.chebyshevs().rows[0][3], f"should be the best row"

# Does you code really run some experimental treatment 20 times for statistical validity?
def test_experimentalTreatment20Times(): 
    the.train = "/workspaces/ezr/data/test_data/test_extend_file.csv"
    data_instance = DATA().adds(csv(the.train))
    assert len(run_smart_strategy(data_instance)) == 20, f"size should be 20"
    assert len(run_dumb_strategy(40, data_instance)) == 20, f"size should be 20"

# Does d.shuffle() really jiggle the order of the data?
def test_dShuffleJiggleTest():
    the.train = "/workspaces/ezr/data/test_data/test_extend_file.csv"
    data_instance = DATA().adds(csv(the.train))
    original_rows = data_instance.rows.copy()
    assert original_rows != data_instance.shuffle().rows, f"these should not be equal"

#test_dShuffleJiggleTest()
