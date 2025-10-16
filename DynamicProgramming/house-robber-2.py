"""
Problem: House Robber II
Category: Dynamic Programming
Link: https://leetcode.com/problems/house-robber-ii/

Statement:
----------
You are a robber planning to rob houses along a circular street.
Each house has some money.
You cannot rob two adjacent houses, and the first and last houses are also adjacent.
Return the maximum amount of money you can rob.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: Rob house 2 (3). Can't rob 1 and 3 together.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (1) + house 3 (3) = 4
"""

# ============================================================
# 🧩 APPROACH 1: BRUTE FORCE (RECURSION)
# ============================================================

"""
How to Think (Deep Intuition):
------------------------------
1️⃣ Consider the circular constraint:
   - First and last houses are adjacent → cannot rob both.
   - Think of two separate scenarios:
       a) Rob houses 0 to n-2 (exclude last)
       b) Rob houses 1 to n-1 (exclude first)
   - Solve each linearly and take max.

2️⃣ Recursive decomposition (linear street):
   - At house i, two choices:
       * Rob i → add nums[i] + rob(i+2)
       * Skip i → rob(i+1)
   - Recurse through all possibilities.

3️⃣ Base cases:
   - i >= len(nums) → return 0

4️⃣ Mental model:
   - All possible rob/not-rob decisions are explored recursively.
   - Exponential branching (2^n in worst-case).

5️⃣ Key intuition:
   - Think: "At each house, I have two paths: rob or skip".
"""

def rob_linear_bruteforce(nums, i):
    if i >= len(nums):
        return 0
    # Rob current house
    rob = nums[i] + rob_linear_bruteforce(nums, i+2)
    # Skip current house
    skip = rob_linear_bruteforce(nums, i+1)
    return max(rob, skip)

def rob_circular_bruteforce(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    return max(rob_linear_bruteforce(nums[:-1], 0), rob_linear_bruteforce(nums[1:], 0))


# ============================================================
# 🧩 VISUALIZATION (Brute Force)
# ============================================================

"""
Example: nums = [2,3,2]

Scenario 1: Exclude last → [2,3]
   Start at i=0:
     Rob 0: 2 + rob(2) → 2 + 0 = 2
     Skip 0: rob(1) → rob 1 = 3
   Max = 3

Scenario 2: Exclude first → [3,2]
   Start at i=0:
     Rob 0: 3 + rob(2) → 3 + 0 = 3
     Skip 0: rob(1) → rob 1 = 2
   Max = 3

Final Max = 3
"""

# ============================================================
# 🧾 COMPLEXITY (Brute Force)
# ============================================================
"""
Time Complexity: O(2^n) → explore all rob/skip choices
Space Complexity: O(n) recursion stack
"""

# ============================================================
# 🧩 APPROACH 2: MEMOIZATION (TOP-DOWN DP)
# ============================================================

"""
How to Think:
-------------
1️⃣ Observe inefficiency in brute force:
   - Many subproblems (rob(i)) repeated multiple times
   - Same i → same result → store in memo

2️⃣ Memoization strategy:
   - Use dictionary or array to cache rob(i) results

3️⃣ Solve two scenarios separately (exclude first or last)
   - Each scenario → memoized recursion (linear street)

4️⃣ Mental roadmap:
   - At house i:
       a) Already computed? → return memo[i]
       b) Else → max(nums[i]+rob(i+2), rob(i+1))
       c) Store result in memo
"""

def rob_linear_memo(nums, i, memo):
    if i >= len(nums):
        return 0
    if i in memo:
        return memo[i]
    rob = nums[i] + rob_linear_memo(nums, i+2, memo)
    skip = rob_linear_memo(nums, i+1, memo)
    memo[i] = max(rob, skip)
    return memo[i]

def rob_circular_memo(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    return max(rob_linear_memo(nums[:-1], 0, {}), rob_linear_memo(nums[1:], 0, {}))

# ============================================================
# 🧩 VISUALIZATION (Memoization)
# ============================================================

"""
Example: nums = [1,2,3,1]

Scenario 1: Exclude last → [1,2,3]
   i=0 → rob 1+rob(2)=1+3=4, skip rob(1)=rob(1)=3
   memo stores results for i=0,1,2
   Max = 4

Scenario 2: Exclude first → [2,3,1]
   i=0 → rob 2+rob(2)=2+1=3, skip rob(1)=rob(1)=3
   Max = 4
Final Max = 4
"""

# ============================================================
# 🧾 COMPLEXITY (Memoization)
# ============================================================
"""
Time Complexity: O(n) → each i computed once per scenario
Space Complexity: O(n) → memo + recursion stack
"""

# ============================================================
# 🧩 APPROACH 3: OPTIMAL (BOTTOM-UP DP / SPACE OPTIMIZED)
# ============================================================

"""
How to Think:
-------------
1️⃣ Observation:
   - DP[i] depends only on DP[i-1] and DP[i-2]
   - Can use two variables instead of full DP array

2️⃣ Solve linear street:
   - prev2 = dp[i-2]
   - prev1 = dp[i-1]
   - current = max(prev1, nums[i]+prev2)
   - Slide window forward

3️⃣ Circular street handled by two linear calls (exclude first or last)

4️⃣ Mental roadmap:
   - Initialize prev1, prev2 for first two houses
   - Loop through houses → compute max rob
   - Take max of two scenarios
"""

def rob_linear_opt(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    prev2, prev1 = nums[0], max(nums[0], nums[1])
    for i in range(2, n):
        curr = max(prev1, nums[i]+prev2)
        prev2, prev1 = prev1, curr
    return prev1

def rob_circular_opt(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    return max(rob_linear_opt(nums[:-1]), rob_linear_opt(nums[1:]))

# ============================================================
# 🧩 VISUALIZATION (Optimal)
# ============================================================

"""
Example: nums = [2,7,9,3,1]

Scenario 1: Exclude last → [2,7,9,3]
   prev2=2, prev1=max(2,7)=7
   i=2 → curr=max(7,9+2)=11
   i=3 → curr=max(11,3+7)=11
   Max = 11

Scenario 2: Exclude first → [7,9,3,1]
   prev2=7, prev1=max(7,9)=9
   i=2 → curr=max(9,3+7)=10
   i=3 → curr=max(10,1+9)=10
   Max = 11

Answer = max(11,10)=11
"""

# ============================================================
# 🧾 COMPLEXITY (Optimal)
# ============================================================
"""
Time Complexity: O(n) → linear pass twice
Space Complexity: O(1) → only two variables used per linear call
"""
