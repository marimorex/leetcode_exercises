import unittest
from arrays.kids_with_the_greatest_number_of_candies import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution() 

    def test_kids_with_candies(self):
        result = self.solution.kidsWithCandies([2,3,5,1,3], 3)
        self.assertEqual(result, [True,True,True,False,True])

        result = self.solution.kidsWithCandies([4,2,1,1,2], 1)
        self.assertEqual(result, [True,False,False,False,False])

        result = self.solution.kidsWithCandies([12,1,12], 10)
        self.assertEqual(result, [True,False,True])
