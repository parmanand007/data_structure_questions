"""
Problem: Group Anagrams
Category: String / Hashing
Link: [LeetCode](https://leetcode.com/problems/group-anagrams/)

Statement:
Group anagrams together from an array of strings. Return groups in any order.

Example 1:
Input: strs=["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
Approach:
- Use sorted string or char count as key.

Complexity:
- Time: O(n * k log k)
- Space: O(nk)
"""




from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        d=defaultdict(list)
        for s in strs: d[''.join(sorted(s))].append(s)
        return list(d.values())

if __name__ == '__main__':
    print(Solution().groupAnagrams(['eat','tea','tan','ate','nat','bat']))
