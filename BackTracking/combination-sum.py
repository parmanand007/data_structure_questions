"""
Problem: Combination Sum
Category: Backtracking / Recursion / DFS
Link: https://leetcode.com/problems/combination-sum/

Statement:
----------
Given an array of distinct integers `candidates` and a target integer `target`, 
return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`.
You may return the combinations in any order.

You may reuse the same number any number of times.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []
"""

# ============================================================
# 🧩 APPROACH 1: BRUTE FORCE (GENERATE ALL SUBSETS)
# ============================================================

"""
How to Think (Deep, for Brute Force)
------------------------------------
Goal of this section: teach you how to *start* if you have no idea, and how the brute-force view reveals structure.

1) Re-state the problem in plain words:
   - "Find all different groups of numbers (allowing reuse) whose sum equals target."

2) Ask: What are the degrees of freedom?
   - For each candidate you can take it 0 times, 1 time, 2 times, ... up to floor(target / candidate).
   - If candidates were allowed only once, this would be subset generation. Because reuse is allowed, brute force must conceptually consider counts per candidate.

3) Brute-force mental model:
   - Imagine a vector of counts [c0, c1, ..., cn-1] where ci = how many times candidate i is used.
   - The search space is all such vectors whose dot-product with candidates equals target.
   - That’s infinite in theory but bounded by target (ci ≤ target / candidates[i]).

4) How this leads to an algorithm:
   - Try all possible counts for candidate0 (0..target/c0).
   - For each choice, try all counts for candidate1 etc. → nested loops of variable depth (exponential).
   - This is equivalent to generating all combinations with repetitions.

5) When to actually use this:
   - Use brute force only to understand and test small cases.
   - It’s the baseline to verify correctness before you introduce pruning/backtracking.

Mental checklist while designing brute force:
   - Can the candidate be reused? Yes → counts model.
   - Is target small enough to allow enumerating counts? If not, we need pruning.
   - Do we need uniqueness? Yes → ensure final combinations are canonical (sorted by candidate index).

Why brute force helps:
   - It forces you to think in terms of choices per candidate, which maps directly to recursive/backtracking formulation.
"""

def combinationSum_bruteforce(candidates, target):
    from itertools import combinations_with_replacement
    res = []
    # This brute force uses combinations_with_replacement to generate length-r combinations.
    for r in range(1, target + 1):
        for comb in combinations_with_replacement(candidates, r):
            if sum(comb) == target:
                res.append(list(comb))
    return res


# ============================================================
# 🧩 APPROACH 2: RECURSIVE BACKTRACKING (Better)
# ============================================================

"""
How to Think (Deep, for Backtracking / DFS)
------------------------------------------
This is the key "how to think" part — make your brain pattern-match this problem to backtracking.

1) Pattern recognition:
   - Problem asks for **all** combinations -> backtracking/DFS.
   - Reuse allowed -> when recursing on index i, you can keep i for the next call.
   - Target sum constraint -> we can stop early when partial sum > target.

2) Mental roadmap to convert words → algorithm:
   - Think of building the answer incrementally: start with empty list `path`.
   - At each step pick a candidate (starting from some index to avoid duplicates),
     append it to `path`, reduce the remaining target, recurse.
   - If remaining target == 0 → record solution.
   - If remaining target < 0 → stop exploring (prune).

3) Key design choices & why:
   - Parameterize recursion with `start` index:
       → ensures combinations are built in non-decreasing candidate index order
       → prevents permutations of the same combination.
   - Use `path` (stack) to hold the current combination.
   - Use `target_remaining` instead of recomputing sums to be efficient.

4) How to reason about pruning:
   - If candidates are unsorted: you still prune when target_remaining < 0, but you can't stop early in the loop.
   - If candidates are sorted: when you encounter candidate > target_remaining, you can break the loop (all subsequent are larger).

5) How to think during recursion (caller's POV):
   - At a node, ask:
       a) Can I accept this node? (target_remaining == 0)
       b) Can I prune? (target_remaining < 0 or candidate > remaining and list sorted)
       c) For each choice, do I recurse deeper with same start (to allow reuse) or start+1 (no reuse)?

6) Debugging tip:
   - Print recursion tree for a small example and follow paths. Every leaf is either accepted (sum==target) or rejected (sum>target).

Heuristic checklist for when this will be efficient:
   - If target is moderate and candidates include relatively large values, pruning will cut big portions.
   - If candidates are small and many combinations exist, output size will be large (inherent cost).

This is the standard template you should memorize:
    dfs(start, path, remaining):
        if remaining == 0: record path
        if remaining < 0: return
        for i in range(start, n):
            choose candidates[i]
            dfs(i, path + [candidates[i]], remaining - candidates[i])
            backtrack
"""

def combinationSum_better(candidates, target):
    res = []

    def dfs(start, path, total):
        if total == target:
            res.append(path[:])
            return
        if total > target:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            dfs(i, path, total + candidates[i])  # reuse same number
            path.pop()  # backtrack

    dfs(0, [], 0)
    return res


# ============================================================
# 🧩 APPROACH 3: OPTIMAL BACKTRACKING WITH PRUNING (Best Practical)
# ============================================================

"""
How to Think (Deep, for Optimal / Pruned Backtracking)
-----------------------------------------------------
Now raise your thinking: how to reduce the branching factor and prune early.

1) Sorting + early break:
   - Sort candidates ascending.
   - In the for-loop, if candidates[i] > remaining_target, **break** because further candidates are larger.
   - This is the most effective cheap pruning.

2) Bound on depth:
   - Maximum depth of recursion = floor(target / smallest_candidate).
   - Use this to estimate memory and recursion depth.

3) Avoid repeated work:
   - Because we always pass index `i` into recursion to allow reuse,
     we ensure combinations are generated in non-decreasing order → uniqueness handled naturally.
   - No need for extra visited/used arrays.

4) Additional pruning ideas (advanced):
   - Precompute prefix sums or greedy bounds to see if even taking the largest possible combination cannot reach the target (rarely needed).
   - Use memoization to cut identical (start, remaining) subproblems if many overlaps exist — but memoization returns existence/counts, not all combinations, so careful.

5) Mental checklist at each node:
   - Is current candidate > remaining? If yes, break loop.
   - Is remaining == 0? record and return.
   - Else choose candidate and recurse.

6) How to think about complexity:
   - Worst-case still exponential because number of valid combinations can be exponential.
   - But in practice, sorting + break drastically reduces branches.

7) Example reasoning on small input:
   - candidates = [2,3,6,7], target = 7
   - path empty:
       try 2 -> remaining 5:
           try 2 -> remaining 3:
               try 2 -> remaining 1 -> candidate 2 > 1 -> break -> backtrack
               try 3 -> remaining 0 -> record [2,2,3]
           try 3 -> remaining 2 -> break early etc.
       try 3 -> remaining 4 ...
       try 6 -> remaining 1 -> break
       try 7 -> remaining 0 -> record [7]

8) Implementation template to memorize:
    candidates.sort()
    dfs(start, path, remaining):
        if remaining == 0: record path
        for i in range(start, n):
            if candidates[i] > remaining: break
            path.append(candidates[i])
            dfs(i, path, remaining - candidates[i])
            path.pop()

9) Debugging/practice suggestion:
   - Trace the recursion tree on paper for a small input and mark which branches are pruned due to the break condition — this trains the mental model.

This is the version you should use in interviews unless you have extra constraints.
"""

def combinationSum_optimal(candidates, target):
    candidates.sort()
    res = []

    def dfs(start, path, remaining):
        if remaining == 0:
            res.append(path[:])
            return

        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break  # pruning step
            path.append(candidates[i])
            dfs(i, path, remaining - candidates[i])  # reuse same index
            path.pop()

    dfs(0, [], target)
    return res


# ============================================================
# 🧠 Visualizations and Recursion Tree Example
# ============================================================

"""
Visualization Example (trace with pruning)
------------------------------------------
Input: candidates = [2,3,6,7], target = 7

Sorted candidates = [2,3,6,7]

Recursion tree (pruned branches omitted):

root (remaining=7)
 ├─ choose 2 -> (remaining=5)
 │   ├─ choose 2 -> (remaining=3)
 │   │   ├─ choose 2 -> (remaining=1)  -> next candidate 2 > 1 -> break (prune)
 │   │   └─ choose 3 -> (remaining=0) -> record [2,2,3]
 │   └─ choose 3 -> (remaining=2) -> candidate 3 > 2 -> break
 ├─ choose 3 -> (remaining=4)
 │   ├─ choose 3 -> (remaining=1) -> candidate 3 > 1 -> break
 ├─ choose 6 -> (remaining=1) -> candidate 6 > 1 -> break
 └─ choose 7 -> (remaining=0) -> record [7]

Output: [[2,2,3], [7]]
"""

# ============================================================
# 🧾 Complexity Summary
# ============================================================

"""
Time Complexity:
- Worst-case exponential. The exact bound is complex because it depends on target and distribution of candidates.
- Practical guideline:
   * brute force: astronomically expensive
   * backtracking: significantly better due to pruning when partial sums exceed target
   * sorting + break: best practical pruning

Space Complexity:
- O(max_depth) for recursion stack where max_depth ≈ target / min(candidates)

Key takeaways (how to think):
- Translate "all combinations" → backtracking template.
- Use "reuse allowed" → recurse with same index.
- Always check pruning opportunities:
    * remaining < 0 -> stop
    * sorted candidates and candidate > remaining -> break
- Practice tracing small cases on paper to internalize recursion tree and pruning.
"""
