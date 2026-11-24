# --- Desafio 2: Analisis temporal (casos 6 a 9) ---
#
# Trabaja con el campo "creado" de cada resena ('AAAA-MM-DDTHH:MM:SSZ').
# Tip: datetime.strptime(texto, "%Y-%m-%dT%H:%M:%SZ") lo convierte a datetime.
# Usa siempre el parametro ruta_json para abrir el archivo.

import json
from datetime import datetime

FORMATO = "%Y-%m-%dT%H:%M:%SZ"
DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]


def distribucion_por_hora(ruta_json):
    """Casos 6 y 7. Cuantas resenas se crearon en cada hora del dia (0 a 23).

    Retorna:
        {"distribucion": {"0": 4, "15": 12, ...}}
    - La llave es la hora como string SIN cero a la izquierda ("9", no "09").
    - Solo aparecen las horas que tienen al menos una resena.
    - No importa el orden de las llaves.
    """
    # TODO
    pass


def distribucion_por_dia(ruta_json):
    """Caso 8. Cuantas resenas se crearon en cada dia de la semana.

    Retorna un dict con EXACTAMENTE estas 7 llaves (con tilde y mayuscula
    inicial), incluso si alguna tiene 0:
        {"Lunes": 30, "Martes": 28, "Miércoles": 41, "Jueves": 33,
         "Viernes": 35, "Sábado": 40, "Domingo": 33}
    Recuerda: datetime.weekday() da 0 para lunes y 6 para domingo.
    """
    # TODO
    pass


def rango_temporal(ruta_json):
    """Caso 9. Primera y ultima resena del dataset segun "creado".

    Retorna (con las fechas en el mismo formato string del JSON):
        {"rango": {"inicio": "2025-10-01T00:12:00Z", "fin": "2025-11-14T22:40:00Z"}}
    """
    # TODO
    pass
