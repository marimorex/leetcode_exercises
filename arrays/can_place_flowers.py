from typing import List


class Solution:
    """
    This class provides a solution to the LeetCode problem:
    "605 Can Place Flowers" (https://leetcode.com/problems/can-place-flowers).

    Problem Description:
        You have a long flowerbed in which some plots are planted, and some are not.
        However, flowers cannot be planted in adjacent plots. Given an integer array
        flowerbed where 0 represents an empty plot and 1 represents a plot with flowers,
        and an integer n representing the number of new flowers you need to plant, return
        True if n new flowers can be planted without violating the no-adjacent-flowers rule.
        Otherwise, return False.

    Example:
        Input: flowerbed = [1,0,0,0,1], n = 1
        Output: True

        Input: flowerbed = [1,0,0,0,1], n = 2
        Output: False

    Constraints:
        1 <= flowerbed.length <= 2 * 10^4
        flowerbed[i] is 0 or 1.
        There are no two adjacent flowers in flowerbed.
        0 <= n <= flowerbed.length
    """

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Determines if 'n' new flowers can be planted in the flowerbed without
        violating the rule that no two flowers can be planted in adjacent plots.

        Parameters
        ----------
        flowerbed : List[int]
            A list of integers where 0 represents an empty plot and 1 represents a plot with a flower.
        n : int
            The number of new flowers that need to be planted.

        Returns
        -------
        bool
            True if 'n' new flowers can be planted without violating the rule, otherwise False.

        Approach
        --------
        - The method extends the flowerbed by adding 0 at both ends to simplify boundary checks.
        - It iterates through the flowerbed and checks if the current plot, along with its adjacent plots, are empty.
        - If so, a flower is planted, and the count is incremented.
        - The method returns True if the number of planted flowers meets or exceeds 'n'; otherwise, it returns False.
        """
        flowerbed_updated = [0] + flowerbed + [0]
        planted = 0

        if n == 0:
            return True

        for i in range(1, len(flowerbed_updated) - 1):
            if (
                flowerbed_updated[i - 1] == 0
                and flowerbed_updated[i] == 0
                and flowerbed_updated[i + 1] == 0
            ):
                flowerbed_updated[i] = 1
                planted += 1

        return planted >= n
