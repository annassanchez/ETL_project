import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.options.display.max_columns = None
pd.set_option('display.float_format', lambda x: '%.3f' % x)

# display
from IPython.display import display

def analisis_basico(dataframe):
    """
    esta función coge un dataframe y saca los principales elementos preiminares de un eda: la estructura de datos, si hay nulos, duplicados, el tipo de variables numéricas o categórcias y un pairplot para ver la relación entre variables.
    param: dataframe
    """
    print("_________________________________\n")
    print (f"1_Data Structure: {dataframe.shape}")
    display(dataframe.head(2))
    display(dataframe.info())
    print("_________________________________\n")
    print("2_Duplicated columns:") 
    print(dataframe.duplicated().sum())
    print("_________________________________\n")
    print("3_Null values distribution:")
    display(pd.concat([dataframe.isnull().sum(), dataframe.dtypes], axis = 1).rename(columns = {0: "nulos", 1: "dtypes"}).T)
    print("_________________________________\n")
    print("4_Numerical variables distribution:")
    display(dataframe.describe())
    print("_________________________________\n")
    print("5_Categorical variables distribution:")
    try:
        display(dataframe.describe(include = "object"))
    except:
        print("No categorical variables available, sorry :(") 
        pass

def regplot_numericas(dataframe, columnas_drop, variable_respuesta):
    """
    esta función da un chart que relaciona las columnas numéricas de un dataframe con la variable
    param: dataframe -> el dataframe a representar
        columnas_drop -> las columnas a borrar (un id alguna columna que no se quiera representar) -> se pasa en formato lista
        variable_respuesta -> las columnas a borrar (en este caso, la variable respuesta)
    """
    print(f'distribución de las variables numéricas en relación con la variable respuesta: {variable_respuesta}')
    df_numericas = dataframe.select_dtypes(include = np.number)
    columnas = df_numericas.drop(columnas_drop, axis = 1)
    fig, axes = plt.subplots(nrows=int(columnas.shape[1]), ncols=int(1), figsize = (10 * columnas.shape[1], 10 * columnas.shape[1]))
    axes = axes.flat
    for i, columns in enumerate(columnas.columns):
        sns.regplot(data = dataframe, 
            x = columns, 
            y = variable_respuesta, 
            ax = axes[i],
            color = 'gray',
            scatter_kws = {"alpha": 0.4}, 
            line_kws = {"color": "red", "alpha": 0.7 }
            )
    fig.tight_layout();

def chart_categoricas_count(df):
    """
    esta función toma un dataframe y presnta unos histogramas con las variables categóricas
    param: dataframe -> dataframe del que se sacan los gráficos
    """
    print(f'this chart gives the categorical distribution of the variables')
    df_cat = df.select_dtypes(include = np.number)
    fig, axes = plt.subplots(nrows=int(df_cat.shape[1]/2), ncols=int(df_cat.shape[1] / 3), figsize = (10 * df_cat.shape[1] / 2,10 * df_cat.shape[1] / 3))
    axes = axes.flat

    for i, colum in enumerate(df_cat.columns):
        chart = sns.countplot(
                x = df_cat[colum],
                #hue = df_cat['Offer_Accepted'],
                ax = axes[i])
        total = float(len(df_cat[colum]))
        for p in chart.patches:
            height = p.get_height()
            chart.text(p.get_x() + p.get_width() / 2., height + 3,
                    '{:.2f}%'.format((height / total) * 100),
                    ha='center')
    fig.tight_layout();

def chart_boxplot(dataframe):
    """
    esta funcion saca los boxplots de las variables numéricas - incluyendo la variable respuesta
    param: dataframe
    """
    print('numeric variables distribution -> outliers')
    dataframe = dataframe.select_dtypes(include = np.number)
    fig, ax = plt.subplots(dataframe.shape[1], 1, figsize=(25, 2.5 * dataframe.shape[1]))

    for i in range(len(dataframe.columns)):
        sns.boxplot(x=dataframe.columns[i], data=dataframe, ax=ax[i])
        ax[i].tick_params(labelsize=10)
    plt.tight_layout()
    plt.show();

def distribucion_numericas(dataframe):
    """
    Genera un conjunto de gráficos de distribución (KDE) para las variables numéricas de un dataframe.
    Args:
        dataframe (pandas.DataFrame): El dataframe que se desea analizar.
    Returns:
        None: La función no retorna ningún valor.
    """
    print('numeric variables distribution')
    # Obtener las columnas numéricas del dataframe
    columnas_numeric = dataframe.select_dtypes(include=np.number).columns

    # Crear el conjunto de subplots para graficar las distribuciones
    fig, axes = plt.subplots(nrows=int(np.ceil(len(columnas_numeric)/2)), ncols=2, figsize=(25, 15))
    axes = axes.flat

    # Graficar la distribución de cada variable
    for i, colum in enumerate(columnas_numeric):
        sns.histplot(
            data=dataframe,
            x=colum,
            alpha=0.2,
            kde=True,
            ax=axes[i])

        axes[i].set_title(colum, fontsize=15, fontweight="bold")
        axes[i].tick_params(labelsize=10)
        axes[i].set_xlabel("")

    fig.tight_layout()

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