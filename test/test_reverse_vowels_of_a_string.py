import unittest

from strings.reverse_vowels_of_a_string import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution() 

    def test_a_is_vowel(self):
        result = self.solution.isVowel('a')
        self.assertEqual(result, True)

        result = self.solution.isVowel('A')
        self.assertEqual(result, True)

    def test_i_is_vowel(self):
        result = self.solution.isVowel('I')
        self.assertEqual(result, True)
        
        result = self.solution.isVowel('i')
        self.assertEqual(result, True)

    def test_c_is_not_vowel(self):
        result = self.solution.isVowel('c')
        self.assertEqual(result, False)

        result = self.solution.isVowel('C')
        self.assertEqual(result, False)

    def test_z_is_not_vowel(self):
        result = self.solution.isVowel('Z')
        self.assertEqual(result, False)

        result = self.solution.isVowel('z')
        self.assertEqual(result, False)

    
    def test_reverse_vowels_IceCreAm(self):
        result = self.solution.reverseVowels("IceCreAm")
        self.assertEqual(result, "AceCreIm")

    
    def test_reverse_vowels_leetcode(self):
        result = self.solution.reverseVowels("leetcode")
        self.assertEqual(result, "leotcede")

    def test_reverse_vowels_HOLa(self):
        result = self.solution.reverseVowels("HOLa")
        self.assertEqual(result, "HaLO")

