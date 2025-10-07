"""
Problem: Reverse Bits
Category: Binary / Bit Manipulation
Link: [LeetCode](https://leetcode.com/problems/reverse-bits/)

Statement:
Reverse bits of a given 32 bits unsigned integer and return the resulting integer.

Example 1:
Input: n = 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Approach:
- Iterate 32 times shifting result and input.

Complexity:
- Time: O(1)
- Space: O(1)
"""




class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result

if __name__ == '__main__':
    print(Solution().reverseBits(43261596))
