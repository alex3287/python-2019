from camelcaseMatching import *
import unittest

class MyTestClass(unittest.TestCase):
    def test_one(self):
        queries = ["CompetitiveProgramming", "CounterPick", "ControlPanel"]
        pattern = "CooP"
        self.assertEqual(camelMatch(queries, pattern),[False, False, True])

    def test_two(self):
        queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
        pattern = "FB"
        self.assertEqual(camelMatch(queries, pattern), [True,False,True,True,False])

    def test_three(self):
        queries = ["uAxaqlzahfialcezsLfj","cAqlzyahaslccezssLfj","AqlezahjarflcezshLfj","AqlzofahaplcejuzsLfj","tAqlzahavslcezsLwzfj","AqlzahalcerrzsLpfonj","AqlzahalceaczdsosLfj","eAqlzbxahalcezelsLfj"]
        pattern = "AqlzahalcezsLfj"
        self.assertEqual(camelMatch(queries, pattern), [True, True, True, True, True, True, True, True])

    def test_four(self):
        queries = ["lBxHyizsymknkbid","lBHyysizcymnkabd","olBHykyizymnekbd","lBHyigzymnkrpbtd","lBHyizysmnkbkiid","lcgBjHxyizymnkbd","xlBHyizuymnkijbd","lxaBHiyiznymnkbd"]
        pattern = "lBHyizymnkbd"
        self.assertEqual(camelMatch(queries, pattern), [True, True, True, True, True, True, True, True])

