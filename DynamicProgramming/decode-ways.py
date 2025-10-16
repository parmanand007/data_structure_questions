"""
Problem: Decode Ways
Category: Dynamic Programming
Link: https://leetcode.com/problems/decode-ways/

Statement:
----------
A message containing letters from A-Z is encoded as numbers using:
'A' -> 1, 'B' -> 2, ..., 'Z' -> 26

Given a string `s` containing only digits, return the number of ways to decode it.

Example 1:
----------
Input: s = "12"
Output: 2
Explanation: "AB" (1 2), "L" (12)

Example 2:
----------
Input: s = "226"
Output: 3
Explanation: "BZ" (2 26), "VF" (22 6), "BBF" (2 2 6)
"""

# ============================================================
# 🧩 APPROACH 1: BRUTE FORCE RECURSION
# ============================================================

"""
How to Think (Deep Intuition):
------------------------------
1️⃣ Identify what is being counted:
   - Every digit or pair of digits can form a letter if valid (1-26)
   - Count all valid decoding paths from start to end

2️⃣ Recursive decomposition:
   - At index i:
       * Take 1 digit → move to i+1 if it's not '0'
       * Take 2 digits → move to i+2 if number ≤ 26

3️⃣ Base case:
   - Reached end of string → 1 valid decoding
   - '0' cannot start a decoding → 0

4️⃣ Mental model:
   - Think like a tree:
     Each node branches into 1-digit and 2-digit choices (if valid)

Visualization Example:
----------------------
s = "12"

        dfs(0)
       /     \
   1-digit    2-digit
     |         |
  dfs(1)       dfs(2)
   |            |
 dfs(2)         1  → total 2 ways

Complexity:
-----------
Time:  O(2^n) — every index branches into 1 or 2 choices
Space: O(n) recursion depth
"""

def numDecodings_bruteforce(s: str) -> int:
    def dfs(i):
        if i == len(s):
            return 1
        if s[i] == '0':
            return 0
        ans = dfs(i + 1)
        if i + 1 < len(s) and int(s[i:i+2]) <= 26:
            ans += dfs(i + 2)
        return ans
    return dfs(0)


# ============================================================
# 🧩 APPROACH 2: MEMOIZATION (TOP-DOWN DP)
# ============================================================

"""
How to Think (Deep Intuition):
------------------------------
1️⃣ Recognize overlapping subproblems:
   - dfs(i) called multiple times with same i → store results

2️⃣ Memoization strategy:
   - Dictionary mapping index i → number of ways from i

3️⃣ Mental model:
   - Same recursion tree as brute force
   - But repeated branches return immediately from memo

Visualization Example:
----------------------
s = "226"

dfs(0)
 ├─ dfs(1)
 │   ├─ dfs(2)
 │   │   ├─ dfs(3) = 1
 │   │   └─ dfs(4) invalid
 │   └─ dfs(3) → reuse memo = 1
 └─ dfs(2) → reuse memo = 2

Complexity:
-----------
Time:  O(n) — each index computed once
Space: O(n) — recursion stack + memo dictionary
"""

def numDecodings_memo(s: str) -> int:
    memo = {}
    def dfs(i):
        if i in memo:
            return memo[i]
        if i == len(s):
            return 1
        if s[i] == '0':
            return 0
        ans = dfs(i + 1)
        if i + 1 < len(s) and int(s[i:i+2]) <= 26:
            ans += dfs(i + 2)
        memo[i] = ans
        return ans
    return dfs(0)


# ============================================================
# 🧩 APPROACH 3: DYNAMIC PROGRAMMING (BOTTOM-UP)
# ============================================================

"""
How to Think (Deep Intuition):
------------------------------
1️⃣ Convert top-down → bottom-up:
   - dp[i] = number of ways to decode substring starting at i

2️⃣ Base case:
   - dp[n] = 1 → empty string has 1 way

3️⃣ Fill dp from end → start:
   - If s[i] != '0', dp[i] = dp[i+1]
   - If two-digit number ≤ 26 → dp[i] += dp[i+2]

Visualization Example:
----------------------
s = "226", n=3

dp[3] = 1
dp[2] = s[2]='6' → dp[2]=dp[3]=1
dp[1] = s[1]='2' → dp[1]=dp[2]+dp[3] = 1+1=2
dp[0] = s[0]='2' → dp[0]=dp[1]+dp[2] = 2+1=3 → Answer

Complexity:
-----------
Time: O(n)
Space: O(n) — dp array
"""

def numDecodings_dp(s: str) -> int:
    n = len(s)
    dp = [0]*(n+1)
    dp[n] = 1
    for i in range(n-1, -1, -1):
        if s[i] == '0':
            dp[i] = 0
        else:
            dp[i] = dp[i+1]
            if i + 1 < n and int(s[i:i+2]) <= 26:
                dp[i] += dp[i+2]
    return dp[0]


# ============================================================
# 🧩 APPROACH 4: OPTIMAL SPACE (O(1) SPACE)
# ============================================================

"""
How to Think (Deep Intuition):
------------------------------
1️⃣ Observation:
   - dp[i] only depends on dp[i+1] and dp[i+2]

2️⃣ Maintain only two variables:
   - next1 = dp[i+1]
   - next2 = dp[i+2]

3️⃣ Iterate from end → start updating current:
   - curr = next1 + next2 (if valid two-digit number)
   - shift next2 = next1, next1 = curr

Visualization Example:
----------------------
s = "226"

next1=dp[3]=1, next2=0
i=2: curr=next1=1 → next2=next1=1, next1=1
i=1: curr=next1+next2=1+1=2 → next2=1, next1=2
i=0: curr=next1+next2=2+1=3 → Answer=3

Complexity:
-----------
Time: O(n)
Space: O(1)
"""

def numDecodings_optimal(s: str) -> int:
    n = len(s)
    next1, next2 = 1, 0
    for i in range(n-1, -1, -1):
        curr = 0
        if s[i] != '0':
            curr = next1
            if i + 1 < n and int(s[i:i+2]) <= 26:
                curr += next2
        next2, next1 = next1, curr
    return next1


# ============================================================
# ✅ Test Examples
# ============================================================

test_cases = ["12", "226", "0", "10", "111", "27", "101"]

for s in test_cases:
    print(f"String: '{s}'")
    print(" Brute Force      :", numDecodings_bruteforce(s))
    print(" Memoization      :", numDecodings_memo(s))
    print(" Bottom-Up DP     :", numDecodings_dp(s))
    print(" Optimal Space    :", numDecodings_optimal(s))
    print("-"*50)
