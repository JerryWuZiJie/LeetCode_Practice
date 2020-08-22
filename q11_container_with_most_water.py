# two pointers!!!
# think thoroughly next time

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_a = 0
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            if area > max_a:
                max_a = area
            if height[i] > height[j]:
                j = j - 1
            else:
                i = i + 1
        return max_a
