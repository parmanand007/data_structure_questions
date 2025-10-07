"""
Problem: Alien Dictionary
Category: Graph / Topological Sort
Link: [LeetCode](https://leetcode.com/problems/alien-dictionary/)

Statement:
Given a list of words sorted lexicographically in an alien language, derive the order of characters in that language's alphabet.

Example 1:
Input: words=["wrt","wrf","er","ett","rftt"]
Output: one valid order: "wertf"
Approach:
- Build directed graph from adjacent words and run topological sort.

Complexity:
- Time: O(C + ΣL)
- Space: O(C + ΣL)
"""




from collections import defaultdict, deque
from typing import List
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        indeg=defaultdict(int); graph=defaultdict(set); chars=set(''.join(words))
        for i in range(len(words)-1):
            w1,w2=words[i], words[i+1]; minlen=min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]: return ""
            for j in range(minlen):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]: graph[w1[j]].add(w2[j]); indeg[w2[j]] +=1
                    break
        q=deque([c for c in chars if indeg[c]==0]); res=[]
        while q:
            c=q.popleft(); res.append(c)
            for nei in graph[c]:
                indeg[nei]-=1
                if indeg[nei]==0: q.append(nei)
        if len(res) != len(chars): return ""
        return ''.join(res)

if __name__ == '__main__':
    print(Solution().alienOrder(["wrt","wrf","er","ett","rftt"]))
