"""
Problem: Longest Consecutive Sequence
Category: Array / Hashing / Sorting
Link: https://leetcode.com/problems/longest-consecutive-sequence/

Statement:
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example:
Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4  # The longest consecutive sequence is [1,2,3,4]
"""

"""
Brute Force Approach
-------------------
How to Think (for this solution only):
    - If you don’t care about efficiency initially, consider: “For each number, can I extend a consecutive sequence from it?”
    - Focus on **what consecutive means**: num, num+1, num+2, ...  
    - Simple, but repeatedly searching in the array wastes time.
Steps:
    1. For each number, try to build a sequence by checking next numbers.
    2. Track the longest sequence.
Complexity Explanation:
    - Time Complexity: O(n^2) → for each num, we may scan almost all others.
    - Space Complexity: O(1) → no extra data structures used.
"""

from typing import List

def longestConsecutive_bruteforce(nums: List[int]) -> int:
    max_length = 0
    for num in nums:
        current_length = 1
        next_num = num + 1
        while next_num in nums:
            current_length += 1
            next_num += 1
        max_length = max(max_length, current_length)
    return max_length


"""
Sorting Approach
----------------
How to Think (for this solution only):
    - Sorting brings order: consecutive numbers will appear next to each other.
    - Once sorted, the problem reduces to counting **lengths of consecutive increasing sequences**.
    - Efficient than brute force if sorting is acceptable.
Complexity Explanation:
    - Time Complexity: O(n log n) → due to sorting
    - Space Complexity: O(1) or O(n) depending on sorting implementation
"""

def longestConsecutive_sorting(nums: List[int]) -> int:
    if not nums:
        return 0
    nums.sort()
    max_length = 1
    current_length = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:  # ignore duplicates
            if nums[i] == nums[i-1] + 1:
                current_length += 1
            else:
                current_length = 1
            max_length = max(max_length, current_length)
    return max_length


"""
HashMap Approach
----------------
How to Think (for this solution only):
    - Use a map to store **existence of each number** or other metadata.
    - Idea: For each number, check if num-1 exists → if not, start a new sequence from num.
    - Tracks sequences efficiently and avoids repeated work like brute force.
Complexity Explanation:
    - Time Complexity: O(n) → each number processed once
    - Space Complexity: O(n) → store numbers in hashmap
"""

def longestConsecutive_hashmap(nums: List[int]) -> int:
    if not nums:
        return 0
    num_map = {num: True for num in nums}  # mark all numbers
    max_length = 0
    for num in nums:
        if num - 1 not in num_map:  # sequence starter
            current_num = num
            current_length = 1
            while current_num + 1 in num_map:
                current_num += 1
                current_length += 1
            max_length = max(max_length, current_length)
    return max_length


"""
HashSet Approach (Optimal)
--------------------------
How to Think (for this solution only):
    - Observation: we need **O(1) existence checks** → HashSet perfect.
    - Only start sequences from numbers that **cannot be extended backward** (num-1 not in set).  
    - This ensures **each number is considered exactly once**, giving O(n) time.
Complexity Explanation:
    - Time Complexity: O(n) → each number visited at most twice
    - Space Complexity: O(n) → for the set
"""

def longestConsecutive_hashset(nums: List[int]) -> int:
    num_set = set(nums)
    max_length = 0

    for num in num_set:
        if num - 1 not in num_set:  # Only sequence starters
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length
