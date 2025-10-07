"""
Problem: Remove Nth Node From End Of List
Category: LinkedList
Link: [LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

Statement:
LeetCode problem: Remove Nth Node From End Of List

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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy=ListNode(0); dummy.next=head; fast=slow=dummy
        for _ in range(n+1): fast=fast.next
        while fast: fast=fast.next; slow=slow.next
        slow.next = slow.next.next
        return dummy.next

if __name__ == '__main__':
    h=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    r=Solution().removeNthFromEnd(h,2); out=[]
    while r: out.append(r.val); r=r.next
    print(out)
