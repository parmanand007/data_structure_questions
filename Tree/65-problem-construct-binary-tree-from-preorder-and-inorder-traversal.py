"""
Problem: Construct Binary Tree From Preorder And Inorder Traversal
Category: Tree
Link: [LeetCode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

Statement:
LeetCode problem: Construct Binary Tree From Preorder And Inorder Traversal

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




from typing import List, Optional
class TreeNode:
    def __init__(self,val=0,left=None,right=None): self.val=val; self.left=left; self.right=right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {v:i for i,v in enumerate(inorder)}
        def helper(l,r):
            if l>r: return None
            val = preorder.pop(0); root = TreeNode(val); pos = idx[val]
            root.left = helper(l,pos-1); root.right = helper(pos+1,r); return root
        return helper(0, len(inorder)-1)

if __name__ == '__main__':
    print('Build tree test in your env')
