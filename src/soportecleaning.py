import pandas as pd
from datetime import date

def calculate_age(birthday):
    today = date.today()
    return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

def playlist_output(df):
    data_usa = df[['title', 'artist', 'url']]
    print('selecting columns:', data_usa.shape)
    print('total artists:',len(data_usa['artist'].tolist()),
          '; total songs (with unique names):',len(data_usa['title'].tolist()),
        '; unique artists:',len(data_usa['artist'].unique().tolist()),
        '; unique songs (with unique names):',
        len(data_usa['title'].unique().tolist())
    )
    data_usa.drop_duplicates(inplace=True)
    print('dropping duplicates', data_usa.shape)
    print('unique artists:',
          len(data_usa['artist'].unique().tolist()),
          '; unique songs (with unique names):',
          len(data_usa['title'].unique().tolist()))
    data_usa['artist_clean'] = data_usa['artist'].str.strip().str.lower()
    print(len(data_usa['artist_clean'].tolist()), len(data_usa['artist'].unique().tolist()))
    data_usa['track_clean'] = data_usa['title'].str.strip().str.lower()
    print(len(data_usa['track_clean'].unique().tolist()), len(data_usa['title'].unique().tolist()))
    data_usa.drop_duplicates(inplace=True)
    return df