"""
Problem: Combination Sum
Category: Backtracking
Link: [LeetCode](https://leetcode.com/problems/combination-sum/)

Statement:
Given candidates and a target, return all unique combinations where chosen numbers sum to target; numbers may be reused.

Example 1:
Input: candidates=[2,3,6,7], target=7
Output: [[7],[2,2,3]]
Approach:
- Backtracking with pruning.

Complexity:
- Time: Exponential
- Space: O(target/min(candidates))
"""




from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(start, path, total):
            if total == target:
                res.append(path.copy()); return
            if total > target: return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])
                path.pop()
        backtrack(0, [], 0)
        return res

if __name__ == '__main__':
    print(Solution().combinationSum([2,3,6,7], 7))
