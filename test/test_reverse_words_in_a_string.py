import unittest

from strings.reverse_words_in_a_string import Solution

class TestReverseWordsInAString(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_reverse_words_in_the_sky_is_blue(self):
        result = self.solution.reverseWords("the sky is blue")
        self.assertEqual(result, "blue is sky the")

    def test_reverse_words_with_many_white_spaces_in_the_middle(self):
        result = self.solution.reverseWords("a good   example")
        self.assertEqual(result, "example good a")

    def test_reverse_words_with_many_white_spaces_in_the_start(self):
        result = self.solution.reverseWords("     la casa es mia")
        self.assertEqual(result, "mia es casa la")