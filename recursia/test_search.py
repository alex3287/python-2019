import unittest
from search import binSearch

class MyTestCase(unittest.TestCase):

    def test_three(self):
        A, t = [4], 4
        self.assertEqual(binSearch(A, t), True)

    def test_on(self):
        A, t = [], 5
        self.assertEqual(binSearch(A,t), False)

    def test_two(self):
        A, t = [1,3,4,5,6,7,7,8,98], 8
        self.assertEqual(binSearch(A, t), True)