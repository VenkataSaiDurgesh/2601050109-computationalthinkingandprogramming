Experiment-12: AI-Assisted Code Review, Refactoring and Testing
Aim
To perform code review, refactoring, and testing of a Python program using AI assistance.

Algorithm / Procedure
Write a simple Python program.
Ask an AI tool to review the code.
Ask AI to improve the code.
Test the improved code.
Check where AI helped and where manual checking was needed.
Python Program
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", add(a, b))
print("Multiplication:", multiply(a, b))
AI Code Review
AI can help to:

Find errors.
Improve the code.
Make the code easier to read.
Suggest test cases.
Example AI Prompt
Review this Python code and suggest simple improvements.
Also give test cases for the program.
Refactored Code
def calculate(a, b):
    return a + b, a * b


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

addition, multiplication = calculate(a, b)

print("Addition:", addition)
print("Multiplication:", multiplication)
Testing
Input
Enter first number: 10
Enter second number: 5
Output
Addition: 15
Multiplication: 50
AI Success
AI found simple improvements.
AI suggested test cases.
AI helped make the code shorter.
Manual Intervention
The programmer checked the suggested code.
The programmer ran the program and verified the output.
Final changes were made manually when required.
Inference
AI helped with review, refactoring, and testing.
Manual checking was still required.
Analysis
AI made coding easier.
Testing confirmed that the program worked correctly.
Result
The Python program was successfully reviewed, refactored, and tested with AI assistance.
