"""
Problem: Same Tree
Category: Tree
Link: [LeetCode](https://leetcode.com/problems/same-tree/)

Statement:
Given two binary tree roots, check if the two trees are the same.

Example 1:
Input: p=[1,2,3], q=[1,2,3]
Output: true
Approach:
- Recursive equality check.

Complexity:
- Time: O(n)
- Space: O(h)
"""




from typing import Optional
class TreeNode:
    def __init__(self,val=0,left=None,right=None): self.val=val; self.left=left; self.right=right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

if __name__ == '__main__':
    print(Solution().isSameTree(TreeNode(1,TreeNode(2)), TreeNode(1,TreeNode(2))))
