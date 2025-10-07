"""
Problem: Climbing Stairs
Category: Dynamic Programming
Link: [LeetCode](https://leetcode.com/problems/climbing-stairs/)

Statement:
You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n=2
Output: 2

Example 2:
Input: n=3
Output: 3
Approach:
- Fibonacci DP.

Complexity:
- Time: O(n)
- Space: O(1)
"""




class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n+1):
            a, b = b, a + b
        return b

if __name__ == '__main__':
    print(Solution().climbStairs(5))
