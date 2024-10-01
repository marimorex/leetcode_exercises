import unittest
from stacks.removing_stars_from_a_string import Solution

class TestRemovingStarsFromAString(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_removing_stars_from_a_string(self):
        result = self.solution.removeStars("leet**cod*e")
        self.assertEqual(result, "lecoe")

        result = self.solution.removeStars("erase*****")
        self.assertEqual(result, "")


    def test_removing_stars_from_a_string_empty(self):
        result = self.solution.removeStars("***")
        self.assertEqual(result, "")

    def test_removing_stars_from_a_string_wihtout_stack(self):
        result = self.solution.removeStars_without_stack("leet**cod*e")
        self.assertEqual(result, "lecoe")

        result = self.solution.removeStars_without_stack("erase*****")
        self.assertEqual(result, "")

        result = self.solution.removeStars_without_stack("***")
        self.assertEqual(result, "")