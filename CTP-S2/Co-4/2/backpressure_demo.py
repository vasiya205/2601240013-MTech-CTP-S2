import asyncio

async def producer(queue):
    for i in range(3):
        print(f"Producing item {i}...")
        await queue.put(i)
        print(f"Item {i} added to queue.")

async def consumer(queue):
    for _ in range(3):
        await asyncio.sleep(1)
        item = await queue.get()
        print(f"--> Consumed item {item}")
        queue.task_done()

async def main():
    queue = asyncio.Queue(maxsize=1)
    await asyncio.gather(producer(queue), consumer(queue))

if __name__ == "__main__":
    asyncio.run(main())
