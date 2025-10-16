"""
Problem: House Robber
Category: Dynamic Programming
Link: https://leetcode.com/problems/house-robber/

Statement:
----------
You are a robber planning to rob houses along a street.
Each house has some amount of money.
You cannot rob two adjacent houses, or the alarm will trigger.
Return the maximum amount of money you can rob.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (1) + house 3 (3) = 4

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (2) + house 3 (9) + house 5 (1) = 12
"""

# ============================================================
# 🧩 APPROACH 1: BRUTE FORCE RECURSION
# ============================================================

"""
How to Think (Deep Intuition):
------------------------------
1️⃣ Understand the choice at each house:
    - Rob this house → skip previous house
    - Skip this house → take whatever maximum we got before

2️⃣ Break it into a decision tree:
    - For house i:
        a) Include nums[i] → max_money(i-2) + nums[i]
        b) Exclude nums[i] → max_money(i-1)
    - Total = max(a, b)

3️⃣ Visualize with nums=[2,7,9]:
       rob(2)
       ├── rob(1) → 7
       │    └── rob(0) → 2
       └── rob(0) → 2
    - At each branch, we pick the max money

4️⃣ Base case:
    - i < 0 → 0 money
    - i == 0 → nums[0]

5️⃣ Mental story:
    - Imagine walking backward along the street.
    - At each house, ask: "If I rob this, I must skip last. If I skip, take last max."

6️⃣ Limitation:
    - Explores all branches → O(2^n) time
    - Good for understanding, not for large n
"""

def rob_bruteforce(nums, i=None):
    if i is None:
        i = len(nums) - 1
    if i < 0:
        return 0
    return max(rob_bruteforce(nums, i-1), nums[i] + rob_bruteforce(nums, i-2))


# ============================================================
# 🧩 APPROACH 2: MEMOIZATION (TOP-DOWN DP)
# ============================================================

"""
How to Think (Deep Intuition):
------------------------------
1️⃣ Observe inefficiency:
    - Same house (i) evaluated multiple times in brute force
    - Repeated branches → wasted computation

2️⃣ Memoization idea:
    - Store results in a dictionary: memo[i] = max_money from house 0..i
    - If house i already computed → return memo[i]

3️⃣ Story:
    - Imagine remembering the best amount for each house
    - Next time you reach that house → pick from memory instantly

4️⃣ Why it works:
    - Decision tree is same
    - We prune duplicate calculations → O(n) time
"""

def rob_memo(nums, i=None, memo=None):
    if i is None:
        i = len(nums) - 1
    if memo is None:
        memo = {}
    if i < 0:
        return 0
    if i in memo:
        return memo[i]
    memo[i] = max(rob_memo(nums, i-1, memo), nums[i] + rob_memo(nums, i-2, memo))
    return memo[i]


# ============================================================
# 🧩 APPROACH 3: DYNAMIC PROGRAMMING (BOTTOM-UP)
# ============================================================

"""
How to Think (Deep Intuition):
------------------------------
1️⃣ Convert recursion → iteration:
    - Start from house 0 → move forward
    - Track max money at each house

2️⃣ dp[i] = maximum money from house 0..i

3️⃣ Base cases:
    - dp[0] = nums[0]
    - dp[1] = max(nums[0], nums[1])

4️⃣ Iterative step:
    - dp[i] = max(dp[i-1], nums[i] + dp[i-2])

5️⃣ Mental story:
    - Walking forward along street
    - At each house, decide: "Rob this house + money 2 houses back or skip?"
    - Keep updating dp array

6️⃣ Visualization (nums=[2,7,9,3,1]):
    dp[0]=2
    dp[1]=max(2,7)=7
    dp[2]=max(7, 9+2)=11
    dp[3]=max(11, 3+7)=11
    dp[4]=max(11, 1+11)=12
"""

def rob_dp(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    dp = [0]*n
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], nums[i]+dp[i-2])
    return dp[-1]


# ============================================================
# 🧩 APPROACH 4: OPTIMAL SPACE
# ============================================================

"""
How to Think (Deep Intuition):
------------------------------
1️⃣ Observation:
    - dp[i] only depends on dp[i-1] and dp[i-2]
    - No need full dp array → keep only last two

2️⃣ Variables:
    - prev2 = max money 2 houses back
    - prev1 = max money 1 house back
    - curr = max(prev1, nums[i]+prev2)

3️⃣ Mental story:
    - Imagine carrying only last 2 maximums while walking forward
    - At each house, decide: rob + prev2 or skip + prev1
"""

def rob_optimal(nums):
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

# ============================================================
# 🧾 Complexity Summary
# ============================================================

"""
| Approach           | Technique                  | Time Complexity | Space Complexity | Notes |
|--------------------|----------------------------|----------------|-----------------|-------|
| Brute Force        | Recursion                  | O(2^n)         | O(n) recursion  | Explores all paths |
| Memoization        | Top-Down DP (cache)        | O(n)           | O(n) + recursion| Avoids recomputation |
| Bottom-Up DP       | Iterative DP               | O(n)           | O(n)             | Build solution forward |
| Optimal Space      | Space-Optimized DP         | O(n)           | O(1)             | Linear time, constant space |
"""
    