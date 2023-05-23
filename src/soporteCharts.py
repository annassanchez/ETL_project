import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.options.display.max_columns = None
pd.set_option('display.float_format', lambda x: '%.3f' % x)

def general_chart(top200, viral50):
    fig, axs = plt.subplots(ncols=2, nrows = len(top200.sort_values(by = ['playlist_date'])['playlist_date'].dt.year.unique().tolist()), figsize = (25, 10), sharex=True,)
    list_years = top200.sort_values(by = ['playlist_date'])['playlist_date'].dt.year.unique().tolist()
    sns.set_theme(style="darkgrid")
    rows = [0, 1]
    fig.suptitle('Valence evolution in the top200 and viral50 playlist', fontsize=15)
    for year in list_years:
        for row in rows:
            if row == 0:
                #print(year, list_years.index(year))
                sns.boxplot(x=top200[top200['playlist_date'].dt.year == year].valence, data = top200[top200['playlist_date'].dt.year == year], medianprops={"color": "coral"}, notch=True,flierprops={"marker": "x"},
                    ax=axs[list_years.index(year)][0]) ;
                axs[list_years.index(year)][0].set_title(str(year), fontsize=10, )
                axs[list_years.index(year)][0].set_xlabel("")
            elif row == 1:
                #print(year, list_years.index(year))
                sns.boxplot(x=viral50[viral50['playlist_date'].dt.year == year].valence, data = viral50[viral50['playlist_date'].dt.year == year], notch=True, flierprops={"marker": "x"},
                    ax=axs[list_years.index(year)][1], medianprops={"color": "coral"}) ;
                axs[list_years.index(year)][1].set_title(str(year), fontsize=10, )
                axs[list_years.index(year)][1].set_xlabel("")
    fig.tight_layout();

def general_chart_energy_danceability(top200, viral50):
    fig, axs = plt.subplots(ncols=4, nrows = len(top200.sort_values(by = ['playlist_date'])['playlist_date'].dt.year.unique().tolist()), figsize = (25, 10), sharex=True,)
    list_years = top200.sort_values(by = ['playlist_date'])['playlist_date'].dt.year.unique().tolist()
    sns.set_theme(style="darkgrid")
    columns = [0, 1]
    column_name = ['danceability', 'energy']
    fig.suptitle('Danceability and energy evolution in the top200 and viral50 playlist', fontsize=15)
    for year in list_years:
        for column in column_name:
            for row in list(range(0,4)):
                if row == 0:
                    sns.boxplot(x=top200[top200['playlist_date'].dt.year == year].danceability, data = top200[top200['playlist_date'].dt.year == year], medianprops={"color": "coral"}, notch=True,flierprops={"marker": "x"}, 
                        ax=axs[list_years.index(year)][row]) ;
                    axs[list_years.index(year)][row].set_title(str(year), fontsize=10, )
                    if year == 2021:
                        axs[list_years.index(year)][row].set_xlabel("danceability -- top200")
                    else:
                        axs[list_years.index(year)][row].set_xlabel("")
                elif row == 1:
                    sns.boxplot(x=viral50[viral50['playlist_date'].dt.year == year].danceability, data = viral50[viral50['playlist_date'].dt.year == year], notch=True, flierprops={"marker": "x"}, 
                        ax=axs[list_years.index(year)][row], medianprops={"color": "coral"}) ;
                    axs[list_years.index(year)][row].set_title(str(year), fontsize=10, )
                    if year == 2021:
                        axs[list_years.index(year)][row].set_xlabel("danceability -- viral50")
                    else:
                        axs[list_years.index(year)][row].set_xlabel("")
                elif row == 2:
                    sns.boxplot(x=top200[top200['playlist_date'].dt.year == year].energy, data = top200[top200['playlist_date'].dt.year == year], medianprops={"color": "coral"}, notch=True,flierprops={"marker": "x"}, 
                        ax=axs[list_years.index(year)][row]) ;
                    axs[list_years.index(year)][row].set_title(str(year), fontsize=10, )
                    if year == 2021:
                        axs[list_years.index(year)][row].set_xlabel("energy -- top200")
                    else:
                        axs[list_years.index(year)][row].set_xlabel("")
                elif row == 3:
                    sns.boxplot(x=viral50[viral50['playlist_date'].dt.year == year].energy, data = viral50[viral50['playlist_date'].dt.year == year], notch=True, flierprops={"marker": "x"}, 
                        ax=axs[list_years.index(year)][row], medianprops={"color": "coral"}) ;
                    axs[list_years.index(year)][row].set_title(str(year), fontsize=10, )
                    if year == 2021:
                        axs[list_years.index(year)][row].set_xlabel("energy -- viral50")
                    else:
                        axs[list_years.index(year)][row].set_xlabel("")
    fig.tight_layout();

def valence_music_genre(top200, viral50, top5_musicgenre):
    sns.set_theme(style="darkgrid")
    genres = [val for val in top5_musicgenre['music_genre'].tolist() for _ in (0, 1)]
    list_years = top200.sort_values(by = ['playlist_date'])['playlist_date'].dt.year.unique().tolist()
    fig, axs = plt.subplots(ncols=len(list_years), nrows = len(genres), figsize = (15,25), sharey=True,)

    fig.suptitle('Valence evolution in the top200 and viral50 playlist for the music genres', fontsize=12)

    for genre, row in zip(genres, list(range(0, 10))):
        for year in list_years:
            if row % 2 == 0:
                #print(genre, year, 'top200')
                sns.boxplot(y=top200[top200['playlist_date'].dt.year == year].valence, data = top200[top200['playlist_date'].dt.year == year], medianprops={"color": "coral"}, notch=True,flierprops={"marker": "x"}, orient='v',
                    ax=axs[row][list_years.index(year)]) ;
                axs[row][list_years.index(year)].set_title(str(year) + ' ' + genre, fontsize=10, )
                axs[row][list_years.index(year)].set_ylabel("top200")
            elif row % 2 != 0:
                #print(genre, year, 'viral50')
                sns.boxplot(y=viral50[viral50['playlist_date'].dt.year == year].valence, data = viral50[viral50['playlist_date'].dt.year == year], notch=True, flierprops={"marker": "x"}, orient='v',
                    ax=axs[row][list_years.index(year)], medianprops={"color": "coral"}) ;
                axs[row][list_years.index(year)].set_title(str(year) + ' ' + genre, fontsize=10, )
                axs[row][list_years.index(year)].set_ylabel("viral50")
    fig.tight_layout;

def energy_danceability_music_genre(top200, viral50, top5_musicgenre):
    sns.set_theme(style="darkgrid")
    list_years = top200.sort_values(by = ['playlist_date'])['playlist_date'].dt.year.unique().tolist()
    fig, axs = plt.subplots(ncols=len(list_years), nrows = 10, figsize = (25, 25), sharex = True, sharey = True)
    genres = [val for val in top5_musicgenre['music_genre'].tolist() for _ in (0, 1)]
    fig.suptitle('Energy vs Danceability evolution in the top200 and viral50 playlist for the music genres', fontsize=15)
    for genre, row in zip(genres, list(range(0, 10))):
            for year in list_years:
                if row % 2 == 0:
                    sns.scatterplot(x = top200[(top200['playlist_date'].dt.year == year) & (top200['music_genre'] == genre)].energy, y = top200[(top200['playlist_date'].dt.year == year) & (top200['music_genre'] == genre)].danceability,
                        hue= top200[(top200['playlist_date'].dt.year == year) & (top200['music_genre'] == genre)].key, ax=axs[row][list_years.index(year)]);
                    axs[row][list_years.index(year)].set_title(str(year) + ' ' + genre, fontsize=10)
                elif row % 2 != 0:
                    sns.scatterplot(x = viral50[(viral50['playlist_date'].dt.year == year) & (viral50['music_genre'] == genre)].energy, y = viral50[(viral50['playlist_date'].dt.year == year) & (viral50['music_genre'] == genre)].danceability, 
                        hue= viral50[(viral50['playlist_date'].dt.year == year) & (viral50['music_genre'] == genre)].key, ax=axs[row][list_years.index(year)]);
                    axs[row][list_years.index(year)].set_title(str(year) + ' ' + genre, fontsize=10)