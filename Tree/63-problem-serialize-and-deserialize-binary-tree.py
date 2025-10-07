"""
Problem: Serialize And Deserialize Binary Tree
Category: Tree
Link: [LeetCode](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

Statement:
LeetCode problem: Serialize And Deserialize Binary Tree

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
class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        vals=[]
        def dfs(node):
            if not node: vals.append('#'); return
            vals.append(str(node.val)); dfs(node.left); dfs(node.right)
        dfs(root); return ','.join(vals)
    def deserialize(self, data: str) -> Optional[TreeNode]:
        it = iter(data.split(','))
        def dfs():
            val = next(it)
            if val == '#': return None
            node = TreeNode(int(val)); node.left = dfs(); node.right = dfs(); return node
        return dfs()

if __name__ == '__main__':
    codec=Codec(); root=TreeNode(1, TreeNode(2), TreeNode(3)); s=codec.serialize(root); print(s); r=codec.deserialize(s); print(r.val)
