"""
Problem: Climbing Stairs
Category: Dynamic Programming
Link: https://leetcode.com/problems/climbing-stairs/

Statement:
----------
You are climbing a staircase. It takes `n` steps to reach the top.
Each time you can either climb 1 or 2 steps.
Return the number of distinct ways you can climb to the top.

Example 1:
Input: n = 2
Output: 2
Explanation: (1+1), (2)

Example 2:
Input: n = 3
Output: 3
Explanation: (1+1+1), (1+2), (2+1)
"""

# ============================================================
# 🧩 APPROACH 1: BRUTE FORCE RECURSION
# ============================================================

"""
How to Think (Deep Intuition):
------------------------------
1️⃣ Identify what is being counted:
   - We need all possible sequences of steps (1 or 2) that sum to n.
   - Each position can be reached in multiple ways → branching problem.

2️⃣ Decide recursive decomposition:
   - Suppose we are at step i. To reach n:
       * We can take 1 step → go to i+1
       * We can take 2 steps → go to i+2
   - This gives the recurrence:
       ways(n) = ways(n-1) + ways(n-2)

3️⃣ Base cases:
   - n=0 → 1 way (we are already at the ground)
   - n=1 → 1 way (only 1 step possible)

4️⃣ Recursive tree reasoning:
   - Every call branches into 2 options.
   - The function will naturally explore all combinations of 1 and 2 steps.
   - Leaves represent reaching the top (n) or overshooting (return).

5️⃣ Mental checklist:
   - Are there repeated calculations? Yes → exponential work
   - Can it be simplified? Not yet, just understand the branching

6️⃣ Key intuition:
   - Think of this as "all paths in a binary tree of decisions"
"""

def climbStairs_bruteforce(n: int) -> int:
    if n <= 1:
        return 1
    return climbStairs_bruteforce(n-1) + climbStairs_bruteforce(n-2)

"""
Visualization Example (n=4):
----------------------------
f(4)
├─ f(3)
│  ├─ f(2)
│  │  ├─ f(1)
│  │  └─ f(0)
│  └─ f(1)
└─ f(2)
   ├─ f(1)
   └─ f(0)

Total ways = 5
"""

"""
Complexity:
-----------
Time: O(2^n) — exponential branching
Space: O(n) — recursion stack
"""


# ============================================================
# 🧩 APPROACH 2: MEMOIZATION (TOP-DOWN DP)
# ============================================================

"""
How to Think (Deep Intuition):
------------------------------
1️⃣ Identify inefficiency in brute force:
   - Subproblems repeat (e.g., ways(3) calculated multiple times)
   - Same inputs → same output → store results

2️⃣ Decide memoization strategy:
   - Use a dictionary (memo) mapping step → number of ways
   - At each recursive call, check memo before computing

3️⃣ Recursive structure remains:
   - The recursion tree is the same, but repeated branches return immediately from memo

4️⃣ How to think during recursion:
   - At each call, ask:
       a) Have I computed this before? → return memo
       b) Is base case? → return 1
       c) Else → compute recursively and store

5️⃣ Mental intuition:
   - Think: "I am exploring all paths, but once I know the number of paths from step i, I reuse it"
   - Reduces redundant computation drastically

6️⃣ Pattern recognition:
   - Classic top-down dynamic programming problem
   - Useful for any problem where recursion has overlapping subproblems
"""

def climbStairs_memo(n: int, memo=None) -> int:
    if memo is None:
        memo = {}
    if n <= 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = climbStairs_memo(n-1, memo) + climbStairs_memo(n-2, memo)
    return memo[n]

"""
Visualization Example (n=4):
----------------------------
Memo dictionary fills as recursion unwinds:
memo[0] = 1
memo[1] = 1
memo[2] = memo[1]+memo[0] = 2
memo[3] = memo[2]+memo[1] = 3
memo[4] = memo[3]+memo[2] = 5
Answer = 5
"""

"""
Complexity:
-----------
Time: O(n) — each subproblem computed once
Space: O(n) — recursion stack + memo dictionary
"""


# ============================================================
# 🧩 APPROACH 3: DYNAMIC PROGRAMMING (BOTTOM-UP)
# ============================================================

"""
How to Think (Deep Intuition):
------------------------------
1️⃣ Convert recursion → iteration:
   - Instead of thinking “from top to bottom”, think “build solution from bottom up”

2️⃣ Identify subproblem sequence:
   - dp[i] = number of ways to reach step i
   - dp[0]=1, dp[1]=1 → base cases

3️⃣ Build systematically:
   - dp[i] = dp[i-1] + dp[i-2]
   - Each dp[i] uses previously computed smaller subproblems
   - No recursion stack needed

4️⃣ Mental roadmap:
   - Start from 0 → compute 1 → compute 2 → ... → compute n
   - Each step uses only last two results (observation for optimization)
   - Think: “I am accumulating the number of ways iteratively”

5️⃣ How to reason correctness:
   - For any step i, only two possibilities: came from i-1 or i-2
   - Sum of ways to reach i-1 and i-2 = total ways to reach i

6️⃣ Key intuition:
   - Bottom-up DP replaces recursion + memo
   - Easier to debug because no stack, all results in dp array
"""

def climbStairs_dp(n: int) -> int:
    if n <= 1:
        return 1
    dp = [0]*(n+1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

"""
Visualization Example (n=5):
----------------------------
dp array fills iteratively:
dp[0] = 1
dp[1] = 1
dp[2] = dp[1]+dp[0] = 2
dp[3] = dp[2]+dp[1] = 3
dp[4] = dp[3]+dp[2] = 5
dp[5] = dp[4]+dp[3] = 8
Answer = 8
"""

"""
Complexity:
-----------
Time: O(n) — iterate through 2..n
Space: O(n) — dp array
"""


# ============================================================
# 🧩 APPROACH 4: OPTIMAL SPACE (FIBONACCI STYLE)
# ============================================================

"""
How to Think (Deep Intuition):
------------------------------
1️⃣ Observation:
   - dp[i] only depends on dp[i-1] and dp[i-2]
   - We don’t need full array → can optimize space

2️⃣ Mental model:
   - prev2 = ways to reach i-2
   - prev1 = ways to reach i-1
   - current = prev1 + prev2
   - Slide window forward

3️⃣ Mental roadmap:
   - Initialize prev2 = 1, prev1 = 1
   - For i = 2 to n:
       * compute current = prev1 + prev2
       * shift prev2 = prev1, prev1 = current

4️⃣ How to reason correctness:
   - Each iteration produces the same result as dp[i]
   - Only two variables suffice because Fibonacci recurrence

5️⃣ Key intuition:
   - Space-optimized bottom-up DP
   - Linear time, constant space
   - Best practical approach
"""

def climbStairs_optimal(n: int) -> int:
    if n <= 1:
        return 1
    prev2, prev1 = 1, 1
    for _ in range(2, n+1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
    return prev1

"""
Visualization Example (n=5):
----------------------------
Iteration table:

i | prev2 | prev1 | curr
------------------------
2 | 1     | 1     | 2
3 | 1     | 2     | 3
4 | 2     | 3     | 5
5 | 3     | 5     | 8

Answer = 8
"""

"""
Complexity:
-----------
Time: O(n) — single iteration from 2..n
Space: O(1) — only prev1, prev2, curr variables
"""
