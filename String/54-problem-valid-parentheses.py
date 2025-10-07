"""
Problem: Valid Parentheses
Category: String / Stack
Link: [LeetCode](https://leetcode.com/problems/valid-parentheses/)

Statement:
Given a string s containing '()[]{}', determine if input is valid (properly closed and nested).

Example 1:
Input: s = "()[]{}"
Output: true
Approach:
- Use stack to match pairs.

Complexity:
- Time: O(n)
- Space: O(n)
"""




class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]; pairs={')':'(',']':'[','}':'{'}
        for ch in s:
            if ch in pairs:
                if not stack or stack.pop()!=pairs[ch]: return False
            else: stack.append(ch)
        return not stack

if __name__ == '__main__':
    print(Solution().isValid('()[]{}'))
