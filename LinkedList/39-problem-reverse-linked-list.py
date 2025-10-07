"""
Problem: Reverse Linked List
Category: LinkedList
Link: [LeetCode](https://leetcode.com/problems/reverse-linked-list/)

Statement:
Reverse a singly linked list and return the head of the reversed list.

Example 1:
Input: Input: head = [1,2,3,4,5]
Output: Output: [5,4,3,2,1]
Approach:
- Iterative in-place reversal using prev pointer.

Complexity:
- Time: O(n)
- Space: O(1)
"""




class ListNode:
    def __init__(self,val=0,next=None): self.val=val; self.next=next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev=None; cur=head
        while cur:
            nxt=cur.next; cur.next=prev; prev=cur; cur=nxt
        return prev

if __name__ == '__main__':
    n1=ListNode(1, ListNode(2, ListNode(3))); r=Solution().reverseList(n1); out=[]
    while r: out.append(r.val); r=r.next
    print(out)
