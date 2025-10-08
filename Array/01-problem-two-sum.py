"""
Problem: Two Sum
Category: Array / HashMap
Link: https://leetcode.com/problems/two-sum/

Statement:
Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target. You may assume that each input has exactly one solution, 
and you may not use the same element twice. You can return the answer in any order.

Example 1:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]

Example 2:
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
"""


"""
Brute Force Approach
--------------------
How to Think:
    - Start simple. The question says “find two numbers whose sum equals target”.
    - A direct idea is to try every pair of numbers and check if they sum to target.
    - Use two nested loops:
        → Outer loop picks the first number.
        → Inner loop checks all remaining numbers for the matching pair.
    - Return the pair of indices as soon as a match is found.

Steps:
    1. Loop i from 0 to n-1.
    2. Loop j from i+1 to n-1.
    3. If nums[i] + nums[j] == target, return [i, j].
    4. If loop ends, no solution found (though problem guarantees one).

Complexity Explanation:
    - Time Complexity: O(N²)
        → For each element, you scan the remaining elements, forming N*(N-1)/2 comparisons.
    - Space Complexity: O(1)
        → No extra data structure used, only loop counters.
"""

from typing import List

def twoSum_bruteforce(nums: List[int], target: int) -> List[int]:
    # Compare every possible pair
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:  # Check if pair sums to target
                return [i, j]  # Return indices
    return []  # (Won't happen as per problem statement)


"""
Two-Pass HashMap Approach
-------------------------
How to Think:
    - Brute force is slow because we check every pair.
    - We can use a HashMap (dictionary in Python) to store previously seen values 
      and their indices for faster lookups.
    - In the first pass, store value → index in a hashmap.
    - In the second pass, for each number x, check if (target - x) exists in hashmap.

Steps:
    1. First pass: store each element’s value → index in hashmap.
    2. Second pass:
         - For each number, compute complement = target - number.
         - If complement exists in hashmap and not the same index, return both indices.

Complexity Explanation:
    - Time Complexity: O(N)
        → Each lookup and insertion in hashmap is O(1) average time.
    - Space Complexity: O(N)
        → We store up to N elements in hashmap.
"""

def twoSum_twopass_hashmap(nums: List[int], target: int) -> List[int]:
    # First pass - store each number and its index
    num_to_index = {}
    for i, num in enumerate(nums):
        num_to_index[num] = i
    
    # Second pass - check for complement
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index and num_to_index[complement] != i:
            return [i, num_to_index[complement]]
    return []


"""
One-Pass HashMap Approach (Optimal)
-----------------------------------
How to Think:
    - In the two-pass method, we first store all elements, then check.
    - But we can merge these two steps!
    - While iterating, we check if the complement exists *before* adding the number.
    - If yes, we immediately have our answer.
    - Otherwise, store the number and continue.

Steps:
    1. Initialize an empty hashmap (num_to_index).
    2. Loop through nums:
         - Compute complement = target - num.
         - If complement exists in hashmap → return [index_of_complement, current_index].
         - Otherwise, store num → index in hashmap.
    3. Guaranteed one solution → will always return.

Complexity Explanation:
    - Time Complexity: O(N)
        → We traverse the list once and do O(1) operations per step.
    - Space Complexity: O(N)
        → We store at most N elements in the hashmap.
"""

def twoSum_onepass_hashmap(nums: List[int], target: int) -> List[int]:
    num_to_index = {}  # To store seen numbers and their indices
    
    for i, num in enumerate(nums):
        complement = target - num  # What number do we need?
        
        if complement in num_to_index:
            return [num_to_index[complement], i]  # Found pair
        
        # Otherwise, store current number with its index
        num_to_index[num] = i
    
    return []  # Won't reach here as per problem constraints

