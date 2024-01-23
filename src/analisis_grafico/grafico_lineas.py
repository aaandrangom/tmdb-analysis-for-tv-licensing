"""
Este módulo proporciona funciones para 
crear gráficos de líneas relacionados con series de televisión.
"""

import pandas as pd
import matplotlib.pyplot as plt

def contar_series_por_decada_y_graficar(dataframe):
    """
    Esta función toma un DataFrame que contiene información sobre series de televisión
    y crea un gráfico de líneas que muestra el número de series por década de inicio,
    separadas por categoría de "type".
    
    :param dataframe: DataFrame con datos de series de televisión.
    :return: DataFrame que contiene el número de series por década y categoría de "type".
    """
    dataframe['anio_inicio'] = pd.to_datetime(
        dataframe['first_air_date']).dt.year
    dataframe['decada_inicio'] = (dataframe['anio_inicio'] // 10) * 10

    series_por_decada = dataframe.groupby(
        ['decada_inicio', 'type']).size().unstack(fill_value=0)

    ax = plt.gca()  # Obtener el objeto de los ejes actuales

    series_por_decada.plot(kind='line', ax=ax)

    ax.set_xlabel('Década de Inicio')
    ax.set_ylabel('Número de Series')
    ax.set_title(
        'Número de Series por Categoría de "type" en cada Década desde 1940')
    ax.legend(title='Categoría de "type"')
    plt.show()
    plt.close()

    return series_por_decada
