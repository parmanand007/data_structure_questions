"""
Problem: Find Minimum in Rotated Sorted Array
Category: Array / Binary Search
Link: [LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

Statement:
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. Given the sorted rotated array nums of unique elements, return the minimum element of this array.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Approach:
- Binary search comparing mid and right.

Complexity:
- Time: O(log n)
- Space: O(1)
"""





from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

if __name__ == '__main__':
    print(Solution().findMin([3,4,5,1,2]))  # 1
    print(Solution().findMin([4,5,6,7,0,1,2]))  # 0
