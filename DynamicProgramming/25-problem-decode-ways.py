"""
Problem: Decode Ways
Category: Dynamic Programming
Link: [LeetCode](https://leetcode.com/problems/decode-ways/)

Statement:
Given string s containing digits, return number of ways to decode it using mapping 1->A...26->Z.

Example 1:
Input: s="12"
Output: 2

Example 2:
Input: s="226"
Output: 3
Approach:
- DP counting valid one/two-digit decodes.

Complexity:
- Time: O(n)
- Space: O(n)
"""




class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0': return 0
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1; dp[1] = 1
        for i in range(2, n+1):
            if s[i-1] != '0': dp[i] += dp[i-1]
            two = int(s[i-2:i])
            if 10 <= two <= 26: dp[i] += dp[i-2]
        return dp[n]

if __name__ == '__main__':
    print(Solution().numDecodings("226"))
