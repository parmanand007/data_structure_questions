"""
Problem: Valid Palindrome
Category: String / Two Pointers
Link: https://leetcode.com/problems/valid-palindrome/

Statement:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward.

Given a string s, return True if it is a palindrome, or False otherwise.

Example:
Input: s = "A man, a plan, a canal: Panama"
Output: True

Input: s = "race a car"
Output: False
"""

"""
Brute Force Approach
--------------------
How to Think (for this solution only):
    - When you hear "palindrome", think: same forwards and backwards.
    - The simplest way: clean the string (keep only letters and digits), 
      make it lowercase, and compare it to its reverse.
    - This is the direct and most intuitive way to check a palindrome.

Steps:
    1. Filter out non-alphanumeric characters.
    2. Convert remaining characters to lowercase.
    3. Compare the cleaned string with its reversed version.

Complexity Explanation:
    - Time Complexity: O(N)
        → O(N) to clean + O(N) to reverse → O(N) overall.
    - Space Complexity: O(N)
        → new string created during cleaning.
"""

def isPalindrome_bruteforce(s: str) -> bool:
    cleaned = ""
    for ch in s:
        if ch.isalnum():  # keep only letters and digits
            cleaned += ch.lower()

    return cleaned == cleaned[::-1]


"""
Two Pointer Approach (Optimal)
------------------------------
How to Think (for this solution only):
    - Instead of creating a new string, think about **comparing characters in place**.
    - Use two pointers:
        → one starts from the beginning,
        → another from the end.
    - Move both inward while skipping invalid characters.
    - If all valid pairs match, it's a palindrome.

Why it’s better:
    - Avoids creating a new string.
    - Directly works on input with O(1) space.

Steps:
    1. Initialize two pointers (left = 0, right = len(s)-1).
    2. Move left forward until alphanumeric.
    3. Move right backward until alphanumeric.
    4. Compare lowercase characters.
    5. Continue until pointers cross or mismatch occurs.

Complexity Explanation:
    - Time Complexity: O(N)
        → Each character is visited at most once.
    - Space Complexity: O(1)
        → No extra data structures; in-place check.
"""

def isPalindrome_two_pointers(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        # Move left pointer to next alphanumeric
        while left < right and not s[left].isalnum():
            left += 1
        # Move right pointer to previous alphanumeric
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters (case insensitive)
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


"""
Optimized Pythonic Approach
---------------------------
How to Think (for this solution only):
    - Once you understand logic, leverage Python’s power.
    - Use list comprehensions and built-ins to clean efficiently.
    - Focus on clarity and expressiveness rather than step-by-step iteration.

Steps:
    1. Use list comprehension to keep only alphanumeric lowercase characters.
    2. Compare the list with its reverse.

Complexity Explanation:
    - Time Complexity: O(N)
        → Filtering + reverse comparison both O(N).
    - Space Complexity: O(N)
        → Stores cleaned characters in a list.
"""

def isPalindrome_pythonic(s: str) -> bool:
    filtered = [ch.lower() for ch in s if ch.isalnum()]
    return filtered == filtered[::-1]
