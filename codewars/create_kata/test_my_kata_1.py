import unittest
from my_kata_1 import sum_max_min

class MyTestClass(unittest.TestCase):
    def test_first(self):
        self.assertEqual(sum_max_min(9),0)
        self.assertEqual(sum_max_min(-8), 0)

    def test_secon(self):
        self.assertEqual(sum_max_min(111),-1)
        self.assertEqual(sum_max_min(-5555), -1)

    def test_third(self):
        self.assertEqual(sum_max_min(10),1)
        self.assertEqual(sum_max_min(14567), 8)
        self.assertEqual(sum_max_min(-3418), 9)
        self.assertEqual(sum_max_min(-3410), 4)


if __name__ == '__main__':
    unittest.main()