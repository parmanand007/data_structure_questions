"""
Problem: Graph Valid Tree
Category: Graph / Union-Find
Link: [LeetCode](https://leetcode.com/problems/graph-valid-tree/)

Statement:
Given n nodes and edges, determine if they make up a valid tree (connected and edges==n-1).

Example 1:
Input: n=5, edges=[[0,1],[0,2],[0,3],[1,4]]
Output: true
Approach:
- Union-find and check edges==n-1/no cycles.

Complexity:
- Time: O(n α(n))
- Space: O(n)
"""




from typing import List
class DSU:
    def __init__(self,n): self.p=list(range(n))
    def find(self,x):
        if self.p[x]!=x: self.p[x]=self.find(self.p[x])
        return self.p[x]
    def union(self,a,b):
        ra,rb=self.find(a),self.find(b)
        if ra==rb: return False
        self.p[ra]=rb; return True
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1: return False
        d=DSU(n)
        for a,b in edges:
            if not d.union(a,b): return False
        return True

if __name__ == '__main__':
    print(Solution().validTree(5, [[0,1],[0,2],[0,3],[1,4]]))
