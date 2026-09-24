## 5. Concurrency Model Selection

* **Objective:** Demonstrate selecting and using a multiprocessing concurrency model for CPU-bound tasks to bypass the Python Global Interpreter Lock (GIL).

* **Input:** A list of numerical inputs requiring heavy mathematical computation.

* **Output:** Computed mathematical results and overall execution time across multiple CPU cores.

* **Algorithm:**
  1. Define a CPU-bound worker function (e.g., heavy arithmetic loops).
  2. Inspect available CPU cores using `os.cpu_count()`.
  3. Initialize a `ProcessPoolExecutor` context manager.
  4. Map the CPU-bound function across inputs in parallel, delegating work to separate system processes.

* **Time Complexity:** O(M \times N / P) where M is tasks, N is work per task, and P is CPU cores.

* **Space Complexity:** O(M) to store input collections and result payloads across process boundaries.
