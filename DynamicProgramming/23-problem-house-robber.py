"""
Problem: House Robber
Category: Dynamic Programming
Link: [LeetCode](https://leetcode.com/problems/house-robber/)

Statement:
Given an array of non-negative integers representing money at each house, return maximum amount without robbing adjacent houses.

Example 1:
Input: nums=[1,2,3,1]
Output: 4
Approach:
- DP include/exclude.

Complexity:
- Time: O(n)
- Space: O(1)
"""




from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0
        for x in nums:
            prev, curr = curr, max(curr, prev + x)
        return curr

if __name__ == '__main__':
    print(Solution().rob([1,2,3,1]))
