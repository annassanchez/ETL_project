# ETL-project

![High Fidelity](https://64.media.tumblr.com/da7235613f6fe6292360d74d410ece3b/01bebaf99b141ae6-a4/s500x750/1070b19f89a4cc2c1b3420495fb027fcfb1acc9f.gif)
<!-- “What came first, the music or the misery? People worry about kids playing with guns, or watching violent videos, that some sort of culture of violence will take them over. Nobody worries about kids listening to thousands, literally thousands of songs about heartbreak, rejection, pain, misery and loss. Did I listen to pop music because I was miserable? Or was I miserable because I listened to pop music?"-->

## Index

> 1. `data / pickle` -> input data storage
> 2. `images` -> images used in this readme
> 3. `notebooks` -> jupyter notebooks with the etl process
>       - `1_extraction_cleaning_csv` -> cleaning of the source file
>       - `2_call_api_lastfm` -> calls to the lastFM api and the cleaning of the results.
>       - `3_call_api_spotify`-> calls to the Spotify API and cleaning of the results.
>       - `4_scraping_genius` -> webscraping from the genius website
>       - `5_extract_SQL` -> file to upload the data to the sql database
>       - `6_alaysis` -> visualizaion of the API and scraped data
> 4. `sql` -> sql schema image and sql script
> 5. `src` -> folder that stores the pipeline files
>       - `biblioteca.py` -> supports data cleaning
>       - `soporteAPIs.py` -> supports the lastFM API calls and data cleaning
>       - `soportecleaning.py` -> supports the cleaning of the input csv data

## Context

Objective: 
- The key of this analysis is to combine multiple programming tools in order to gather data from a public dataset, APIs and webscrapping and analyse it.

Hypothesis:
- Did we listen to more sad music because of the Covid-19 pandemic? Analyse the `top200` and `viral50` playlist, the general `valence`, `danceability` and `energy` values, but also how it changes for the top music genres, the artist gender or the top 5 most listened artis on the given period. 

## Spotify playlist dataset 

The source database for this analysis is published [here](https://www.kaggle.com/datasets/dhruvildave/spotify-charts). The dataset compiles the songs that were on the `Top200` and `Viral50` since January 1st 2017 until 31st of December of 2021. This playlists are updated each 2-3 days. For this analysis, I will keep the data for USA region.

## Data from LastFM 

LastFM is a music based social network that tracks the music you listen to. Also it has a really big open-source music description database, in which the users can tag the given artist or songs and add information about them. In order to make the API calls, [here](https://ws.audioscrobbler.com/2.0/) is the link. The main sections used of the API are:
- **artist info:** information on each artist and its tags
- **track tags:** the track tags
On the `src` folder are some built-in functions in order to make the API calls.

## Data from Spotify

Spotify is a music streaming service that also provides information on the music to the public.
The main sections used from the api are:
- **search:** to get the `uri`s or the codes that spotify gives to all tracks. Also with the search method is possible to exract the `popularity` and the `release_date` from the tracks.
- **audio features:** to get a categorical information behind the tracks. Some of the categories are the `tone`, `tempo`, `mode`.
The Spotify API has a Python library called `spotipy` that helps with the data extraction.

## Further steps

Getting info from `genius`, a website that publishes song lyrics, in order to get the song lyrics and information on the song (as who wrote it, the discography that publishes or other song credits).

## Some results

On the selected playlist (`top200` and `viral50`) there's seems to be no significant change on the `valence`, `danceability` and `energy` values, a way to measure the emotional state of the most listened music on Spotify.
![valence result for the whole items from the top200 and viral50 playlists](https://github.com/annassanchez/ETL_project/blob/main/images/valence.png)
![energy and danceability result for the whole items from the top200 and viral50 playlists ](https://github.com/annassanchez/ETL_project/blob/main/images/danceability_energy.png)

## Libraries

- [**pandas**](https://pypi.org/project/pandas/): this library is used to work with related and table like data structures.
- [**numpy**](https://pypi.org/project/numpy/): library used for scientific calculation.
- [**pickle**](https://docs.python.org/3/library/pickle.html): a module that generates files that can be used within python to store any kind of data -- from dataframes to dicionaries and so on.
- [**clean-text**](https://pypi.org/project/clean-text/): this library helps to normalise text extracted from social media -- cleans emojis, weird characters and so on.
- [**requests**](https://pypi.org/project/requests/): requests is used to make http requests -- mostly used on the API calls notebooks
- [**os**](https://docs.python.org/es/3.10/library/os.html): os is used for operating system functionalities within python -- for example, accessing .pickle files or navigating on folders within this project.
- [**dotenv**](https://pypi.org/project/python-dotenv/): dotenv reads key-value files from and `.env` (enviroment) file -- mostly used to store the api keys.
- [**tqdm**](https://pypi.org/project/tqdm/): this library is used to print a progress meter when iterating.
- [**re**](https://docs.python.org/3/library/re.html): re provides regular expression matching operations to python -- mostly used for cleaning the api results.
- [**fuzzywuzzy**](https://pypi.org/project/fuzzywuzzy/): library that creates string matching comparing two values to a given thereshold -- mostly used to create equivalences and clean strings.
- [**collections**](https://docs.python.org/3/library/collections.html): this module implements special containers datatypes providing alternatives to the python's built-in containers -- in this case, `Counter` is used.
- [**calendar**](https://docs.python.org/3/library/calendar.html): this module allows to generate calendars and provides functions related to the calendar -- for example, it gives a list with the months as texts.
- [**spotipy**](https://spotipy.readthedocs.io/en/2.22.0/): spotipy is a python library for maiking api calls to the Spotify web API.
- [**selenium**](https://pypi.org/project/selenium/): this package is used to automate web browser interaction from Python -- used for webscrapping.
- [**beautifulSoup**](https://pypi.org/project/beautifulsoup4/): this library scrapes information from webpages, iterating searching and modifying the html parser.
- [**time**](https://docs.python.org/3/library/time.html): this module provides various time-related functions -- in this case, related to scraping to add timers
- [**SQLAlchemy**](https://pypi.org/project/SQLAlchemy/): python toolkit that connects python to SQL.

<!--Se extrae la siguiente información:
- información de los géneros musicales de las canciones
- información de los génmeros musicales de los artistas
- información sobre los artistas
- información sobre las canciones seleccionadas
    - duración en ms
    - duración en minutos
    - nivel de acústica
    - nivel de energía
    - nivel de instrumentalidad
    - tono de las canciones
    - como de en directo es la grabación
    - nivel de sonido (en dbs)
    - modo (si es mayor/menor)
    - cantidad de "discurso" que hay en un tema -> es decir, si se trata de una pista hablada, recitada...
    - tempo de la cación en bpms
    - valence, una forma de valorar como de positivas son las canciones (cuanto mejor mayor de valence que tengan) o negativas (valor de valence más bajo)
- se extraen las letras
- se analiza el significado de las letras
- se extrae la fecha de publicación de las canciones

El objetivo de este análisis es extraer la información de la lista de los más escuchados. 
- ver los artistas más escuchados por cantidad de streams.
- los géneros más populares por cantidad de streams.
- recorrido de los artistas más escuchados en las listas.
- ver cuales son los géneros más escuchados.
- ver como evoluciona una canción en el top200 a lo largo del tiempo-->
