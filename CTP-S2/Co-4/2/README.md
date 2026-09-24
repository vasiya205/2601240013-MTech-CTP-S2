## 2. Backpressure in a Data-Ingestion System

* **Objective:** Demonstrate flow control where a fast data producer is automatically throttled by a slower consumer using a bounded queue to prevent memory overflow.

* **Input:** A queue maximum size limit (e.g., `maxsize=1`) and a sequence of data items from the producer.

* **Output:** Interleaved logs showing the producer pausing when the queue is full and resuming once the consumer processes an item.

* **Algorithm:**
  1. Initialize a bounded `asyncio.Queue` with a strict `maxsize`.
  2. Run the producer and consumer concurrently using `asyncio.gather`.
  3. The producer calls `queue.put()`; if the queue reaches its limit, execution pauses (applying backpressure).
  4. The consumer periodically calls `queue.get()`, removing an item, freeing space, and unblocking the producer.

* **Time Complexity:** O(N) where N is the total number of items processed.

* **Space Complexity:** O(K) where K is the fixed maximum size of the queue buffer.
