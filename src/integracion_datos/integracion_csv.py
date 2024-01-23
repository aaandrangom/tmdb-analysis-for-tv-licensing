"""
Este módulo proporciona una función 
para integrar datos de archivos CSV en un diccionario.
"""

import csv
import time

def integrar_csv_en_diccionario():
    """
    Esta función integra datos de varios archivos CSV
    en un diccionario, utilizando la columna 'id' como clave.

    :return: Un diccionario que contiene los datos 
    integrados y el tiempo de procesamiento.
    """
    archivos_csv = ['data/TMDB_info.csv',
                    'data/TMDB_overview.csv', 'data/TMDB_distribution.csv']

    inicio_tiempo = time.time()

    diccionario_integrado = {}

    for archivo in archivos_csv:
        with open(archivo, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                id_valor = row['id']
                diccionario_integrado[id_valor] = row

    fin_tiempo = time.time()

    tiempo_procesamiento = fin_tiempo - inicio_tiempo

    return diccionario_integrado, tiempo_procesamiento
