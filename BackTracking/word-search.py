"""
Problem: Word Search
Category: Backtracking / DFS
Link: https://leetcode.com/problems/word-search/

Statement:
----------
Given an m x n grid of characters `board` and a string `word`, 
return true if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example 1:
----------
Input:
board = [
  ["A","B","C","E"],
  ["S","F","C","S"],
  ["A","D","E","E"]
]
word = "ABCCED"
Output: True

Example 2:
----------
Input:
board = [
  ["A","B","C","E"],
  ["S","F","C","S"],
  ["A","D","E","E"]
]
word = "SEE"
Output: True

Example 3:
----------
Input:
board = [
  ["A","B","C","E"],
  ["S","F","C","S"],
  ["A","D","E","E"]
]
word = "ABCB"
Output: False
"""

# ============================================================
# 🧩 APPROACH 1: BRUTE FORCE (DFS from every cell)
# ============================================================

"""
How to Think:
-------------
When you read “word exists in grid” → immediately think:
  → “DFS or Backtracking on a matrix.”

Here’s the intuition process:

1️⃣ Try starting the word from every cell in the grid.
2️⃣ If the cell matches the first letter of the word, 
    explore all 4 directions (up, down, left, right).
3️⃣ Move to next letter (index + 1) recursively.
4️⃣ Don’t revisit the same cell twice → mark it as visited.
5️⃣ If all letters match in sequence → return True.

👉 This is a classic "Path finding in a grid" + "Backtracking" question.

Visualization:
--------------
Let’s say word = "ABCCED"

Grid:
A B C E
S F C S
A D E E

Try paths:
A(0,0) → B(0,1) → C(0,2) → C(1,2) → E(2,2) → D(2,1)
✅ Word found.

Algorithm Steps:
----------------
1. Loop through each cell in the grid.
2. If board[r][c] == word[0]:
     → start DFS from here.
3. In DFS:
   - Base Case: if index == len(word): return True
   - Out of bounds or mismatch → return False
   - Temporarily mark cell visited (e.g., with '#')
   - Explore 4 directions
   - Restore the cell after exploring (backtrack)
4. If any DFS returns True → the word exists.

Complexity:
-----------
Time:  O(N * M * 4^L)
       - N*M = total cells
       - L = length of the word
       Each cell can branch up to 4 directions for each letter.
Space: O(L) recursion depth + visited path set
"""

from typing import List

def exist_bruteforce(board: List[List[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])
    visited = set()

    def dfs(r, c, i):
        # Base case → full word matched
        if i == len(word):
            return True
        
        # Boundary or mismatch check
        if (r < 0 or c < 0 or r >= rows or c >= cols or
            board[r][c] != word[i] or (r, c) in visited):
            return False
        
        # Mark current cell visited
        visited.add((r, c))

        # Explore 4 directions
        res = (dfs(r+1, c, i+1) or
               dfs(r-1, c, i+1) or
               dfs(r, c+1, i+1) or
               dfs(r, c-1, i+1))

        # Backtrack → unmark
        visited.remove((r, c))

        return res

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0] and dfs(r, c, 0):
                return True
    return False

# Example:
# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# print(exist_bruteforce(board, "ABCCED"))  # Output: True


# ============================================================
# 🧩 APPROACH 2: OPTIMIZED BACKTRACKING (In-place marking)
# ============================================================

"""
How to Think:
-------------
The brute-force approach uses a `visited` set — this costs extra space.

Optimization idea:
→ Instead of keeping a separate `visited` set, 
   we can modify the board temporarily to mark a cell as visited
   (e.g., replace character with '#').

Then, restore the character when backtracking.

This reduces space usage and makes DFS cleaner.

Algorithm Steps:
----------------
1. Start DFS from any cell that matches the first character.
2. In DFS:
   - If index == len(word) → found full word → return True.
   - If out of bounds or mismatch → return False.
   - Temporarily mark cell with '#' to block reuse.
   - Explore all 4 directions recursively.
   - Restore cell after all directions explored.
3. If any DFS returns True → return True.
4. Else return False.

Complexity:
-----------
Time:  O(N * M * 4^L)
Space: O(L) recursion stack (no extra visited set)
"""

def exist_optimal(board: List[List[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])

    def dfs(r, c, i):
        # Base case
        if i == len(word):
            return True

        # Out of bounds or mismatch
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
            return False

        # Temporarily mark cell visited
        temp = board[r][c]
        board[r][c] = "#"

        # Explore in all 4 directions
        res = (dfs(r+1, c, i+1) or
               dfs(r-1, c, i+1) or
               dfs(r, c+1, i+1) or
               dfs(r, c-1, i+1))

        # Restore character (backtrack)
        board[r][c] = temp

        return res

    # Try DFS from every cell
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0] and dfs(r, c, 0):
                return True

    return False


# Example Run:
# ============
# board = [
#   ["A","B","C","E"],
#   ["S","F","C","S"],
#   ["A","D","E","E"]
# ]
# print(exist_optimal(board, "ABCCED"))  # ✅ Output: True
# print(exist_optimal(board, "SEE"))     # ✅ Output: True
# print(exist_optimal(board, "ABCB"))    # ❌ Output: False
