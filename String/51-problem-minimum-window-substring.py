"""
Problem: Minimum Window Substring
Category: Hash Table / String / Sliding Window
Link: [LeetCode](https://leetcode.com/problems/minimum-window-substring/)

Statement:
Given two strings s and t, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If no such window exists, return "". The answer is unique for the testcases.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Example 2:
Input: s="a", t="a"
Output: "a"
Approach:
- Sliding window with counts: expand right until valid, then shrink left to minimize.

Complexity:
- Time: O(n) average
- Space: O(1) or O(|charset|)
"""




from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ''
        need=Counter(t); missing=len(t); left=start=end=0
        for right,ch in enumerate(s,1):
            if need[ch]>0: missing-=1
            need[ch]-=1
            if missing==0:
                while left<right and need[s[left]]<0:
                    need[s[left]]+=1; left+=1
                if end==0 or right-left < end-start: start,end=left,right
                need[s[left]]+=1; missing+=1; left+=1
        return s[start:end]

if __name__ == '__main__':
    print(Solution().minWindow('ADOBECODEBANC','ABC'))
