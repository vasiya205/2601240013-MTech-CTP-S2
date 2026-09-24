## 4. Async Generators


* **Objective:** Stream values asynchronously over time using `async def` and `yield` without loading entire datasets into memory all at once.

* **Input:** A limit or sequence range parameter (e.g., `limit = 3`).

* **Output:** Streamed sequence of items printed incrementally with async delays between each item.

* **Algorithm:**
  1. Define a generator function using the `async def` syntax and the `yield` keyword.
  2. Within the generator loop, use `await` to simulate asynchronous operations (such as fetching database rows chunk-by-chunk).
  3. Consume the generator externally using an `async for` loop to process items as they arrive.

* **Time Complexity:** O(N) where N is the total number of yielded items, processed sequentially.

* **Space Complexity:** O(1) auxiliary space, since items are streamed dynamically instead of being buffered.
