"""
Problem: Meeting Rooms
Category: Interval
Link: [LeetCode](https://leetcode.com/problems/meeting-rooms/)

Statement:
Determine if a person can attend all meetings (no overlap) given intervals.

Example 1:
Input: [[0,30],[5,10],[15,20]]
Output: false
Approach:
- Sort and check adjacent overlaps.

Complexity:
- Time: O(n log n)
- Space: O(1)
"""




from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[i-1][1]: return False
        return True

if __name__ == '__main__':
    print(Solution().canAttendMeetings([[0,30],[5,10],[15,20]]))
