"""
Problem: Detect Cycle In A Linked List
Category: LinkedList
Link: [LeetCode](https://leetcode.com/problems/detect-cycle-in-a-linked-list/)

Statement:
LeetCode problem: Detect Cycle In A Linked List

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




class ListNode:
    def __init__(self,val=0,next=None): self.val=val; self.next=next
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next; fast=fast.next.next
            if slow is fast: return True
        return False

if __name__ == '__main__':
    a=ListNode(3); b=ListNode(2); c=ListNode(0); d=ListNode(-4)
    a.next=b; b.next=c; c.next=d; d.next=b
    print(Solution().hasCycle(a))
