"""
Problem: Container With Most Water
Category: Array / Two Pointers
Link: [LeetCode](https://leetcode.com/problems/container-with-most-water/)

Statement:
Given n non-negative integers where each represents a vertical line, find two lines that together with the x-axis form a container, such that it contains the most water.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Approach:
- Two pointers from ends, move smaller inward.

Complexity:
- Time: O(n)
- Space: O(1)
"""





from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        best = 0
        while left < right:
            h = min(height[left], height[right])
            area = h * (right - left)
            best = max(best, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best

if __name__ == '__main__':
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))  # 49
