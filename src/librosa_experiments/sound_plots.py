from matplotlib import pyplot as plt
import librosa.display
import librosa

import numpy as np


def rms_plot(data):
    # As a first step, we can plot the root-mean-square (RMS) curve
    rms = librosa.feature.rms(y=data)[0]

    times = librosa.frames_to_time(np.arange(len(rms)))

    fig, ax = plt.subplots()
    ax.plot(times, rms)
    ax.set(xlabel='Time', ylabel='RMS')

    plt.show()


def create_waveplot(data, sr, e=None):
    plt.figure(figsize=(10, 3))
    plt.title('Waveplot for audio with {} '.format(e), size=15)
    librosa.display.waveshow(data, sr=sr)
    plt.show()


def create_spectrogram(data, sr, e):
    # stft function converts the data into short term fourier transform
    X = librosa.stft(data)
    Xdb = librosa.amplitude_to_db(abs(X))
    plt.figure(figsize=(12, 3))
    plt.title('Spectrogram for audio with {} '.format(e), size=15)
    librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
    #librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar()
