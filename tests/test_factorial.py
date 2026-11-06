import unittest
from factorial import factorial


class TestFactorial(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_one(self):
        self.assertEqual(factorial(1), 1)

    def test_positive(self):
        self.assertEqual(factorial(5), 120)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_non_integer_raises(self):
        with self.assertRaises(ValueError):
            factorial(2.5)