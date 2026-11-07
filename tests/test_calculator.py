import unittest
from main import (
    add_numbers,
    subtract_numbers,
    multiply_numbers,
    divide_numbers,
    modulus_numbers
)

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add_numbers(10, 20), 30)

    def test_subtraction(self):
        self.assertEqual(subtract_numbers(20, 10), 10)

    def test_multiply(self):
        self.assertEqual(multiply_numbers(5, 4), 20)

    def test_divide(self):
        self.assertEqual(divide_numbers(20, 4), 5.0)

    def test_modulus(self):
        self.assertEqual(modulus_numbers(10, 3), 1)

    def test_division_by_zero(self):
        self.assertEqual(divide_numbers(10, 0), "Cannot divide using 0.")

    def test_modulus_by_zero(self):
        self.assertEqual(modulus_numbers(10, 0), "Cannot operate modulus using 0.")

    def test_negative_addition(self):
        self.assertEqual(add_numbers(-5, 10), 5)

    def test_decimal_multiplication(self):
        self.assertEqual(multiply_numbers(2.5, 4), 10.0)

    def test_negative_subtraction(self):
        self.assertEqual(subtract_numbers(5, 10), -5)

    def test_addition_with_floating_point_numbers(self):
        self.assertAlmostEqual(add_numbers(0.1, 0.2), 0.3)

if __name__ == "__main__":
    unittest.main()