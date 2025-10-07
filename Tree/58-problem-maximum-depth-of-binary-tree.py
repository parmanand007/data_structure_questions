"""
Problem: Maximum Depth Of Binary Tree
Category: Tree
Link: [LeetCode](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

Statement:
LeetCode problem: Maximum Depth Of Binary Tree

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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

if __name__ == '__main__':
    print(Solution().maxDepth(TreeNode(1, TreeNode(2), TreeNode(3))))
