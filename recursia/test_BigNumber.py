import unittest
from bigNumber import bigNum

class MyTestCase(unittest.TestCase):
    def test_one(self):
        A = [1,2,3,4,5,4,3,3]
        self.assertEqual(bigNum(A), 5)
