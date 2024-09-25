'''
You have a long flowerbed in which some of the plots are planted, 
and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty 
and 1 means not empty, and an integer n, return true if n new flowers can 
be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

'''

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # update the flowebed, add zeros in the edges, to process all positions with the same logic
        # left and right and current position must be 0.
        flowerbed_updated = [0] + flowerbed + [0]
        planted = 0
        
        if n==0 : return True

        for i in range(1,len(flowerbed_updated)-1):
            if flowerbed_updated[i-1]==0 and flowerbed_updated[i]==0 and flowerbed_updated[i+1] ==0:
                flowerbed_updated[i]=1
                planted+=1
 
        return planted >= n