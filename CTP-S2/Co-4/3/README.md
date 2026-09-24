## 3. Futures in Concurrent Programming

* **Objective:** Showcase a placeholder object (`asyncio.Future`) that represents the eventual result of an asynchronous computation.

* **Input:** An unfulfilled `asyncio.Future` instance created by the event loop.

* **Output:** Logs showing the program awaiting the future, a background task completing work, and the final resolved result being printed.

* **Algorithm:**
  1. Create a `Future` object via the running event loop (`loop.create_future()`).
  2. Schedule a background coroutine task that simulates asynchronous processing.
  3. Await the future object (`await fut`) in the main routine to pause execution until a result is available.
  4. Once background work completes, invoke `future.set_result(data)` to fulfill the future and wake up the awaited task.

* **Time Complexity:** O(1) for future state management; total duration depends on background task delay.

* **Space Complexity:** O(1) to store the future object reference and its internal result payload.
