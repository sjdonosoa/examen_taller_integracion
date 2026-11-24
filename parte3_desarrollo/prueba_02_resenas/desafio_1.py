# --- Desafio 1: Extraccion y preparacion de datos (casos 1 a 5) ---
#
# resenas.json tiene la forma {"meta": {...}, "data": [ resena, resena, ... ]}
# y cada resena es:
# {
#   "id": "R1001",
#   "texto": "El servicio fue excelente y la comida rica",
#   "local_id": "L07",
#   "creado": "2025-10-06T15:16:00Z",
#   "autor": {"usuario": "user_020", "seguidores": 1053, "verificado": true},
#   "interacciones": {
#       "likes": ["2025-10-08T06:53:00Z", ...],          # NO vienen ordenados
#       "respuestas": [{"autor": "user_011", "fecha": "2025-10-07T10:00:00Z"}, ...],
#       "reportes": 0
#   }
# }
# Todas las fechas vienen en el mismo formato ISO ('AAAA-MM-DDTHH:MM:SSZ').
#
# En todas las funciones la lista se entrega en el MISMO ORDEN en que las
# resenas aparecen en el JSON. Usa siempre el parametro ruta_json para abrir
# el archivo (los tests usan otros archivos de control).

import json


def autores_influyentes(ruta_json):
    """Caso 1 y 2. Resenas cuyo autor tiene MAS de 1000 seguidores (estricto:
    un autor con exactamente 1000 NO entra).

    Retorna una lista de dicts con exactamente estas llaves:
        [{"id": "R1001", "texto": "...", "autor": "user_020"}, ...]
    donde "autor" es el nombre de usuario (str), no el dict completo.
    """
    # TODO
    pass


def con_interacciones(ruta_json, minimo=50):
    """Casos 3 y 4. Resenas con AL MENOS `minimo` interacciones totales, donde
    interacciones totales = cantidad de likes + cantidad de respuestas
    (los reportes NO cuentan). El borde es inclusivo: con minimo=50, una
    resena con exactamente 50 interacciones SI entra.

    Retorna el mismo formato que autores_influyentes.
    """
    # TODO
    pass


def ultimas_interacciones(ruta_json):
    """Caso 5. Para TODAS las resenas, la fecha del ultimo like y de la ultima
    respuesta (la mas reciente, no la ultima de la lista). Si no hay likes o
    no hay respuestas, ese valor es None.

    Retorna:
        [{"id": "R1001", "autor": "user_020",
          "ultimo_like": "2025-10-10T01:01:00Z",
          "ultima_respuesta": None}, ...]
    """
    # TODO
    pass
