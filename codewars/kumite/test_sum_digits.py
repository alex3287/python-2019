import unittest
from sum_digits import sum_digits

class MyTestCase(unittest.TestCase):
    def test_first(self):
        self.assertEqual(sum_digits(2346), 9)

    def test_second(self):
        self.assertEqual(sum_digits(23459), 11)

    def test_third(self):
        self.assertEqual(sum_digits(0), 0)

    def test_fourth(self):
        self.assertEqual(sum_digits(1234567890), 5)

    def test_fifth(self):
        self.assertEqual(sum_digits(5), 5)

    def test_sixth(self):
        self.assertEqual(sum_digits(3579), 24)

    def test_seventh(self):
        self.assertEqual(sum_digits(4), 4)

if __name__ == "__main__":
    unittest.main()