"""
Problem: How to Identify and Approach Dynamic Programming Problems
Category: Algorithmic Thinking / DP Template
"""

# ============================================================
# 🧩 DP THINKING TEMPLATE
# ============================================================

"""
Step 1: Identify if DP is applicable
------------------------------------
1️⃣ Overlapping subproblems:
   - Does the problem ask you to solve the same smaller problem multiple times?
   - Example: Fibonacci, paths in grid, climbing stairs

2️⃣ Optimal substructure:
   - Can a solution to a bigger problem be constructed from solutions to smaller problems?
   - Example: max sum of subarray ending at i → depends on max sum ending at i-1

3️⃣ Problem asks for:
   - Count of ways
   - Maximum / Minimum value
   - Whether some state is possible (True/False)
   - This is a hint for DP

Step 2: Define the state
------------------------
- Determine what parameters uniquely define a subproblem
- Example: 
   * For climbing stairs: step number i → dp[i]
   * For knapsack: item index + remaining weight → dp[i][w]
   * For palindrome substring: start index + end index → dp[i][j]

Step 3: Recurrence relation
---------------------------
- How does a subproblem relate to smaller subproblems?
- Example:
   * Fibonacci: f(n) = f(n-1) + f(n-2)
   * House robber: dp[i] = max(dp[i-1], nums[i] + dp[i-2])

Step 4: Base cases
------------------
- Identify smallest subproblems that can be solved trivially
- Example:
   * Fibonacci: f(0)=0, f(1)=1
   * Climbing stairs: dp[0]=1, dp[1]=1
   * Palindrome substring: dp[i][i]=True

Step 5: Top-Down or Bottom-Up
-----------------------------
- Top-Down: Recursion + memoization → easier to write initially
- Bottom-Up: Iterative → often more efficient, avoids recursion stack

Step 6: Optimization
--------------------
- Can we reduce space? Often you don’t need full DP table
- Example: Fibonacci / climbing stairs → O(1) space
"""

# ============================================================
# 🧩 DP THINKING EXAMPLE FUNCTION (Template)
# ============================================================

def dp_problem_template():
    """
    Example Template: Generic DP problem
    """
    
    # Step 1: Define state function
    def state(params):
        """
        Describe what each state represents
        """
        # Example: f(i) = solution for subproblem ending at index i
        pass

    # Step 2: Base cases
    base_cases = {}
    # base_cases[i] = value for trivial subproblem i

    # Step 3: Recurrence
    # Recurrence relation using smaller states
    # f(i) = some combination of f(j) where j < i

    # Step 4: Implement memoization if top-down
    memo = {}

    def solve(i):
        if i in memo:
            return memo[i]
        # compute using recurrence
        result = 0
        # ...
        memo[i] = result
        return result

    # Step 5: Bottom-up implementation (optional)
    # dp = [0] * n
    # for i in range(n):
    #     dp[i] = ... recurrence using dp[...]
    
    # Step 6: Return final answer
    return 0

# ============================================================
# 🧩 EXAMPLE USAGE
# ============================================================

"""
Suppose we have Climbing Stairs problem:
1️⃣ Overlapping subproblems? → Yes, f(n-1), f(n-2)
2️⃣ Optimal substructure? → Yes, ways(n) = ways(n-1)+ways(n-2)
3️⃣ State? → f(i) = ways to reach step i
4️⃣ Base case? → f(0)=1, f(1)=1
5️⃣ Implement top-down or bottom-up
6️⃣ Optimize space → only store last 2 values
"""

def climbStairs_example(n: int) -> int:
    if n <= 1:
        return 1
    prev2, prev1 = 1, 1
    for _ in range(2, n+1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
    return prev1

"""
Key Intuition Summary:
---------------------
- Ask: Can I break problem into smaller subproblems? (Overlapping + Optimal substructure)
- Define state clearly
- Find recurrence
- Identify base cases
- Implement (top-down memo or bottom-up)
- Optimize if possible
"""

