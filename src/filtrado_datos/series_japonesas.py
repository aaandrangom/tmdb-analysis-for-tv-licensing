"""
Este módulo proporciona una función 
para obtener series de televisión japonesas.
"""

def obtener_series_japonesas(dataframe):
    """
    Esta función filtra series de televisión que están en japonés (idioma 'ja').

    :param dataframe: DataFrame con datos de series de televisión.
    :return: DataFrame que contiene las series japonesas seleccionadas.
    """
    series_japonesas = dataframe[dataframe['languages'].str.contains(
        'ja', case=False, na=False)]

    columnas_requeridas = ['name', 'original_name',
                           'networks', 'production_companies']
    series_japonesas_seleccionadas = series_japonesas[columnas_requeridas]

    return series_japonesas_seleccionadas
