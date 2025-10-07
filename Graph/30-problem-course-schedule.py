"""
Problem: Course Schedule
Category: Graph / Topological Sort
Link: [LeetCode](https://leetcode.com/problems/course-schedule/)

Statement:
Given numCourses and prerequisites pairs, determine if you can finish all courses (i.e., graph has no cycle).

Example 1:
Input: numCourses=2, prerequisites=[[1,0]]
Output: true
Approach:
- Kahn's algorithm or DFS cycle detection.

Complexity:
- Time: O(V+E)
- Space: O(V+E)
"""




from collections import deque, defaultdict
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg=[0]*numCourses; g=defaultdict(list)
        for a,b in prerequisites:
            g[b].append(a); indeg[a]+=1
        q=deque([i for i in range(numCourses) if indeg[i]==0]); seen=0
        while q:
            u=q.popleft(); seen+=1
            for v in g[u]:
                indeg[v]-=1
                if indeg[v]==0: q.append(v)
        return seen==numCourses

if __name__ == '__main__':
    print(Solution().canFinish(2, [[1,0]]))
