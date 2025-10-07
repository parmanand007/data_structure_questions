"""
Problem: Validate Binary Search Tree
Category: Tree
Link: [LeetCode](https://leetcode.com/problems/validate-binary-search-tree/)

Statement:
Given the root of a binary tree, determine if it is a valid BST.

Example 1:
Input: root=[2,1,3]
Output: true
Approach:
- Recursion with (low,high) bounds.

Complexity:
- Time: O(n)
- Space: O(h)
"""




from typing import Optional
import math
class TreeNode:
    def __init__(self,val=0,left=None,right=None): self.val=val; self.left=left; self.right=right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lo, hi):
            if not node: return True
            if not (lo < node.val < hi): return False
            return dfs(node.left, lo, node.val) and dfs(node.right, node.val, hi)
        return dfs(root, -math.inf, math.inf)

if __name__ == '__main__':
    print('Test in your env')
