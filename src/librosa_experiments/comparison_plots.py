import pandas as pd

from src.librosa_experiments.sound_plots import *
from constants import metadata_file_mappings_path


df = pd.read_csv(metadata_file_mappings_path)

df_accuracy_1 = df[(df.accuracy == 1) & (df.participant == 1)]
df_accuracy_0 = df[(df.accuracy == 0) & (df.participant == 1)]


n = 3

paths_1 = df_accuracy_1.path[0:n].values
paths_0 = df_accuracy_0.path[0:n].values


for i in range(n):
    plt.figure(figsize=(10, 4))  # Set the figure size

    plt.subplot(1, 2, 1)  # Create the first subplot in a 1x2 grid
    data1, sampling_rate1 = librosa.load(paths_1[i])
    librosa.display.waveshow(data1, sr=sampling_rate1)
    plt.title("Accuracy=1")  # Set the title for the first plot

    plt.subplot(1, 2, 2)  # Create the first subplot in a 1x2 grid
    data0, sampling_rate0 = librosa.load(paths_0[i])
    librosa.display.waveshow(data0, sr=sampling_rate0)
    plt.title("Accuracy=0")  # Set the title for the first plot

    plt.show()

    plt.figure(figsize=(10, 4))  # Set the figure size
    plt.subplot(1, 2, 1)  # Create the first subplot in a 1x2 grid
    X = librosa.stft(data1)
    Xdb = librosa.amplitude_to_db(abs(X))
    librosa.display.specshow(Xdb, sr=sampling_rate1, x_axis='time', y_axis='hz')
    plt.title("Accuracy=1")
    plt.colorbar()

    plt.subplot(1, 2, 2)  # Create the first subplot in a 1x2 grid
    # stft function converts the data into short term fourier transform
    X = librosa.stft(data0)
    Xdb = librosa.amplitude_to_db(abs(X))
    librosa.display.specshow(Xdb, sr=sampling_rate0, x_axis='time', y_axis='hz')
    plt.title("Accuracy=0")
    plt.colorbar()

    plt.show()
