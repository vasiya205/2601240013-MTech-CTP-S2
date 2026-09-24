## Exercise 2: 0/1 Knapsack (`knapsack.py`)

* **Objective:** Implement Dynamic Programming for 0/1 Knapsack and analyze time and space complexity[cite: 1]. 

* **Input:** Weights list `[2, 3, 4, 5]`, Values list `[3, 4, 5, 6]`, and Knapsack capacity `5`.

* **Output:** Maximum total value achievable within the given capacity (`7`).

* **Algorithm:**
  1. Initialize a 2D DP table with dimensions `(n + 1) \times (capacity + 1)` filled with zeros.
  2. Iterate through each item and each possible weight capacity.
  3. If the item's weight is less than or equal to the current capacity, choose the maximum between including the item or excluding it.
  4. Return the bottom-right value of the table.

* **Time Complexity:** O(n \cdot W) (where $n$ is the number of items and $W$ is the capacity)

* **Space Complexity:** O(n \cdot W)
