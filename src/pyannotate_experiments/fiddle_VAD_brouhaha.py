from dotenv import load_dotenv
import os
from pyannote.audio import Pipeline
from playsound import playsound

import pandas as pd
from constants import metadata_file_mappings_path

from src.librosa_experiments.vector_creation import analyze_wave

load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

df = pd.read_csv(metadata_file_mappings_path)

paths = df["path"].values

pipeline = Pipeline.from_pretrained("pyannote/brouhaha",
                                    use_auth_token=ACCESS_TOKEN)

print("hej")