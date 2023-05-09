from pydub import AudioSegment

# Load the audio file
audio_file = AudioSegment.from_file('path/to/audio/file')

# Define the frequency range to boost (in Hz)
low_cutoff_freq = 100
high_cutoff_freq = 200

# Apply a low-frequency boost
boost_amount = 6  # Boost amount in dB
eq_filter = audio_file \
    .low_pass_filter(high_cutoff_freq) \
    .high_pass_filter(low_cutoff_freq)
eq_boosted = eq_filter + boost_amount

# Save the equalized audio file
eq_boosted.export('path/to/eq/audio/file', format='wav')
