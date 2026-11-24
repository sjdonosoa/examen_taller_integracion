# solucion.py
# Prueba 01 (Parte 3 - Desarrollo) - Bicicletas compartidas de Santiago 2025.
#
# Completa las 6 funciones de este archivo. Cada una se prueba por separado,
# asi que puedes avanzar y sumar casos aunque otra quede pendiente.
#
# PUNTAJE: nota = 1.0 + (casos aprobados / 20) * 6.0
#   A.1 aporta 2 casos, A.2 aporta 2, A.3 aporta 4, A.4 aporta 4,
#   B.1 aporta 4 y B.2 aporta 4.
#
# CONTRATO DE LOS CSV (ambos separados por coma, encoding='utf-8-sig').
# Vienen sin celdas vacias, pero OJO: algunos textos traen espacios extra o
# mayusculas/minusculas mezcladas (el enunciado dice cuales).
#
#   archivos/viajes.csv: 7.200 viajes de marzo a mayo 2025. Columnas:
#     id_viaje      str  'V00001'
#     fecha         str  'AAAA-MM-DD'
#     hora_inicio   str  '0' a '23'
#     id_origen     str  id de la estacion donde se saco la bicicleta ('E101')
#     id_destino    str  id de la estacion donde se devolvio
#     duracion_seg  str  numerico, segundos que duro el viaje
#     distancia_m   str  numerico, metros recorridos
#     tipo_usuario  str  'SUSCRITO' o 'CASUAL' (a veces con espacios o en minuscula)
#
#   archivos/estaciones.csv: catalogo de 44 estaciones. Columnas:
#     id_estacion   str  'E101'
#     nombre        str  nombre de la estacion (a veces con espacios extra)
#     comuna        str
#     capacidad     str  numerico, cantidad de anclajes (puede ser '0')
#
# Ojo: unos pocos viajes usan estaciones piloto (E901, E902, E903) que NO
# estan en estaciones.csv. El enunciado A.4 dice que hacer con ellas.
#
# Puedes usar lo que quieras de la libreria estandar o pandas, pero lo que
# RETORNA cada funcion debe ser la estructura nativa del contrato (listas,
# dicts, int, float, str), no DataFrames ni Series.
# Si dejas una funcion a medias, deja codigo valido (pass sirve): un error de
# sintaxis anula TODOS los casos.

import csv


def cargar_viajes(ruta):
    """A.1 (casos 1 y 2) - Carga del CSV de viajes.

    Lee viajes.csv desde la ruta recibida y devuelve una lista de
    diccionarios, una fila por viaje, con los valores como string tal como
    vienen en el archivo (lo que entrega csv.DictReader).

    Parametros:
        ruta: ruta del archivo viajes.csv.

    Retorna:
        Lista de dicts. Cada dict mapea nombre de columna a su valor (str).
    """
    # TODO
    pass


def cargar_estaciones(ruta):
    """A.2 (casos 3 y 4) - Carga del catalogo de estaciones.

    Lee estaciones.csv y construye un diccionario indexado por id_estacion.

    Parametros:
        ruta: ruta del archivo estaciones.csv.

    Retorna:
        Dict {id_estacion: {'nombre': str, 'comuna': str, 'capacidad': int}}
        - 'nombre' va SIN espacios al inicio ni al final (usa strip()).
        - 'capacidad' convertida a int.
        Ejemplo: {'E101': {'nombre': 'Plaza de Armas', 'comuna': 'Santiago',
                           'capacidad': 12}, ...}
    """
    # TODO
    pass


def limpiar_viajes(viajes):
    """A.3 (casos 5 a 8) - Limpieza fila a fila.

    Modifica cada dict de la lista de viajes:
    - Convierte a int: hora_inicio, duracion_seg y distancia_m. Los demas
      campos (fecha, ids, etc.) quedan como string.
    - Normaliza tipo_usuario con strip().upper(): ' casual' queda 'CASUAL'.
    - Agrega 'duracion_min' = round(duracion_seg / 60, 1)  (float).
    - Agrega 'franja' segun hora_inicio (ya convertida a int):
          0 a 5   -> 'MADRUGADA'
          6 a 9   -> 'PUNTA_AM'
          10 a 16 -> 'VALLE'
          17 a 20 -> 'PUNTA_PM'
          21 a 23 -> 'NOCHE'
      Los bordes son inclusivos: la hora 9 es 'PUNTA_AM' y la 10 ya es 'VALLE';
      la 20 es 'PUNTA_PM' y la 21 ya es 'NOCHE'.

    Parametros:
        viajes: lista de dicts como la retorna cargar_viajes.

    Retorna:
        La lista con esos cambios (da lo mismo mutar la original o construir
        una nueva equivalente).
    """
    # TODO
    pass


def construir_datos_estaciones(viajes, estaciones):
    """A.4 (casos 9 a 12) - Diccionario consolidado por estacion.

    Construye, a partir de los viajes limpios, el dict datos_estaciones: la
    clave es el id de la estacion y el valor un dict con exactamente estos
    7 campos:
    - nombre: str, el nombre del catalogo (ya sin espacios extra). Si la
      estacion no esta en el catalogo, el nombre es el mismo id (ej. 'E901').
    - comuna: str, la del catalogo, o 'DESCONOCIDA' si no esta en el catalogo.
    - capacidad: int, la del catalogo, o 0 si no esta en el catalogo.
    - salidas: int, cantidad de viajes cuyo id_origen es esta estacion.
    - llegadas: int, cantidad de viajes cuyo id_destino es esta estacion.
    - duracion_promedio_min: float, promedio de duracion_min de los viajes que
      SALEN de esta estacion, redondeado con round(..., 1). Si la estacion no
      tiene salidas, vale 0.0.
    - salidas_punta: int, viajes que SALEN de esta estacion con franja
      'PUNTA_AM' o 'PUNTA_PM'.

    Deben aparecer TODAS las estaciones que figuran como origen o como destino
    en algun viaje (aunque solo tengan llegadas). Las estaciones del catalogo
    que no aparecen en ningun viaje NO van.

    Parametros:
        viajes: lista limpia, como la retorna limpiar_viajes.
        estaciones: dict como el que retorna cargar_estaciones.

    Retorna:
        El dict datos_estaciones descrito arriba.
    """
    # TODO
    pass


def resumen_por_comuna(datos_estaciones):
    """B.1 (casos 13 a 16) - Resumen por comuna.

    Junta las estaciones de datos_estaciones segun su campo comuna (incluida
    'DESCONOCIDA') y construye un dict cuya clave es la comuna y el valor un
    dict con exactamente estos 5 campos:
    - estaciones: int, cuantas estaciones de datos_estaciones son de la comuna.
    - salidas: int, suma de salidas de sus estaciones.
    - llegadas: int, suma de llegadas de sus estaciones.
    - balance: int, llegadas - salidas (positivo = la comuna "recibe" bicicletas).
    - estacion_top: str, el nombre de la estacion de la comuna con MAS salidas.
      Si dos empatan en salidas, gana la primera en orden alfabetico de nombre.

    Parametros:
        datos_estaciones: dict como el que retorna construir_datos_estaciones.

    Retorna:
        El dict de resumen por comuna, con todas las comunas que aparecen.
    """
    # TODO
    pass


def ranking_rotacion(datos_estaciones):
    """B.2 (casos 17 a 20) - Ranking de rotacion de bicicletas.

    Omite las estaciones con capacidad igual a 0 (no se puede dividir). Para
    cada una de las demas calcula:

        rotacion = round(salidas / capacidad, 2)

    y arma una lista de dicts, uno por estacion, con exactamente estos 5
    campos: estacion (el nombre), comuna, salidas, capacidad y rotacion (float).

    Ordena la lista de MAYOR a MENOR rotacion (la ya redondeada). Si dos
    estaciones empatan en rotacion, van entre ellas en orden alfabetico de
    estacion. Retorna la lista COMPLETA, no solo el top.

    Parametros:
        datos_estaciones: dict como el que retorna construir_datos_estaciones.

    Retorna:
        La lista completa ordenada.
    """
    # TODO
    pass


# Para probar a mano (los tests NO ejecutan este bloque):
# if __name__ == "__main__":
#     viajes = limpiar_viajes(cargar_viajes("archivos/viajes.csv"))
#     estaciones = cargar_estaciones("archivos/estaciones.csv")
#     datos = construir_datos_estaciones(viajes, estaciones)
#     print(len(viajes), "viajes |", len(datos), "estaciones con movimiento")
#     for fila in ranking_rotacion(datos)[:5]:
#         print(fila)
