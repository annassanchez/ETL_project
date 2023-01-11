# ETL_project

The source database for this analysis is published [here](https://www.kaggle.com/datasets/dhruvildave/spotify-charts). The dataset compiles the songs that were on the `Top200` and `Viral50` since January 1st 2007. This playlists are updated each 2-3 days.

The key of this analysis is to see if the music that is in this playlist varies in the given period -- the genre, meaning of the lyrics or the artists. If the most popular music is brand new or is not so new, which are the most listened artist and how they evolve in the charts.

Se extrae la siguiente información:
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
- ver como evoluciona una canción en el top200 a lo largo del tiempo
