from dotenv import load_dotenv
import os
from pyannote.audio import Pipeline
from playsound import playsound
import json
import pandas as pd
from constants import metadata_file_mappings

from src.librosa_experiments.vector_creation import analyze_wave

load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

df = pd.read_csv(metadata_file_mappings)

paths = df["path"].values

pipeline = Pipeline.from_pretrained("pyannote/voice-activity-detection",
                                    use_auth_token=ACCESS_TOKEN)

pauses_dict = {}

for idx, path in enumerate(paths[0:100]):
    # print("\nanalysing path ", idx)

    output = pipeline(path)

    # analyze_wave(path)

    pauses = []

    if len(output.get_timeline().support()) > 2:
        for jdx, speech in enumerate(output.get_timeline().support()):
            if jdx == 0:
                start_silent = speech.end
            else:
                silent_duration = speech.start - start_silent
                pauses.append(silent_duration)
                start_silent = speech.end

    pauses_dict[path] = pauses

json.dump(pauses_dict, "files/out/pauses_dict.json")


sum_dict = {}
for key, val in pauses_dict.items():
    sum_dict[key] = sum(val)

df['sum_pauses'] = df['path'].map(sum_dict)

# df.to_csv("files/out/master_file_with_pauses")
