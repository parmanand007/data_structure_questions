"""
Problem: Non Overlapping Intervals
Category: Interval
Link: [LeetCode](https://leetcode.com/problems/non-overlapping-intervals/)

Statement:
LeetCode problem: Non Overlapping Intervals

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
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda x:x[1])
        end = intervals[0][1]; cnt=0
        for s,e in intervals[1:]:
            if s < end: cnt+=1
            else: end = e
        return cnt

if __name__ == '__main__':
    print(Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
