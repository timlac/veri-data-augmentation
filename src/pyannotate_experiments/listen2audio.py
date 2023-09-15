import os
from playsound import playsound
from constants import metadata_file_mappings_path, ROOT_DIR
import json

path = os.path.join(ROOT_DIR, "files/out/wav2rttm.json")

# Open the file in read mode and use json.load() to load the JSON data into a Python dictionary
with open(path, "r") as json_file:
    wav2rttm = json.load(json_file)

for key, val in wav2rttm.items():
    with open(val, "r") as file:
        print(file)
        file_contents = file.read()
        print(file_contents)
    playsound(key)
    print()


