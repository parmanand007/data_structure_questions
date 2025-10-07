"""
Problem: Group Anagrams
Category: String / HashMap
Link: https://leetcode.com/problems/group-anagrams/

Statement:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word formed by rearranging the letters of another word, using all letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""

"""
Sorted String as Key Approach
-----------------------------
How to Think (for this solution only):
    - For anagrams, sorting the characters in a word gives the same string for all anagrams.
    - So, we can use the sorted string as a key in a dictionary to group them.

Steps:
    1. Initialize a dictionary `anagram_groups` (key: sorted string, value: list of strings).
    2. Iterate through each string:
         - Sort the string → key
         - Append the string to `anagram_groups[key]`.
    3. Return all values (lists) from the dictionary.

Complexity Explanation:
    - Let n = number of strings, k = maximum length of a string.
    - Time Complexity:
        - Sorting each string: O(k log k)
        - Iterating n strings: O(n * k log k)
        - Total: O(n * k log k)
    - Space Complexity:
        - Dictionary stores all strings: O(n * k)
"""

from typing import List
from collections import defaultdict

def groupAnagrams_sorted(strs: List[str]) -> List[List[str]]:
    anagram_groups = defaultdict(list)

    for s in strs:
        key = ''.join(sorted(s))  # Sorted string as key
        anagram_groups[key].append(s)

    return list(anagram_groups.values())



"""
Character Count as Key Approach (Optimized)
------------------------------------------
How to Think (for this solution only):
    - Instead of sorting, we can represent each string by a character frequency count.
    - Anagrams will produce the same frequency array → use as a key in a dictionary.

Steps:
    1. Initialize a dictionary `anagram_groups`.
    2. For each string:
         - Initialize a 26-length array `count` to 0.
         - Count frequency of each character.
         - Convert array to tuple → key
         - Append string to `anagram_groups[key]`.
    3. Return all values (lists) from the dictionary.

Complexity Explanation:
    - Let n = number of strings, k = maximum length of a string.
    - Time Complexity: O(n * k)
        - Counting characters in each string: O(k)
        - Looping over n strings: O(n * k)
    - Space Complexity: O(n * k)
        - Dictionary stores all strings
        - Keys are tuples of length 26 → O(n)
"""

def groupAnagrams_count(strs: List[str]) -> List[List[str]]:
    anagram_groups = defaultdict(list)

    for s in strs:
        count = [0] * 26  # 26 lowercase letters
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        key = tuple(count)  # Immutable tuple can be dictionary key
        anagram_groups[key].append(s)

    return list(anagram_groups.values())
