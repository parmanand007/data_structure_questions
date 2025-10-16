"""
Problem: Longest Palindromic Substring
Category: Dynamic Programming / String
Link: https://leetcode.com/problems/longest-palindromic-substring/

Statement:
----------
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also valid.

Example 2:
Input: s = "cbbd"
Output: "bb"
"""

# ============================================================
# 🧩 APPROACH 1: BRUTE FORCE
# ============================================================

"""
How to Think (Deep Intuition):
------------------------------
1️⃣ Identify the goal: Find the *longest substring* that reads the same forward and backward.

2️⃣ First idea: Check all possible substrings:
   - Start index i, end index j
   - Check if s[i:j+1] is palindrome
   - Keep track of the longest palindrome

3️⃣ Base reasoning:
   - Every single character is a palindrome
   - Two equal characters side by side form a palindrome

4️⃣ Mental model:
   - Imagine all possible substrings as nodes
   - Check each node for palindrome property
   - Keep the longest one

Visualization:
--------------
s = "babad"
Substrings:
b, ba, bab → palindrome, longest=3
a, ab, aba → palindrome, longest still=3
...

Complexity:
-----------
Time:  O(n^3)  → O(n^2) substrings * O(n) palindrome check
Space: O(1)   → only storing current longest
"""

def longestPalindrome_bruteforce(s: str) -> str:
    def isPalindrome(sub):
        return sub == sub[::-1]

    max_len = 0
    res = ""
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            sub = s[i:j+1]
            if isPalindrome(sub) and len(sub) > max_len:
                max_len = len(sub)
                res = sub
    return res

# ============================================================
# 🧩 APPROACH 2: DYNAMIC PROGRAMMING
# ============================================================

"""
How to Think (Deep Intuition):
------------------------------
1️⃣ Recognize overlapping subproblems:
   - s[i:j] is palindrome if s[i] == s[j] AND s[i+1:j-1] is palindrome

2️⃣ Define dp table:
   - dp[i][j] = True if s[i:j+1] is palindrome

3️⃣ Fill base cases:
   - dp[i][i] = True  (single character)
   - dp[i][i+1] = s[i]==s[i+1]  (two characters)

4️⃣ Build dp for length >= 3:
   - dp[i][j] = s[i]==s[j] and dp[i+1][j-1]

Visualization:
--------------
s = "babad"
dp table (True for palindrome):
b a b a d
T F T F F
  T F T F
    T F T
      T F
        T

Complexity:
-----------
Time:  O(n^2) → filling dp table
Space: O(n^2) → storing dp table
"""

def longestPalindrome_dp(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""

    dp = [[False]*n for _ in range(n)]
    start, max_len = 0, 1

    for i in range(n):
        dp[i][i] = True

    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            start = i
            max_len = 2

    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                start = i
                max_len = length

    return s[start:start+max_len]

# ============================================================
# 🧩 APPROACH 3: EXPAND AROUND CENTER
# ============================================================

"""
How to Think (Deep Intuition):
------------------------------
1️⃣ Observation: Palindrome mirrors around a center.
   - Center can be a single char (odd length)
   - Center can be between two chars (even length)

2️⃣ For each center:
   - Expand left and right while characters match
   - Update longest palindrome

3️⃣ Mental model:
   - Imagine every char as a potential pivot
   - Expand like a wave until mismatch

Visualization:
--------------
s = "babad", center at 'a' (index 1)
Expand: left='b', right='b' → matches → "bab"
Stop at next mismatch

Complexity:
-----------
Time:  O(n^2) → each expansion takes at most O(n) and we have O(n) centers
Space: O(1)  → only storing start and max_len
"""

def longestPalindrome_center(s: str) -> str:
    if not s:
        return ""

    start, max_len = 0, 0

    def expand(left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    for i in range(len(s)):
        len1 = expand(i, i)       # odd-length
        len2 = expand(i, i+1)     # even-length
        length = max(len1, len2)
        if length > max_len:
            max_len = length
            start = i - (length - 1)//2

    return s[start:start+max_len]

# ============================================================
# 🧩 APPROACH 4: MANACHER'S ALGORITHM
# ============================================================

"""
How to Think (Deep Intuition):
------------------------------
1️⃣ Transform string:
   - Insert '#' between letters to handle even/odd uniformly

2️⃣ Use array p[i]:
   - p[i] = palindrome radius around center i

3️⃣ Mirror property:
   - If i is inside a palindrome, p[i] can reuse mirrored value

4️⃣ Expand only when necessary:
   - Compare characters beyond known palindrome region

5️⃣ Extract result:
   - Longest radius → map back to original string

Visualization:
--------------
s = "babad" → t = "#b#a#b#a#d#"
p array records radius at each index

Complexity:
-----------
Time:  O(n) → each character expanded at most once
Space: O(n) → transformed string and p array
"""

def longestPalindrome_manacher(s: str) -> str:
    if not s:
        return ""
    
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0]*n
    c = r = 0
    max_len = 0
    center_index = 0
    
    for i in range(n):
        mirror = 2*c - i
        if i < r:
            p[i] = min(r-i, p[mirror])
        a, b = i + (1 + p[i]), i - (1 + p[i])
        while a < n and b >= 0 and t[a] == t[b]:
            p[i] += 1
            a += 1
            b -= 1
        if i + p[i] > r:
            c = i
            r = i + p[i]
        if p[i] > max_len:
            max_len = p[i]
            center_index = i
    
    start = (center_index - max_len)//2
    return s[start:start+max_len]
