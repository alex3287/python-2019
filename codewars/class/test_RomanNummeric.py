import unittest
from RomanNummeric import RomanNumerals


class MyTestClass(unittest.TestCase):
    def test_to_roman_1(self):
        t = RomanNumerals()
        self.assertEqual(t.to_roman(3), 'III')
        self.assertEqual(t.to_roman(9), 'IX')

    def test_to_roman_2(self):
        t = RomanNumerals()
        self.assertEqual(t.to_roman(13), 'XIII')
        self.assertEqual(t.to_roman(19), 'XIX')
        self.assertEqual(t.to_roman(20), 'XX')
        self.assertEqual(t.to_roman(18), 'XVIII')
        self.assertEqual(t.to_roman(15), 'XV')
        self.assertEqual(t.to_roman(14), 'XIV')

    def test_to_roman(self):
        t = RomanNumerals()
        self.assertEqual(t.to_roman(1000), 'M')
        self.assertEqual(t.to_roman(1649), 'MDCXLIX')
        self.assertEqual(t.to_roman(99), 'XCIX')
        self.assertEqual(t.to_roman(433), 'CDXXXIII')
        self.assertEqual(t.to_roman(3000), 'MMM')


    def test_from_roman(self):
        t = RomanNumerals()
        self.assertEqual(t.from_roman('M'), 1000)
        self.assertEqual(t.from_roman('MMM'), 3000)
        self.assertEqual(t.from_roman('MCMXCVIII'), 1998)
        self.assertEqual(t.from_roman('XXXIV'), 34)
        self.assertEqual(t.from_roman('MCDV'), 1405)
        self.assertEqual(t.from_roman('DC'), 600)
        self.assertEqual(t.from_roman('MMMDCCCXLIII'), 3843)

if __name__ == '__main__':
    unittest.main()


