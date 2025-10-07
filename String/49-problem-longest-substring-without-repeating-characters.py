"""
Problem: Longest Substring Without Repeating Characters
Category: String / Sliding Window
Link: [LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

Statement:
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Approach:
- Sliding window with last-seen indices.

Complexity:
- Time: O(n)
- Space: O(min(n,m))
"""




class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last={}; start=0; best=0
        for i,ch in enumerate(s):
            if ch in last and last[ch]>=start:
                start=last[ch]+1
            last[ch]=i
            best=max(best, i-start+1)
        return best

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('abcabcbb'))
