# --- Desafio 3: Analisis de sentimiento (casos 10 a 16) ---
#
# Tienes la funcion cargar_lexico (ya implementada en cargar_csv.py), que
# retorna {"excelente": {"polaridad": "positivo", "intensidad": 3}, ...}.
#
# REGLA DE TOKENIZACION (usala en TODAS las funciones de este archivo):
#   1. Pasa el texto a minuscula.
#   2. Quita las tildes: á->a, é->e, í->i, ó->o, ú->u, ü->u (la ñ se mantiene).
#   3. Las palabras son las secuencias de letras: re.findall(r"[a-zñ]+", texto)
#   Ejemplo: "¡Pésimo! No fue rápido" -> ["pesimo", "no", "fue", "rapido"]
#
# PUNTAJE de una resena = suma de la intensidad de cada palabra del texto que
# este en el lexico: + si es "positivo", - si es "negativo". Si una palabra se
# repite, cuenta cada vez que aparece.
#   "Muy malo y además lento" -> malo (-2) + lento (-2) = -4
#
# Usa siempre los parametros ruta_json y ruta_csv para abrir los archivos.

import json
import re

from cargar_csv import cargar_lexico

TILDES = str.maketrans("áéíóúü", "aeiouu")


def clasificacion(ruta_json, ruta_csv):
    """Caso 10. Clasifica cada resena: "positivo" si su puntaje es > 0,
    "negativo" si es < 0 y "neutro" si es 0.

    Retorna:
        {"publicaciones": {"R1001": {"sentimiento": "neutro"}, ...}}
    """
    # TODO
    pass


def puntaje_sentimiento(ruta_json, ruta_csv):
    """Casos 11 y 12. Igual que clasificacion pero agregando el puntaje y un
    resumen con los totales.

    Retorna:
        {
          "publicaciones": {"R1001": {"sentimiento": "negativo", "puntaje": -3}, ...},
          "resumen": {"total_positivas": 10, "total_negativas": 7, "total_neutras": 2}
        }
    """
    # TODO
    pass


def palabras_frecuentes(ruta_json, ruta_csv, top=5):
    """Caso 13. Las `top` palabras DEL LEXICO que mas veces aparecen en todos
    los textos (contando cada aparicion). Palabras que no estan en el lexico
    no cuentan.

    Orden: frecuencia de mayor a menor; si empatan, orden alfabetico.
    Retorna solo las primeras `top`:
        [{"palabra": "excelente", "frecuencia": 20},
         {"palabra": "bueno", "frecuencia": 15}, ...]
    """
    # TODO
    pass


def puntaje_con_negacion(ruta_json, ruta_csv):
    """Casos 14 y 15. Igual que el puntaje normal, pero con NEGACION:
    si alguna de las DOS palabras inmediatamente anteriores a una palabra del
    lexico es "no" o "nada", esa palabra suma con el signo INVERTIDO.

        "No fue rápido"     -> no, fue, rapido: "no" esta 2 antes -> rapido vale -1
        "Nada agradable"    -> agradable vale -1
        "No me gustó, malo" -> malo tiene antes "gusto" y "me" -> NO se invierte: -2
        "no bueno no malo"  -> bueno -2, malo +2 -> total 0

    Retorna un dict {id_resena: puntaje_int} con TODAS las resenas.
    """
    # TODO
    pass


def ranking_locales(ruta_json, ruta_csv, min_resenas=3):
    """Caso 16. Ranking de locales por puntaje promedio (puntaje normal, SIN
    negacion). Solo entran los locales con al menos `min_resenas` resenas.

    puntaje_promedio = round(suma de puntajes del local / cantidad de resenas, 2)

    Retorna la lista ordenada de mayor a menor puntaje_promedio; si empatan,
    por local_id alfabetico:
        [{"local_id": "L03", "resenas": 31, "puntaje_promedio": 1.45}, ...]
    """
    # TODO
    pass
