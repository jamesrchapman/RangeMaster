# Certainly! Here is some Python code that uses the `pytube` library to download a YouTube video by URL:

# ```python
from pytube import YouTube

# ask user for the video URL
video_url = input("Enter the YouTube video URL: ")

# create a YouTube object from the video URL
yt = YouTube(video_url)

# select the highest resolution stream
stream = yt.streams.get_highest_resolution()

# download the video
stream.download()
# ```

# This code prompts the user to enter a YouTube video URL and then creates a `YouTube` object using the `pytube` library. It then selects the highest resolution stream available for the video and downloads it to the current working directory.

# Note that you'll need to have the `pytube` library installed for this code to work. You can install it using pip:

# ```
# pip install pytube
# ```

# I hope that helps! Let me know if you have any further questions.