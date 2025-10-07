"""
Problem: Lowest Common Ancestor Of Bst
Category: Tree
Link: [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-bst/)

Statement:
LeetCode problem: Lowest Common Ancestor Of Bst

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




from typing import Optional
class TreeNode:
    def __init__(self,val=0,left=None,right=None): self.val=val; self.left=left; self.right=right
class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        node = root
        while node:
            if p.val < node.val and q.val < node.val: node = node.left
            elif p.val > node.val and q.val > node.val: node = node.right
            else: return node

if __name__ == '__main__':
    print('Test in your env')
