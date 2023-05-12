import librosa
import numpy as np

# Load the audio file
y, sr = librosa.load('your_wav_file.wav')

# Get the pitches of the notes played at a given time
def get_notes_at_time(y, sr, time):
    # Get the spectral content of the audio signal
    stft = np.abs(librosa.stft(y))
    chroma = librosa.feature.chroma_stft(S=stft, sr=sr)
    
    # Get the indices of the highest values in each chroma vector
    max_indices = np.argmax(chroma, axis=0)
    
    # Get the pitches of the notes corresponding to the highest values
    notes = librosa.core.midi_to_note(max_indices)
    
    # Find the notes that are being played at the given time
    notes_at_time = []
    for i, note in enumerate(notes):
        onset = librosa.frames_to_time(i, sr=sr)
        if onset <= time < onset + 0.1:  # Adjust the duration as needed
            notes_at_time.append(note)
            
    return notes_at_time

# Get the notes played at time 5 seconds
notes_at_5s = get_notes_at_time(y, sr, 5.0)
print(notes_at_5s)
