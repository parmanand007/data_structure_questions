"""
Problem: 3Sum
Category: Array / Two Pointers
Link: [LeetCode](https://leetcode.com/problems/3sum/)

Statement:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] so that they add to zero without duplicates.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Approach:
- Sort + two pointers + skip duplicates.

Complexity:
- Time: O(n^2)
- Space: O(1)
"""





from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left, right = i+1, n-1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left]==nums[left-1]:
                        left += 1
                    while left < right and nums[right]==nums[right+1]:
                        right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1
        return res

if __name__ == '__main__':
    print(Solution().threeSum([-1,0,1,2,-1,-4]))  # [[-1,-1,2],[-1,0,1]]
