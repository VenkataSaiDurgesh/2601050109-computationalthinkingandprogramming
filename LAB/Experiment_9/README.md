# Experiment: Unit and Integration Testing Using Pytest and Hypothesis

## 1. Algorithm / Procedure

1. Create simple `add()` and `multiply()` functions.
2. Create a `calculate()` function using them.
3. Test individual functions using `pytest`.
4. Use `Hypothesis` to test `add()` with different inputs.
5. Test `calculate()` as an integration test.
6. Run the file using `pytest`.

---

## 2. Simple Python Program

```python
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
```

### Run the program

Install:

```text
pip install pytest hypothesis
```

Run:

```text
pytest test_app.py
```

---

## 3. Data & Result

**Data:**

```text
a = 2
b = 3
```

**Result:**

```text
add → 5
multiply → 6
calculate → (5, 6)
```

**Sample Test Result:**

```text
4 passed
```

---

## 4. Inference

* `pytest` tests the functions.
* `Hypothesis` generates different inputs automatically.
* Unit tests check individual functions.
* Integration test checks the functions working together.

---

## 5. Analysis

* **Unit Testing:** Tests individual functions.
* **Integration Testing:** Tests multiple functions together.
* **Hypothesis:** Automatically generates test data.
* **Pytest:** Runs all tests.

