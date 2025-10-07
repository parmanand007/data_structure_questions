"""
Problem: Encode And Decode Strings
Category: Additional
Link: [LeetCode](https://leetcode.com/problems/encode-and-decode-strings/)

Statement:
LeetCode problem: Encode And Decode Strings

    Examples/Test Cases:
    - Example inputs and outputs from LeetCode should be added here.

    Approach:
    - Provide final optimal approach here (brief).

    Complexity:
    - Time: O(...)
    - Space: O(...)

Examples/Test Cases:
- See LeetCode

Approach:
- Provide final optimal approach here.

Complexity:
- Time: O(...)
- Space: O(...)
"""




from typing import List
class Codec:
    def encode(self, strs: List[str]) -> str:
        return ''.join(f'{len(s)}#{s}' for s in strs)
    def decode(self, s: str) -> List[str]:
        res=[]; i=0
        while i < len(s):
            j = s.find('#', i); length = int(s[i:j]); i = j+1
            res.append(s[i:i+length]); i += length
        return res
if __name__ == '__main__':
    c=Codec(); enc=c.encode(['hello','world']); print(enc); print(c.decode(enc))
