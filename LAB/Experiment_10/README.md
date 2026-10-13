# Experiment 10: Configure mypy, Docker, and GitHub Actions CI/CD

## Aim

To configure **mypy**, **Docker**, and **GitHub Actions CI/CD** for an existing Python project.

---

## Algorithm / Procedure

1. Create a simple Python program with type hints.
2. Install and run **mypy** to check the Python code.
3. Create a **Dockerfile** for the Python program.
4. Build a Docker image.
5. Run the Docker container.
6. Create a **GitHub Actions** workflow.
7. Push the project to GitHub.
8. Check the workflow execution in GitHub Actions.

---

## Very Simple Python Program

### `main.py`

```python
def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


print("Addition:", add(10, 20))
print("Multiplication:", multiply(10, 20))
```

---

## 1. Configure mypy

Install mypy:

```bash
pip install mypy
```

Run mypy:

```bash
mypy main.py
```

Expected output:

```text
Success: no issues found in 1 source file
```

mypy checks whether the program uses the correct data types.

---

## 2. Configure Docker

### `Dockerfile`

```dockerfile
FROM python:3.11

WORKDIR /app

COPY main.py .

CMD ["python", "main.py"]
```

### Build Docker Image

```bash
docker build -t mypythonapp .
```

### Run Docker Container

```bash
docker run mypythonapp
```

Output:

```text
Addition: 30
Multiplication: 200
```

---

## 3. Configure GitHub Actions CI/CD

Create the following folder:

```text
.github/workflows/
```

Create:

```text
python.yml
```

### `python.yml`

```yaml
name: Python CI

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install mypy
        run: pip install mypy

      - name: Run mypy
        run: mypy LAB/Experiment_10/main.py

      - name: Run program
        run: python LAB/Experiment_10/main.py
```

The workflow automatically runs when code is pushed to GitHub.

---

## Data & Result

### Input

```text
10
20
```

### Python Output

```text
Addition: 30
Multiplication: 200
```

### mypy Result

```text
Success: no issues found in 1 source file
```

### Docker Result

```text
Addition: 30
Multiplication: 200
```

### GitHub Actions Result

```text
✓ Checkout
✓ Setup Python
✓ Install mypy
✓ Run mypy
✓ Run program
```

The GitHub Actions workflow completed successfully.

---

## Inference

* **mypy** checks the types in the Python program.
* **Docker** packages the application into a container.
* **GitHub Actions** automatically checks and runs the project.
* The project was successfully pushed to GitHub.

---

## Analysis

* mypy helps find type errors.
* Docker provides a consistent environment to run the program.
* GitHub Actions automates the checking process.
* These tools make the Python project easier to test, run, and maintain.

---

## Result

The Python project was successfully configured with **mypy, Docker, and GitHub Actions CI/CD**. The program was checked, containerized, and automatically executed through GitHub Actions.
