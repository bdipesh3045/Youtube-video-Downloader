import os

from pytube import YouTube

# Prompt the user for the video URL
url = input("Enter the YouTube video URL: ")

# Get the YouTube video
video = YouTube(url)

stream = video.streams.get_by_resolution("360p")

if stream is None:
    raise ValueError("No 240p resolution stream available.")

# Create a directory with the same name as the video title
directory = video.title
if not os.path.exists(directory):
    os.makedirs(directory)

# Download the video to the created directory
stream.download(output_path=directory)

print("Video downloaded successfully to", directory)
# Get the stream for 240p resolution
stream = video.streams.get_by_resolution("240p")

# Create a directory with the same name as the video title
directory = video.title
if not os.path.exists(directory):
    os.makedirs(directory)

# Download the video to the created directory
stream.download(output_path=directory)

print("Video downloaded successfully to", directory)
