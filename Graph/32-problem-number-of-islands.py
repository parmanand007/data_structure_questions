"""
Problem: Number Of Islands
Category: Graph
Link: [LeetCode](https://leetcode.com/problems/number-of-islands/)

Statement:
LeetCode problem: Number Of Islands

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
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        m,n=len(grid),len(grid[0])
        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]!='1': return
            grid[i][j]='0'
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                dfs(i+dx, j+dy)
        cnt=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    cnt+=1; dfs(i,j)
        return cnt

if __name__ == '__main__':
    g=[['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']]
    print(Solution().numIslands(g))
