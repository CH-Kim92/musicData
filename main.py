""" Author : Changhyun Kim 
    Starting date : 05/06/2022
"""

import numpy as np
import pandas as pd

musicdb = pd.read_csv(
    'src/genres_v2.csv', usecols=['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'tempo', 'song_name'], low_memory=False)

print(musicdb.dtypes)
print(musicdb.head())
print("Music data shape : ", musicdb.shape)
print(musicdb.describe())
