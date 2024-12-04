import unittest

from basic_python_course.my_functions import least_difference, round_to_two_places, round_to_n_places


class MyTestCase(unittest.TestCase):
    def test_least_difference(self):
        result = least_difference(1, 5, -5)
        self.assertEqual(result, 4, "Should equal to 4")

    def test_round(self):
        #given
        to_round = 3.1343321

        #when
        rounded = round_to_two_places(to_round)

        #then
        self.assertEqual(3.13, rounded)

    def test_round_to_negative_places(self):
        # given
        to_round = 132.1343321

        # when
        rounded = round_to_n_places(to_round, -2)

        # then
        self.assertEqual(100, rounded)
