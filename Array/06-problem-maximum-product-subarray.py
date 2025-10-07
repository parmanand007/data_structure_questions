"""
Problem: Maximum Product Subarray
Category: Array / DP
Link: [LeetCode](https://leetcode.com/problems/maximum-product-subarray/)

Statement:
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Approach:
- Track max and min products at each step.

Complexity:
- Time: O(n)
- Space: O(1)
"""





from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_ending = min_ending = result = nums[0]
        for x in nums[1:]:
            candidates = (x, x * max_ending, x * min_ending)
            max_ending = max(candidates)
            min_ending = min(candidates)
            result = max(result, max_ending)
        return result

if __name__ == '__main__':
    print(Solution().maxProduct([2,3,-2,4]))  # 6
    print(Solution().maxProduct([-2,0,-1]))   # 0
