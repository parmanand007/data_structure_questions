"""
Problem: Longest Substring Without Repeating Characters
Category: String / Sliding Window / Two Pointers
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Statement:
Given a string s, find the length of the longest substring without repeating characters.

Example:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with length = 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b".
"""

"""
Brute Force Approach
--------------------
How to Think (for this solution only):
    - Whenever you hear "substring" + "without repeating characters", your first instinct might be:
      → Try all possible substrings and check which one has unique characters.
    - This means generating every substring (O(N²)) and verifying uniqueness using a set.

Steps:
    1. Generate all substrings using two loops (i, j).
    2. For each substring, check if all characters are unique.
    3. Keep track of the maximum length found.

Complexity Explanation:
    - Time Complexity: O(N³)
        → O(N²) substrings × O(N) to check uniqueness.
    - Space Complexity: O(N)
        → Temporary set to store unique characters.
"""

def lengthOfLongestSubstring_bruteforce(s: str) -> int:
    def all_unique(sub):
        return len(set(sub)) == len(sub)

    max_len = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if all_unique(s[i:j+1]):
                max_len = max(max_len, j - i + 1)
    return max_len


"""
Sliding Window with Set (Better Approach)
-----------------------------------------
How to Think (for this solution only):
    - Brute force rechecks the entire substring again and again — wasteful.
    - Instead, think dynamically:
        → As you move through the string, maintain a "window" of unique characters.
        → Expand the window when no duplicates.
        → Shrink the window when a duplicate appears.

    - This forms the **core sliding window pattern**:
        → Expand with `right` pointer.
        → Shrink with `left` pointer when condition breaks.

Steps:
    1. Initialize two pointers (left, right) and a set to store current unique characters.
    2. Expand right until a duplicate character is found.
    3. When duplicate found, move left pointer to remove characters until duplicate is gone.
    4. Update max length each step.

Complexity Explanation:
    - Time Complexity: O(2N) ≈ O(N)
        → Each character visited at most twice (once by left, once by right).
    - Space Complexity: O(min(N, charset))
        → Set stores at most unique characters currently in window.
"""

def lengthOfLongestSubstring_sliding_window_set(s: str) -> int:
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


"""
Optimized Sliding Window with HashMap (Most Efficient)
------------------------------------------------------
How to Think (for this solution only):
    - In the previous approach, when a duplicate appears,
      we move the left pointer **one by one** — can we jump faster?
    - Yes, if we **store the last index** of every character.
    - When we see a duplicate, we can directly move `left` to `last_seen_index + 1`.
    - This reduces unnecessary left pointer movement.

    - This is the **optimized sliding window** version using HashMap.

Steps:
    1. Use a dictionary `last_seen` to store the last seen index of each character.
    2. Iterate through string with `right` pointer.
    3. If character already seen and last index ≥ left,
       then move left to `last_seen[ch] + 1` to skip duplicates.
    4. Update last_seen[ch] = right and compute max length.

Complexity Explanation:
    - Time Complexity: O(N)
        → Each character processed once.
    - Space Complexity: O(min(N, charset))
        → Dictionary for character indices.
"""

def lengthOfLongestSubstring_optimal(s: str) -> int:
    last_seen = {}
    left = 0
    max_len = 0

    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1  # Jump directly past last duplicate
        last_seen[ch] = right
        max_len = max(max_len, right - left + 1)

    return max_len


"""
Visualization Example
---------------------
Example: s = "abcabcbb"

Step | Left | Right | Char | Last Seen | Window | MaxLen
-----|-------|--------|------|------------|---------|--------
0 | 0 | 0 | a | {a:0} | "a" | 1
1 | 0 | 1 | b | {a:0,b:1} | "ab" | 2
2 | 0 | 2 | c | {a:0,b:1,c:2} | "abc" | 3
3 | 0 | 3 | a | {a:3,b:1,c:2} | move left→1 | "bca" | 3
4 | 1 | 4 | b | {a:3,b:4,c:2} | move left→2 | "cab" | 3
5 | 2 | 5 | c | {a:3,b:4,c:5} | move left→3 | "abc" | 3
6 | 3 | 6 | b | {a:3,b:6,c:5} | move left→5 | "cb" | 3
7 | 5 | 7 | b | {a:3,b:7,c:5} | move left→7 | "b" | 3

Result: maxLen = 3  → “abc”
"""


"""
Comparison Summary
------------------
| Approach | Data Structure Used | Time Complexity | Space Complexity | Notes |
|-----------|--------------------|-----------------|------------------|--------|
| Brute Force | Set | O(N³) | O(N) | Very slow, checks all substrings |
| Sliding Window (Set) | Set | O(N) | O(N) | Efficient but shifts left one-by-one |
| Optimized Sliding Window | HashMap | O(N) | O(N) | Fastest, directly jumps over duplicates |
"""
