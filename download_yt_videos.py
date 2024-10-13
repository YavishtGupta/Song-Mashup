import os
from yt_dlp import YoutubeDL

# List of URLs to download
URLS = ['https://youtube.com/playlist?list=PL_u1w9wImcNCsAjqoxlQqwP3tBZZN7cYV&si=wPv1lokCn1PxgbZU']

# Define the folder name
folder_name = './downloads'

# Define the download options
ydl_opts = {
    'playliststart': 1,  # Start downloading from the first video in the playlist
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',  # Flexible video/audio formats
    'merge_output_format': 'mp4',  # Ensure the final file is mp4
    'outtmpl': os.path.join(folder_name, '%(title)s.%(ext)s'),  # Save in the new folder
}

# Create folder if it doesn't exist
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Download the videos
with YoutubeDL(ydl_opts) as ydl:
    ydl.download(URLS)
