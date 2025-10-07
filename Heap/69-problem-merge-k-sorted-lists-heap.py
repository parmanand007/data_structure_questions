"""
Problem: Merge K Sorted Lists Heap
Category: Heap
Link: [LeetCode](https://leetcode.com/problems/merge-k-sorted-lists-heap/)

Statement:
LeetCode problem: Merge K Sorted Lists Heap

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




import heapq
class ListNode:
    def __init__(self,val=0,next=None): self.val=val; self.next=next
    def __lt__(self, other): return self.val < other.val
class Solution:
    def mergeKLists(self, lists):
        heap=[]
        for node in lists:
            if node: heapq.heappush(heap, node)
        dummy=ListNode(0); cur=dummy
        while heap:
            node=heapq.heappop(heap); cur.next=node; cur=cur.next
            if node.next: heapq.heappush(heap, node.next)
        return dummy.next

if __name__ == '__main__':
    a=ListNode(1,ListNode(4,ListNode(5))); b=ListNode(1,ListNode(3,ListNode(4))); c=ListNode(2,ListNode(6))
    r=Solution().mergeKLists([a,b,c]); out=[]
    while r: out.append(r.val); r=r.next
    print(out)
