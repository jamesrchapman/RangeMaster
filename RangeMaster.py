from pydub import AudioSegment
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from pytube import YouTube
from spleeter.separator import Separator
import subprocess
import wave

import numpy as np
import scipy.signal as signal
def signal_frequency_range(audio_data,sample_rate):
    # Assume audio_data is a 1D numpy array containing the audio samples
    # Assume sample_rate is the sampling rate of the audio data

    # Compute the power spectrum of the audio signal using the FFT
    frequencies, power_spectrum = signal.welch(audio_data, sample_rate, nperseg=1024)
    power_spectrum=np.sqrt(np.multiply(power_spectrum[:,0],power_spectrum[:,0])+np.multiply(power_spectrum[:,1],power_spectrum[:,1]))
    print("power spectrum dimensions")
    print(power_spectrum.size)
    print(power_spectrum)
    # Find the mean and standard deviation of the power spectrum
    mean_spectrum = np.mean(power_spectrum)
    print("mean_spectrum is "+str(mean_spectrum))
    std_spectrum = np.std(power_spectrum)

    # Find the upper and lower bounds for the power spectrum within two standard deviations
    upper_bound = mean_spectrum + 2 * std_spectrum
    print('upper_bound = ' + str(upper_bound))
    lower_bound = mean_spectrum - 2 * std_spectrum
    print('lower_bound = ' + str(lower_bound))

    # Find the frequency range within the bounds
    indices = np.where((power_spectrum <= upper_bound) & (power_spectrum >= lower_bound))[0]
    print("indices")
    print(indices.size)
    print(indices)
    actual_frequencies = np.fft.fftfreq(len(power_spectrum), 1/sample_rate)
    frequencies=actual_frequencies
    print("frequency")
    print(frequencies)

    min_frequency = frequencies[indices[0]]
    max_frequency = frequencies[indices[-1]]

    # Print the frequency range
    print("Frequency range within the first two standard deviations: [{:.2f} Hz, {:.2f} Hz]".format(min_frequency, max_frequency))
    return (min_frequency,max_frequency)


def wav_data_extraction(wav_path):
    # Open the WAV file
    with wave.open(wav_path, "rb") as wav_file:
        # Get the number of audio channels and the sample rate
        num_channels = wav_file.getnchannels()
        sample_rate = wav_file.getframerate()

        # Read all the audio samples from the WAV file
        audio_data = wav_file.readframes(wav_file.getnframes())

        # Convert the audio data to a numpy array
        audio_samples = np.frombuffer(audio_data, dtype=np.int16)

        # Reshape the audio samples to a 2D array, where each row represents a channel
        audio_samples = audio_samples.reshape((-1, num_channels))

    # Get the duration of the WAV file in seconds
    duration = len(audio_samples) / sample_rate

    # Create a time axis in seconds
    time_axis = np.linspace(0, duration, len(audio_samples))

    # # Plot the waveform for each channel
    # for i in range(num_channels):
    #     plt.plot(time_axis, audio_samples[:, i])

    # # Add labels and title
    # plt.xlabel("Time (s)")
    # plt.ylabel("Amplitude")
    # plt.title("Waveform")

    # # Show the plot
    # plt.show()
    return (audio_samples, sample_rate)






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

def vocal_splitter(audio_data):
    # Load the pre-trained vocal separation model
    separator = Separator('spleeter:2stems')

    # # Load the audio file
    # waveform, sample_rate = sepagtrator.load_audio(wav_path)

    # Separate the vocals from the audio
    prediction = separator.separate(audio_data)

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




def power_spectral_density(audio_data, sample_rate):


    # Compute the FFT of the audio signal
    fft_data = np.fft.fft(audio_data)

    # Compute the power spectral density (PSD) of the FFT
    psd_data = np.abs(fft_data) ** 2

    # Compute the frequency range corresponding to each FFT bin
    freqs = np.fft.fftfreq(len(psd_data), 1/sample_rate)

    # Find the range of frequencies that contain the highest signal power
    max_freq_range = freqs[np.argmax(psd_data)]  # Peak frequency
    low_freq_range = freqs[np.argmin(np.abs(psd_data[:len(psd_data)//2] - max(psd_data)/2))]  # Lower frequency range
    high_freq_range = freqs[np.argmin(np.abs(psd_data[len(psd_data)//2:] - max(psd_data)/2)) + len(psd_data)//2]  # Higher frequency range

    # Print the results
    print(f"Frequency range: {low_freq_range} Hz - {high_freq_range} Hz")






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
    audio_data, sample_rate=wav_data_extraction(r"C:\Projects\RangeMaster\test.wav")
    vocals=vocal_splitter(audio_data)
    print(sample_rate)
    signal_frequency_range(vocals,sample_rate)

if __name__ == '__main__':
    main()

