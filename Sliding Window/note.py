"""
Understanding Sliding Window Problems
=====================================

1. What Is a Sliding Window Problem?
------------------------------------
A sliding window problem involves finding a subarray (continuous part of an array or string)
that satisfies a certain condition (max sum, longest substring, count of something, etc.).
Instead of rechecking all elements every time, we reuse previous computations as the window
"slides" through the data.

2. The Core Idea
----------------
- Maintain a window (a range [left, right]) over the data.
- Expand the right boundary to explore more data.
- Shrink the left boundary when constraints are violated.
- Track a property inside the window (sum, count, length, etc.).
- Move the window one step at a time without recalculating everything from scratch.

3. How to Recognize a Sliding Window Problem
--------------------------------------------
Use this checklist — if you see these clues, it's likely a sliding window problem:

| Situation                                | Typical Pattern                                      |
|------------------------------------------|------------------------------------------------------|
| You are asked about subarrays/substrings | “continuous” or “contiguous” elements                |
| You must find max/min/longest/shortest   | Optimization over length, sum, or count              |
| You must track elements within constraint| Example: sum ≤ k, substring has ≤ 2 distinct chars   |
| You can reuse previous computations      | Example: reuse previous window sum                   |
| You move sequentially through the array  | The window slides one step at a time                 |

4. Two Types of Sliding Window
------------------------------

A. Fixed-size Window
--------------------
When the window size is known or constant.

Examples:
- Find max sum of subarray of size k
- Find average of every window of length 3

Typical Pattern:
----------------
for right in range(len(nums)):
    current_sum += nums[right]
    if right - left + 1 > k:
        current_sum -= nums[left]
        left += 1

B. Variable-size Window
-----------------------
When the window size changes dynamically.

Examples:
- Longest substring without repeating characters
- Smallest subarray with sum ≥ target

Typical Pattern:
----------------
for right in range(len(nums)):
    add nums[right] to window
    
    while condition_not_satisfied:
        remove nums[left]
        left += 1
    
    update answer

5. Quick Recognition Examples
-----------------------------

| Problem                                   | Key Words / Pattern                           | Sliding Window Type |
|-------------------------------------------|-----------------------------------------------|---------------------|
| Maximum sum subarray of size k            | "of size k" → fixed window                    | Fixed-size          |
| Longest substring without repeating chars | "longest substring" + "unique"                | Variable-size       |
| Minimum window substring (LeetCode 76)    | "minimum window" + "contains all chars"       | Variable-size       |
| Count anagrams in a string                | "substring" + "check every window"            | Fixed-size          |
| Subarray sum ≤ k                          | "subarray" + "sum constraint"                 | Variable-size       |

6. Why Sliding Window Is Powerful
---------------------------------
The sliding window technique reduces O(N²) brute-force solutions to O(N) time complexity by:
- Avoiding reprocessing the same elements.
- Maintaining state (sum, frequency, etc.) as the window moves.
- Reusing previous computations efficiently.

7. Example Visualization
------------------------
Problem: Longest substring without repeating characters

s = "abcabcbb"

| Step | Left | Right | Window | Seen     | MaxLen |
|------|------|--------|---------|----------|--------|
| 0    | 0    | 0      | "a"     | {a}      | 1      |
| 1    | 0    | 1      | "ab"    | {a,b}    | 2      |
| 2    | 0    | 2      | "abc"   | {a,b,c}  | 3      |
| 3    | 0    | 3      | "abca" (duplicate 'a') → shrink left → 1 | {b,c,a} | 3 |
| 4    | 1    | 4      | "bca"   | {b,c,a}  | 3      |
| 5    | 1    | 5      | "bcab" (duplicate 'b') → shrink left → 2 | {c,a,b} | 3 |

Result: maxLen = 3

8. Rule of Thumb to Identify Quickly
------------------------------------
If you ever see any of these in a problem statement:

- "subarray" or "substring"
- "continuous" or "contiguous"
- "longest / shortest / max / min"
- "sum" or "unique characters"

Then think Sliding Window.
"""
