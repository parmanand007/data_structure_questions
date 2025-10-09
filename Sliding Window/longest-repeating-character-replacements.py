"""
Problem: Longest Repeating Character Replacement
Category: String / Sliding Window
Link: https://leetcode.com/problems/longest-repeating-character-replacement/

Statement:
You are given a string s and an integer k. You can choose any character of the string
and change it to any other uppercase English character. You can perform this operation
at most k times.

Return the length of the longest substring containing the same letter you can get after 
performing the above operations.

Example:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace both 'A's with 'B's or both 'B's with 'A's.

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'B' in the middle to get "AAAA".
"""

"""
Brute Force Approach
--------------------
How to Think (for this solution only):
    Rephrase the problem:
        → “I can choose a window (substring) and change at most k characters inside it to make all characters same.”
        → So I want the longest substring where after ≤ k changes, it’s uniform.
        First Intuition:
        -    ry every substring — for each substring, check if you can make it valid (by counting most frequent char and how many need to be changed).
            This is brute force because we are trying all possibilities.

        Key Insight:

            For any substring:
            → If (len(substring) - max_frequency_char_count) <= k,
            then we can replace the rest and make it uniform.

        So our plan:
            Loop through all substrings.
            For each, count the frequency of chars.
            Check if it’s valid (using formula above).
            Keep max valid length.

Steps:
    1. Iterate through all substrings (two loops).
    2. For each substring, count frequency of all characters.
    3. Check if replacements needed ≤ k.
    4. Track maximum valid length.

Complexity Explanation:
    - Time Complexity: O(N³)
        → O(N²) substrings × O(N) to count frequency.
    - Space Complexity: O(1)
        → Constant extra space for 26 letters.
"""

def characterReplacement_bruteforce(s: str, k: int) -> int:
    max_len = 0
    n = len(s)

    for i in range(n):
        for j in range(i, n):
            freq = [0] * 26
            for ch in s[i:j+1]:
                freq[ord(ch) - ord('A')] += 1
            max_freq = max(freq)
            if (j - i + 1) - max_freq <= k:
                max_len = max(max_len, j - i + 1)
    return max_len

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            count, maxf = {}, 0
            for j in range(i, len(s)):
                count[s[j]] = 1 + count.get(s[j], 0)
                maxf = max(maxf, count[s[j]])
                if (j - i + 1) - maxf <= k:
                    res = max(res, j - i + 1)
        return res


"""
Optimal Sliding Window Approach
-------------------------------

How to Think (for this solution only):
--------------------------------------
This is a classic *variable-size sliding window* problem.

The key observation: we want the **longest substring** we can make into repeating characters 
after replacing at most `k` characters.

To think in the right direction:
    1. Ask yourself: “Do I need to find a longest/shortest subarray or substring that satisfies some condition?”
       → YES → Sliding Window.

    2. Think about what makes a window “valid.”
       - Here, a window is valid if we can make all characters the same 
         by changing at most `k` of them.
       - That means: (window_length - count_of_most_frequent_char) ≤ k

    3. So we must track:
        - `window_length = right - left + 1`
        - `max_freq = frequency of most common character in the current window`

    4. Move the window like this:
        - Expand the right side by including new characters.
        - If the window becomes invalid (needs more than k changes), shrink from the left.
        - Keep updating the maximum valid window length.

Why we don't recompute max_freq every time:
    - Even if we shrink, the previously recorded max_freq might be slightly outdated,
      but it doesn’t affect correctness, since the window will shrink until valid again.
    - This keeps the algorithm O(n).

Visualization:
---------------
Example: s = "AABABBA", k = 1

Step | Window | Max_Freq | (Size - Max_Freq) | Valid | Action
---------------------------------------------------------------
 1   | "A"        1            0              ✅     expand
 2   | "AA"       2            0              ✅     expand
 3   | "AAB"      2            1              ✅     expand
 4   | "AABA"     3            1              ✅     expand
 5   | "AABAB"    3            2              ❌     shrink left
 6   | "ABAB"     2            2              ❌     shrink left
 7   | "BAB"      2            1              ✅     expand

Max valid window length = 4 → "AABA" or "ABBA"

Algorithm Steps:
----------------
1. Initialize two pointers `left = 0` and `right = 0`
2. Use a hashmap `freq` to store frequency of chars in window
3. Track `max_freq` (highest frequency of any char in window)
4. For each step:
   - Add right char to window
   - Update `max_freq`
   - If window invalid → shrink from left
   - Update max window length
5. Return max valid length

Complexity Analysis:
--------------------
Let n = length of input string s

Time Complexity:
    - O(n): Each character is visited at most twice (once by right, once by left)
Space Complexity:
    - O(26) = O(1): Frequency map stores at most 26 characters

Key Intuition Recap:
--------------------
Think “grow window until invalid → then shrink until valid again.”
That’s the heart of every variable-size sliding window problem.

"""

def characterReplacement_sliding_window(s: str, k: int) -> int:
    freq = {}
    left = 0
    max_len = 0
    max_freq = 0

    for right in range(len(s)):
        freq[s[right]] = 1 + freq.get(s[right], 0)
        max_freq = max(max_freq, freq[s[right]])

        # If replacements needed exceed k, shrink window
        while (right - left + 1) - max_freq > k:
            freq[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


"""
Visualization Example
---------------------
Example: s = "AABABBA", k = 1

Step | Left | Right | Window | FreqMap      | MaxFreq | (window - maxFreq) | Action
-----|-------|--------|---------|--------------|----------|---------------------|--------
0 | 0 | 0 | "A" | {'A':1} | 1 | 0 | valid → max_len=1
1 | 0 | 1 | "AA" | {'A':2} | 2 | 0 | valid → max_len=2
2 | 0 | 2 | "AAB" | {'A':2,'B':1} | 2 | 1 | valid → max_len=3
3 | 0 | 3 | "AABA" | {'A':3,'B':1} | 3 | 1 | valid → max_len=4
4 | 0 | 4 | "AABAB" | {'A':3,'B':2} | 3 | 2 | invalid → shrink
   → left++ → left=1 → window="ABAB"
5 | 1 | 5 | "ABABB" | {'A':2,'B':3} | 3 | 2 | invalid → shrink
   → left++ → left=2 → window="BABB"
6 | 2 | 6 | "ABBBA" | {'A':2,'B':3} | 3 | 1 | valid → max_len=4

Result: 4
"""


"""
Comparison Summary
------------------
| Approach | Data Structure Used | Time Complexity | Space Complexity | Notes |
|-----------|--------------------|-----------------|------------------|--------|
| Brute Force | Array (26 chars) | O(N³) | O(1) | Checks all substrings |
| Sliding Window | HashMap | O(N) | O(1) | Expands/contracts dynamically |
"""
