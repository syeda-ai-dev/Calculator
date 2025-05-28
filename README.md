# Simple CLI Calculator

This project is a command-line interface (CLI) calculator that supports basic arithmetic, scientific operations, and memory functions.

## Features

- Basic arithmetic: Addition, Subtraction, Multiplication, Division.
- Scientific operations: Exponentiation (`power`), Natural Logarithm (`log`), Base-10 Logarithm (`log10`), Sine (`sin`), Cosine (`cos`), Tangent (`tan`), Arc Sine (`asin`), Arc Cosine (`acos`), Arc Tangent (`atan`).
- Memory functions: Store (`ms`), Recall (`mr`), Clear (`mc`).
- Persistent state: The calculator remembers the current value between operations.
- Interactive CLI: User-friendly command input.

## Project Structure

```
calculator/
├── core/
│   ├── __init__.py
│   ├── calculator.py   # Calculator class, manages state and operations
│   ├── operations.py   # Basic arithmetic functions
│   └── scientific.py   # Scientific mathematical functions
├── utils/              # (Currently empty, for future utility functions)
│   └── __init__.py
└── __init__.py

tests/
├── __init__.py
├── test_calculator.py  # Unit tests for Calculator class
├── test_operations.py  # Unit tests for basic operations
└── test_scientific.py  # Unit tests for scientific functions

main.py                 # Main script to run the CLI calculator
README.md               # This file
```

## Getting Started

### Prerequisites

- Python 3.x

### Running the Calculator

To run the CLI calculator, navigate to the project's root directory and execute `main.py`:

```bash
python main.py
```

You will see a prompt like this: `[0.0] > ` where `0.0` is the current value in the calculator.

#### How to Use the CLI

1.  **Entering Numbers**:
    Simply type a number and press Enter. This will set the calculator's current value.
    Example: `[0.0] > 42`
             `[42.0] >`

2.  **Performing Operations**:
    Operations generally take the current value as the first operand.

    *   **Basic Arithmetic**: `+ <num>`, `- <num>`, `* <num>`, `/ <num>`
        Example: `[42.0] > + 8` (Result: 50.0)
                 `[50.0] > * 2` (Result: 100.0)

    *   **Exponentiation**: `power <exponent>`
        Example: `[5.0] > power 3` (Result: 125.0)

    *   **Scientific Functions (unary, operate on current value)**: `sin`, `cos`, `tan`, `log`, `log10`, `asin`, `acos`, `atan`
        Example: `[1.0] > acos` (Result: 0.0, assuming current value was 1.0 after `cos(0)`)
                 `[3.14159] > sin` (Result: approx 0.0)

3.  **Commands**:
    *   `clear`: Resets the current value to 0.0.
    *   `ms`: Stores the current value in memory.
    *   `mr`: Recalls the value from memory and sets it as the current value.
    *   `mc`: Clears the memory (sets memory to 0.0).
    *   `quit` or `exit`: Exits the calculator.

#### Example Session

```
python main.py
Simple CLI Calculator
Enter expressions, or 'quit'/'exit' to exit.
Supported operations: +, -, *, /
Supported scientific functions: sin, cos, tan, asin, acos, atan, log, log10, power
Other commands: clear, ms (memory store), mr (memory recall), mc (memory clear)
Example: '5' (sets current value to 5)
         '+ 3' (adds 3 to current value)
         'sin' (calculates sine of current value)
         'power 2' (calculates current value to the power of 2)
[0.0] > 10
[10.0] > + 5
[15.0] > ms
Value stored in memory.
[15.0] > * 2
[30.0] > clear
[0.0] > mr
[15.0] > power 2
[225.0] > log10
[2.3521825181113624] > quit
Exiting calculator.
```

### Running Tests

The project uses Python's built-in `unittest` module. To run the tests, navigate to the project's root directory and run the following command:

```bash
python -m unittest discover -s tests
```

Alternatively, you can run individual test files:

```bash
python tests/test_operations.py
python tests/test_scientific.py
python tests/test_calculator.py
```

All tests should pass if the calculator is functioning correctly.

## Error Handling

The calculator provides feedback for errors such as:
- Division by zero.
- Logarithm of a non-positive number.
- Arc sine or Arc cosine of a number outside the [-1, 1] range.
- Unknown commands.

If an error occurs during an operation, the current value in the calculator usually remains unchanged.
```
