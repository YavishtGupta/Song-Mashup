import os
from pydub import AudioSegment
import random

# Folder paths
input_folder = "audios"  # Folder containing the audio files
output_folder = "trimmed_audios"  # Folder to save trimmed files
trim_duration_ms = 6000  # Duration to trim in milliseconds (e.g., 5000ms = 5 seconds)

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each audio file in the folder
for filename in os.listdir(input_folder):
    if filename.endswith(".mp3"):
        # Load the audio file
        file_path = os.path.join(input_folder, filename)
        audio = AudioSegment.from_mp3(file_path)
        start = random.randint(5000, len(audio)-10000)  # Random start point
        
        # Trim the audio (start trim from both beginning and end)
        trimmed_audio = audio[start:start+trim_duration_ms]  # Trim from start and end
        
        # Save the trimmed audio to the output folder
        output_path = os.path.join(output_folder, f"trimmed_{filename}")
        trimmed_audio.export(output_path, format="mp3")
        
        print(f"Trimmed and saved: {output_path}")

print("All files trimmed successfully.")
