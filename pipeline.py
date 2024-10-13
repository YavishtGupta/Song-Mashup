import os
import time

# Define the script names
scripts = [
    "download_yt_videos.py",
    "video_to_audio.py",
    "trim_audio.py",
    "merge_audio.py"
]

# Function to run a script using os.system and measure the time
def run_script(script_name):
    print(f"Running {script_name}...")
    
    # Record the start time
    start_time = time.time()
    
    # Run the script using os.system
    result = os.system(f'python {script_name}')
    
    # Calculate the time taken for this script
    elapsed_time = time.time() - start_time
    
    # Check if the script ran successfully
    if result != 0:
        print(f"Error: {script_name} failed to run.")
        exit(1)  # Stop the pipeline if any script fails
    else:
        print(f"{script_name} completed successfully in {elapsed_time:.2f} seconds.\n")

# Record the total start time for the entire pipeline
total_start_time = time.time()

# Run each script in the defined sequence
for script in scripts:
    run_script(script)

# Calculate the total time taken for the entire pipeline
total_elapsed_time = time.time() - total_start_time

print(f"All scripts completed successfully! Total time taken: {total_elapsed_time:.2f} seconds.")
