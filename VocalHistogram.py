!pip install spleeter  # Install spleeter

import numpy as np
import matplotlib.pyplot as plt
from spleeter.separator import Separator

# Load the pre-trained vocal separation model
separator = Separator('spleeter:2stems')

# Load the audio file
audio_path = 'path/to/audio/file'
waveform, sample_rate = separator.load_audio(audio_path)

# Separate the vocals from the audio
prediction = separator.separate(waveform)

# Extract the vocals from the prediction dictionary
vocals = prediction['vocals']

# Compute the histogram of the vocals
hist, bins = np.histogram(vocals, bins=50)

# Plot the histogram
plt.bar(bins[:-1], hist, width=bins[1]-bins[0])
plt.title('Histogram of Vocal Amplitudes')
plt.xlabel('Amplitude')
plt.ylabel('Count')
plt.show()
