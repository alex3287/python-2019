import unittest
from alphabetic import listPosition

class MyTestClass(unittest.TestCase):
    def test_one(self):
        self.assertEqual(listPosition('AAAB'), 1)

if __name__ == '__main__':
    unittest.main()

