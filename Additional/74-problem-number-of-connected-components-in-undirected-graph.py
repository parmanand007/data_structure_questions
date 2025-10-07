"""
Problem: Number Of Connected Components In Undirected Graph
Category: Additional
Link: [LeetCode](https://leetcode.com/problems/number-of-connected-components-in-undirected-graph/)

Statement:
LeetCode problem: Number Of Connected Components In Undirected Graph

    Examples/Test Cases:
    - Example inputs and outputs from LeetCode should be added here.

    Approach:
    - Provide final optimal approach here (brief).

    Complexity:
    - Time: O(...)
    - Space: O(...)

Examples/Test Cases:
- See LeetCode

Approach:
- Provide final optimal approach here.

Complexity:
- Time: O(...)
- Space: O(...)
"""




from typing import List
class DSU:
    def __init__(self,n): self.p=list(range(n))
    def find(self,x):
        if self.p[x]!=x: self.p[x]=self.find(self.p[x])
        return self.p[x]
    def union(self,a,b):
        ra,rb=self.find(a),self.find(b)
        if ra!=rb: self.p[ra]=rb
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d=DSU(n)
        for a,b in edges: d.union(a,b)
        return len({d.find(i) for i in range(n)})

if __name__ == '__main__':
    print(Solution().countComponents(5, [[0,1],[1,2],[3,4]]))
