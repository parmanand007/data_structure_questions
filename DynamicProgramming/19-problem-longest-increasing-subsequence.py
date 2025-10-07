"""
Problem: Longest Increasing Subsequence
Category: Dynamic Programming / Binary Search
Link: [LeetCode](https://leetcode.com/problems/longest-increasing-subsequence/)

Statement:
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example 1:
Input: nums=[10,9,2,5,3,7,101,18]
Output: 4
Approach:
- Patience sorting (tails + bisect).

Complexity:
- Time: O(n log n)
- Space: O(n)
"""




from bisect import bisect_left
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for x in nums:
            i = bisect_left(tails, x)
            if i == len(tails):
                tails.append(x)
            else:
                tails[i] = x
        return len(tails)

if __name__ == '__main__':
    print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
