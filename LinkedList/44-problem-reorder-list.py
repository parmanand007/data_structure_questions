"""
Problem: Reorder List
Category: LinkedList
Link: [LeetCode](https://leetcode.com/problems/reorder-list/)

Statement:
Reorder list L0→L1→…→Ln into L0→Ln→L1→Ln-1… in-place.

Example 1:
Input: head=[1,2,3,4]
Output: [1,4,2,3]
Approach:
- Split, reverse second half, merge.

Complexity:
- Time: O(n)
- Space: O(1)
"""




class ListNode:
    def __init__(self,val=0,next=None): self.val=val; self.next=next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next: return
        slow=fast=head
        while fast and fast.next: slow=slow.next; fast=fast.next.next
        prev=None; cur=slow.next; slow.next=None
        while cur:
            nxt=cur.next; cur.next=prev; prev=cur; cur=nxt
        p1, p2 = head, prev
        while p2:
            n1, n2 = p1.next, p2.next; p1.next = p2; p2.next = n1; p1, p2 = n1, n2

if __name__ == '__main__':
    h=ListNode(1,ListNode(2,ListNode(3,ListNode(4)))); Solution().reorderList(h); out=[]
    while h: out.append(h.val); h=h.next
    print(out)
