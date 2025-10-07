"""
Problem: Insert Interval
Category: Interval
Link: [LeetCode](https://leetcode.com/problems/insert-interval/)

Statement:
Insert new interval into sorted non-overlapping intervals and merge if necessary.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Approach:
- Append intervals before, merge overlaps, append rest.

Complexity:
- Time: O(n)
- Space: O(n)
"""




from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]; i=0; n=len(intervals)
        while i<n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i]); i+=1
        while i<n and intervals[i][0] <= newInterval[1]:
            newInterval=[min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]; i+=1
        res.append(newInterval)
        while i<n: res.append(intervals[i]); i+=1
        return res

if __name__ == '__main__':
    print(Solution().insert([[1,3],[6,9]],[2,5]))
