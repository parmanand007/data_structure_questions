"""
Problem: Palindromic Substrings
Category: String / DP
Link: [LeetCode](https://leetcode.com/problems/palindromic-substrings/)

Statement:
Given a string s, return the number of palindromic substrings in it.

Example 1:
Input: s = "aaa"
Output: 6
Approach:
- Expand around centers.

Complexity:
- Time: O(n^2)
- Space: O(1)
"""




class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s); res=0
        for center in range(2*n-1):
            left=center//2; right=left+center%2
            while left>=0 and right<n and s[left]==s[right]:
                res+=1; left-=1; right+=1
        return res

if __name__ == '__main__':
    print(Solution().countSubstrings('aaa'))
