"""
Problem: Contains Duplicate
Category: Array / Hashing
Link: https://leetcode.com/problems/contains-duplicate/

Statement:
Given an integer array nums, return True if any value appears at least twice in the array,
and return False if every element is distinct.

Example:
Input: nums = [1, 2, 3, 1]
Output: True
"""


"""
Brute Force Approach
--------------------
How to Think:
    - Start simple: when asked "is there any duplicate?", 
      your first thought should be to compare every element with every other element.
    - Use two nested loops:
        → Outer loop picks one number.
        → Inner loop checks if it appears again later.
    - If any match is found, return True; otherwise, False.

Steps:
    1. Iterate i from 0 to n-1.
    2. For each i, iterate j from i+1 to n-1.
    3. If nums[i] == nums[j], return True (duplicate found).
    4. If loop ends, return False (no duplicates).

Complexity Explanation:
    - Time Complexity: O(N^2)
        → Because for each element, we may compare it with all other remaining elements.
        → For example, if nums = [1,2,3,4], comparisons = (3 + 2 + 1) = O(N^2).
    - Space Complexity: O(1)
        → No extra data structure used, only loop variables.
"""

from typing import List

def hasDuplicate_bruteforce(nums: List[int]) -> bool:
    # Compare each element with every other element
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:  # Found duplicate
                return True
    return False  # No duplicates found


"""
Sorting Approach
----------------
How to Think:
    - Sorting can group duplicates together.
    - Once sorted, if any two adjacent elements are equal → duplicate exists.
    - This avoids checking all pairs.

Steps:
    1. Sort the array.
    2. Traverse it once, compare each element with the next.
    3. If nums[i] == nums[i + 1], return True.
    4. Otherwise, return False after loop.

Complexity Explanation:
    - Time Complexity: O(N log N)
        → Sorting dominates as it takes O(N log N).
        → Then a single O(N) pass to check adjacent elements.
    - Space Complexity: O(1)
        → If sorting is done in-place.
        → O(N) if sorting creates a copy.
"""

def hasDuplicate_sorting(nums: List[int]) -> bool:
    nums.sort()  # Sort the list to bring duplicates together
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:  # Compare adjacent elements
            return True
    return False  # No duplicates found


"""
HashSet Approach (Optimal)
--------------------------
How to Think:
    - Whenever you need to "remember what you've seen", 
      think of using a Set or HashMap.
    - Sets allow O(1) average lookup and insert operations.
    - As we iterate, check if the number has been seen before.

Steps:
    1. Create an empty set 'seen'.
    2. For each number in nums:
         - If number already in 'seen', return True (duplicate found).
         - Otherwise, add it to 'seen'.
    3. If loop completes, return False (no duplicates).

Complexity Explanation:
    - Time Complexity: O(N)
        → Each lookup and insertion in a set takes O(1) average time.
        → For N elements, total = O(N).
    - Space Complexity: O(N)
        → In worst case (no duplicates), all N elements are stored in the set.
"""

def hasDuplicate_hashset(nums: List[int]) -> bool:
    seen = set()  # Initialize empty set to store seen numbers
    for num in nums:
        if num in seen:  # Check if already seen
            return True  # Duplicate found
        seen.add(num)  # Otherwise, add to set
    return False  # No duplicates found
