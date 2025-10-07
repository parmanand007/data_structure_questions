"""
Problem: Encode and Decode Strings
Category: String / Hashing
Link: https://leetcode.com/problems/encode-and-decode-strings/

Statement:
Design an algorithm to encode a list of strings to a single string, and decode it back.
You need to implement:
    - encode(strs: List[str]) -> str
    - decode(s: str) -> List[str]

Example:
Input: ["hello","world"]
Encoded string: "5#hello5#world"
Decoded output: ["hello","world"]
"""

"""
Delimiter-based Approach
------------------------
How to Think (Problem-solving intuition):
    1. Understand the problem: You need to convert a list of strings into a single string, then recover the original list exactly.
    2. Identify constraints:
        - Strings may contain any character (including common delimiters like ',' or '#').
        - Simple joining with a fixed delimiter may fail if the delimiter exists inside the string.
    3. Look for a unique way to separate strings:
        - Use the **length of the string** as a prefix. This guarantees you can always extract the exact string, regardless of its content.
    4. Decide encoding format:
        - "<length>#<string>" is simple and unambiguous.
    5. For decoding:
        - Use the length prefix to know exactly how many characters to read.
        - This avoids issues with delimiters inside strings.
    6. Intuition summary:
        - Always think about **what information is necessary to uniquely recover the original data**.
        - When delimiters can appear in strings, using length or structured metadata is a robust solution.

Steps:
1. Encoding:
    - For each string, append "<length>#<string>" to the result.
    - Join all such segments to get a single encoded string.
2. Decoding:
    - Iterate through the encoded string.
    - Read characters until '#' to get the length of the next string.
    - Read the next 'length' characters as the string.
    - Repeat until the end of the encoded string.

Complexity Explanation:
    - Time Complexity: O(N), N = total number of characters in all strings
    - Space Complexity: O(N), for storing encoded string and decoded list
"""

from typing import List

def encode(strs: List[str]) -> str:
    """Encode a list of strings to a single string"""
    encoded = ""
    for s in strs:
        encoded += f"{len(s)}#{s}"  # Format: length#string
    return encoded

def decode(s: str) -> List[str]:
    """Decode a single string back to list of strings"""
    decoded = []
    i = 0
    while i < len(s):
        # Find the delimiter '#' to get the length of the string
        j = i
        while s[j] != '#':
            j += 1
        length = int(s[i:j])
        # Extract the string of 'length' characters
        decoded.append(s[j+1:j+1+length])
        i = j + 1 + length  # Move to the next encoded segment
    return decoded

