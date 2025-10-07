"""
Problem: Subtree Of Another Tree
Category: Tree
Link: [LeetCode](https://leetcode.com/problems/subtree-of-another-tree/)

Statement:
LeetCode problem: Subtree Of Another Tree

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
    def isSame(self, a, b):
        if not a and not b: return True
        if not a or not b: return False
        if a.val != b.val: return False
        return self.isSame(a.left,b.left) and self.isSame(a.right,b.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        if self.isSame(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

if __name__ == '__main__':
    t=TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5)); s=TreeNode(4, TreeNode(1), TreeNode(2))
    print(Solution().isSubtree(t,s))
