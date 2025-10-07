"""
Problem: Longest Consecutive Sequence
Category: Graph / Hashing
Link: [LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/)

Statement:
Given an unsorted array of integers, return the length of the longest consecutive elements sequence.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Approach:
- Use set and expand from starts (where x-1 not in set).

Complexity:
- Time: O(n)
- Space: O(n)
"""




from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums); best=0
        for x in s:
            if x-1 not in s:
                cur=1
                while x+cur in s: cur+=1
                best=max(best, cur)
        return best

if __name__ == '__main__':
    print(Solution().longestConsecutive([100,4,200,1,3,2]))
