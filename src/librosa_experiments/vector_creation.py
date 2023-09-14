import librosa
import pandas as pd
from playsound import playsound
from matplotlib import pyplot as plt


from src.librosa_experiments.sound_plots import rms_plot
from constants import metadata_file_mappings


def analyze_wave(path):
    data, sampling_rate = librosa.load(path)
    # voiced_intervals = librosa.effects.split(data, top_db=5)
    # total_duration = librosa.get_duration(y=data, sr=sampling_rate)

    plt.figure(figsize=(10, 3))
    librosa.display.waveshow(data, sr=sampling_rate)

    # for i in silent_intervals:
    #     # Add vertical lines at specific x-values (e.g., x=2 and x=4)
    #     plt.axvline(x=i[0], color='blue', linestyle='--', label='Vertical Line at x=2')
    #     plt.axvline(x=i[1], color='red', linestyle='-.', label='Vertical Line at x=4')

    plt.show()

def main():
    df = pd.read_csv(metadata_file_mappings)

    paths = df["path"].values
    for path in paths[209:210]:

        # Load the audio file (replace 'your_audio_file.wav' with your audio file path)
        data, sampling_rate = librosa.load(path)

        rms_plot(data)

        # create_waveplot(data, sampling_rate)

        # Segment the audio into silent intervals
        voiced_intervals = librosa.effects.split(data, top_db=5)

        # Calculate total audio duration in seconds
        total_duration = librosa.get_duration(y=data, sr=sampling_rate)

        silent_intervals = []
        start_silent = 0
        last_interval = False

        for idx in range(len(voiced_intervals)):
            start_voiced = voiced_intervals[idx][0] / sampling_rate
            end_voiced = voiced_intervals[idx][1] / sampling_rate

            silent_interval = (start_voiced - start_silent)
            silent_intervals.append((start_silent, start_voiced))

            start_silent = end_voiced

        silent_interval = start_silent - total_duration
        silent_intervals.append((start_silent, total_duration))

        # for idx in range(len(voiced_intervals) + 1):
        #     if idx == len(voiced_intervals):
        #         last_interval = True
        #         start_voiced = total_duration
        #     else:
        #         start_voiced = voiced_intervals[idx][0] / sampling_rate
        #         end_voiced = voiced_intervals[idx][1] / sampling_rate
        #
        #     silent_interval = (start_voiced - start_silent)
        #     silent_intervals.append((start_silent, start_voiced))
        #
        #     if not last_interval:
        #         start_silent = end_voiced

        plt.figure(figsize=(10, 3))
        librosa.display.waveshow(data, sr=sampling_rate)

        for i in silent_intervals:
            # Add vertical lines at specific x-values (e.g., x=2 and x=4)
            plt.axvline(x=i[0], color='blue', linestyle='--', label='Vertical Line at x=2')
            plt.axvline(x=i[1], color='red', linestyle='-.', label='Vertical Line at x=4')

        plt.show()

        playsound(path)







    # Initialize silent intervals as the entire audio duration
    # silent_intervals = []







    # # Iterate through non-silent intervals to find silent intervals
    # for start, end in voiced_intervals:
    #     silent_intervals.append((end, start))
    #
    # # Calculate the durations of silent intervals in seconds
    # silent_intervals_durations = []
    # for start, end in voiced_intervals:
    #     duration = (end - start) / sampling_rate
    #     silent_intervals_durations.append(duration)






    #     silent_intervals_durations.append(duration)
    #
    # # silent_intervals_durations = [((end - start) / sampling_rate) for start, end in intervals]
    #
    # # Convert the durations to a feature vector (you can choose to normalize if needed)
    # feature_vector = np.array(silent_intervals_durations)
    #
    # # Print the feature vector
    # print("Feature Vector:", feature_vector)
