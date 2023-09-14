import os
import pandas as pd
from matplotlib import pyplot as plt
from playsound import playsound

from constants import ROOT_DIR

path = os.path.join(ROOT_DIR, 'files/data/S2_w01_t1_s60.wav.csv')
df = pd.read_csv(path)

F_0 = df["F0semitoneFrom27.5Hz_sma3nz"]

plt.plot(F_0)
plt.show()

path = os.path.join(ROOT_DIR, 'files/data/S2_w01_t1_s60.wav')

playsound(path)
