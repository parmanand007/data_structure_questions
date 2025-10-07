"""
Problem: Set Matrix Zeroes
Category: Matrix
Link: [LeetCode](https://leetcode.com/problems/set-matrix-zeroes/)

Statement:
If an element is 0, set its entire row and column to 0 in-place.

Example 1:
Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Approach:
- Use first row/col as markers.

Complexity:
- Time: O(mn)
- Space: O(1)
"""




from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix), len(matrix[0])
        row0 = any(matrix[0][j]==0 for j in range(n))
        col0 = any(matrix[i][0]==0 for i in range(m))
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0: matrix[i][0]=0; matrix[0][j]=0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0: matrix[i][j]=0
        if row0:
            for j in range(n): matrix[0][j]=0
        if col0:
            for i in range(m): matrix[i][0]=0

if __name__ == '__main__':
    mat=[[1,1,1],[1,0,1],[1,1,1]]; Solution().setZeroes(mat); print(mat)
