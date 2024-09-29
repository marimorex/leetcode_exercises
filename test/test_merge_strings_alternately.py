import unittest
from strings.merge_strings_alternately import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_merge_alternately(self):
        result = self.solution.mergeAlternately("abc", "xyz")
        self.assertEqual(result, "axbycz")

        result = self.solution.mergeAlternately("abc", "pqr")
        self.assertEqual(result, "apbqcr")

        result = self.solution.mergeAlternately("ab", "pqrs")
        self.assertEqual(result, "apbqrs")

        result = self.solution.mergeAlternately("abcd", "pq")
        self.assertEqual(result, "apbqcd")

        result = self.solution.mergeAlternately("", "")
        self.assertEqual(result, "")

        result = self.solution.mergeAlternately("", "a")
        self.assertEqual(result, "a")


if __name__ == "__main__":
    unittest.main()