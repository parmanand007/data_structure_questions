"""
Problem: Coin Change
Category: Dynamic Programming
Link: [LeetCode](https://leetcode.com/problems/coin-change/)

Statement:
Given coins of different denominations and a total amount, compute the fewest number of coins needed to make up that amount, or -1 if impossible.

Example 1:
Input: coins=[1,2,5], amount=11
Output: 3
Approach:
- DP bottom-up.

Complexity:
- Time: O(amount * m)
- Space: O(amount)
"""




from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x], dp[x-coin] + 1)
        return dp[amount] if dp[amount] <= amount else -1

if __name__ == '__main__':
    print(Solution().coinChange([1,2,5], 11))
