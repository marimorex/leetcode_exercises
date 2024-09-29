'''
LeetCode Exercise URL :https://leetcode.com/problems/maximum-average-subarray-i

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that 
has the maximum average value and return this value. 
Any answer with a calculation error less than 10-5 will be accepted.


Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000

'''

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_k = sum(nums[:k])
        result = sum_k/k
        
        for i in range(len(nums)-k):
            # remove from sum the number of the left, and sum the number on the right 
            sum_k = sum_k - nums[i] + nums[k+i]
            result = max(result, sum_k/k)

        return result