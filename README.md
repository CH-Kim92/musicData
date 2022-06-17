## musicRecommand

dataset : songs in Spotify from kaggle.  
https://www.kaggle.com/datasets/mrmorj/dataset-of-songs-in-spotify?resource=download
Audio file features from Spotify
https://www.therecordindustry.io/spotify-audio-features/
<br />
<br />
I want to use specific columns such as energy, danceability, song_name .. from the dataset.  
Pandas is very good for managing data type so if a coloumn contains multiply data types it will be denided to import.  
To solve that, using `read_csv('file_path',low_memory_False)`.
<br />
<br />

<h3> Checking data type of all columns in data frame </h3>
  Using dtypes.     
  `musicdb.dtypes`
<p> Every mesic file is basically made up of two important things, the smaple rate, and the sample data.</p>
