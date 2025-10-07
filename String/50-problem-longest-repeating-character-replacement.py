"""
Problem: Longest Repeating Character Replacement
Category: String / Sliding Window
Link: [LeetCode](https://leetcode.com/problems/longest-repeating-character-replacement/)

Statement:
Given a string s and integer k, you can replace any character at most k times. Return length of longest substring containing the same letter after replacements.

Example 1:
Input: s="AABABBA", k=1
Output: 4
Approach:
- Sliding window tracking most frequent char count.

Complexity:
- Time: O(n)
- Space: O(1)
"""




from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=defaultdict(int); left=0; maxf=0; res=0
        for right,ch in enumerate(s):
            count[ch]+=1; maxf=max(maxf,count[ch])
            while (right-left+1)-maxf>k:
                count[s[left]]-=1; left+=1
            res=max(res, right-left+1)
        return res

if __name__ == '__main__':
    print(Solution().characterReplacement('AABABBA',1))
