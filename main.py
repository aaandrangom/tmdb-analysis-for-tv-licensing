"""
Este módulo realiza varias operaciones 
relacionadas con el procesamiento de datos de series de televisión.
"""

from src.descompresion.descomprimir import descomprimir_archivo
from src.integracion_datos.integracion_csv import integrar_csv_en_diccionario
from src.integracion_datos.integracion_pandas import integrar_csv_en_dataframe
from src.procesamiento_datos.calculo_dias import calcular_air_days
from src.procesamiento_datos.diccionario_posters import crear_diccionario_posters
from src.filtrado_datos.filtrado_series import filtrar_series_por_palabras_clave
from src.filtrado_datos.series_2023_canceladas import obtener_series_2023_canceladas
from src.filtrado_datos.series_japonesas import obtener_series_japonesas
from src.analisis_grafico.grafico_barras import contar_series_por_anio_y_graficar
from src.analisis_grafico.grafico_lineas import contar_series_por_decada_y_graficar
from src.analisis_grafico.grafico_circular import generar_grafico_pie

RUTA_ZIP = '../data/TMDB.zip'

descomprimir_archivo(RUTA_ZIP)

diccionario_datos, tiempo_diccionario = integrar_csv_en_diccionario()
print("Tiempo de integración en diccionario:", tiempo_diccionario, "segundos")

df_datos, tiempo_dataframe = integrar_csv_en_dataframe()
print("Tiempo de integración en DataFrame:", tiempo_dataframe, "segundos")

df_procesado = calcular_air_days(df_datos)
print("Ejemplo de datos con días de transmisión calculados:")
print(df_procesado[['name', 'first_air_date', 'last_air_date', 'air_days']].head())

diccionario_posters = crear_diccionario_posters(df_procesado)
print("Ejemplos de URLs de pósters:")
for name, url in list(diccionario_posters.items())[:5]:
    print(name + ": " + url)

df_series_palabras_clave = filtrar_series_por_palabras_clave(df_procesado)
print("Series que contienen palabras clave:")
print(df_series_palabras_clave[['name', 'overview']].head())

df_series_canceladas_2023 = obtener_series_2023_canceladas(df_procesado)
print("Series canceladas en 2023:")
print(df_series_canceladas_2023[['name', 'status']].head())

df_series_japonesas = obtener_series_japonesas(df_procesado)
print("Series japonesas seleccionadas:")
print(df_series_japonesas.head())

contar_series_por_anio_y_graficar(df_procesado)
contar_series_por_decada_y_graficar(df_procesado)
generar_grafico_pie(df_procesado)
