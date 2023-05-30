import pandas as pd
from datetime import date
import numpy as np
from collections import Counter
import re
import src.soporteAPIs as sa
import tqdm

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

def cleaningLastFM(df):
    """
    The objective of the 'cleaningLastFM' function is to clean and transform data from LastFM API. The function takes a pandas dataframe as input and performs cleaning operations on the 'bio', 'artist_tag', and 'track_tag' columns. The cleaned data is then concatenated with the original dataframe and returned as output.

    Inputs:
    - df: a pandas dataframe containing data from LastFM API

    Flow:
    1. The 'bio' column is extracted from the input dataframe and converted into a pandas series.
    2. The 'artist_tag' column is extracted from the input dataframe and converted into a pandas series.
    3. The column names of the 'artist_tag' series are modified to include a prefix 'artist_genre_'.
    4. The values in each row of the 'artist_tag' series are converted into a list and only the first value is retained.
    5. The 'track_tag' column is extracted from the input dataframe and converted into a pandas series.
    6. The column names of the 'track_tag' series are modified to include a prefix 'track_genre_'.
    7. The values in each row of the 'track_tag' series are converted into a list and only the first value is retained.
    8. The cleaned 'bio', 'artist_tag', and 'track_tag' series are concatenated with the original dataframe along the columns axis.
    9. The concatenated dataframe is returned as output.

    Outputs:
    - cleaned pandas dataframe containing the original data and cleaned 'bio', 'artist_tag', and 'track_tag' columns.

    Additional aspects:
    - The function uses the pandas library to manipulate data.
    - The function handles missing values in the 'artist_tag' and 'track_tag' columns by skipping rows that cannot be cleaned.
    - The function does not modify the original input dataframe.
    """
    ## getting bio info
    bio = df['bio'].apply(pd.Series)
    ## cleaning artist column
    artist_tag = df['artist_tag'].apply(pd.Series)
    artist_tag.columns = ['aritist_genre_'+str(item) for item in artist_tag.columns.to_list()]
    artist_tag = artist_tag.applymap(lambda x: list(x.values())[0] if isinstance(x, dict) else x)
    ## leaning tags info
    track_tag = df['track_tag'].apply(pd.Series)
    track_tag.columns = ['aritist_genre_'+str(item) for item in track_tag.columns.to_list()]
    track_tag = track_tag.applymap(lambda x: list(x.values())[0] if isinstance(x, dict) else x)
    return pd.concat([df, bio, artist_tag, track_tag], axis = 1)

def newColumnsLastFM(df):
    """
    Objective:
    The objective of the 'newColumnsLastFM' function is to generate new columns for a given dataframe. These new columns include music genre, gender, and age. The function also cleans and formats the data in the existing columns to make them more usable.

    Inputs:
    - df: a pandas dataframe containing the data to be processed

    Flow:
    1. Generate genre columns based on artist and track genres
    2. Count the number of different music genres and select the top 25
    3. Clean the music genre column using a function from 'soporteAPIs'
    4. Add a gender column using a function from 'soporteAPIs'
    5. Extract the birthdate from the 'content' column using regular expressions
    6. Clean and format the birthdate data
    7. Convert the birthdate to a datetime object and calculate age
    8. Drop unnecessary columns and rename the cleaned music genre column
    9. Return the processed dataframe

    Outputs:
    - df: a pandas dataframe with new columns for music genre, gender, and age

    Additional aspects:
    - The function uses external functions from 'soporteAPIs' for cleaning and formatting data
    - The function uses the 'tqdm' library to display a progress bar during processing
    - The function uses the 'Counter' class from the 'collections' module to count the number of different music genres
    """
    ## generate genre columns
    df['music_genre'] = np.where(df['aritist_genre_0'].isnull() == True, df['track_genre_0'].str.lower(), df['aritist_genre_0'].str.lower())
    count_genres = Counter(genres for genres in df['music_genre'])
    print(f"There are {len(count_genres)} different music genres.")
    dict_genres = dict(count_genres.most_common(25))
    df["clean_music_genre"] = df.apply(lambda x: sa.music_genres(x["music_genre"], dict_genres), axis = 1)
    ## add gender column 
    df["gender"] = df['summary'].apply(sa.generos)
    ## add age
    df['birthday'] =  df['content'].apply(lambda x: re.findall(r'\w{1,} \d{1,2}, \d{4}|\d{1,2} \w{4,} \d{4}',str(x))).str[0]
    df[[1, 2, 3]] = df['birthday'].str.split(' ', expand=True)
    df['month_text'] = ''
    df['day'] = ''
    for index, row in tqdm(df.iterrows(), total = df.shape[0]):
        try:
            if ',' in row[2]:
                #print('str')
                row['month_text'] = row[1]
                row['day'] = row[2].replace(',', '')
        except:
            if row[2] == np.nan:
                #print('nan')
                row['month_text'] = np.nan
                row['day'] = np.nan
            else:
                #print('float')
                row['month_text'] = row[2]
                row['day'] = row[1]
    df["month"] = df["month_text"].apply(sa.month_as_number)
    df['birthday_date'] = df.apply(lambda x: sa.date_conversion(x[3], x["month"], x["day"]), axis = 1)
    df['age'] = df['birthday_date'].apply(sa.calculate_age)
    df.drop(['birthday',	1,	2,	3,	'month_text',	'day',	'month', 'music_genre'], axis =1, inplace=True)
    df.rename({'clean_music_genre':'music_genre'}, axis = 1, inplace=True)
    return df