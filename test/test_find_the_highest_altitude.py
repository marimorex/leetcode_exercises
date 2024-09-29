import unittest

from arrays.find_the_highest_altitude import Solution

class TestFindTheHigestAltitude(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_find_the_highest_altitude(self):
        result = self.solution.largestAltitude([-5,1,5,0,-7])
        self.assertEqual(result, 1)

        result = self.solution.largestAltitude([-4,-3,-2,-1,4,3,2])
        self.assertEqual(result, 0)