## Exercise 4: List vs. Generator Processing (`list_vs_generator.py`)

* **Objective:** Compare list-based processing and generator-based processing for a large dataset in terms of execution time and memory usage[cite: 1].

* **Input:** Range of 1,000,000 integers to compute squares.

* **Output:** Execution time and memory size footprint comparison (List consumes ~8.4 MB, Generator consumes ~104 
bytes).

* **Algorithm:**
  1. Create a list comprehension for 1 million elements and measure size (`sys.getsizeof`) and time.
  2. Create a generator expression for the same dataset and measure size and time.
  3. Compare the memory efficiency and lazy evaluation benefits of generators.

* **Time Complexity:** O(n) for generation/iteration.

* **Space Complexity:** 
  * List-based: O(n) (stores all elements in memory).
  * Generator-based: O(1) (computes on-the-fly via lazy evaluation).
