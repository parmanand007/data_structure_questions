"""
Problem: Best Time to Buy and Sell Stock
Category: Array / Greedy / Two Pointers
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Statement:
You are given an array prices[] where prices[i] is the price of a stock on the i-th day.
You want to maximize your profit by choosing a single day to buy and a later day to sell.
Return the maximum profit you can achieve. If no profit is possible, return 0.

Example:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy at price 1 and sell at 6 → profit = 6 - 1 = 5.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: No profit can be made since prices always decrease.
"""

"""
Brute Force Approach
--------------------
How to Think (for this solution only):
    - The most direct way is to compare every pair of days (buy before sell).
    - For each day, assume it’s your buying day and check all future days for selling.
    - Keep track of the maximum difference (profit) found.
    - Although inefficient, this builds intuition about what "profit" means in this problem.

Steps:
    1. Initialize max_profit = 0
    2. For each i (buy day):
         For each j > i (sell day):
            - profit = prices[j] - prices[i]
            - update max_profit = max(max_profit, profit)
    3. Return max_profit

Complexity Explanation:
    - Time Complexity: O(N²)
        → Two nested loops comparing each pair.
    - Space Complexity: O(1)
        → Constant space used.
"""

def maxProfit_bruteforce(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    return max_profit


"""
Better Approach (Precomputing max on right)
-------------------------------------------
How to Think (for this solution only):
    - Instead of rechecking future prices each time, precompute the highest price that comes after each day.
    - If you know the best future selling price, profit = future_max[i] - prices[i].
    - This reduces redundant comparisons and builds intuition for using precomputed arrays.

Steps:
    1. Create a list future_max[] same size as prices.
    2. Traverse from right to left to fill future_max[i] = max(future_max[i+1], prices[i]).
    3. Traverse from left to right:
         - For each i, calculate profit = future_max[i] - prices[i].
         - Keep track of max_profit.
    4. Return max_profit.

Complexity Explanation:
    - Time Complexity: O(N)
        → Two passes through array.
    - Space Complexity: O(N)
        → For storing future_max array.
"""

def maxProfit_better(prices):
    n = len(prices)
    future_max = [0] * n
    future_max[-1] = prices[-1]

    # Fill future max prices from right to left
    for i in range(n - 2, -1, -1):
        future_max[i] = max(future_max[i + 1], prices[i])

    max_profit = 0
    for i in range(n):
        profit = future_max[i] - prices[i]
        max_profit = max(max_profit, profit)

    return max_profit


"""
Optimal Approach (Greedy - One Pass)
------------------------------------
How to Think (for this solution only):
    - Think in terms of **tracking the lowest buying price** and **max profit so far**.
    - As you scan from left to right:
         - Update min_price whenever you find a smaller price.
         - At each step, calculate potential profit = current_price - min_price.
         - Update max_profit if it’s larger.
    - This avoids storing or revisiting data, using a single linear scan.

Visualization:
    prices = [7, 1, 5, 3, 6, 4]
    → min_price = 7 → 1
    → max_profit updates: (5-1)=4, (3-1)=2, (6-1)=5 ✅

Steps:
    1. Initialize min_price = ∞, max_profit = 0
    2. For each price in prices:
         - If price < min_price → update min_price
         - Else → calculate profit = price - min_price and update max_profit
    3. Return max_profit

Complexity Explanation:
    - Time Complexity: O(N)
        → Single traversal of array.
    - Space Complexity: O(1)
        → Only two variables maintained.
"""

def maxProfit_optimal(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)

    return max_profit


"""
Two pointers
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP