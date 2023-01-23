# ETL-project

![High Fidelity](https://64.media.tumblr.com/da7235613f6fe6292360d74d410ece3b/01bebaf99b141ae6-a4/s500x750/1070b19f89a4cc2c1b3420495fb027fcfb1acc9f.gif)
<!-- “What came first, the music or the misery? People worry about kids playing with guns, or watching violent videos, that some sort of culture of violence will take them over. Nobody worries about kids listening to thousands, literally thousands of songs about heartbreak, rejection, pain, misery and loss. Did I listen to pop music because I was miserable? Or was I miserable because I listened to pop music?"-->

## Index

> 1. `data / pickle` -> input data storage
> 2. `notebooks` -> jupyter notebooks with the etl process
>   1. `extraction_cleaning_csv` -> cleaning of the source file
>   2. `call_api_lastfm` -> calls to the lastFM api and the cleaning of the results.
>   3. `call_api_spotify`-> calls to the Spotify API and cleaning of the results.
>   4. `scraping_genius` -> webscraping from the genius website
>   5. `extract_SQL` -> file to upload the data to the sql database
>   6. `alaysis` -> visualizaion of the API and scraped data
> 3. `sql` -> sql schema image and sql script
> 4. `src` -> folder that stores the pipeline files
>   1. `biblioteca.py` -> supports data cleaning
>   2. `soporteAPIs.py` -> supports the lastFM API calls and data cleaning
>   3. `soportecleaning.py` -> supports the cleaning of the input csv data
## Context

Objective: The key of this analysis is to combine multiple programming tools in order to gather data from a public dataset, APIs and webscrapping and analyse it.

Hypothesis:
- Did we listen to more sad music because of the Covid-19 pandemic? See what of the top artist and top genres are in the given period, the characteristics of the music and the lyrics, and see if there is a swift in music taste due to that event.

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

## Libraries

- [**pandas**](https://pypi.org/project/pandas/): this library is used to work with related and table like data structures.
- [**numpy**](https://pypi.org/project/numpy/): library used for scientific calculation.
- [**pickle**](https://docs.python.org/3/library/pickle.html): a module that generates files that can be used within python to store any kind of data -- from dataframes to dicionaries and so on.
- [**clean-text**](https://pypi.org/project/clean-text/): this library helps to normalise text extracted from social media -- cleans emojis, weird characters and so on.
- **requests**
- **os**
- **dotenv**
- **tqdm**
- **re**
- **fuzzywuzzy**
- **collections**
- **calendar**
- **spotipy**
- **selenium**
- **beautifulSoup**
- **time**

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
