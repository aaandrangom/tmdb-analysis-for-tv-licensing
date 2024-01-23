"""
Este módulo contiene pruebas unitarias para las funciones en el módulo principal.
"""
import os
import unittest
import pandas as pd
from HTMLTestRunner import HTMLTestRunner
from testing_imports import descomprimir_archivo
from testing_imports import integrar_csv_en_diccionario
from testing_imports import integrar_csv_en_dataframe
from testing_imports import calcular_air_days
from testing_imports import crear_diccionario_posters
from testing_imports import filtrar_series_por_palabras_clave
from testing_imports import obtener_series_2023_canceladas

class TestPublic(unittest.TestCase):
    """
    Esta clase contiene pruebas unitarias para las funciones en el módulo principal.
    """

    def test_descomprimir_archivo(self):
        """
        Esta prueba verifica la función de descomprimir archivo.
        """
        archivo_prueba = 'tests/test.zip'
        descomprimir_archivo(archivo_prueba)

        carpeta_descomprimida = 'tests'
        self.assertTrue(os.path.exists(carpeta_descomprimida))

        archivos_descomprimidos = os.listdir(carpeta_descomprimida)
        self.assertTrue('archivo1.txt' in archivos_descomprimidos)
        self.assertTrue('archivo2.txt' in archivos_descomprimidos)

    def test_integrar_csv_en_diccionario(self):
        """
        Esta prueba verifica la función de integrar CSV en diccionario.
        """
        diccionario, tiempo = integrar_csv_en_diccionario()
        self.assertIsInstance(diccionario, dict)
        self.assertGreater(tiempo, 0)

    def test_integrar_csv_en_dataframe(self):
        """
        Esta prueba verifica la función de integrar CSV en DataFrame.
        """
        dataframe, tiempo = integrar_csv_en_dataframe()
        self.assertIsInstance(dataframe, pd.DataFrame)
        self.assertGreater(tiempo, 0)

    def test_calcular_air_days(self):
        """
        Esta prueba verifica la función de calcular air days.
        """
        dataframe_prueba,  tiempo = integrar_csv_en_dataframe()
        resultado = calcular_air_days(dataframe_prueba)
        self.assertIsInstance(resultado, pd.DataFrame)
        self.assertTrue('air_days' in resultado.columns)
        self.assertIsInstance(tiempo, float)
        self.assertGreater(tiempo, 0)

    def test_crear_diccionario_posters(self):
        """
        Esta prueba verifica la función de crear diccionario de posters.
        """
        dataframe_prueba,  tiempo = integrar_csv_en_dataframe()
        diccionario_posters = crear_diccionario_posters(dataframe_prueba)
        self.assertIsInstance(diccionario_posters, dict)
        self.assertIsInstance(tiempo, float)
        self.assertGreater(tiempo, 0)

    def test_filtrar_series_por_palabras_clave(self):
        """
        Esta prueba verifica la función de filtrar series por palabras clave.
        """
        dataframe_prueba,  tiempo = integrar_csv_en_dataframe()
        resultado = filtrar_series_por_palabras_clave(dataframe_prueba)
        self.assertIsInstance(resultado, pd.DataFrame)
        self.assertIsInstance(tiempo, float)
        self.assertGreater(tiempo, 0)

    def test_obtener_series_2023_canceladas(self):
        """
        Esta prueba verifica la función de obtener series canceladas en 2023.
        """
        dataframe_prueba,  tiempo = integrar_csv_en_dataframe()
        resultado = obtener_series_2023_canceladas(dataframe_prueba)
        self.assertIsInstance(resultado, pd.DataFrame)
        self.assertIsInstance(tiempo, float)
        self.assertGreater(tiempo, 0)

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='test_reports'))
