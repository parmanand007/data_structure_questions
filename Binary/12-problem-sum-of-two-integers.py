"""
Problem: Sum of Two Integers
Category: Binary / Bit Manipulation
Link: [LeetCode](https://leetcode.com/problems/sum-of-two-integers/)

Statement:
Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:
Input: a=1,b=2
Output: 3
Approach:
- Use XOR and carry operations iteratively.

Complexity:
- Time: O(1)
- Space: O(1)
"""





class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
        return a if a <= 0x7FFFFFFF else ~(a ^ MASK)

if __name__ == '__main__':
    print(Solution().getSum(1,2))
