import asyncio

async def set_future_result(future):
    print("Async operation started...")
    await asyncio.sleep(1)
    future.set_result("Data successfully fetched!")
    print("Async operation completed.")

async def main():
    loop = asyncio.get_running_loop()
    fut = loop.create_future()

    asyncio.create_task(set_future_result(fut))

    print("Waiting for future result...")
    result = await fut
    print(f"Received result: {result}")

if __name__ == "__main__":
    asyncio.run(main())
