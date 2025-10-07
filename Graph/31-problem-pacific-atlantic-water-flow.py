"""
Problem: Pacific Atlantic Water Flow
Category: Graph / BFS/DFS
Link: [LeetCode](https://leetcode.com/problems/pacific-atlantic-water-flow/)

Statement:
Given matrix heights, return coordinates where water can flow to both Pacific and Atlantic (flow to equal or lower heights).

Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Approach:
- BFS from ocean borders inward to find reachable cells.

Complexity:
- Time: O(mn)
- Space: O(mn)
"""




from collections import deque
from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []
        m,n=len(heights),len(heights[0])
        def bfs(starts):
            seen=[[False]*n for _ in range(m)]; q=deque(starts)
            for x,y in starts: seen[x][y]=True
            while q:
                x,y=q.popleft()
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx,ny=x+dx,y+dy
                    if 0<=nx<m and 0<=ny<n and not seen[nx][ny] and heights[nx][ny]>=heights[x][y]:
                        seen[nx][ny]=True; q.append((nx,ny))
            return seen
        pac=bfs([(0,j) for j in range(n)] + [(i,0) for i in range(m)])
        atl=bfs([(m-1,j) for j in range(n)] + [(i,n-1) for i in range(m)])
        res=[]
        for i in range(m):
            for j in range(n):
                if pac[i][j] and atl[i][j]: res.append([i,j])
        return res

if __name__ == '__main__':
    h=[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(Solution().pacificAtlantic(h))
