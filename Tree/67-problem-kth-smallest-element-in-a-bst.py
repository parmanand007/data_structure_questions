"""
Problem: Kth Smallest Element In A Bst
Category: Tree
Link: [LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

Statement:
LeetCode problem: Kth Smallest Element In A Bst

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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack=[]; cur=root
        while True:
            while cur: stack.append(cur); cur=cur.left
            cur = stack.pop(); k-=1
            if k==0: return cur.val
            cur = cur.right

if __name__ == '__main__':
    print('Test in your env')
