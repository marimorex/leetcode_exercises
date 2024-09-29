import unittest

from arrays.can_place_flowers import Solution

class TestCanPlaceFlowers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_can_place_flowers_odd(self):
        result = self.solution.canPlaceFlowers([1,0,0,0,1],1)
        self.assertEqual(result, True)

        result = self.solution.canPlaceFlowers([1,0,0,0,1],2)
        self.assertEqual(result, False)

    def test_can_place_flowers_even(self):
        result = self.solution.canPlaceFlowers([1,0,0,0,1,0],1)
        self.assertEqual(result, True)

        result = self.solution.canPlaceFlowers([1,0,0,0,1,0],2)
        self.assertEqual(result, False)

        result = self.solution.canPlaceFlowers([1,0,0,0,1,0],3)
        self.assertEqual(result, False)

    def test_can_place_flowers_3_plots(self):
        result = self.solution.canPlaceFlowers([0,1,0],1)
        self.assertEqual(result, False)

    def test_can_place_flowers_1_plot(self):
        result = self.solution.canPlaceFlowers([0],1)
        self.assertEqual(result, True)

        result = self.solution.canPlaceFlowers([1],1)
        self.assertEqual(result, False)

    def test_can_place_flowers_2_plots(self):
        result = self.solution.canPlaceFlowers( [0,0],1)
        self.assertEqual(result, True)

        result = self.solution.canPlaceFlowers([0,0],2)
        self.assertEqual(result, False)

        result = self.solution.canPlaceFlowers([0,1],1)
        self.assertEqual(result, False)

    def test_can_place_flowers_zero_plots(self):
        result = self.solution.canPlaceFlowers( [0,0],0)
        self.assertEqual(result, True)

        result = self.solution.canPlaceFlowers([0,1,0],0)
        self.assertEqual(result, True)

        result = self.solution.canPlaceFlowers([1,0,0,0,1,0],0)
        self.assertEqual(result, True)