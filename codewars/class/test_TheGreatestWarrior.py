import unittest
from TheGreatestWarrior import Warrior

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.temp = Warrior()

    def test_training_one(self):
        self.temp.training(["Defeated Chuck Norris", 9000, 1])
        self.assertEqual(self.temp.level, 91)
        self.assertEqual(self.temp.rank, 'Master')
        self.assertEqual(self.temp.experience, 9100)
        self.assertEqual(self.temp.achievements, ['Defeated Chuck Norris'])

    def test_training_two(self):
        self.temp.training(["Hello", 1000, 1])
        self.temp.training(["Hello", 1000, 12])
        self.assertEqual(self.temp.level, 11)

    def test_training_three(self):
        self.temp.training(["Hi bro", 1000, 1])
        self.temp.battle(11)
        self.assertEqual(self.temp.level, 11)
        self.assertEqual(self.temp.experience, 1110)

    def test_training_four(self):
        self.temp.training(["Hey wey", 1080, 1])
        self.assertEqual(self.temp.level, 11)
        self.temp.battle(11)
        self.temp.battle(10)
        self.temp.battle(9)
        self.assertEqual(self.temp.experience, 1195)
        self.assertEqual(self.temp.level, 11)




if __name__ == '__main__':
    unittest.main()
