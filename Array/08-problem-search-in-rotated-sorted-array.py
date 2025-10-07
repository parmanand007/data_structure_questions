"""
Problem: Search in Rotated Sorted Array
Category: Array / Binary Search
Link: [LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/)

Statement:
Given a rotated sorted array nums and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target=0
Output: 4
Approach:
- Modified binary search determining sorted half.

Complexity:
- Time: O(log n)
- Space: O(1)
"""





from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:  # left half sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # right half sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

if __name__ == '__main__':
    print(Solution().search([4,5,6,7,0,1,2], 0))  # 4
    print(Solution().search([4,5,6,7,0,1,2], 3))  # -1
