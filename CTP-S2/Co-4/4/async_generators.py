import asyncio

async def async_number_stream(limit):
    for i in range(limit):
        await asyncio.sleep(0.5)
        yield i

async def main():
    async for number in async_number_stream(3):
        print(f"Received stream item: {number}")

if __name__ == "__main__":
    asyncio.run(main())
