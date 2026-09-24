## Exercise 1: Merge Sort (`merge_sort.py`)

* **Objective:** Implement Divide-and-Conquer algorithms for merge sort and calculate their time complexities[cite: 1].
* **Input:** A list of unsorted numbers (e.g., `[38, 27, 43, 3, 9, 82, 10]`). 

* **Output:** A sorted list of numbers in ascending order (e.g., `[3, 9, 10, 27, 38, 43, 82]`).

* **Algorithm:** 
  1. Check if the length of the array is 1 or less; if yes, return it.
  2. Split the array into two halves.
  3. Recursively apply merge sort to both halves.
  4. Merge the sorted halves back together in order.

* **Time Complexity: O(n \log n)

* **Space Complexity: O(n)
