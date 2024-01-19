import unittest

from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(2, 3)
        self.assertEqual(result, 5, "Addition failed")

    def test_subtract(self):
        result = self.calculator.subtract(5, 3)
        self.assertNotEqual(result, 2, "Subtraction failed")

    def test_multiply(self):
        result = self.calculator.multiply(2, 3)
        self.assertTrue(result == 6, "Multiplication failed")

    def test_divide(self):
        result = self.calculator.divide(6, 2)
        self.assertFalse(result != 3, "Division failed")

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(5, 0)

if __name__ == '__main__':
    unittest.main()
