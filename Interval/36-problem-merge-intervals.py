"""
Problem: Merge Intervals
Category: Interval
Link: [LeetCode](https://leetcode.com/problems/merge-intervals/)

Statement:
Merge all overlapping intervals and return result.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Approach:
- Sort by start and merge.

Complexity:
- Time: O(n log n)
- Space: O(n)
"""




from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals.sort(key=lambda x:x[0]); res=[intervals[0]]
        for s,e in intervals[1:]:
            if s<=res[-1][1]: res[-1][1]=max(res[-1][1], e)
            else: res.append([s,e])
        return res

if __name__ == '__main__':
    print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
