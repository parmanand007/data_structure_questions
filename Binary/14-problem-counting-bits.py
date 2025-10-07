"""
Problem: Counting Bits
Category: Binary / DP
Link: [LeetCode](https://leetcode.com/problems/counting-bits/)

Statement:
Given a non-negative integer n, for every number i in the range 0 ≤ i ≤ n, return an array of the number of 1's in the binary representation of i.

Example 1:
Input: n=5
Output: [0,1,1,2,1,2]
Approach:
- DP: bits[i] = bits[i>>1] + (i&1).

Complexity:
- Time: O(n)
- Space: O(n)
"""




from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res

if __name__ == '__main__':
    print(Solution().countBits(5))
