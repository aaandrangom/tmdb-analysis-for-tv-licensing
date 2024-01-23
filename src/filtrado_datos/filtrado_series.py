"""
Este módulo proporciona una función
para filtrar series de televisión por palabras clave.
"""

def filtrar_series_por_palabras_clave(dataframe):
    """
    Esta función filtra series de televisión en 
    inglés que contienen palabras clave como 'mystery' o 'crime'
    en su descripción (overview).

    :param dataframe: DataFrame con datos de series de televisión.
    :return: DataFrame que contiene las series filtradas.
    """
    series_ingles = dataframe[dataframe['original_language'] == 'en']

    series_ingles = series_ingles.dropna(subset=['overview'])

    palabras_clave = ['mystery', 'crime']
    filtro = series_ingles['overview'].str.lower().str.contains(
        '|'.join(palabras_clave), na=False, case=False)
    series_con_palabras_clave = series_ingles[filtro]

    return series_con_palabras_clave
