"""
Problem: Word Search
Category: Matrix / Backtracking
Link: [LeetCode](https://leetcode.com/problems/word-search/)

Statement:
Given a board and a word, return true if the word exists in the grid (adjacent cells, each used once).

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Approach:
- DFS with backtracking.

Complexity:
- Time: O(mn * 4^L)
- Space: O(L) recursion)
"""




from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        def dfs(i,j,k):
            if k==len(word): return True
            if i<0 or j<0 or i>=m or j>=n or board[i][j]!=word[k]: return False
            tmp=board[i][j]; board[i][j]='#'
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                if dfs(i+dx,j+dy,k+1): board[i][j]=tmp; return True
            board[i][j]=tmp; return False
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0] and dfs(i,j,0): return True
        return False

if __name__ == '__main__':
    b=[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]; print(Solution().exist(b,'ABCCED'))
