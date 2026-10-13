from hypothesis import given
from hypothesis import strategies as st


# Application
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def calculate(a, b):
    return add(a, b), multiply(a, b)


# Unit Tests
def test_add():
    assert add(2, 3) == 5


def test_multiply():
    assert multiply(2, 3) == 6


# Hypothesis Test
@given(st.integers(), st.integers())
def test_add_hypothesis(a, b):
    assert add(a, b) == a + b


# Integration Test
def test_calculate():
    assert calculate(2, 3) == (5, 6)
