from dotenv import load_dotenv
import os
from pyannote.audio import Pipeline
from playsound import playsound
import json
import pandas as pd
from constants import metadata_file_mappings


load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

df = pd.read_csv(metadata_file_mappings)

paths = df["path"].values
path = paths[1]

# path = "/home/tim/Downloads/klippta_ljudfiler/w02_t01/S2_w02_t1_s56.wav"
path = "/home/tim/Downloads/klippta_ljudfiler/w31_t01/S2_w31_t1_s61.wav"

pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1",
                                    use_auth_token=ACCESS_TOKEN)

# apply the pipeline to an audio file
diarization = pipeline(path)

# dump the diarization output to disk using RTTM format
with open("audio.rttm", "w") as rttm:
    diarization.write_rttm(rttm)
