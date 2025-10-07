"""
Problem: Jump Game
Category: Array / Greedy
Link: [LeetCode](https://leetcode.com/problems/jump-game/)

Statement:
Given an array of non-negative integers where each element represents maximum jump length at that position, determine if you can reach the last index.

Example 1:
Input: nums=[2,3,1,1,4]
Output: true

Example 2:
Input: nums=[3,2,1,0,4]
Output: false
Approach:
- Greedy tracking furthest reachable index.

Complexity:
- Time: O(n)
- Space: O(1)
"""




from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i, v in enumerate(nums):
            if i > reach: return False
            reach = max(reach, i + v)
        return True

if __name__ == '__main__':
    print(Solution().canJump([2,3,1,1,4]))
