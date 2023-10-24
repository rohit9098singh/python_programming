import time

# Get the current time in seconds since the epoch
current_time_seconds = time.time()
print("Current time in seconds since the epoch:", current_time_seconds)

# Get the current time as a string in a preferred format
current_time_string = time.ctime(current_time_seconds)
print("Current time as a string:", current_time_string)

# Wait for 2 seconds
print("Waiting for 2 seconds...")
time.sleep(2)

# Get the current time in seconds since the epoch again
current_time_seconds_after_waiting = time.time()

# Calculate the elapsed time
elapsed_time = current_time_seconds_after_waiting - current_time_seconds
print("Elapsed time:", elapsed_time, "seconds")

# Demonstrate the conversion of seconds to a structured time
structured_time = time.localtime(current_time_seconds)
print("Structured Time:", structured_time)
