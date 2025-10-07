"""
Problem: Top K Frequent Elements
Category: Heap / Hashing
Link: [LeetCode](https://leetcode.com/problems/top-k-frequent-elements/)

Statement:
Given an integer array nums and integer k, return the k most frequent elements.

Example 1:
Input: nums=[1,1,1,2,2,3], k=2
Output: [1,2]
Approach:
- Use Counter.most_common or heap/bucket sort.

Complexity:
- Time: O(n)
- Space: O(n)
"""




from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        return [x for x,_ in Counter(nums).most_common(k)]

if __name__ == '__main__':
    print(Solution().topKFrequent([1,1,1,2,2,3],2))
