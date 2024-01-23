"""
Este módulo proporciona una función
para crear un diccionario de URLs 
de pósters de series de televisión.
"""

import pandas as pd

def crear_diccionario_posters(dataframe):
    """
    Esta función crea un diccionario de URLs 
    de pósters de series de televisión.

    :param dataframe: DataFrame con datos de series de 
    televisión que incluye columnas 'name', 'homepage', y 'poster_path'.
    :return: Un diccionario que mapea el nombre de la serie a su URL de póster.
    """
    diccionario_posters = {}

    for _, row in dataframe.iterrows():
        nombre_serie = row['name']
        homepage = row['homepage']
        poster_path = row['poster_path']

        if pd.isna(homepage) or homepage == "":
            homepage = "NOT AVAILABLE"
        if pd.isna(poster_path) or poster_path == "":
            poster_path = "NOT AVAILABLE"

        poster_url = f"{homepage}{poster_path}"

        diccionario_posters[nombre_serie] = poster_url

    return diccionario_posters
