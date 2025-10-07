"""
Problem: Find Median From Data Stream
Category: Heap
Link: [LeetCode](https://leetcode.com/problems/find-median-from-data-stream/)

Statement:
LeetCode problem: Find Median From Data Stream

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
class MedianFinder:
    def __init__(self):
        self.small=[]; self.large=[]
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small); heapq.heappush(self.large, val)
        if len(self.small) > len(self.large) + 1: heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small) + 1: heapq.heappush(self.small, -heapq.heappop(self.large))
    def findMedian(self) -> float:
        if len(self.small) > len(self.large): return -self.small[0]
        if len(self.large) > len(self.small): return self.large[0]
        return (-self.small[0] + self.large[0]) / 2

if __name__ == '__main__':
    mf=MedianFinder(); mf.addNum(1); mf.addNum(2); print(mf.findMedian()); mf.addNum(3); print(mf.findMedian())
