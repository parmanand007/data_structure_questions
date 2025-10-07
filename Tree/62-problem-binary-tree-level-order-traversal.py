"""
Problem: Binary Tree Level Order Traversal
Category: Tree / BFS
Link: [LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal/)

Statement:
Return level order traversal of a binary tree's nodes' values.

Example 1:
Input: root=[3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Approach:
- BFS by levels.

Complexity:
- Time: O(n)
- Space: O(n)
"""




from typing import List, Optional
from collections import deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None): self.val=val; self.left=left; self.right=right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res=[]; q=deque([root])
        while q:
            level=[]
            for _ in range(len(q)):
                node=q.popleft(); level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(level)
        return res

if __name__ == '__main__':
    t=TreeNode(1, TreeNode(2), TreeNode(3)); print(Solution().levelOrder(t))
