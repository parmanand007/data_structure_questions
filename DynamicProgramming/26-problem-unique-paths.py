"""
Problem: Unique Paths
Category: DP / Combinatorics
Link: [LeetCode](https://leetcode.com/problems/unique-paths/)

Statement:
Count unique paths in m x n grid moving only right/down.

Example 1:
Input: m=3,n=7
Output: 28
Approach:
- Use combinatorics or DP.

Complexity:
- Time: O(1) or O(mn)
- Space: O(1) or O(n)
"""




class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from math import comb
        return comb(m+n-2, m-1)

if __name__ == '__main__':
    print(Solution().uniquePaths(3,7))
