"""
Problem: Clone Graph
Category: Graph / DFS/BFS
Link: [LeetCode](https://leetcode.com/problems/clone-graph/)

Statement:
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.

Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Approach:
- BFS/DFS with hashmap mapping original to copy.

Complexity:
- Time: O(V+E)
- Space: O(V)
"""




from collections import deque
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val; self.neighbors = neighbors or []
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        mapping = {}
        q = deque([node]); mapping[node] = Node(node.val)
        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in mapping:
                    mapping[nei] = Node(nei.val); q.append(nei)
                mapping[cur].neighbors.append(mapping[nei])
        return mapping[node]

if __name__ == '__main__':
    n1=Node(1); n2=Node(2); n1.neighbors=[n2]; n2.neighbors=[n1]
    print(Solution().cloneGraph(n1).val)
