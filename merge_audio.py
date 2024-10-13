import os
from pydub import AudioSegment

# Folder containing the trimmed audio files
trimmed_folder = "trimmed_audios"
merged_audio_file = "output.mp3"  # Output file to save the merged audio

# Initialize an empty AudioSegment object for merging
merged_audio = AudioSegment.empty()

# Process each trimmed audio file in the folder
for filename in os.listdir(trimmed_folder):
    if filename.endswith(".mp3"):
        # Load the trimmed audio file
        file_path = os.path.join(trimmed_folder, filename)
        trimmed_audio = AudioSegment.from_mp3(file_path)
        
        # Append the trimmed audio to the merged audio
        merged_audio += trimmed_audio
        print(f"Merged: {filename}")

# Export the merged audio as a single file
merged_audio.export(merged_audio_file, format="mp3")
print(f"All trimmed audios merged and saved as: {merged_audio_file}")
