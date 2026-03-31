# Project Euler

## What is Project Euler?

"Project Euler is a series of challenging mathematical/computer programming problems that will require more than just mathematical insights to solve. Although mathematics will help you arrive at elegant and efficient methods, the use of a computer and programming skills will be required to solve most problems."

> https://projecteuler.net/

## Solutions

The Python solutions are in the `peuler` directory, and the unit tests are in the `tests` directory.

## Running the Problems and Tests

To run the solutions or tests, you can use the following commands:

### Using `uv`

1. Run a specific problem:
   ```bash
   uv run peuler.problem_name
   ```

2. Run all tests:
   ```bash
   uv test
   ```

### Using `pip`

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run a specific problem:
   ```bash
   python -m peuler.problem_name
   ```

3. Run all tests:
   ```bash
   python -m unittest discover -s peuler/tests
   ```