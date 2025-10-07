"""
Problem: Product of Array Except Self
Category: Array / Prefix Product
Link: [LeetCode](https://leetcode.com/problems/product-of-array-except-self/)

Statement:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

Example 1:
Input: nums = [1,2,3,4]
Output: Output: [24,12,8,6]

Approach:
Explanation & Approach (Prefix and Suffix products):
- We want for each i: product of nums[0..i-1] * product of nums[i+1..n-1].
- First pass: compute prefix products and store in output: out[i] = product of nums[0..i-1].
- Second pass (right-to-left): keep a running suffix product and multiply into out[i].
- This avoids division and uses O(1) extra space besides output.
Correctness:
- By construction out[i] = prefix[i] * suffix[i].
Complexity:
- Time: O(n), Space: O(1) extra (output excluded).

Complexity:
- Time: O(...)
- Space: O(...)
"""







from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1] * n
        prefix = 1
        for i in range(n):
            out[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n-1, -1, -1):
            out[i] *= suffix
            suffix *= nums[i]
        return out

if __name__ == '__main__':
    print(Solution().productExceptSelf([1,2,3,4]))  # [24,12,8,6]
    print(Solution().productExceptSelf([-1,1,0,-3,3]))  # [0,0,9,0,0]
