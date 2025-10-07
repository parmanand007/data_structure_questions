"""
Problem: House Robber Ii
Category: DynamicProgramming
Link: [LeetCode](https://leetcode.com/problems/house-robber-ii/)

Statement:
LeetCode problem: House Robber Ii

    Examples/Test Cases:
    - Example inputs and outputs from LeetCode should be added here.

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
    def robLinear(self, nums):
        prev, curr = 0, 0
        for x in nums:
            prev, curr = curr, max(curr, prev + x)
        return curr
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        return max(self.robLinear(nums[1:]), self.robLinear(nums[:-1]))

if __name__ == '__main__':
    print(Solution().rob([2,3,2]))
