import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid ="c27d762046d144e48d9d7d929e9c2206" 
secret = "fd9583d5356249e1a32e262640b989dc"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# timeit library to measure the time needed to run this code
import timeit
start = timeit.default_timer()

# create empty lists where the results are going to be stored
artist_name = []
track_name = []
popularity = []
track_id = []

for i in range(0,10000,50):
    track_results = sp.search(q='year:2018', type='track', limit=50,offset=i)
    for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])
      

stop = timeit.default_timer()
print ('Time to run this code (in seconds):', stop - start)

print('number of elements in the track_id list:', len(track_id))


import pandas as pd

df_tracks = pd.DataFrame({'artist_name':artist_name,'track_name':track_name,'track_id':track_id,'popularity':popularity})
print(df_tracks.shape)
df_tracks.head()
df_tracks.info()

# group the entries by artist_name and track_name and check for duplicates

grouped = df_tracks.groupby(['artist_name','track_name'], as_index=True).size()
grouped[grouped > 1].count()

# drop duplicate entries
df_tracks.drop_duplicates(subset=['artist_name','track_name'], inplace=True)

# doing the same grouping as before to verify the solution
grouped_after_dropping = df_tracks.groupby(['artist_name','track_name'], as_index=True).size()
grouped_after_dropping[grouped_after_dropping > 1].count()

df_tracks[df_tracks.duplicated(subset=['artist_name','track_name'],keep=False)].count()

df_tracks.shape


## Retrieve Audio Features
# Measuring time
start = timeit.default_timer()

rows = []
batchsize = 100
None_counter = 0

for i in range(0, len(df_tracks['track_id']), batchsize): 
    batch = df_tracks['track_id'][i:i+batchsize]
    feature_results = sp.audio_features(batch)
    
    for i, t in enumerate(feature_results):
        if t == None:
            Non_counter = None_counter + 1
        else:
            rows.append(t)
            
print('Number of tracks where no audio features were available:', None_counter)

stop = timeit.default_timer()
print ('Code runtime (sec):', stop - start)


## EDA & Data preparation
print('Number of elements in track_id list:', len(rows))

Loading autdio features into a dataframe:
df_audio_features = pd.DataFrame.from_dict(rows, orient='columns')
print("Shape of dataset:", df_audio_features.shape)
df_audio_features.head()

df_audio_features.info()

# Dropping all variables (columns) not relevant to the analysis:
columns_to_drop = ['analysis_url', 'track_href', 'type', 'uri']
df_audio_features.drop(columns_to_drop, axis=1, inplace=True)

# Renaming id to track_id to match the df_tracks dataframe
df_audio_features.rename(columns = {'id': 'track_id'}, inplace=True)
df_audio_features.shape # checking our progress

# Merge dataframes
df = pd.merge(df_tracks, df_audio_features, on='track_id', how='inner')
print("Shape of dataset:", df_audio_features.shape)
df.head()

df.info()

# Check again for duplicates
df[df.duplicated(subset=['artist_name', 'track_name'], keep=False)]

# Save to csv
df.to_csv('SpotifyAudioFeatures25052019.csv')



## Get audio_analysis() of a track
# Measuring time
'''
start = time.time()

rows = []
None_counter = 0

for i in range(0, len(df['uri'])): 
    if (df['uri'][i] != 'spotify:track:0OyBzq066dZIW5nbgcfY36'):
    # This track is an hour long mix with no audio_analysis
        audio_analysis_results = sp.audio_analysis(df['uri'][i])

        if audio_analysis_results: 
            rows.append(audio_analysis_results)
        else:
            None_counter = None_counter + 1

stop = time.time()
print ('Code runtime (sec):', stop - start)        
print('Number of tracks where no audio features were available:', None_counter)
'''










