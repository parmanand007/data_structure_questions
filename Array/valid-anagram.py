"""
Problem: Valid Anagram
Category: String / Hashing
Link: https://leetcode.com/problems/valid-anagram/

Statement:
Given two strings s and t, return True if t is an anagram of s, and False otherwise.

An Anagram means both strings contain the same characters with the same frequency, 
but possibly in a different order.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: True

Example 2:
Input: s = "rat", t = "car"
Output: False
"""


"""
Sorting Approach
----------------
How to Think:
    - When both strings are anagrams, they contain exactly the same characters, just jumbled.
    - If we sort both strings alphabetically, they should look identical.
    - Hence, sort both and compare.

Steps:
    1. If lengths differ, immediately return False.
    2. Sort both strings.
    3. If sorted(s) == sorted(t), return True; else False.

Complexity Explanation:
    - Time Complexity: O(N log N)
        → Sorting takes O(N log N) for both strings (where N = len(s)).
    - Space Complexity: O(1)
        → If sorting is in-place (else O(N) if Python creates new strings).
"""

def isAnagram_sorting(s: str, t: str) -> bool:
    if len(s) != len(t):  # Quick check: anagrams must have equal length
        return False
    return sorted(s) == sorted(t)  # Compare sorted results


"""
HashMap / Frequency Count Approach
----------------------------------
How to Think:
    - Sorting is O(N log N); we can do better.
    - The definition of an anagram says: 
        → Each character must appear the same number of times in both strings.
    - So, count how many times each letter appears in both strings.
    - Compare the two frequency counts.

Steps:
    1. If lengths differ, return False.
    2. Create two dictionaries (or counters) for s and t.
    3. Count frequency of each character in both.
    4. Compare both dictionaries.

Complexity Explanation:
    - Time Complexity: O(N)
        → One pass for counting, one for comparison.
    - Space Complexity: O(1)
        → Since only 26 lowercase letters (fixed size alphabet), space is constant.
"""

from collections import Counter

def isAnagram_hashmap(s: str, t: str) -> bool:
    if len(s) != len(t):  # Quick check
        return False
    return Counter(s) == Counter(t)  # Compare character counts directly

"""
HashMap / Frequency Count Approach
----------------------------------
How to Think:
    - Sorting takes O(N log N), but we can achieve O(N) using counting.
    - The key idea: in an anagram, both strings must have the same frequency for each character.
    - Use hashmaps (dicts) to count character occurrences in both strings, then compare them.

Steps:
    1. If lengths differ, return False (quick elimination).
    2. Create two dictionaries (countS and countT) for frequency counts.
    3. Loop through both strings simultaneously:
         - Increment count for each character in both strings.
    4. After counting, compare both dictionaries.
    5. If equal → return True, else → return False.

Complexity Explanation:
    - Let n = length of the strings (s and t).
    - Time Complexity:
        1. Looping through the strings: O(n)
            - Each iteration updates the dictionary using get() and assignment.
            - Dictionary operations (lookup and insert) are O(1) on average.
        2. Comparing dictionaries: O(k)
            - k = number of unique characters in the string.
            - For lowercase English letters, k <= 26 → constant time.
        3. Total: O(n + k) ≈ O(n) in practice for lowercase letters.
        4. If the character set is arbitrary (e.g., Unicode), then k can be large → O(n + k).
    - Space Complexity:
        1. We use two dictionaries to store character counts.
        2. Each dictionary can have at most k entries (unique characters).
        3. For lowercase English letters, k <= 26 → O(1) space.
        4. For arbitrary characters, space = O(k), which may grow with input size.
"""

def isAnagram_hashmap(s: str, t: str) -> bool:
    if len(s) != len(t):  # Quick length check
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    return countS == countT


"""
Optimized Array Counting Approach (Best)
----------------------------------------
How to Think:
    - Problem guarantees lowercase English letters only ('a' to 'z').
    - Instead of a dictionary, we can use a fixed-size array of length 26.
    - Each index corresponds to one letter ('a' → 0, 'b' → 1, ...).
    - Increase counts for s, decrease for t.
    - If all counts return to zero → anagram.

Steps:
    1. If lengths differ, return False.
    2. Initialize a list of 26 zeros (for 'a'–'z').
    3. Loop through both s and t simultaneously:
         - Increment count for s[i].
         - Decrement count for t[i].
    4. After loop, check if all counts are zero.

Complexity Explanation:
    - Time Complexity: O(N)
        → Single pass through both strings.
    - Space Complexity: O(1)
        → Fixed-size array of length 26, independent of input length.
"""

def isAnagram_array(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = [0] * 26  # 26 letters
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1  # Increment for s
        count[ord(t[i]) - ord('a')] -= 1  # Decrement for t

    # If all zeros → anagram
    for c in count:
        if c != 0:
            return False
    return True
