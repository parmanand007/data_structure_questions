"""
Problem: Number of 1 Bits
Category: Binary / Bit Manipulation
Link: [LeetCode](https://leetcode.com/problems/number-of-1-bits/)

Statement:
Write a function that takes an unsigned integer and returns the number of '1' bits it has (Hamming weight).

Example 1:
Input: n = 00000000000000000000000000001011
Output: 3
Approach:
- Repeatedly clear lowest set bit using n &= n-1.

Complexity:
- Time: O(k)
- Space: O(1)
"""





class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count

if __name__ == '__main__':
    print(Solution().hammingWeight(11))
