"""
Problem: Invertflip Binary Tree
Category: Tree
Link: [LeetCode](https://leetcode.com/problems/invertflip-binary-tree/)

Statement:
LeetCode problem: Invertflip Binary Tree

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

if __name__ == '__main__':
    t=TreeNode(1,TreeNode(2),TreeNode(3)); r=Solution().invertTree(t); print(r.val, r.left.val, r.right.val)
