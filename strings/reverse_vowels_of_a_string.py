"""
LeetCode Exercise URL : https://leetcode.com/problems/reverse-vowels-of-a-string
Description :
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:
Input: s = "leetcode"
Output: "leotcede"
"""


class Solution:
    def isVowel(self, s: str) -> bool:
        if s in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            return True
        return False

    def reverseVowels(self, s: str) -> str:
        reversed_vowels = list(s)
        left = 0
        right = len(s) - 1

        while left < right:
            if not self.isVowel(reversed_vowels[left]):
                left += 1
                continue

            if not self.isVowel(reversed_vowels[right]):
                right -= 1
                continue

            left_temp = reversed_vowels[left]
            reversed_vowels[left] = reversed_vowels[right]
            reversed_vowels[right] = left_temp

            left += 1
            right -= 1

        return "".join(reversed_vowels)
