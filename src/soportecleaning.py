import pandas as pd
from datetime import date

import warnings
warnings.filterwarnings("ignore")

def calculate_age(birthday):
    today = date.today()
    return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

def new_columns(data_usa):
    """
    Objective:
    The objective of the 'new_columns' function is to add new columns to a given pandas dataframe 'data_usa'. These new columns include 'week_in_charts' and 'times_in_charts' which are calculated based on the existing columns 'url', 'chart', and 'rank' in the dataframe. Additionally, the function converts the 'date' column to datetime format.

    Inputs:
    - data_usa: a pandas dataframe containing columns 'url', 'chart', 'rank', and 'date'.

    Flow:
    1. Merge the dataframe with a new dataframe that contains the count of how many times each combination of 'url' and 'chart' appears in the original dataframe. This creates a new column 'week_in_charts'.
    2. Drop the '_merge' column that was created during the merge.
    3. Merge the dataframe with a new dataframe that contains the first occurrence of each combination of 'url' and 'chart' in the original dataframe. This creates a new column 'times_in_charts'.
    4. Drop the '_merge' column that was created during the merge.
    5. Convert the 'date' column to datetime format.
    6. Return the modified dataframe.

    Outputs:
    - data_usa: a pandas dataframe with new columns 'week_in_charts', 'times_in_charts', and 'date' in datetime format.

    Additional aspects:
    - The function uses pandas merge function to combine dataframes based on specific columns.
    - The function uses pandas value_counts function to count the occurrences of specific combinations of columns in the dataframe.
    - The function uses pandas drop_duplicates function to remove duplicate rows based on specific columns.
    """
    data_usa = data_usa.merge(data_usa[['url', 'chart']].value_counts().reset_index().rename({0:'week_in_charts'}, axis = 1), on=['url', 'chart'], indicator=True, how = 'left')
    data_usa.drop(['_merge'], axis = 1, inplace=True)
    data_usa = data_usa.merge(data_usa.sort_values('rank').drop_duplicates(['url','chart'])[['url', 'rank', 'chart']].rename({'rank':'times_in_charts'}, axis = 1), on=['url', 'chart'], 
        indicator=True, how = 'left')
    data_usa.drop(['_merge'], axis = 1, inplace=True)
    data_usa['date'] = pd.to_datetime(data_usa['date'])
    return data_usa

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
    print('artist clean column', 
          len(data_usa['artist_clean'].tolist()), 
          'original artist column',
          len(data_usa['artist'].unique().tolist()))
    data_usa['track_clean'] = data_usa['title'].str.strip().str.lower()
    print('tracks clean column',
        len(data_usa['track_clean'].unique().tolist()), 
        'tracks original column',
        len(data_usa['title'].unique().tolist()))
    data_usa.drop_duplicates(inplace=True)
    return data_usa