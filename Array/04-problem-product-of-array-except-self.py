"""
Problem: Product of Array Except Self
Category: Array / Prefix-Suffix
Link: https://leetcode.com/problems/product-of-array-except-self/

Statement:
Given an integer array nums, return an array answer such that
answer[i] is equal to the product of all the elements of nums except nums[i].
You must solve it **without using division**.

Example:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""

"""
Brute Force Approach
-------------------
How to Think (for this solution only):
    - Start simple: for each index, compute product of all elements except current.
    - Two nested loops: for each i, multiply all nums[j] where j != i.
    - This is straightforward but inefficient.
Steps:
    1. Initialize an empty result array.
    2. For each index i:
        - Initialize product = 1
        - Multiply all nums[j] where j != i
        - Append product to result
    3. Return result

Complexity Explanation:
    - Time Complexity: O(n^2) → nested loops
    - Space Complexity: O(n) → result array
"""

from typing import List

def productExceptSelf_bruteforce(nums: List[int]) -> List[int]:
    n = len(nums)
    result = []
    for i in range(n):
        prod = 1
        for j in range(n):
            if i != j:
                prod *= nums[j]
        result.append(prod)
    return result

"""
Mid Approach (Using Left and Right Product Arrays)
-------------------------------------------------
How to Think (for this solution only):
    - Observe: result[i] = product of elements to the left * product of elements to the right
    - Use two arrays:
        1. left_product[i] = product of all elements before i
        2. right_product[i] = product of all elements after i
    - Multiply left and right for final result
Steps:
    1. Initialize left and right arrays of size n with 1s.
    2. Fill left_product array by iterating from left to right.
    3. Fill right_product array by iterating from right to left.
    4. Multiply left_product[i] * right_product[i] for each i to get result
    5. Return result

Complexity Explanation:
    - Time Complexity: O(n) → 3 passes over array
    - Space Complexity: O(n) → left and right arrays
"""

def productExceptSelf_mid(nums: List[int]) -> List[int]:
    n = len(nums)
    left = [1] * n
    right = [1] * n
    result = [1] * n

    # Fill left products
    for i in range(1, n):
        left[i] = left[i-1] * nums[i-1]

    # Fill right products
    for i in range(n-2, -1, -1):
        right[i] = right[i+1] * nums[i+1]

    # Multiply left and right products
    for i in range(n):
        result[i] = left[i] * right[i]

    return result

"""
Optimal Prefix-Suffix Approach
------------------------------
How to Think (for this solution only):
    - Observation: We don’t need two extra arrays, we can compute left products in result array itself.
    - Keep a running right product while iterating from right to left.
    - This gives O(1) extra space while maintaining O(n) time.
Steps:
    1. Initialize result array with 1s
    2. Compute left products in result array
    3. Initialize right_product = 1
    4. Traverse array from right to left:
        - Multiply result[i] *= right_product
        - Update right_product *= nums[i]
    5. Return result

Complexity Explanation:
    - Time Complexity: O(n) → two passes over array
    - Space Complexity: O(1) → excluding output array
"""

def productExceptSelf_optimal(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1] * n

    # Left products
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]

    # Right products and multiply
    right_product = 1
    for i in range(n-1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result


"""
Division Approach (Not Always Safe)
-----------------------------------
How to Think (for this solution only):
    - Observation: If you can use division, the problem becomes simpler:
        → Compute the product of all elements in the array.
        → For each index, divide total product by nums[i] to get result[i].
    - Caveat: This **fails if nums contains zeros** (division by zero is undefined).
    - To handle zeros:
        1. Count the number of zeros in the array.
        2. If more than one zero → all products except self are zero.
        3. If exactly one zero → only the position with zero gets the product of non-zero elements.
Steps:
    1. Count zeros in nums.
    2. Compute product of all non-zero numbers.
    3. Handle three cases:
        - More than one zero → return all zeros
        - Exactly one zero → result[i] = product for index with zero, else 0
        - No zeros → result[i] = total_product // nums[i]
Complexity Explanation:
    - Time Complexity: O(n) → one pass for product, one for result
    - Space Complexity: O(n) → for result array
"""

from typing import List

def productExceptSelf_division(nums: List[int]) -> List[int]:
    n = len(nums)
    zero_count = nums.count(0)
    result = [0] * n

    if zero_count > 1:
        # More than one zero: all products except self = 0
        return result
    elif zero_count == 1:
        # Exactly one zero: only the zero position gets product of non-zero elements
        total_product = 1
        zero_index = nums.index(0)
        for i in range(n):
            if i != zero_index:
                total_product *= nums[i]
        result[zero_index] = total_product
        return result
    else:
        # No zeros: divide total product by each element
        total_product = 1
        for num in nums:
            total_product *= num
        for i in range(n):
            result[i] = total_product // nums[i]
        return result