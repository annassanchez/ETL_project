# ETL-project

![](https://31.media.tumblr.com/129e2f001fb7837a8c14e10e4d5aea47/tumblr_mf3f1bxXVb1qhbo1ko1_500.gif)
> “What came first, the music or the misery? People worry about kids playing with guns, or watching violent videos, that some sort of culture of violence will take them over. Nobody worries about kids listening to thousands, literally thousands of songs about heartbreak, rejection, pain, misery and loss. Did I listen to pop music because I was miserable? Or was I miserable because I listened to pop music?"

# Context

The source database for this analysis is published [here](https://www.kaggle.com/datasets/dhruvildave/spotify-charts). The dataset compiles the songs that were on the `Top200` and `Viral50` since January 1st 2017 until 31st of December of 2021. This playlists are updated each 2-3 days.

The key of this analysis is to see if the music that is in this playlist varies in the given period -- the genre, meaning of the lyrics or the artists. If the most popular music is brand new or is not so new, which are the most listened artist and how they evolve in the charts.

Hypothesis:
- Did we listen to more sad music because of the Covid-19 pandemic?
  - mirar la `valence`, `energy`, `tone`, `key`.
- After its rise on the 90s and 00s is still pop music so popular?
- How are the most popular listened top genres? Are there similarities on music genres?
- Most of the most listened artist are men -- did Me too affect the music that we listen? 
- Los artistas más populares son jóvenes y hay mucah volatilidad -- las canciones pasan rápido de moda?

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
