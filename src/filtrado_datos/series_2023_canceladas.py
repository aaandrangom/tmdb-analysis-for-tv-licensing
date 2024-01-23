"""
Este módulo proporciona una función 
para obtener series de televisión canceladas en 2023.
"""

def obtener_series_2023_canceladas(dataframe):
    """
    Esta función filtra series de televisión que fueron canceladas en el año 2023.

    :param dataframe: DataFrame con datos de series de televisión.
    :return: DataFrame que contiene las series canceladas en 2023.
    """
    df_copy = dataframe.copy()

    df_copy['first_air_date'] = df_copy['first_air_date'].astype(str)

    series_2023_canceladas = df_copy[
        df_copy['first_air_date'].str.startswith('2023') &
        (df_copy['status'] == 'Canceled')
    ]

    primeros_20_elementos = series_2023_canceladas.head(20)

    return primeros_20_elementos
