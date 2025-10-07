"""
Problem: Valid Palindrome
Category: String / Two Pointers
Link: [LeetCode](https://leetcode.com/problems/valid-palindrome/)

Statement:
Given a string s, determine if it is a palindrome considering only alphanumeric characters and ignoring cases.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Approach:
- Two pointers with alphanumeric check.

Complexity:
- Time: O(n)
- Space: O(1)
"""




class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1
        while i<j:
            while i<j and not s[i].isalnum(): i+=1
            while i<j and not s[j].isalnum(): j-=1
            if s[i].lower()!=s[j].lower(): return False
            i+=1; j-=1
        return True

if __name__ == '__main__':
    print(Solution().isPalindrome('A man, a plan, a canal: Panama'))
