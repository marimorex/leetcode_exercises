import unittest

from dictionaries_sets.find_the_difference_of_two_arrays import Solution


class TestFindTheDifferenceOfTwoArrays(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_find_the_difference_of_two_arrays_with_same_size(self):
        result = self.solution.findDifference([1, 2, 3], [2, 4, 6])
        self.assertEqual(result, [[1, 3], [4, 6]])

        result = self.solution.findDifference([1, 2, 3, 3], [1, 1, 2, 2])
        self.assertEqual(result, [[3], []])

    def test_find_the_difference_of_two_arrays_with_different_sizes(self):
        result = self.solution.findDifference([-68, -80, -19, -94, 82, 21, -43], [-63])
        self.assertEqual(result, [[-94, -19, -80, 82, 21, -43, -68], [-63]])

    def test_find_the_difference_of_two_arrays_with_empty_arrays(self):
        result = self.solution.findDifference([], [1])
        self.assertEqual(result, [[], [1]])
