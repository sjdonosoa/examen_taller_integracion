# cargar_csv.py - YA IMPLEMENTADO. No necesitas modificarlo.
import csv


def cargar_lexico(ruta_csv):
    """Lee lexico.csv y retorna un dict de la forma:

        {
            "excelente": {"polaridad": "positivo", "intensidad": 3},
            "malo": {"polaridad": "negativo", "intensidad": 2},
            ...
        }

    Las palabras del lexico vienen en minuscula y SIN tildes.
    La intensidad siempre es positiva (1, 2 o 3): el signo lo da la polaridad.
    """
    lexico = {}
    with open(ruta_csv, encoding="utf-8") as f:
        for fila in csv.DictReader(f):
            lexico[fila["palabra"]] = {"polaridad": fila["polaridad"], "intensidad": int(fila["intensidad"])}
    return lexico
