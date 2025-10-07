"""
Problem: Longest Palindromic Substring
Category: String / Expand Center
Link: [LeetCode](https://leetcode.com/problems/longest-palindromic-substring/)

Statement:
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab" or "aba"
Approach:
- Expand around centers for O(n^2) or Manacher for O(n).

Complexity:
- Time: O(n^2)
- Space: O(1)
"""




class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ''
        start=end=0
        for i in range(len(s)):
            l1=self.expand(s,i,i); l2=self.expand(s,i,i+1); l=max(l1,l2)
            if l> end-start+1:
                start = i - (l-1)//2; end = i + l//2
        return s[start:end+1]
    def expand(self,s,left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1; right+=1
        return right-left-1

if __name__ == '__main__':
    print(Solution().longestPalindrome('babad'))
