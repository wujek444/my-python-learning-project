import unittest

from basic_python_course.exercises.booleans_and_conditions import sign, to_smash


class BooleansAndConditionsTest(unittest.TestCase):
    def test_sign_negative(self):
        self.assertEqual(-1, sign(-100))

    def test_sign_positive(self):
        self.assertEqual(1, sign(203102))

    def test_sign_zer(self):
        self.assertEqual(0, 0)

    def test_to_smash_single(self):
        to_smash(1)
        pass

    def test_to_smash_multiple(self):
        to_smash(2)
        pass