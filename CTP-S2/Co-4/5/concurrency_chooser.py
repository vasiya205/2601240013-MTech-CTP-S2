import time
from concurrent.futures import ProcessPoolExecutor
import os

def cpu_heavy_task(n):
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    print(f"Available CPU cores: {os.cpu_count()}")
    print("Running CPU-bound task using Multiprocessing...")
    
    start = time.time()
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(cpu_heavy_task, [10**6, 10**6]))
        
    print(f"Results computed successfully.")
    print(f"Execution time: {time.time() - start:.2f} seconds")
