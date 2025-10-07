"""
Problem: Meeting Rooms Ii
Category: Additional
Link: [LeetCode](https://leetcode.com/problems/meeting-rooms-ii/)

Statement:
LeetCode problem: Meeting Rooms Ii

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




import heapq
from typing import List
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda x:x[0]); heap=[]
        for s,e in intervals:
            if heap and heap[0] <= s: heapq.heappop(heap)
            heapq.heappush(heap, e)
        return len(heap)

if __name__ == '__main__':
    print(Solution().minMeetingRooms([[0,30],[5,10],[15,20]]))
