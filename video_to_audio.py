import moviepy.editor as mp
import os

def convert_videos_to_audio(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp4"):  # Assuming you're only converting .mp4 files
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + ".mp3")
            
            # Check if the audio file already exists
            if not os.path.exists(output_file):
                clip = mp.VideoFileClip(input_file)
                clip.audio.write_audiofile(output_file)
                print(f"Converted {input_file} to {output_file}")
            else:
                print(f"{output_file} already exists. Skipping conversion.")

# Define input and output folders
input_folder = "./downloads"
output_folder = "./audios"

# Call the function
convert_videos_to_audio(input_folder, output_folder)
