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


def _palabras(texto):
    return re.findall(r"[a-zñ]+", texto.lower().translate(TILDES))


def _puntaje(texto, lexico):
    total = 0
    for p in _palabras(texto):
        if p in lexico:
            signo = 1 if lexico[p]["polaridad"] == "positivo" else -1
            total += signo * lexico[p]["intensidad"]
    return total


def _sentimiento(puntaje):
    if puntaje > 0:
        return "positivo"
    if puntaje < 0:
        return "negativo"
    return "neutro"


def _cargar(ruta_json):
    with open(ruta_json, encoding="utf-8") as f:
        return json.load(f)["data"]


def clasificacion(ruta_json, ruta_csv):
    """Caso 10. Clasifica cada resena: "positivo" si su puntaje es > 0,
    "negativo" si es < 0 y "neutro" si es 0.

    Retorna:
        {"publicaciones": {"R1001": {"sentimiento": "neutro"}, ...}}
    """
    lexico = cargar_lexico(ruta_csv)
    return {"publicaciones": {r["id"]: {"sentimiento": _sentimiento(_puntaje(r["texto"], lexico))}
                              for r in _cargar(ruta_json)}}


def puntaje_sentimiento(ruta_json, ruta_csv):
    """Casos 11 y 12. Igual que clasificacion pero agregando el puntaje y un
    resumen con los totales.

    Retorna:
        {
          "publicaciones": {"R1001": {"sentimiento": "negativo", "puntaje": -3}, ...},
          "resumen": {"total_positivas": 10, "total_negativas": 7, "total_neutras": 2}
        }
    """
    lexico = cargar_lexico(ruta_csv)
    pubs = {}
    resumen = {"total_positivas": 0, "total_negativas": 0, "total_neutras": 0}
    llave = {"positivo": "total_positivas", "negativo": "total_negativas", "neutro": "total_neutras"}
    for r in _cargar(ruta_json):
        p = _puntaje(r["texto"], lexico)
        s = _sentimiento(p)
        pubs[r["id"]] = {"sentimiento": s, "puntaje": p}
        resumen[llave[s]] += 1
    return {"publicaciones": pubs, "resumen": resumen}


def palabras_frecuentes(ruta_json, ruta_csv, top=5):
    """Caso 13. Las `top` palabras DEL LEXICO que mas veces aparecen en todos
    los textos (contando cada aparicion). Palabras que no estan en el lexico
    no cuentan.

    Orden: frecuencia de mayor a menor; si empatan, orden alfabetico.
    Retorna solo las primeras `top`:
        [{"palabra": "excelente", "frecuencia": 20},
         {"palabra": "bueno", "frecuencia": 15}, ...]
    """
    lexico = cargar_lexico(ruta_csv)
    conteo = {}
    for r in _cargar(ruta_json):
        for p in _palabras(r["texto"]):
            if p in lexico:
                conteo[p] = conteo.get(p, 0) + 1
    orden = sorted(conteo.items(), key=lambda x: (-x[1], x[0]))
    return [{"palabra": p, "frecuencia": n} for p, n in orden[:top]]


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
    lexico = cargar_lexico(ruta_csv)
    salida = {}
    for r in _cargar(ruta_json):
        palabras = _palabras(r["texto"])
        total = 0
        for i, p in enumerate(palabras):
            if p in lexico:
                signo = 1 if lexico[p]["polaridad"] == "positivo" else -1
                if any(x in ("no", "nada") for x in palabras[max(0, i - 2):i]):
                    signo = -signo
                total += signo * lexico[p]["intensidad"]
        salida[r["id"]] = total
    return salida


def ranking_locales(ruta_json, ruta_csv, min_resenas=3):
    """Caso 16. Ranking de locales por puntaje promedio (puntaje normal, SIN
    negacion). Solo entran los locales con al menos `min_resenas` resenas.

    puntaje_promedio = round(suma de puntajes del local / cantidad de resenas, 2)

    Retorna la lista ordenada de mayor a menor puntaje_promedio; si empatan,
    por local_id alfabetico:
        [{"local_id": "L03", "resenas": 31, "puntaje_promedio": 1.45}, ...]
    """
    lexico = cargar_lexico(ruta_csv)
    acum = {}
    for r in _cargar(ruta_json):
        suma, n = acum.get(r["local_id"], (0, 0))
        acum[r["local_id"]] = (suma + _puntaje(r["texto"], lexico), n + 1)
    lista = [{"local_id": l, "resenas": n, "puntaje_promedio": round(s / n, 2)}
             for l, (s, n) in acum.items() if n >= min_resenas]
    lista.sort(key=lambda d: (-d["puntaje_promedio"], d["local_id"]))
    return lista
