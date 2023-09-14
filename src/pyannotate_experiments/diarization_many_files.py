from dotenv import load_dotenv
import os
from pyannote.audio import Pipeline
import pandas as pd
from pathlib import Path

from constants import metadata_file_mappings, ROOT_DIR
import json


load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

df = pd.read_csv(metadata_file_mappings)

paths = df["path"].values

pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1",
                                    use_auth_token=ACCESS_TOKEN)

rttm_path = os.path.join(ROOT_DIR, "files/out/rttm_files")

# dict mapping from wav file path: rttm file path
many_speakers_found = {}

for idx, path in enumerate(paths[200:]):
    print("Processing file: ", path)

    output = pipeline(path)
    if len(output.labels()) <= 1:
        continue

    else:
        print("Non empty diarization found for file: ", path)
        filename = Path(path).stem
        output_path = os.path.join(rttm_path, filename + ".rttm")

        many_speakers_found[path] = output_path

        with open(output_path, "w") as rttm:
            output.write_rttm(rttm)


# Specify the file path where you want to save the JSON data
json_path = os.path.join(ROOT_DIR, "files/out/wav2rttm.json")

# Open the file in write mode and use json.dump() to write the dictionary as a JSON object
with open(json_path, "w") as json_file:
    json.dump(many_speakers_found, json_file)

print(f"The JSON data has been saved to {json_path}")