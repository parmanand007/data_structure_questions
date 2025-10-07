"""
Problem: Rotate Image
Category: Matrix
Link: [LeetCode](https://leetcode.com/problems/rotate-image/)

Statement:
Rotate n x n matrix by 90 degrees clockwise in-place.

Example 1:
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Approach:
- Transpose then reverse rows.

Complexity:
- Time: O(n^2)
- Space: O(1)
"""




from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n): matrix[i].reverse()

if __name__ == '__main__':
    m=[[1,2,3],[4,5,6],[7,8,9]]; Solution().rotate(m); print(m)
