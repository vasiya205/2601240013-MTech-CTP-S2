import asyncio
import time

async def fetch_page(url: str, delay: float) -> str:
    """
    Simulates a non-blocking network call. In CPython, waiting on 
    asyncio.sleep releases the GIL, letting other tasks run on the event loop.
    """
    print(f"[CPython Event Loop] Starting request to: {url}")
    await asyncio.sleep(delay)  # Yields control back to the CPython event loop
    print(f"[CPython Event Loop] Finished request to: {url}")
    return f"Response content from {url}"

async def main() -> None:
    urls_with_delays = [
        ("https://api.example.com/data1", 1.5),
        ("https://api.example.com/data2", 0.5),
        ("https://api.example.com/data3", 1.0),
    ]
    
    start_time = time.perf_counter()
    
    # Schedule all coroutines concurrently within CPython's event loop
    tasks = [fetch_page(url, delay) for url, delay in urls_with_delays]
    results = await asyncio.gather(*tasks)
    
    end_time = time.perf_counter()
    
    print("\n--- CPython Crawler Results ---")
    for res in results:
        print(res)
    print(f"Total execution time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    # CPython runs the event loop via asyncio.run()
    asyncio.run(main())
