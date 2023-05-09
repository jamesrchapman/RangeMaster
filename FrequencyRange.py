import numpy as np
from scipy.io import wavfile

# Load the audio file
sample_rate, audio_data = wavfile.read('path/to/audio/file')

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
