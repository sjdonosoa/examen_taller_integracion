# main_test.py - los 16 casos de la Prueba 02 (Resenas). NO lo modifiques.
#
# Algunos casos usan archivos/resenas.json real; la mayoria usa un JSON de
# control (FIXTURE) que se escribe en una carpeta temporal. Esta a la vista:
# leerlo te ayuda a entender que se espera.

import json
import os

import pytest

from desafio_1 import autores_influyentes, con_interacciones, ultimas_interacciones
from desafio_2 import distribucion_por_hora, distribucion_por_dia, rango_temporal
from desafio_3 import (clasificacion, puntaje_sentimiento, palabras_frecuentes,
                       puntaje_con_negacion, ranking_locales)

GRUPOS = [
    ("D1", "Desafio 1: Extraccion", 5),
    ("D2", "Desafio 2: Analisis temporal", 4),
    ("D3", "Desafio 3: Sentimiento", 7),
]

JSON_REAL = os.path.join("archivos", "resenas.json")
CSV_REAL = os.path.join("archivos", "lexico.csv")


def _likes(n, maximo):
    """n likes desordenados; el mas reciente es `maximo` y queda al medio."""
    fechas = [f"2025-10-0{1 + i % 5}T10:{i % 60:02d}:00Z" for i in range(n - 1)]
    fechas.insert(len(fechas) // 2, maximo)
    return fechas if n else []


def _resp(fechas):
    return [{"autor": "user_x", "fecha": f} for f in fechas]


def _r(id_, usuario, seg, texto, creado, local, likes, resp, reportes=0):
    return {"id": id_, "texto": texto, "local_id": local, "creado": creado,
            "autor": {"usuario": usuario, "seguidores": seg, "verificado": False},
            "interacciones": {"likes": likes, "respuestas": resp, "reportes": reportes}}


FIXTURE = {"meta": {"total": 6}, "data": [
    _r("R1", "ana", 1500, "¡Excelente! Muy rápido y RICO", "2025-10-06T09:05:00Z", "L1",
       _likes(49, "2025-10-09T08:00:00Z"), _resp(["2025-10-07T12:00:00Z"])),
    _r("R2", "beto", 1000, "Pésimo, frío y caro. No fue rápido", "2025-10-07T09:59:00Z", "L1",
       _likes(10, "2025-10-08T23:59:00Z"), [], reportes=40),
    _r("R3", "caro", 1001, "Pedí el menú del día", "2025-10-12T23:10:00Z", "L1", [], []),
    _r("R4", "dani", 20, "Nada agradable: grosero. Malo malo", "2025-10-08T00:00:00Z", "L2",
       _likes(60, "2025-10-20T00:00:00Z"), _resp(["2025-10-09T10:00:00Z", "2025-10-11T09:00:00Z",
                                                  "2025-10-10T10:00:00Z"])[:2]),
    _r("R5", "eli", 5000, "no bueno no malo", "2025-10-06T09:30:00Z", "L2",
       _likes(3, "2025-10-06T10:00:00Z"), _resp(["2025-10-07T00:00:00Z"] * 46 + ["2025-10-08T00:00:00Z"])),
    _r("R6", "feña", 999, "Bueno y barato, nada caro", "2025-10-10T15:00:00Z", "L3",
       _likes(1, "2025-10-11T11:11:00Z"), []),
]}


@pytest.fixture
def ruta(tmp_path):
    p = tmp_path / "control.json"
    p.write_text(json.dumps(FIXTURE, ensure_ascii=False), encoding="utf-8")
    return str(p)


# ================================================================ Desafio 1
def test_c01_D1_influyentes_real():
    r = autores_influyentes(JSON_REAL)
    assert isinstance(r, list) and len(r) == 121, f"Se esperaban 121 resenas y llegaron {len(r) if r else r}"
    assert r[0] == {"id": "R1001", "texto": "Pedí el menú del día", "autor": "user_020"}, r[0]


def test_c02_D1_influyentes_borde(ruta):
    r = autores_influyentes(ruta)
    assert [x["id"] for x in r] == ["R1", "R3", "R5"], (
        "Solo MAS de 1000 seguidores (1000 exacto no entra), en el orden del JSON")
    assert r[1] == {"id": "R3", "texto": "Pedí el menú del día", "autor": "caro"}, r[1]


def test_c03_D1_interacciones_default(ruta):
    r = con_interacciones(ruta)
    assert [x["id"] for x in r] == ["R1", "R4", "R5"], (
        "likes + respuestas >= 50 (R1 y R5 tienen exactamente 50; los reportes NO cuentan)")


def test_c04_D1_interacciones_minimo(ruta):
    assert [x["id"] for x in con_interacciones(ruta, 11)] == ["R1", "R4", "R5"]
    assert [x["id"] for x in con_interacciones(ruta, 10)] == ["R1", "R2", "R4", "R5"], "minimo es inclusivo"
    assert len(con_interacciones(JSON_REAL)) == 70, "con el archivo real deben ser 70"


def test_c05_D1_ultimas(ruta):
    r = {x["id"]: x for x in ultimas_interacciones(ruta)}
    assert r["R1"] == {"id": "R1", "autor": "ana", "ultimo_like": "2025-10-09T08:00:00Z",
                       "ultima_respuesta": "2025-10-07T12:00:00Z"}, r.get("R1")
    assert r["R3"]["ultimo_like"] is None and r["R3"]["ultima_respuesta"] is None, "sin likes/respuestas -> None"
    assert r["R4"]["ultimo_like"] == "2025-10-20T00:00:00Z", "el ultimo like es el MAS RECIENTE, no el ultimo de la lista"
    assert r["R4"]["ultima_respuesta"] == "2025-10-11T09:00:00Z"
    assert len(ultimas_interacciones(JSON_REAL)) == 240


# ================================================================ Desafio 2
def test_c06_D2_hora_control(ruta):
    assert distribucion_por_hora(ruta) == {"distribucion": {"9": 3, "23": 1, "0": 1, "15": 1}}, (
        "Llaves string sin cero a la izquierda y solo horas con resenas")


def test_c07_D2_hora_real():
    d = distribucion_por_hora(JSON_REAL)["distribucion"]
    assert sum(d.values()) == 240 and d["15"] == 14 and d["21"] == 4 and d["0"] == 12, d


def test_c08_D2_dia_semana(ruta):
    assert distribucion_por_dia(ruta) == {"Lunes": 2, "Martes": 1, "Miércoles": 1, "Jueves": 0,
                                          "Viernes": 1, "Sábado": 0, "Domingo": 1}
    assert distribucion_por_dia(JSON_REAL)["Sábado"] == 30


def test_c09_D2_rango(ruta):
    assert rango_temporal(ruta) == {"rango": {"inicio": "2025-10-06T09:05:00Z", "fin": "2025-10-12T23:10:00Z"}}
    assert rango_temporal(JSON_REAL) == {"rango": {"inicio": "2025-10-01T00:40:00Z", "fin": "2025-11-14T22:22:00Z"}}


# ================================================================ Desafio 3
def test_c10_D3_clasificacion(ruta):
    r = clasificacion(ruta, CSV_REAL)
    esperado = {"R1": "positivo", "R2": "negativo", "R3": "neutro", "R4": "negativo", "R5": "neutro", "R6": "positivo"}
    obtenido = {k: v["sentimiento"] for k, v in r["publicaciones"].items()}
    assert obtenido == esperado, f"Ojo con tildes y mayusculas ('Pésimo', 'RICO'). Obtenido: {obtenido}"


def test_c11_D3_puntajes(ruta):
    r = puntaje_sentimiento(ruta, CSV_REAL)["publicaciones"]
    esperado = {"R1": 6, "R2": -4, "R3": 0, "R4": -5, "R5": 0, "R6": 2}
    obtenido = {k: v["puntaje"] for k, v in r.items()}
    assert obtenido == esperado, f"Puntajes esperados {esperado}, obtenido {obtenido}"


def test_c12_D3_resumen(ruta):
    r = puntaje_sentimiento(ruta, CSV_REAL)
    assert r["resumen"] == {"total_positivas": 2, "total_negativas": 2, "total_neutras": 2}, r["resumen"]
    real = puntaje_sentimiento(JSON_REAL, CSV_REAL)
    assert real["resumen"] == {"total_positivas": 134, "total_negativas": 67, "total_neutras": 39}, real["resumen"]
    assert real["publicaciones"]["R1003"] == {"sentimiento": "positivo", "puntaje": 6}


def test_c13_D3_frecuentes(ruta):
    assert palabras_frecuentes(ruta, CSV_REAL, 3) == [
        {"palabra": "malo", "frecuencia": 3}, {"palabra": "bueno", "frecuencia": 2},
        {"palabra": "caro", "frecuencia": 2}], "Orden: frecuencia desc y luego alfabetico"
    real = palabras_frecuentes(JSON_REAL, CSV_REAL)
    assert [x["palabra"] for x in real] == ["buenisimo", "barato", "rapido", "rico", "amable"], real


def test_c14_D3_negacion_simple(ruta):
    r = puntaje_con_negacion(ruta, CSV_REAL)
    assert r["R1"] == 6 and r["R3"] == 0, "sin negaciones el puntaje no cambia"
    assert r["R2"] == -6, "'No fue rápido': 'no' esta 2 palabras antes -> rapido vale -1 (total -6)"


def test_c15_D3_negacion_ventana(ruta):
    r = puntaje_con_negacion(ruta, CSV_REAL)
    assert r["R5"] == 0, "'no bueno no malo' -> -2 + 2 = 0"
    assert r["R6"] == 4, "'Bueno y barato, nada caro' -> 2 + 1 + 1 = 4"
    assert r["R4"] == -3, ("'Nada agradable: grosero. Malo malo' -> agradable -1, grosero +2 "
                           "(nada esta 2 antes), malo -2, malo -2 = -3")


def test_c16_D3_ranking_locales(ruta):
    assert ranking_locales(ruta, CSV_REAL, 2) == [
        {"local_id": "L1", "resenas": 3, "puntaje_promedio": 0.67},
        {"local_id": "L2", "resenas": 2, "puntaje_promedio": -2.5}], "L3 tiene solo 1 resena y queda fuera"
    assert ranking_locales(ruta, CSV_REAL, 1)[0] == {"local_id": "L3", "resenas": 1, "puntaje_promedio": 2.0}
    real = ranking_locales(JSON_REAL, CSV_REAL)
    assert [x["local_id"] for x in real] == ["L03", "L02", "L07", "L06", "L05", "L01", "L04"], real
