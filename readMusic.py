"""
Extracting features using librosa 
"""

import numpy as np
import matplotlib.pyplot as plt
import librosa


#filename = librosa.example('tropicana.mp3')

y, sr = librosa.load('tropicana.mp3')

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
