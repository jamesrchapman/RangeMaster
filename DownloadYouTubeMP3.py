from pytube import YouTube

# ask user for the video URL
video_url = input("Enter the YouTube video URL: ")

# create a YouTube object from the video URL
yt = YouTube(video_url)

# select the audio-only stream
stream = yt.streams.filter(only_audio=True).first()

# download the audio
stream.download()
