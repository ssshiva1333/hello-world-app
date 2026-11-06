import unittest
from hello import greet


class TestHello(unittest.TestCase):
    def test_greet_default(self):
        self.assertEqual(greet(), "Hello, World!")

    def test_greet_custom_name(self):
        self.assertEqual(greet("Tester"), "Hello, Tester!")


if __name__ == "__main__":
    unittest.main()