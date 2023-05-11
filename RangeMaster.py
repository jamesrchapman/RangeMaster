from pydub import AudioSegment
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from pytube import YouTube
from spleeter.separator import Separator
import subprocess


def mp4_to_wav(filename_mp4,filename_wav):
    # Execute the ffmpeg command to convert the input file to a WAV file
    subprocess.run(["ffmpeg", "-i", filename_mp4, "-vn", "-acodec", "pcm_s16le", "-ar", "44100", "-ac", "2", filename_wav])



def user_YT_url_request():
    return input("Enter the YouTube video URL: ")


def download_YT_mp3_by_url_ui():
    download_YT_mp3_by_url(user_YT_url_request())


def download_YT_mp3_by_url(url):
    # create a YouTube object from the video URL
    yt = YouTube(url)

    # select the audio-only stream
    stream = yt.streams.filter(only_audio=True).first()

    # download the audio
    stream.download()

def vocal_splitter(wav_path):
    # Load the pre-trained vocal separation model
    separator = Separator('spleeter:2stems')

    # # Load the audio file
    # waveform, sample_rate = separator.load_audio(wav_path)

    # Separate the vocals from the audio
    prediction = separator.separate(wav_path)

    # Extract the vocals from the prediction dictionary
    vocals = prediction['vocals']
    return vocals

def histogram(vocals):
    # Compute the histogram of the vocals
    hist, bins = np.histogram(vocals, bins=50)

    # Plot the histogram
    plt.bar(bins[:-1], hist, width=bins[1]-bins[0])
    plt.title('Histogram of Vocal Amplitudes')
    plt.xlabel('Amplitude')
    plt.ylabel('Count')
    plt.show()






# # Load the audio file
# sample_rate, audio_data = wavfile.read('path/to/audio/file')

# # Compute the FFT of the audio signal
# fft_data = np.fft.fft(audio_data)

# # Compute the power spectral density (PSD) of the FFT
# psd_data = np.abs(fft_data) ** 2

# # Compute the frequency range corresponding to each FFT bin
# freqs = np.fft.fftfreq(len(psd_data), 1/sample_rate)

# # Find the range of frequencies that contain the highest signal power
# max_freq_range = freqs[np.argmax(psd_data)]  # Peak frequency
# low_freq_range = freqs[np.argmin(np.abs(psd_data[:len(psd_data)//2] - max(psd_data)/2))]  # Lower frequency range
# high_freq_range = freqs[np.argmin(np.abs(psd_data[len(psd_data)//2:] - max(psd_data)/2)) + len(psd_data)//2]  # Higher frequency range

# # Print the results
# print(f"Frequency range: {low_freq_range} Hz - {high_freq_range} Hz")






# # Load the audio file
# audio_file = AudioSegment.from_file('path/to/audio/file')

# # Define the frequency shift amount (in Hz)
# shift_amount = 100

# # Shift the frequency of the audio file
# shifted = audio_file._spawn(audio_file.raw_data, overrides={
#     "frame_rate": audio_file.frame_rate + shift_amount
# })

# # Save the shifted audio file
# shifted.export('path/to/shifted/audio/file', format='wav')




def main():
    # download_YT_mp3_by_url_ui()
    # audio_file=r"C:\Projects\RangeMaster\test.mp4"
    # mp4_to_wav(audio_file,r"C:\Projects\RangeMaster\test.wav")
    vocals=vocal_splitter(r"C:\Projects\RangeMaster\test.wav")
    histogram(vocals)

if __name__ == '__main__':
    main()

