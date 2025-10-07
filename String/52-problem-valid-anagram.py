"""
Problem: Valid Anagram
Category: String / Hashing
Link: [LeetCode](https://leetcode.com/problems/valid-anagram/)

Statement:
Given two strings s and t, return true if t is an anagram of s, otherwise false.

Example 1:
Input: s="anagram", t="nagaram"
Output: true
Approach:
- Compare frequency counts.

Complexity:
- Time: O(n)
- Space: O(1) or O(k)
"""




from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)

if __name__ == '__main__':
    print(Solution().isAnagram('anagram','nagaram'))
