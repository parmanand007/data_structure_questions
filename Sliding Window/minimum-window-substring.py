"""
Problem: Minimum Window Substring
Category: Sliding Window / Two Pointers
Link: https://leetcode.com/problems/minimum-window-substring/

Statement:
----------
Given two strings s and t, return the minimum window substring of s 
such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return an empty string "".

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Example 2:
Input: s = "a", t = "a"
Output: "a"

Example 3:
Input: s = "a", t = "aa"
Output: ""
"""

# ============================================================
# 🧩 APPROACH 1: BRUTE FORCE
# ============================================================

"""
How to Think:
-------------
When you see “minimum window substring” your first thought:
→ "Let's check all possible substrings and see which one contains all characters of t."

This is your *brute force* starting point — no optimization yet, just verifying the concept.

1. Generate all substrings of s.
2. Check if each substring contains all characters from t (frequency included).
3. Track the shortest valid substring.

It’s inefficient, but helps you *understand the pattern* before optimizing.

Visualization:
---------------
s = "ADOBECODEBANC", t = "ABC"

All substrings that contain A, B, C are:
→ "ADOBEC", "DOBECODEBA", "BECODEBANC", "BANC"
Among them, the smallest is "BANC"

Algorithm Steps:
----------------
1. Loop `i` from 0 to len(s)
2. Loop `j` from i+1 to len(s)
3. Check if substring s[i:j] contains all characters of t
4. Track the shortest substring found

Complexity:
-----------
Time: O(n³) → Generate O(n²) substrings * O(n) check for inclusion
Space: O(1)
"""

def minWindow_bruteforce(s: str, t: str) -> str:
    from collections import Counter

    def contains(sub: str, t_count: dict) -> bool:
        sub_count = Counter(sub)
        for ch in t_count:
            if sub_count[ch] < t_count[ch]:
                return False
        return True

    t_count = Counter(t)
    min_len = float("inf")
    res = ""

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            if contains(sub, t_count) and len(sub) < min_len:
                res = sub
                min_len = len(sub)
    return res

# Example:
# print(minWindow_bruteforce("ADOBECODEBANC", "ABC"))  # Output: "BANC"


# ============================================================
# 🧩 APPROACH 2: OPTIMIZED USING CHARACTER FILTERING
# ============================================================

"""
How to Think:
-------------
Brute force rechecks many useless substrings.
Notice: we only care about characters that are in t!

→ So we can *filter s* and only iterate over characters that matter.

1. Preprocess s → keep only (index, char) where char is in t.
2. Then apply a mini sliding window on this filtered list.
3. This avoids checking irrelevant characters and reduces window size dramatically.

Visualization:
---------------
s = "ADOBECODEBANC", t = "ABC"
Filtered s = [(0, 'A'), (3, 'B'), (5, 'C'), (9, 'B'), (10, 'A'), (12, 'C')]
Now apply window only over this filtered array.

Algorithm Steps:
----------------
1. Build Counter for t.
2. Filter s keeping only chars in t.
3. Use left, right pointers on filtered list.
4. Expand right until window valid → shrink left to minimize.
5. Keep track of smallest valid window.

Complexity:
-----------
Time: O(2n)  → Each char processed max twice
Space: O(n)
"""

from collections import Counter

def minWindow_filtered(s: str, t: str) -> str:
    if not s or not t:
        return ""

    t_count = Counter(t)
    required = len(t_count)

    filtered_s = [(i, ch) for i, ch in enumerate(s) if ch in t_count]

    l = 0
    formed = 0
    window_count = {}
    ans = (float("inf"), None, None)

    for r in range(len(filtered_s)):
        ch = filtered_s[r][1]
        window_count[ch] = window_count.get(ch, 0) + 1

        if window_count[ch] == t_count[ch]:
            formed += 1

        while l <= r and formed == required:
            start = filtered_s[l][0]
            end = filtered_s[r][0]
            if end - start + 1 < ans[0]:
                ans = (end - start + 1, start, end)

            left_char = filtered_s[l][1]
            window_count[left_char] -= 1
            if window_count[left_char] < t_count[left_char]:
                formed -= 1
            l += 1

    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]

# Example:
# print(minWindow_filtered("ADOBECODEBANC", "ABC"))  # Output: "BANC"


# ============================================================
# 🧩 APPROACH 3: OPTIMAL SLIDING WINDOW
# ============================================================

"""
How to Think:
-------------
This is a *classic variable-size sliding window* problem.

When you hear:
   - “minimum window” or “substring”
   - “must contain all characters”
   → think: **Sliding Window + HashMap**

Directional thinking 👇:

1. What do we need to maintain?
   → Whether current window contains all chars from t with required frequency.

2. What are we tracking?
   → Window character frequencies + how many required chars are satisfied.

3. When to expand vs contract?
   → Expand right until valid.
     Shrink left until invalid (to get smallest valid window).

4. When valid?
   → When all required chars are satisfied (have == need_count)

Visualization:
---------------
Let s = "ADOBECODEBANC", t = "ABC"

Step | Left | Right | Window        | Valid? | Action
------------------------------------------------------
1    | 0    | 0     | "A"           | No     | expand right
2    | 0    | 5     | "ADOBEC"      | Yes    | shrink left
3    | 1    | 5     | "DOBEC"       | No     | expand right
4    | 3    | 12    | "BECODEBANC"  | Yes    | shrink left
5    | 9    | 12    | "BANC"        | ✅ Yes | best window found

Algorithm Steps:
----------------
1. Build `need` map for t.
2. Initialize:
   - window = {}
   - have = 0
   - need_count = len(need)
   - res = [-1, -1], res_len = ∞
   - left = 0
3. Move right pointer:
   - Add s[right] to window.
   - If freq matches need → have += 1.
   - While have == need_count:
        * Update best result.
        * Shrink from left and update have.
4. Return substring from res.

Complexity:
-----------
Time: O(n + m)
Space: O(1)  (at most 52 chars in hashmap)

Key Intuition:
---------------
Expand window → gain validity.
Shrink window → gain minimality.
Balance both → get smallest valid window.
"""

def minWindow_optimal(s: str, t: str) -> str:
    if not t or not s:
        return ""

    # Step 1: Build frequency map for t
    need = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1

    window = {}       # Frequency of chars in current window
    have = 0          # How many unique chars satisfied
    need_count = len(need)

    res = [-1, -1]    # store indices of smallest window
    res_len = float("inf")
    left = 0

    # Step 2: Expand the window
    for right in range(len(s)):
        ch = s[right]
        window[ch] = window.get(ch, 0) + 1

        # Check if this char satisfies a requirement
        if ch in need and window[ch] == need[ch]:
            have += 1

        # Step 3: Try to shrink window when valid
        while have == need_count:
            # Update smallest valid window
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = right - left + 1

            # Pop leftmost char and shrink window
            window[s[left]] -= 1
            if s[left] in need and window[s[left]] < need[s[left]]:
                have -= 1  # window became invalid
            left += 1  # move left pointer forward

    l, r = res
    return s[l:r + 1] if res_len != float("inf") else ""

# Example:
# s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
print(minWindow_optimal("ADOBECODEBANC", "ABC"))
