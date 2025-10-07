"""
Problem: Longest Common Subsequence
Category: Dynamic Programming
Link: [LeetCode](https://leetcode.com/problems/longest-common-subsequence/)

Statement:
Given two strings text1 and text2, return the length of their longest common subsequence.

Example 1:
Input: text1="abcde", text2="ace"
Output: 3
Approach:
- DP table.

Complexity:
- Time: O(n*m)
- Space: O(min(n,m))
"""




from typing import List
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        n, m = len(text1), len(text2)
        prev = [0] * (m + 1)
        for i in range(1, n+1):
            cur = [0] * (m + 1)
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    cur[j] = prev[j-1] + 1
                else:
                    cur[j] = max(prev[j], cur[j-1])
            prev = cur
        return prev[m]

if __name__ == '__main__':
    print(Solution().longestCommonSubsequence("abcde", "ace"))
