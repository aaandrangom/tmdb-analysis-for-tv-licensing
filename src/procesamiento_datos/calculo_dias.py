"""
Este módulo proporciona una función 
para calcular la cantidad de días 
entre la primera y la última fecha
de emisión de una serie de televisión.
"""

import pandas as pd

def calcular_air_days(dataframe):
    """
    Esta función calcula la cantidad de días 
    entre la primera y la última fecha 
    de emisión de una serie de televisión.

    :param dataframe: DataFrame con datos 
    de series de televisión que incluye 
    columnas 'first_air_date' y 'last_air_date'.
    :return: El DataFrame con una nueva columna 'air_days' 
    que contiene la cantidad de días.
    """
    dataframe['first_air_date'] = pd.to_datetime(
        dataframe['first_air_date'], format='%Y-%m-%d', errors='coerce')
    dataframe['last_air_date'] = pd.to_datetime(
        dataframe['last_air_date'], format='%Y-%m-%d', errors='coerce')

    dataframe['air_days'] = (
        dataframe['last_air_date'] - dataframe['first_air_date']).dt.days

    return dataframe
