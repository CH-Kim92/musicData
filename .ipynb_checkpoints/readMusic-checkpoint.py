"""
Extracting features using librosa 
"""

import numpy as np
import matplotlib.pyplot as plt
import librosa

import librosa.display

#filename = librosa.example('tropicana.mp3')

y, sr = librosa.load('tropicana.mp3')

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('Estimated tempo: {:.2f} beats per minute'.format(tempo))


S_full, phase = librosa.magphase(librosa.stft(y))
fig, ax = plt.subplots()
img = librosa.display.specshow(librosa.amplitude_to_db(S_full, ref=np.max),
                               y_axis='log', x_axis='time', sr=sr, ax=ax)
fig.colorbar(img, ax=ax)

rms = librosa.feature.rms(y=y)[0]

times = librosa.frames_to_time(np.arange(len(rms)))

fig, ax = plt.subplots()
ax.plot(times, rms)
ax.axhline(0.02, color='r', alpha=0.5)
ax.set(xlabel='Time', ylabel='RMS')

# D = librosa.stft(y)

# s = np.abs(D**2)
# chroma = librosa.feature.chroma_stft(S=s, sr=sr)
# chroma = np.cumsum(chroma)

# x = np.linspace(-chroma, chroma)
# plt.plot(x, np.sin(x))
# plt.xlabel('Angle [rad]')
# plt.ylabel('sin(x)')
# plt.axis('tight')
# plt.show()
