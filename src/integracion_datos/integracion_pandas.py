"""
Este módulo proporciona una función 
para integrar datos de archivos CSV en un 
DataFrame utilizando la biblioteca pandas.
"""

import time
import pandas as pd

def integrar_csv_en_dataframe():
    """
    Esta función integra datos de varios archivos 
    CSV en un DataFrame, utilizando la columna 
    'id' como clave de unión.

    :return: Un DataFrame que contiene los datos 
    integrados y el tiempo de procesamiento.
    """
    archivos_csv = ['../data/TMDB_info.csv',
                    '../data/TMDB_overview.csv', '../data/TMDB_distribution.csv']

    inicio_tiempo = time.time()

    dataframes = [pd.read_csv(archivo) for archivo in archivos_csv]

    df_integrado = dataframes[0]
    for df in dataframes[1:]:
        df_integrado = df_integrado.merge(df, on='id', how='outer')

    fin_tiempo = time.time()

    tiempo_procesamiento = fin_tiempo - inicio_tiempo

    return df_integrado, tiempo_procesamiento
