import unittest

from arrays.move_zeroes import Solution

class TestMoveZeroes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_move_middle_zeroes(self):
        result = self.solution.moveZeroes([0,1,0,3,12])
        self.assertEqual(result,[1,3,12,0,0])

    def test_move_empty_list(self):
        result = self.solution.moveZeroes([0])
        self.assertEqual(result,[0])

    def test_move_two_zeroes_list(self):
        result = self.solution.moveZeroes([0,0])
        self.assertEqual(result,[0,0])

    def test_move_start_zeroes_list(self):
        result = self.solution.moveZeroes([0,0,1,2,3])
        self.assertEqual(result,[1,2,3,0,0])