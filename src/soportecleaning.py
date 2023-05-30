import pandas as pd
from datetime import date

import warnings
warnings.filterwarnings("ignore")

def calculate_age(birthday):
    """
    Objective:
    The objective of the "calculate_age" function is to calculate the age of a person based on their birthday.

    Inputs:
    The function takes one input:
    - "birthday": a date object representing the person's birthday.

    Flow:
    The main flow of the function is as follows:
    1. Get the current date using the "date.today()" method.
    2. Calculate the difference between the current year and the year of the person's birthday.
    3. If the current month and day are before the person's birthday, subtract 1 from the age.

    Outputs:
    The function returns one output:
    - The age of the person as an integer.

    Additional aspects:
    - The function uses the "date" module to work with dates.
    - The function takes into account leap years when calculating the age.
    - The function assumes that the person's birthday has already occurred in the current year.
    """
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
    """
    Objective:
    The objective of the function is to clean and process a given dataframe containing information about songs and artists, and return a new dataframe with selected columns, cleaned and deduplicated data, and additional columns for cleaned artist and track names.

    Inputs:
    - df: a pandas dataframe containing information about songs and artists, with columns 'title', 'artist', and 'url'.

    Flow:
    1. Select columns 'title', 'artist', and 'url' from the input dataframe.
    2. Print information about the selected columns and the number of unique artists and songs.
    3. Drop duplicate rows from the selected dataframe.
    4. Print information about the deduplicated dataframe and the number of unique artists and songs.
    5. Create a new column 'artist_clean' with cleaned and standardized artist names.
    6. Print information about the new column and the number of unique artists in the original 'artist' column.
    7. Create a new column 'track_clean' with cleaned and standardized track names.
    8. Print information about the new column and the number of unique tracks in the original 'title' column.
    9. Drop duplicate rows from the dataframe with cleaned and standardized data.
    10. Return the cleaned and processed dataframe.

    Outputs:
    - data_usa: a pandas dataframe with selected columns, cleaned and deduplicated data, and additional columns for cleaned artist and track names.

    Additional aspects:
    - The function only processes data for the USA, as indicated by the name of the output dataframe.
    - The function assumes that the input dataframe contains data for songs and artists in the USA.
    - The function does not modify the input dataframe, but creates a new dataframe with the cleaned and processed data.
    """
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

def split_artists(df):
    """
    Objective:
    The objective of the 'split_artists' function is to split the 'artist' column of a given pandas DataFrame into multiple columns based on the comma separator. The function also replaces a specific artist name and renames the columns of the resulting DataFrame.

    Inputs:
    The function takes a pandas DataFrame 'df' as input.

    Flow:
    1. The function renames the 'track_clean' and 'artist_clean' columns of the DataFrame to 'track' and 'artist', respectively.
    2. It replaces the string 'tyler, the creator' with 'tyler the creator' in the 'artist' column using the 'str.replace()' method.
    3. It splits the 'artist' column using the comma separator and creates new columns using the 'str.split()' method.
    4. The resulting DataFrame is concatenated with the newly created columns using the 'pd.concat()' method.
    5. The function renames the newly created columns using the 'rename()' method.
    6. The resulting DataFrame is returned.

    Outputs:
    The main output of the function is a pandas DataFrame with the 'artist' column split into multiple columns.

    Additional aspects:
    - The function modifies the input DataFrame in place using the 'inplace=True' parameter in the 'rename()' method.
    - The 'str.split()' method has a parameter 'n' which limits the number of splits to be made. In this case, it is set to 2.
    - The 'axis' parameter in the 'pd.concat()' method is set to 1 to concatenate the new columns horizontally.
    """
    df.rename(columns={'track_clean':'track','artist_clean':'artist'}, inplace=True)
    test = df['artist'].str.replace('tyler, the creator', 'tyler the creator').str.split(',', n=2, expand = True)
    tracks = pd.concat([df, test], axis = 1)
    tracks.rename(columns={0:'artist_0', 1:'artist_1', 2:'artist_2'}, inplace=True)
    return tracks