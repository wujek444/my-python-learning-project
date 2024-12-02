import unittest

from learning.my_functions import least_difference


class MyTestCase(unittest.TestCase):
    def test_least_difference(self):
        result = least_difference(1, 5, -5)
        self.assertEqual(result, 4, "Should equal to 4")
