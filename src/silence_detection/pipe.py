import numpy as np
import pandas as pd
import os
import librosa
import opensmile

from nexa_preprocessing.utils.time_series_operations import slice_by

from src.silence_detection.process_with_smile import SmileProcess
from src.silence_detection.segmentation import segment_based_on_silence
from constants import master_functionals_path, master_low_level_path, master_functionals_new_features_path


def get_number_of_pauses_above_length(pauses, threshold):
    ret = 0
    for pause in pauses_segment_lengths:
        if pause > threshold:
            ret += 1
    return ret


df_llds = pd.read_csv(master_low_level_path)
slices = slice_by(df_llds, "filename")
df_funcs = pd.read_csv(master_functionals_path)

# P value 4.5684061918112104e-08
df_funcs["CumPauseLength"] = float(0)

# P value 0.020535450608944142
df_funcs["MeanPauseSegmentLength"] = float(0)

df_funcs["PausesAbove0.5Sec"] = float(0)
df_funcs["PausesAbove1Sec"] = float(0)
df_funcs["PausesAbove1.5Sec"] = float(0)
df_funcs["PausesAbove2Sec"] = float(0)

for idx, df_lld in enumerate(slices):

    print()
    print(idx)
    filename = df_lld["filename"].iloc[0]

    print(filename)

    df_func = df_funcs.loc[df_funcs['filename'] == filename]

    # total_duration = df_lld.index.get_level_values("end").max().total_seconds()
    total_duration = pd.to_timedelta(df_lld["end"].max()).total_seconds()
    total_segments = len(df_lld)

    silent_segment_lengths, voiced_segment_lengths = segment_based_on_silence(
        df_lld['F0semitoneFrom27.5Hz_sma3nz'].values)

    voiced_segments_per_second = len(voiced_segment_lengths) / total_duration

    print("voiced per sec")
    print(voiced_segments_per_second)
    print(df_func["VoicedSegmentsPerSec"].values[0])

    mean_length_voiced_segments = np.asarray(voiced_segment_lengths).mean()

    print("mean length of voiced")
    print(mean_length_voiced_segments / 100)
    print(df_func["MeanVoicedSegmentLengthSec"].values[0])

    print("mean length of silence")
    mean_length_silence_segments = np.asarray(silent_segment_lengths).mean()
    print(mean_length_silence_segments / 100)
    print(df_func["MeanUnvoicedSegmentLength"].values[0])

    print("pauses")
    # finding pauses should be as easy as simply removing the first and last silent segments...
    # the downside of using cumulative pauses is that it doesn't take into account the length of the file as much?
    if len(silent_segment_lengths) > 2:
        pauses_segment_lengths = silent_segment_lengths[1:-1]
        cum_pause_length = sum(silent_segment_lengths) / 100
        mean_length_pauses = np.asarray(pauses_segment_lengths).mean() / 100

        condition = df_funcs['filename'] == filename
        df_funcs.loc[condition, 'CumPauseLength'] = cum_pause_length
        df_funcs.loc[condition, 'MeanPauseSegmentLength'] = mean_length_pauses

        df_funcs.loc[condition, 'PausesAbove0.5Sec'] = get_number_of_pauses_above_length(pauses_segment_lengths, 50)
        df_funcs.loc[condition, 'PausesAbove1Sec'] = get_number_of_pauses_above_length(pauses_segment_lengths, 100)
        df_funcs.loc[condition, 'PausesAbove1.5Sec'] = get_number_of_pauses_above_length(pauses_segment_lengths, 150)
        df_funcs.loc[condition, 'PausesAbove2Sec'] = get_number_of_pauses_above_length(pauses_segment_lengths, 200)


df_funcs.to_csv(master_functionals_new_features_path)


