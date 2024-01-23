"""
Este módulo proporciona una función
para descomprimir archivos ZIP y archivos tar.gz.
"""

import zipfile
import tarfile
import os

def descomprimir_archivo(ruta_archivo):
    """
    Esta función descomprime un archivo ZIP o
    un archivo tar.gz en el directorio de origen del archivo.

    :param ruta_archivo: Ruta del archivo a descomprimir.
    """
    if ruta_archivo.endswith('.zip'):
        with zipfile.ZipFile(ruta_archivo, 'r') as archivo_zip:
            archivo_zip.extractall(os.path.dirname(ruta_archivo))
            print(f'Archivo {ruta_archivo} descomprimido con éxito.')

    elif ruta_archivo.endswith('.tar.gz'):
        with tarfile.open(ruta_archivo, 'r:gz') as archivo_tar:
            archivo_tar.extractall(os.path.dirname(ruta_archivo))
            print(f'Archivo {ruta_archivo} descomprimido con éxito.')

    else:
        print('Error: El archivo no es zip ni tar.gz.')
