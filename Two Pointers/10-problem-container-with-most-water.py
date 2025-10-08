"""
Problem: Container With Most Water
Category: Array / Two Pointers
Link: https://leetcode.com/problems/container-with-most-water/

Statement:
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: Lines at index 1 and 8 form the container with area 49.
"""



"""
Brute Force Approach
--------------------
How to Think (for this solution only):
    - The area between two lines = (width) × (min of both heights).
    - Width = (right_index - left_index)
    - So the naive way is to check all possible pairs of lines and calculate the area.
    - This will give the correct answer, but is inefficient.

Steps:
    1. Initialize max_area = 0.
    2. For every pair (i, j):
         - Compute height = min(height[i], height[j]).
         - Compute width = j - i.
         - Compute area = height × width.
         - Update max_area if current area > max_area.
    3. Return max_area at the end.

Complexity Explanation:
    - Time Complexity: O(N²)
        → Double nested loop over all pairs.
    - Space Complexity: O(1)
        → Constant extra memory.
"""

def maxArea_bruteforce(height):
    max_area = 0
    n = len(height)

    for i in range(n):
        for j in range(i + 1, n):
            h = min(height[i], height[j])
            width = j - i
            area = h * width
            max_area = max(max_area, area)

    return max_area


"""
Two Pointer Approach (Optimal)
------------------------------
How to Think (for this solution only):
    - Brute force compares all pairs — too slow.
    - Notice the formula: area = min(height[left], height[right]) × (right - left)
    - The limiting factor is always the smaller height.
    - So, if we move the pointer with the smaller height inward, 
      we might find a taller line that gives a larger area.

Key Intuition:
    - Start with the widest container (left = 0, right = n-1).
    - Move inward greedily:
        → Always move the pointer with smaller height.
        → Because moving the taller one can never increase the area 
          (width decreases and height doesn’t increase).
    - Keep track of the maximum area during iteration.

Steps:
    1. Initialize left = 0, right = n - 1, max_area = 0.
    2. While left < right:
         - Compute area using current pointers.
         - Update max_area if needed.
         - Move the pointer with smaller height inward.
    3. Return max_area.

Complexity Explanation:
    - Time Complexity: O(N)
        → Each element is visited at most once.
    - Space Complexity: O(1)
        → Uses only pointers and a few variables.

Visualization Example:
    height = [1,8,6,2,5,4,8,3,7]
    Start -> left=0, right=8 → area = 1×8 = 8
    Move left (1 < 7) → left=1
    Now area = min(8,7)×7 = 49 → update max_area = 49
    Move right (7 < 8)? No → move right=7
    Keep repeating until pointers cross.
"""

def maxArea_two_pointers(height):
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        h = min(height[left], height[right])
        width = right - left
        area = h * width
        max_area = max(max_area, area)

        # Move pointer with smaller height inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area
