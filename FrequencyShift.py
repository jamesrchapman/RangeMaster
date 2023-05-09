from pydub import AudioSegment

# Load the audio file
audio_file = AudioSegment.from_file('path/to/audio/file')

# Define the frequency shift amount (in Hz)
shift_amount = 100

# Shift the frequency of the audio file
shifted = audio_file._spawn(audio_file.raw_data, overrides={
    "frame_rate": audio_file.frame_rate + shift_amount
})

# Save the shifted audio file
shifted.export('path/to/shifted/audio/file', format='wav')
