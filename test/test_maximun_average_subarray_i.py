import unittest

from sliding_window.maximun_average_subarray_i import Solution

class TestMaximunAverageSubarrayI(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maximun_average_of_five_numbers(self):
        result = self.solution.findMaxAverage(nums=[1,12,-5,-6,50,3], k=4)
        self.assertEqual(result, 12.75000)

    def test_maximun_average_of_one_number(self):
        result = self.solution.findMaxAverage(nums=[5], k=1)
        self.assertEqual(result, 5)


    def test_maximun_average_of_one_negative_number(self):
        result = self.solution.findMaxAverage(nums=[-1], k=1)
        self.assertEqual(result, -1)