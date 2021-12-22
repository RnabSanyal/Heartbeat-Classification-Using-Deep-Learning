import pandas as pd
import os
import re
import librosa


DATA_PATH = ".\\DataSet\\"

FILES = os.listdir(DATA_PATH)

data = []

for file in FILES:
	path = DATA_PATH + file

	audio, sr = librosa.load(path)

	data.append([audio, sr, len(audio), re.match('\D+', file).group()])

	print("processed " + file + " @" + str(sr))

heartbeats = pd.DataFrame(data, columns = ['audio', 'sampling_rate', 'length', 'label'])
print(heartbeats.describe())

heartbeats.to_hdf('audio_df.h5', 'raw')