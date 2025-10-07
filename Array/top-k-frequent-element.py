"""
Problem: Top K Frequent Elements
Category: Array / HashMap / Heap
Link: https://leetcode.com/problems/top-k-frequent-elements/

Statement:
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""

"""
HashMap + Bucket Sort Approach
------------------------------
How to Think (for this solution only):
    - Count frequency of each number using a hashmap.
    - Use bucket sort: create an array of lists, where index = frequency.
    - Bucket sort is used because frequencies are bounded (0 to n), allowing O(n) time complexity.
      Other approaches like sorting or heap may be slower or more complex depending on n and k.
    - Traverse buckets from high to low and collect elements until we have k.

Steps:
    1. Count frequency of each number in nums using a dictionary.
    2. Initialize a list of empty lists (buckets) with size = len(nums) + 1.
    3. For each number and frequency, append number to buckets[frequency].
    4. Initialize result list.
    5. Traverse buckets from end to start:
         - Append numbers to result
         - Stop once result has k elements
    6. Return result

Complexity Explanation:
    - Time Complexity: O(n), counting + filling buckets + traversal
    - Space Complexity: O(n), frequency map + buckets
"""

from typing import List

def topKFrequent_bucket(nums: List[int], k: int) -> List[int]:
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in freq_map.items():
        buckets[freq].append(num)

    result = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result


"""
HashMap + Heap (Priority Queue) Approach
----------------------------------------
How to Think (for this solution only):
    - Count frequency of each number using hashmap.
    - Use a min-heap of size k to keep track of top k frequent elements.
    - The heap ensures we efficiently maintain the largest k frequencies.

Steps:
    1. Count frequency of each number in nums using a dictionary.
    2. Push tuples (frequency, number) into a min-heap.
    3. Maintain heap size ≤ k: if size exceeds k, pop the smallest frequency.
    4. Collect numbers from heap and return them.

Complexity Explanation:
    - Let n = number of elements in nums
    - Time Complexity: O(n log k), heap operations for n elements
    - Space Complexity: O(n) for frequency dictionary + O(k) for heap
"""

import heapq

def topKFrequent_heap(nums: List[int], k: int) -> List[int]:
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    min_heap = []
    for num, freq in freq_map.items():
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return [num for freq, num in min_heap]

"""
Min-Heap Implementation from Scratch with Visualization
-------------------------------------------------------
Concept:
    - A min-heap is a complete binary tree where every parent node is <= its children.
    - The smallest element is always at the root (index 0 in the list representation).
    - We can represent a heap as an array:
        - Parent at index i:
            Left child: 2*i + 1
            Right child: 2*i + 2
        - Child at index j:
            Parent: (j - 1) // 2

Operations:
1. insert(val) - Add a value while maintaining min-heap property
2. extract_min() - Remove and return the smallest value (root)
3. peek() - Get the smallest value without removing it

Visualization Example:
    Insert 5, 3, 8:
        Step 1: Insert 5 -> [5]
        Step 2: Insert 3 -> [5, 3]
                  Bubble up: 3 < 5, swap -> [3, 5]
        Step 3: Insert 8 -> [3, 5, 8]
                  No swap needed (8 > 3)
"""

class MinHeap:
    def __init__(self):
        # Initialize an empty list to store heap elements
        self.heap = []

    def insert(self, val):
        """Insert value into heap and maintain heap property"""
        self.heap.append(val)  # Add new element at the end
        # Visual: New element at the last position
        # Example: [3, 5] insert 2 -> [3, 5, 2]
        self._bubble_up(len(self.heap) - 1)  # Restore heap property

    def extract_min(self):
        """Remove and return the minimum element (root of heap)"""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            # Only one element, just pop it
            return self.heap.pop()
        
        # Swap root with last element
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        # Visual: Remove root and replace with last element
        # Example: [2, 5, 8] -> swap root 2 with last 8 -> [8, 5]
        self._bubble_down(0)  # Restore heap property
        return min_val

    def peek(self):
        """Return the minimum element without removing"""
        return self.heap[0] if self.heap else None

    def _bubble_up(self, index):
        """
        Move the element at index up until heap property is restored.
        Visual:
            - Compare with parent
            - If smaller than parent, swap
            - Repeat until root or no swap needed
        """
        parent = (index - 1) // 2
        while index > 0 and self.heap[parent] > self.heap[index]:
            # Swap parent and current node
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            # Move index to parent for next iteration
            index = parent
            parent = (index - 1) // 2

    def _bubble_down(self, index):
        """
        Move the element at index down until heap property is restored.
        Visual:
            - Compare node with left and right children
            - Swap with the smallest child if needed
            - Repeat until no swaps are required
        """
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        # Check if left child exists and is smaller
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        # Check if right child exists and is smaller
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        # If a swap is needed
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            # Recursive call to bubble down the swapped element
            self._bubble_down(smallest)



"""
HashMap + Sorting Approach
--------------------------
How to Think (for this solution only):
    - Count frequency of each number using hashmap.
    - Sort all numbers by their frequency in descending order.
    - Take the first k numbers as top k frequent elements.

Steps:
    1. Count frequency of each number using a dictionary.
    2. Sort keys of dictionary by frequency descending.
    3. Return first k elements.

Complexity Explanation:
    - Let n = number of elements, m = number of unique elements
    - Time Complexity: O(n + m log m), counting + sorting
    - Space Complexity: O(n) for frequency dictionary
"""

def topKFrequent_sort(nums: List[int], k: int) -> List[int]:
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    sorted_nums = sorted(freq_map.keys(), key=lambda x: freq_map[x], reverse=True)
    return sorted_nums[:k]
