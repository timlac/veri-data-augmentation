import os
from copy import copy

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

metadata_file_mappings_path = os.path.join(ROOT_DIR, "files/data/master_file_mappings.csv")
master_functionals_path = os.path.join(ROOT_DIR, "files/data/master_functionals.csv")
master_low_level_path = os.path.join(ROOT_DIR, "files/data/master_low_level.csv")
master_functionals_new_features_path = os.path.join(ROOT_DIR, "files/data/master_functionals_new_features.csv")


AUDIO_FUNCTIONALS_EGEMAPS_V2_COLS = ['F0semitoneFrom27.5Hz_sma3nz_amean',
                                     'F0semitoneFrom27.5Hz_sma3nz_stddevNorm',
                                     'F0semitoneFrom27.5Hz_sma3nz_percentile20.0',
                                     'F0semitoneFrom27.5Hz_sma3nz_percentile50.0',
                                     'F0semitoneFrom27.5Hz_sma3nz_percentile80.0',
                                     'F0semitoneFrom27.5Hz_sma3nz_pctlrange0-2',
                                     'F0semitoneFrom27.5Hz_sma3nz_meanRisingSlope',
                                     'F0semitoneFrom27.5Hz_sma3nz_stddevRisingSlope',
                                     'F0semitoneFrom27.5Hz_sma3nz_meanFallingSlope',
                                     'F0semitoneFrom27.5Hz_sma3nz_stddevFallingSlope', 'loudness_sma3_amean',
                                     'loudness_sma3_stddevNorm', 'loudness_sma3_percentile20.0',
                                     'loudness_sma3_percentile50.0', 'loudness_sma3_percentile80.0',
                                     'loudness_sma3_pctlrange0-2', 'loudness_sma3_meanRisingSlope',
                                     'loudness_sma3_stddevRisingSlope', 'loudness_sma3_meanFallingSlope',
                                     'loudness_sma3_stddevFallingSlope', 'spectralFlux_sma3_amean',
                                     'spectralFlux_sma3_stddevNorm', 'mfcc1_sma3_amean',
                                     'mfcc1_sma3_stddevNorm', 'mfcc2_sma3_amean', 'mfcc2_sma3_stddevNorm',
                                     'mfcc3_sma3_amean', 'mfcc3_sma3_stddevNorm', 'mfcc4_sma3_amean',
                                     'mfcc4_sma3_stddevNorm', 'jitterLocal_sma3nz_amean',
                                     'jitterLocal_sma3nz_stddevNorm', 'shimmerLocaldB_sma3nz_amean',
                                     'shimmerLocaldB_sma3nz_stddevNorm', 'HNRdBACF_sma3nz_amean',
                                     'HNRdBACF_sma3nz_stddevNorm', 'logRelF0-H1-H2_sma3nz_amean',
                                     'logRelF0-H1-H2_sma3nz_stddevNorm', 'logRelF0-H1-A3_sma3nz_amean',
                                     'logRelF0-H1-A3_sma3nz_stddevNorm', 'F1frequency_sma3nz_amean',
                                     'F1frequency_sma3nz_stddevNorm', 'F1bandwidth_sma3nz_amean',
                                     'F1bandwidth_sma3nz_stddevNorm', 'F1amplitudeLogRelF0_sma3nz_amean',
                                     'F1amplitudeLogRelF0_sma3nz_stddevNorm', 'F2frequency_sma3nz_amean',
                                     'F2frequency_sma3nz_stddevNorm', 'F2bandwidth_sma3nz_amean',
                                     'F2bandwidth_sma3nz_stddevNorm', 'F2amplitudeLogRelF0_sma3nz_amean',
                                     'F2amplitudeLogRelF0_sma3nz_stddevNorm', 'F3frequency_sma3nz_amean',
                                     'F3frequency_sma3nz_stddevNorm', 'F3bandwidth_sma3nz_amean',
                                     'F3bandwidth_sma3nz_stddevNorm', 'F3amplitudeLogRelF0_sma3nz_amean',
                                     'F3amplitudeLogRelF0_sma3nz_stddevNorm', 'alphaRatioV_sma3nz_amean',
                                     'alphaRatioV_sma3nz_stddevNorm', 'hammarbergIndexV_sma3nz_amean',
                                     'hammarbergIndexV_sma3nz_stddevNorm', 'slopeV0-500_sma3nz_amean',
                                     'slopeV0-500_sma3nz_stddevNorm', 'slopeV500-1500_sma3nz_amean',
                                     'slopeV500-1500_sma3nz_stddevNorm', 'spectralFluxV_sma3nz_amean',
                                     'spectralFluxV_sma3nz_stddevNorm', 'mfcc1V_sma3nz_amean',
                                     'mfcc1V_sma3nz_stddevNorm', 'mfcc2V_sma3nz_amean',
                                     'mfcc2V_sma3nz_stddevNorm', 'mfcc3V_sma3nz_amean',
                                     'mfcc3V_sma3nz_stddevNorm', 'mfcc4V_sma3nz_amean',
                                     'mfcc4V_sma3nz_stddevNorm', 'alphaRatioUV_sma3nz_amean',
                                     'hammarbergIndexUV_sma3nz_amean', 'slopeUV0-500_sma3nz_amean',
                                     'slopeUV500-1500_sma3nz_amean', 'spectralFluxUV_sma3nz_amean',
                                     'loudnessPeaksPerSec', 'VoicedSegmentsPerSec',
                                     'MeanVoicedSegmentLengthSec', 'StddevVoicedSegmentLengthSec',
                                     'MeanUnvoicedSegmentLength', 'StddevUnvoicedSegmentLength',
                                     'equivalentSoundLevel_dBp']

new_features = ["CumPauseLength",
                "MeanPauseSegmentLength",
                "PausesAbove0.5Sec",
                "PausesAbove1Sec",
                "PausesAbove1.5Sec",
                "PausesAbove2Sec"]

AUDIO_FUNCTIONALS_EGEMAPS_V2_COLS_NEW_FEATURES = copy(AUDIO_FUNCTIONALS_EGEMAPS_V2_COLS)
AUDIO_FUNCTIONALS_EGEMAPS_V2_COLS_NEW_FEATURES.extend(new_features)