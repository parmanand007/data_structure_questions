"""
Problem: Binary Tree Maximum Path Sum
Category: Tree
Link: [LeetCode](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

Statement:
Given a non-empty binary tree, return the maximum path sum. The path may start and end at any node.

Example 1:
Input: root = [1,2,3]
Output: Output: 6

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: Output: 42

Approach:
Explanation & Approach (DFS with max gain):
- For each node, define max_gain(node) as maximum sum of a path starting at node and going downwards
  (may choose left or right or neither if they are negative).
- Recursively compute left_gain = max(0, max_gain(node.left)) and right_gain = max(0, max_gain(node.right)).
- The best path that uses this node as highest node is node.val + left_gain + right_gain; update global_max.
- Return node.val + max(left_gain, right_gain) as the contribution to parent.
Correctness proof sketch:
- Any max path either lies entirely in left subtree, entirely in right subtree, or passes through current node.
  The recursion computes these candidates; the global maximum collects the best over all nodes.
Complexity:
- Time: O(n) visiting each node once.
- Space: O(h) recursion stack (h = tree height).

Complexity:
- Time: O(...)
- Space: O(...)
"""






from typing import Optional
import math
class TreeNode:
    def __init__(self,val=0,left=None,right=None): self.val=val; self.left=left; self.right=right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = -math.inf
        def dfs(node):
            if not node: return 0
            left = max(0, dfs(node.left)); right = max(0, dfs(node.right))
            self.best = max(self.best, node.val + left + right)
            return node.val + max(left, right)
        dfs(root); return self.best

if __name__ == '__main__':
    r=TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))); print(Solution().maxPathSum(r))
