import librosa
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

from constants import metadata_file_mappings

df = pd.read_csv(metadata_file_mappings)

path2data = {}

for idx, df_p in df.groupby("participant"):

    paths = df_p["path"].values

    participant_data = []

    for path in paths:
        print("processing path: ", path)
        # Load the audio file (replace 'your_audio_file.wav' with your audio file path)
        data, sampling_rate = librosa.load(path)

        # print(sampling_rate)

        participant_data.append(data)
        path2data[path] = data

    participant_array = np.concatenate(participant_data)
    participant_array = participant_array.reshape(-1, 1)
    scaler = StandardScaler()
    scaler.fit(participant_array)

    for path in path2data:
        data = path2data[path]
        data = data.reshape(-1, 1)

        data = np.nan_to_num(data)

        normalized_data = scaler.transform(data)
        normalized_data = normalized_data.flatten()
        path2data[path] = normalized_data


