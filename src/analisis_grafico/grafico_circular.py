"""
Este módulo proporciona funciones para crear 
gráficos circulares relacionados con series de televisión.
"""

import matplotlib.pyplot as plt

def generar_grafico_pie(dataframe):
    """
    Esta función toma un DataFrame que contiene información sobre series de televisión
    y crea un gráfico circular que muestra la distribución de series por género.
    
    :param dataframe: DataFrame con datos de series de televisión.
    :return: Series que contiene la distribución de series por género.
    """
    df_copy = dataframe.copy()

    df_copy = df_copy.dropna(subset=['genres'])
    df_copy['genres'] = df_copy['genres'].str.split(
        ', ').apply(lambda x: x if isinstance(x, list) else [])

    generos_contados = df_copy['genres'].explode().value_counts()

    generos_mayor_1_porcentaje = generos_contados[generos_contados /
                                                  generos_contados.sum() >= 0.01]

    otros_generos = generos_contados[generos_contados /
                                     generos_contados.sum() < 0.01]
    generos_mayor_1_porcentaje['Other'] = otros_generos.sum()

    plt.figure(figsize=(8, 8))
    plt.pie(generos_mayor_1_porcentaje, labels=generos_mayor_1_porcentaje.index,
            autopct='%1.1f%%', startangle=140)
    plt.title('Número de Series por Género')
    plt.axis('equal')

    plt.show()
    plt.close()

    return generos_mayor_1_porcentaje
