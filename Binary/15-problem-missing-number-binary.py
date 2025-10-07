"""
Problem: Missing Number
Category: Array / Math
Link: [LeetCode](https://leetcode.com/problems/missing-number/)

Statement:
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Approach:
- Use XOR or sum formula.

Complexity:
- Time: O(n)
- Space: O(1)
"""




from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

if __name__ == '__main__':
    print(Solution().missingNumber([3,0,1]))
