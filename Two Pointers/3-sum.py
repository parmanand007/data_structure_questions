"""
Problem: 3Sum
Category: Array / Two Pointers / Hashing
Link: https://leetcode.com/problems/3sum/

Statement:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that:
    - i ≠ j, i ≠ k, and j ≠ k
    - nums[i] + nums[j] + nums[k] == 0
The solution set must not contain duplicate triplets.

Example:
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
"""


"""
Brute Force Approach
--------------------
How to Think (for this solution only):
    - “Find three numbers that sum to zero” → your first thought should be:
      check all possible triplets.
    - This means using three nested loops and testing each combination.
    - It’s simple but very inefficient — a good way to start reasoning.

Steps:
    1. Use three nested loops (i, j, k).
    2. For each unique combination, check if nums[i] + nums[j] + nums[k] == 0.
    3. Store the triplet (sorted) in a set to avoid duplicates.
    4. Convert set to list at the end.

Complexity Explanation:
    - Time Complexity: O(N³)
        → Three nested loops → all combinations of triplets.
    - Space Complexity: O(M)
        → M = number of unique triplets stored.
"""

def threeSum_bruteforce(nums):
    res = set()
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    res.add(tuple(sorted((nums[i], nums[j], nums[k]))))
    return [list(t) for t in res]

"""
Sorting + Two Pointer Approach (Optimal)
----------------------------------------
How to Think (for this solution only):
    - Once you think brute force is too slow (O(N³)), ask:
      “Can I reduce one loop using sorted order?”
    - If array is sorted, we can fix one element and use **two pointers** 
      to find the other two numbers (similar to 2-sum).
    - Sorting helps easily skip duplicates and efficiently move pointers.

Steps:
    1. Sort the array.
    2. Loop i from 0 to n-3:
         - Skip duplicates for i.
         - Initialize left = i+1, right = n-1.
         - While left < right:
             - Calculate total = nums[i] + nums[left] + nums[right].
             - If total == 0 → store triplet, move both pointers (skip duplicates).
             - If total < 0 → move left forward (need bigger sum).
             - If total > 0 → move right backward (need smaller sum).

Complexity Explanation:
    - Time Complexity: O(N²)
        → Outer loop (N) × inner two-pointer loop (N).
    - Space Complexity: O(1)
        → Only output list; no extra data structures.
"""

def threeSum_two_pointers(nums):
    nums.sort()
    res = []
    n = len(nums)

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicate fixed element

        left, right = i + 1, n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                # Skip duplicates for left and right
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1  # Need bigger number
            else:
                right -= 1  # Need smaller number

    return res


"""
HashSet Based Approach
----------------------
How to Think (for this solution only):
    - “Can I convert this 3-sum into a 2-sum problem?”
    - Fix one element → now you just need two numbers whose sum = -fixed_number.
    - Use a hashset to detect the complement efficiently.

Steps:
    1. Sort the array to handle duplicates.
    2. Loop i through nums:
         - Skip duplicate fixed numbers.
         - Create an empty set `seen`.
         - For each j > i, compute complement = -nums[i] - nums[j].
         - If complement exists in `seen`, we found a triplet.
         - Add nums[j] to `seen` after processing.
    3. Store triplets in a set to avoid duplicates.

Complexity Explanation:
    - Time Complexity: O(N²)
        → Outer loop (N) × inner loop (N) with O(1) hash lookup.
    - Space Complexity: O(N)
        → Set used for complements.
"""

def threeSum_hashset(nums):
    nums.sort()
    res = set()
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        seen = set()
        for j in range(i + 1, n):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.add((nums[i], complement, nums[j]))
            seen.add(nums[j])

    return [list(t) for t in res]



"""
HashSet Based Approach
----------------------
How to Think (for this solution only):
    - “Can I convert this 3-sum into a 2-sum problem?”
    - Fix one element → now you just need two numbers whose sum = -fixed_number.
    - Use a hashset to detect the complement efficiently.

Steps:
    1. Sort the array to handle duplicates.
    2. Loop i through nums:
         - Skip duplicate fixed numbers.
         - Create an empty set `seen`.
         - For each j > i, compute complement = -nums[i] - nums[j].
         - If complement exists in `seen`, we found a triplet.
         - Add nums[j] to `seen` after processing.
    3. Store triplets in a set to avoid duplicates.

Complexity Explanation:
    - Time Complexity: O(N²)
        → Outer loop (N) × inner loop (N) with O(1) hash lookup.
    - Space Complexity: O(N)
        → Set used for complements.
"""

def threeSum_hashset(nums):
    nums.sort()
    res = set()
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        seen = set()
        for j in range(i + 1, n):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.add((nums[i], complement, nums[j]))
            seen.add(nums[j])

    return [list(t) for t in res]
