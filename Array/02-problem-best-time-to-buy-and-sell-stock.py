"""
Problem: Best Time to Buy and Sell Stock
Category: Array / Greedy
Link: [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

Statement:
You are given an array prices where prices[i] is the price of a given stock on the ith day. Return the maximum profit from one buy-sell transaction.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: Output: 5

Example 2:
Input: prices = [7,6,4,3,1]
Output: Output: 0

Approach:
Explanation & Approach (Track minimum):
- Observation: Profit = sell_price - buy_price. To maximize profit, we need the smallest buy price before each sell day.
- Iterate prices once, maintain min_price so far and max_profit so far:
  max_profit = max(max_profit, price - min_price); min_price = min(min_price, price).
Correctness:
- For each day considered as selling day, the best possible buy day among earlier days is captured by min_price.
Complexity:
- Time: O(n), Space: O(1).

Complexity:
- Time: O(...)
- Space: O(...)
"""







from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = float('inf')
        max_profit = 0
        for p in prices:
            if p < min_price:
                min_price = p
            else:
                max_profit = max(max_profit, p - min_price)
        return max_profit

if __name__ == '__main__':
    print(Solution().maxProfit([7,1,5,3,6,4]))  # 5
    print(Solution().maxProfit([7,6,4,3,1]))    # 0
