import sys
import time

# List-based processing
start_time = time.time()
list_data = [x**2 for x in range(1_000_000)]
list_time = time.time() - start_time
list_size = sys.getsizeof(list_data)

# Generator-based processing
start_time = time.time()
gen_data = (x**2 for x in range(1_000_000))
gen_time = time.time() - start_time
gen_size = sys.getsizeof(gen_data)

print(f"List Size: {list_size:,} bytes | Time: {list_time:.5f}s")
print(f"Generator Size: {gen_size} bytes | Time: {gen_time:.6f}s")
