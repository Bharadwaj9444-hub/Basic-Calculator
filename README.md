# Basic Calculator
A command-line calculator developed using Python that supports five basic arithmetic operations: addition, subtraction, multiplication, division, and modulus.

## Features
- Addition of two numbers
- Subtraction of two numbers
- Multiplication of two numbers
- Division of two numbers
- Modulus (remainder) operation
- Handles division by zero
- Handles modulus by zero
- Handles invalid user input
- Handles invalid number input
- Supports decimal and negative numbers

## Technologies Used
- Python 3
- Python `unittest` module 

## How to Run the Calculator
1. Install Python 3 on your computer.
2. Open the project folder in your terminal.
3. Run the following command:
```bash
python main.py
```
4. Select an operation from the menu.
5. Enter two numbers.
6. View the result.
7. Choose another operation or select option 6 to exit.

## Python Code Example
The following function performs addition:
```python
def add_numbers(first_number, second_number):
    """Returns the sum of two numbers."""
    return first_number + second_number
```

## Available Operations
| Operation | Description |
|---|---|
| Addition | Adds two numbers |
| Subtraction | Finds the difference between two numbers |
| Multiplication | Multiplies two numbers |
| Division | Divides the first number by the second |
| Modulus | Returns the remainder after division |

## Running Unit Tests
To run the project's unit tests, execute the following command:
```bash
python -m unittest discover -s tests -v
```

## Project Testing
- [x] Addition
- [x] Subtraction
- [x] Multiplication
- [x] Division
- [x] Modulus
- [x] Division by zero
- [x] Modulus by zero
- [x] Negative number calculations
- [x] Decimal number calculations
- [x] Floating-point precision

## Future Improvements
- Add a graphical user interface (GUI).
- Add more mathematical operations.
- Improve the user interface.
- Add calculation history.
- Develop a scientific calculator.


---

**Project:** Basic Calculator

**Language:** Python

