"""
Problem: Merge Two Sorted Lists
Category: LinkedList
Link: [LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/)

Statement:
Merge two sorted linked lists and return it as a sorted list.

Example 1:
Input: l1=[1,2,4], l2=[1,3,4]
Output: [1,1,2,3,4,4]
Approach:
- Merge with dummy head.

Complexity:
- Time: O(n+m)
- Space: O(1)
"""




class ListNode:
    def __init__(self,val=0,next=None): self.val=val; self.next=next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy=ListNode(0); cur=dummy
        while l1 and l2:
            if l1.val < l2.val: cur.next=l1; l1=l1.next
            else: cur.next=l2; l2=l2.next
            cur=cur.next
        cur.next = l1 or l2
        return dummy.next

if __name__ == '__main__':
    a=ListNode(1,ListNode(2,ListNode(4))); b=ListNode(1,ListNode(3,ListNode(4)))
    r=Solution().mergeTwoLists(a,b); out=[]
    while r: out.append(r.val); r=r.next
    print(out)
