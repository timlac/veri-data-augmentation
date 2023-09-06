# code generated by chat gpt

import librosa
import numpy as np

# Load the audio file (replace 'your_audio_file.wav' with your audio file path)
y, sr = librosa.load('your_audio_file.wav')

# Segment the audio into silent intervals
intervals = librosa.effects.split(y)

# Calculate the durations of silent intervals in seconds
silent_intervals_durations = [((end - start) / sr) for start, end in intervals]

# Convert the durations to a feature vector (you can choose to normalize if needed)
feature_vector = np.array(silent_intervals_durations)

# Print the feature vector
print("Feature Vector:", feature_vector)
