"""
Problem: Spiral Matrix
Category: Matrix
Link: [LeetCode](https://leetcode.com/problems/spiral-matrix/)

Statement:
Return all elements of matrix in spiral order.

Example 1:
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Approach:
- Traverse boundaries layer by layer.

Complexity:
- Time: O(mn)
- Space: O(1)
"""




from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        res=[]; top,left=0,0; bottom,right=len(matrix)-1,len(matrix[0])-1
        while top<=bottom and left<=right:
            for j in range(left,right+1): res.append(matrix[top][j])
            top+=1
            for i in range(top,bottom+1): res.append(matrix[i][right])
            right-=1
            if top<=bottom:
                for j in range(right,left-1,-1): res.append(matrix[bottom][j]); bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1): res.append(matrix[i][left]); left+=1
        return res

if __name__ == '__main__':
    print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
