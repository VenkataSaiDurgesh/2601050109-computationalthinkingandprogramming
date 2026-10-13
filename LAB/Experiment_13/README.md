Experiment-13: AI-Assisted Specification-First, Type-Driven and Test-First Development
Aim
To develop a simple Python program using AI assistance with specification-first, type-driven, and test-first development.

Algorithm / Procedure
Write the program requirements.

Define the data types using type hints.

Write test cases before the program.

Develop the Python program using AI assistance.

Run the tests and check the output.

1. Specification
Create a program that:

Accepts two integers.

Calculates their sum.

Returns an integer result.

Passes the test cases.

2. Python Program
Create main.py:

Python

Run

def add(a: int, b: int) -> int:
    return a + b


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", add(a, b))
3. Test-First Development
Create test_main.py:

Python

Run

from main import add

def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-2, 2) == 0
Run the tests:

Bash

python3 -m pip install pytest
pytest -q
4. Type Checking
Install mypy:

Bash

python3 -m pip install mypy
Run:

Bash

mypy main.py
Data & Result
Input:

Enter first number: 10
Enter second number: 20
Output:

Sum: 30
Test result:

1 passed
Type-checking result:

Success: no issues found in 1 source file
Inference
The specification defines the requirements.

Type hints define the data types.

Tests check the program's correctness.

Analysis
AI helped develop the program.

Tests and type checking helped find errors.

Result
A Python program was developed using specification-first, type-driven, and test-first development with AI assistance.
