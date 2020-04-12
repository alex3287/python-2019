import unittest

from integertoRoman import intToRoman

class MyTestClass(unittest.TestCase):
    def test_one(self):
        self.assertEqual(intToRoman(6000),'MMMMMM')
    def test_two(self):
        self.assertEqual(intToRoman(3),'III')
    def test_three(self):
        self.assertEqual(intToRoman(4004),'MMMMIV')
    def test_four(self):
        self.assertEqual(intToRoman(4),'IV')
    def test_five2(self):
        self.assertEqual(intToRoman(55),'LV')
    def test_six(self):
        self.assertEqual(intToRoman(99),'XCIX')
    def test_seven(self):
        self.assertEqual(intToRoman(9),'IX')


