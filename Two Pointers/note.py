"""
Understanding the Two Pointers Technique
========================================

1. What Is the Two Pointers Technique?
--------------------------------------
The Two Pointers technique is a common algorithmic strategy used to solve problems involving
arrays or linked lists by using two indices (pointers) that traverse the data structure
— usually from opposite ends or in a coordinated manner.

Instead of using nested loops (O(N²)), we strategically move two pointers to reduce the time
complexity to O(N). It’s often used when data is sorted or when the relationship between
two or more elements needs to be analyzed efficiently.

2. The Core Idea
----------------
- Maintain two indices (usually called left and right).
- Each pointer moves based on specific logic:
  - Sometimes both move toward each other.
  - Sometimes one moves while the other stays fixed.
- The pointers help in narrowing down the search space or finding optimal pairs.
- By using comparisons, we eliminate unnecessary checks and achieve linear complexity.

3. When to Use the Two Pointers Technique
-----------------------------------------
Use this pattern when you observe any of the following:

| Situation | Example Problem Type | Typical Pointer Movement |
|------------|----------------------|---------------------------|
| Sorted array or list | Pair sum problems, 3Sum, removing duplicates | Left & Right move inward |
| Compare two sequences | Merge sorted arrays, intersection | Both move forward |
| Optimize subarray/subsequence | Container with most water, trapping rain water | Left & Right adjust based on condition |
| Linked lists | Detect cycle, find intersection | Slow & fast pointer approach |

4. Types of Two Pointer Patterns
--------------------------------

A. Opposite Ends Pointers
-------------------------
Used when we start from both ends and move toward each other.
Common in sorted arrays or problems requiring minimizing or maximizing differences.

Typical Pattern:
----------------
left = 0
right = len(arr) - 1

while left < right:
    if condition_satisfied:
        update_answer()
        move_pointers_based_on_condition()
    elif need_smaller_value:
        right -= 1
    else:
        left += 1

Example: Pair Sum in Sorted Array
---------------------------------
nums = [1, 2, 3, 4, 6], target = 6

left, right = 0, 4
while left < right:
    curr_sum = nums[left] + nums[right]
    if curr_sum == target:
        return [left, right]
    elif curr_sum < target:
        left += 1
    else:
        right -= 1

Result: (1, 3) → 2 + 4 = 6

Time Complexity: O(N)
Space Complexity: O(1)

B. Same Direction Pointers (Forward Scan)
-----------------------------------------
Used when both pointers start from the same side and move forward through the data.
Commonly used for removing duplicates, comparing subarrays, or merging.

Typical Pattern:
----------------
i = 0
for j in range(len(arr)):
    if valid_condition:
        arr[i] = arr[j]
        i += 1

Example: Remove Duplicates from Sorted Array
--------------------------------------------
nums = [1,1,2,2,3]
i = 0
for j in range(1, len(nums)):
    if nums[i] != nums[j]:
        i += 1
        nums[i] = nums[j]

Unique elements: [1,2,3]
Length = i + 1

Time Complexity: O(N)
Space Complexity: O(1)

C. Fast and Slow Pointers
-------------------------
Used in linked list problems or array-based cycle detection.
The fast pointer moves 2 steps at a time, the slow one moves 1 step.
If they ever meet, a cycle exists.

Typical Pattern:
----------------
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True  # Cycle detected

Time Complexity: O(N)
Space Complexity: O(1)

5. Why Two Pointers Is Powerful
-------------------------------
- Eliminates the need for nested loops (reduces O(N²) → O(N)).
- Works perfectly on sorted data to optimize comparisons.
- Allows solving both numeric and string problems efficiently.
- Ideal for "pair", "triplet", "subarray", or "linked list" type questions.

6. Common Clues That Indicate Two Pointers
------------------------------------------
If you see these in a problem statement, two pointers might be the right approach:

| Clue | Example |
|------|----------|
| “Find pair/triplet that sum to X” | Two Sum II, 3Sum |
| “Remove duplicates” | Sorted array deduplication |
| “Sorted array” | Combine, merge, or minimize difference |
| “Compare elements of two lists” | Merge two sorted lists |
| “Detect cycle / middle of linked list” | Fast and slow pointer approach |

7. Example Visualization
-------------------------
Problem: Container With Most Water

heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]

Step | Left | Right | Min(Height) | Width | Area | MaxArea
-----|-------|--------|-------------|--------|-------|--------
0 | 0 | 8 | 1 | 8 | 8 | 8
1 | 1 | 8 | 7 | 7 | 49 | 49
2 | 1 | 7 | 3 | 6 | 18 | 49
3 | 1 | 6 | 8 | 5 | 40 | 49
4 | 1 | 5 | 4 | 4 | 16 | 49
5 | 1 | 4 | 5 | 3 | 15 | 49
6 | 1 | 3 | 2 | 2 | 4 | 49
7 | 1 | 2 | 6 | 1 | 6 | 49

Result: Max Area = 49

8. Rule of Thumb to Identify Quickly
------------------------------------
If you ever see:
- “Pair”, “Triplet”, or “Two elements”
- “Sorted array or list”
- “Optimize something with boundaries”
- “Linked list traversal with two speeds”

Then think Two Pointers.
"""
