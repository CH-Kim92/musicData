""" Author : Changhyun Kim 
    Starting date : 05/06/2022
"""

import numpy as np
import pandas as pd
import random 
import tensorflow as tf 
import matplotlib.pyplot as plt


musicdb = pd.read_csv(
    'src/genres_v2.csv', usecols=['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'tempo', 'song_name'], low_memory=False)

# Drop na value
musicDB = musicdb.dropna()
print(musicDB.dtypes)
print(musicDB.head())
print("Music data shape : ", musicDB.shape)
print(musicDB.describe())

musicdb_columns = musicdb.columns

# devide dataset into predictors and target 
predictors = musicdb[musicdb_columns[musicdb_columns != 'song_name']]
target = musicdb['song_name']

rand_number = random.randrange(0,21519)
print(musicDB.iloc[rand_number])
