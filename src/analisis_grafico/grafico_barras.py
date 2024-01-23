"""
Este módulo proporciona funciones para 
crear gráficos de barras relacionados con series de televisión.
"""

import pandas as pd
import matplotlib.pyplot as plt

def contar_series_por_anio_y_graficar(dataframe):
    """
    Esta función toma un DataFrame que contiene información sobre series de televisión
    y crea un gráfico de barras que muestra el número de series por año de inicio.
    
    :param dataframe: DataFrame con datos de series de televisión.
    :return: Series que contiene el número de series por año de inicio.
    """
    dataframe['anio_inicio'] = pd.to_datetime(
        dataframe['first_air_date']).dt.year

    series_por_anio = dataframe['anio_inicio'].value_counts().sort_index()

    plt.figure(figsize=(12, 6))
    plt.bar(series_por_anio.index, series_por_anio.values)
    plt.xlabel('Año de Inicio')
    plt.ylabel('Número de Series')
    plt.title('Número de Series por Año de Inicio')
    plt.show()
    plt.close()

    return series_por_anio
