"""
Problem: Palindromic Substrings
Category: Dynamic Programming / String
Link: https://leetcode.com/problems/palindromic-substrings/

Statement:
----------
Given a string s, return the number of substrings within s that are palindromes.
A palindrome is a string that reads the same forward and backward.

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic substrings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic substrings: "a", "a", "a", "aa", "aa", "aaa".
"""

# ============================================================
# 🧩 APPROACH 1: BRUTE FORCE (CHECK ALL SUBSTRINGS)
# ============================================================

"""
How to Think (Deep Intuition):
------------------------------
1️⃣ Identify what is being counted:
   - Every contiguous substring that is a palindrome counts.
   
2️⃣ Brute force approach:
   - Generate all possible substrings of s
   - Check each substring for palindrome property (read same forward/backward)
   
3️⃣ Recursive/iterative check:
   - For substring s[i:j+1], check if s[i]==s[j] recursively inward.
   
4️⃣ Mental model:
   - Think of all substrings as a 2D grid (start index i, end index j)
   - Each cell represents a substring s[i:j+1]
   - Check palindrome property for each cell
"""

def countSubstrings_bruteforce(s: str) -> int:
    def isPalindrome(sub: str) -> bool:
        return sub == sub[::-1]

    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i, n):
            if isPalindrome(s[i:j+1]):
                count += 1
    return count

"""
Visualization:
---------------
s = "aaa"
Substrings checked:
"a" → yes
"aa" → yes
"aaa" → yes
"a" → yes
"aa" → yes
"a" → yes
Total = 6

Complexity:
-----------
Time:  O(n^3) → O(n^2) substrings × O(n) check each
Space: O(1)
"""

# ============================================================
# 🧩 APPROACH 2: EXPAND AROUND CENTER
# ============================================================

"""
How to Think (Deep Intuition):
------------------------------
1️⃣ Observation:
   - Every palindrome mirrors around its center
   - A palindrome can have:
     * Odd length → single character center
     * Even length → two-character center

2️⃣ Mental roadmap:
   - For each index i in string:
     * Expand around center i (odd length)
     * Expand around center i,i+1 (even length)
   - Count all valid expansions

3️⃣ Why efficient:
   - Avoids generating all substrings
   - Each center expands at most n times

4️⃣ How to reason correctness:
   - Any palindrome must have a center
   - Expanding captures all possibilities
"""

def countSubstrings_center(s: str) -> int:
    n = len(s)
    count = 0

    def expand(l: int, r: int) -> int:
        c = 0
        while l >= 0 and r < n and s[l] == s[r]:
            c += 1
            l -= 1
            r += 1
        return c

    for i in range(n):
        count += expand(i, i)     # odd length
        count += expand(i, i+1)   # even length

    return count

"""
Visualization:
---------------
s = "aaa"
Centers:
i=0: "a" → count=1, expand even "aa" → count=2
i=1: "a" → count=3, expand even "aa" → count=4, expand odd "aaa" → count=5
i=2: "a" → count=6
Total = 6

Complexity:
-----------
Time: O(n^2) → each center may expand to n length
Space: O(1)
"""

# ============================================================
# 🧩 APPROACH 3: DYNAMIC PROGRAMMING (DP TABLE)
# ============================================================

"""
How to Think (Deep Intuition):
------------------------------
1️⃣ Observation:
   - Use dp[i][j] = True if s[i..j] is palindrome
   - Recurrence:
       * dp[i][j] = True if s[i]==s[j] and (j-i <=2 or dp[i+1][j-1] is True)
       * j-i <=2 covers length 1 and 2 substrings

2️⃣ Build systematically:
   - Fill table for increasing substring lengths
   - Count when dp[i][j] = True

3️⃣ Mental roadmap:
   - Start from length 1 → mark all dp[i][i] = True
   - Length 2 → check equality
   - Length >=3 → use dp[i+1][j-1]
"""

def countSubstrings_dp(s: str) -> int:
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    count = 0

    for length in range(1, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j]:
                if length <= 2:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i+1][j-1]
            if dp[i][j]:
                count += 1

    return count

"""
Visualization:
---------------
s = "aaa"
dp table:
[True, True, True]
[False, True, True]
[False, False, True]
Total = 6 palindromes

Complexity:
-----------
Time: O(n^2)
Space: O(n^2)
"""
