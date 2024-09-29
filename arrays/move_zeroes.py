'''
LeetCode Exercise URL : https://leetcode.com/problems/move-zeroes/

Given an integer array nums, move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.


Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

'''

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = []

        for i in range(len(nums)):
            num = nums[i]
            if(num==0):
                # store the zero position
                zeros.append(i)
            else:
                # check if we can swapp if we have available zeroes
                if(len(zeros)>0):
                   nums[zeros.pop(0)] = num
                   nums[i] = 0
                   zeros.append(i)
        return nums

