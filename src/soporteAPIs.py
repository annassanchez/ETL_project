import pandas as pd
import numpy as np
import requests
import os 
from dotenv import load_dotenv
import requests
from tqdm import tqdm
import pickle
import re
pd.options.display.max_columns = None
from fuzzywuzzy import process, fuzz

load_dotenv()
api = os.getenv("lastfm-id")
username = os.getenv("lastfm-user")

def getLastFMData(params):
    """
    This function extracts the basic lastFM API info. For that, takes the params as an input and makes the request with the given params. 
    Also takes the url, the username and the link in orther to call the API.
    """
    headers = {'user-agent': username} ## defino mi usuario
    url = 'https://ws.audioscrobbler.com/2.0/' ##url a la que voy a contactar

    ## configuro los params para hacer la petición
    params['api_key'] = api
    params['format'] = 'json'

    res = requests.get(url, headers=headers, params=params)
    return res

def getArtistInfo(artist):
    """
    This function extracts the info for artist given the artist name. 
    It takes the params defined by getLastFMData, and returns the artist bio and tags info.
    """
    res = getLastFMData({
        'method': 'artist.getInfo',
        'artist':  artist,
    })

    # por si me da un timeout
    if res.status_code != 200:
        return None

    # extraigo los top 5 tags de cada artistas
    try:
        #tags = [tag['name'] for tag in res.json()['toptags']['tag'][:3]]
        return res.json()['artist']['bio'], res.json()['artist']['tags']['tag']
    except:
        return np.nan

def getTrackTags(artist, track):
    """
    This function extracts the info on tracks given the artist and track name.
    It takes the params defined by getLastFMData, and returns the artist bio and tags info.
    """
    ## hago la colsulta para obtener los datos de tags por artista
    res = getLastFMData({
        'method': 'track.getInfo',
        'artist':  artist,
        'track': track,
    })

    # por si me da un timeout
    if res.status_code != 200:
        return None

    # extraigo los top 5 tags de cada artistas
    try:
        #tags = [tag['name'] for tag in res.json()['toptags']['tag'][:3]]
        return res.json()['track']['toptags']['tag'], res.json()['track']['wiki']['published'] ## no va muy bien esta parte y solo me extrae tres géneros... 
    except:
        return np.nan, np.nan

def music_genres(column, genres):
    """
    This function compares a given music genre with the top 24 genders of the dataset; 
    returns the given genre if it's on the top genre list, if not it matches to the most similar genre from the given dictionary
    """
    max = 0
    for key in genres.keys():
        try:
            similar = fuzz.ratio(column, key)
            if similar > max:
                max = similar
                genre = key     
        except:
            return "other"
    if max > 60:
        return genre
    else:
        return "other"