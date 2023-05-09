import numpy as np
from scipy.io import wavfile

# Load the audio file
sample_rate, audio_data = wavfile.read('path/to/audio/file')

# Generate a carrier signal
carrier_frequency = 1000 # Hz
t = np.arange(len(audio_data)) / sample_rate
carrier_signal = np.sin(2 * np.pi * carrier_frequency * t)

# Apply frequency modulation to the carrier signal
modulation_index = 10  # Modulation index
fm_signal = np.sin(2 * np.pi * (carrier_frequency + modulation_index * audio_data) * t)

# Save the frequency modulated audio file
wavfile.write('path/to/fm/audio/file', sample_rate, fm_signal.astype(np.float32))
