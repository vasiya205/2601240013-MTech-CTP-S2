import time
from collections import Counter
import io

# (c) Decorator for measuring execution time
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Execution Time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# (a) Generator function for lazy, line-by-line reading
def stream_log_data(file_obj):
    for line in file_obj:
        yield line.strip()

# (b) Function utilizing collections.Counter to track error types
@measure_time
def process_logs(file_obj):
    error_counter = Counter()
    
    for line in stream_log_data(file_obj):
        if "ERROR" in line:
            # Expected format: "TIMESTAMP - ERROR - ErrorType"
            parts = line.split(" - ERROR - ")
            if len(parts) > 1:
                error_type = parts[1].strip()
                error_counter[error_type] += 1
                
    return error_counter

# --- Demonstration with Simulated Log Data ---
if __name__ == "__main__":
    # Simulating a log file stream using io.StringIO (representing a large log file)
    mock_log_contents = """
    2026-06-06 10:00:01 - INFO - Server started successfully
    2026-06-06 10:01:15 - ERROR - DatabaseTimeout
    2026-06-06 10:02:30 - WARNING - High memory usage
    2026-06-06 10:03:45 - ERROR - NullPointerException
    2026-06-06 10:04:10 - ERROR - DatabaseTimeout
    2026-06-06 10:05:00 - ERROR - ConnectionRefused
    2026-06-06 10:06:12 - INFO - User logged in
    2026-06-06 10:07:22 - ERROR - DatabaseTimeout
    2026-06-06 10:08:05 - ERROR - NullPointerException
    """
    
    mock_log_file = io.StringIO(mock_log_contents.strip())

    print("--- Starting Log Analysis ---")
    error_frequencies = process_logs(mock_log_file)
    
    print("\n--- Error Frequency Report ---")
    for error_type, count in error_frequencies.most_common():
        print(f"{error_type}: {count}")
