import pytest
from src.statistics import Statistics

def test_exercise():
    statistics = Statistics()
    statistics.add_number(3)

    assert statistics.get_count() == 1

    statistics.add_number(5)
    statistics.add_number(1)
    statistics.add_number(2)

    assert statistics.get_count() == 4
    assert statistics.sum == 11
    assert statistics.average() == 2.75
