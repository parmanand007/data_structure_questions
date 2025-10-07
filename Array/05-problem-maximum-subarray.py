"""
Problem: Maximum Subarray (Kadane's Algorithm)
Category: Array / Dynamic Programming
Link: [LeetCode](https://leetcode.com/problems/maximum-subarray-(kadane's-algorithm)/)

Statement:
Find the contiguous subarray (containing at least one number) which has the largest sum.

Examples/Test Cases:
- [-2,1,-3,4,-1,2,1,-5,4] -> 6 (subarray [4,-1,2,1])
- [1] -> 1

Approach:
Use Kadane's algorithm: track current sum and reset to current element if it drops below zero; track max seen.

Complexity:
Time: O(n)
Space: O(1)

    Examples/Test Cases:
    - [-2,1,-3,4,-1,2,1,-5,4] -> 6 (subarray [4,-1,2,1])
- [1] -> 1

Approach:
Use Kadane's algorithm: track current sum and reset to current element if it drops below zero; track max seen.

Complexity:
Time: O(n)
Space: O(1)

    Approach:
    - Provide final optimal approach here (brief).

    Complexity:
    - Time: O(...)
    - Space: O(...)

Examples/Test Cases:
- See LeetCode

Approach:
- Provide final optimal approach here.

Complexity:
- Time: O(...)
- Space: O(...)
"""





from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ending = nums[0]
        max_so_far = nums[0]
        for x in nums[1:]:
            max_ending = max(x, max_ending + x)
            max_so_far = max(max_so_far, max_ending)
        return max_so_far

if __name__ == '__main__':
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
    print(Solution().maxSubArray([1]))  # 1
