## Exercise 3: Stack and Queue (`stack_queue.py`)

* **Objective:** Develop a reusable Python package implementing Stack and Queue using type hints and dataclasses[cite: 1]. 

* **Input:** Operations (`push`, `pop` for Stack; `enqueue`, `dequeue` for Queue).

* **Output:** Popped or dequeued elements based on LIFO (Stack) and FIFO (Queue) principles.

* **Algorithm:**
  1. Define generic classes `Stack[T]` and `Queue[T]` using Python's `@dataclass` and `Generic`.
  2. For Stack, use list append for push and list pop for pop (LIFO).
  3. For Queue, use list append for enqueue and list pop(0) for dequeue (FIFO).

* **Time Complexity:** 
  * Stack: O(1) for push and pop.
  * Queue: O(1) for enqueue, O(n) for dequeue (using standard lists).

* **Space Complexity:** O(n) where n is the number of elements stored.
