# main_test.py - los 20 casos de la Prueba 01 (Bicicletas). NO lo modifiques.
#
# Cada caso prueba UNA funcion de solucion.py:
# - los casos 1 a 4 usan los CSV reales de archivos/
# - los demas usan datos de control (FIXTURE_*) definidos aca mismo, a la
#   vista, con sus valores esperados. Leerlos te ayuda a entender el contrato.
# Los casos son independientes entre si: una funcion pendiente no resta
# puntos a las otras.

import copy
import os

from solucion import (  # noqa: E402
    cargar_viajes,
    cargar_estaciones,
    limpiar_viajes,
    construir_datos_estaciones,
    resumen_por_comuna,
    ranking_rotacion,
)

GRUPOS = [
    ("A1", "A.1 Carga de viajes", 2),
    ("A2", "A.2 Carga de estaciones", 2),
    ("A3", "A.3 Limpieza y franja", 4),
    ("A4", "A.4 Diccionario por estacion", 4),
    ("B1", "B.1 Resumen por comuna", 4),
    ("B2", "B.2 Ranking de rotacion", 4),
]

VIAJES = os.path.join("archivos", "viajes.csv")
ESTACIONES = os.path.join("archivos", "estaciones.csv")


def _fila(hora="8", tipo="SUSCRITO", dur="600", dist="2000", origen="E1", destino="E2", i=1):
    return {"id_viaje": f"V{i:05d}", "fecha": "2025-03-10", "hora_inicio": hora, "id_origen": origen,
            "id_destino": destino, "duracion_seg": dur, "distancia_m": dist, "tipo_usuario": tipo}


def _limpio(origen, destino, dur_min, franja, i=1):
    return {"id_viaje": f"V{i:05d}", "fecha": "2025-03-10", "hora_inicio": 8, "id_origen": origen,
            "id_destino": destino, "duracion_seg": int(dur_min * 60), "distancia_m": 1000,
            "tipo_usuario": "SUSCRITO", "duracion_min": dur_min, "franja": franja}


# ---------------------------------------------------------------- A.4 fixture
FIXTURE_ESTACIONES = {
    "E1": {"nombre": "Alameda", "comuna": "Santiago", "capacidad": 10},
    "E2": {"nombre": "Bustamante", "comuna": "Providencia", "capacidad": 20},
    "E3": {"nombre": "Colón", "comuna": "Las Condes", "capacidad": 0},
    "E4": {"nombre": "Sin Uso", "comuna": "Santiago", "capacidad": 15},   # no aparece en viajes
}
FIXTURE_VIAJES_LIMPIOS = [
    _limpio("E1", "E2", 10.0, "PUNTA_AM", 1),
    _limpio("E1", "E3", 20.0, "VALLE", 2),
    _limpio("E1", "E2", 15.5, "PUNTA_PM", 3),
    _limpio("E2", "E1", 8.0, "NOCHE", 4),
    _limpio("E9", "E2", 30.0, "PUNTA_PM", 5),   # E9 no esta en el catalogo
    _limpio("E2", "E9", 12.0, "MADRUGADA", 6),
]
ESPERADO_A4 = {
    "E1": {"nombre": "Alameda", "comuna": "Santiago", "capacidad": 10, "salidas": 3, "llegadas": 1,
           "duracion_promedio_min": 15.2, "salidas_punta": 2},
    "E2": {"nombre": "Bustamante", "comuna": "Providencia", "capacidad": 20, "salidas": 2, "llegadas": 3,
           "duracion_promedio_min": 10.0, "salidas_punta": 0},
    "E3": {"nombre": "Colón", "comuna": "Las Condes", "capacidad": 0, "salidas": 0, "llegadas": 1,
           "duracion_promedio_min": 0.0, "salidas_punta": 0},
    "E9": {"nombre": "E9", "comuna": "DESCONOCIDA", "capacidad": 0, "salidas": 1, "llegadas": 1,
           "duracion_promedio_min": 30.0, "salidas_punta": 1},
}


def _a4():
    return construir_datos_estaciones(copy.deepcopy(FIXTURE_VIAJES_LIMPIOS), copy.deepcopy(FIXTURE_ESTACIONES))


# ---------------------------------------------------------------- B fixture
def _est(nombre, comuna, cap, sal, lle):
    return {"nombre": nombre, "comuna": comuna, "capacidad": cap, "salidas": sal, "llegadas": lle,
            "duracion_promedio_min": 12.0, "salidas_punta": 0}


FIXTURE_DATOS = {
    "E1": _est("Mapocho", "Santiago", 10, 50, 40),
    "E2": _est("Bellas Artes", "Santiago", 20, 50, 70),      # empata con Mapocho en salidas
    "E3": _est("Santa Lucía", "Santiago", 0, 10, 5),
    "E4": _est("Tobalaba", "Providencia", 12, 30, 31),
    "E5": _est("Salvador", "Providencia", 15, 45, 30),
    "E6": _est("E906", "DESCONOCIDA", 0, 4, 9),
    "E7": _est("El Golf", "Las Condes", 25, 50, 50),
    "E8": _est("Apoquindo", "Las Condes", 3, 7, 6),
    "E9": _est("Alcántara", "Las Condes", 6, 14, 20),
}
ESPERADO_B1 = {
    "Santiago": {"estaciones": 3, "salidas": 110, "llegadas": 115, "balance": 5, "estacion_top": "Bellas Artes"},
    "Providencia": {"estaciones": 2, "salidas": 75, "llegadas": 61, "balance": -14, "estacion_top": "Salvador"},
    "DESCONOCIDA": {"estaciones": 1, "salidas": 4, "llegadas": 9, "balance": 5, "estacion_top": "E906"},
    "Las Condes": {"estaciones": 3, "salidas": 71, "llegadas": 76, "balance": 5, "estacion_top": "El Golf"},
}
# rotaciones: Mapocho 5.0, Bellas Artes 2.5, Tobalaba 2.5, Salvador 3.0,
#             El Golf 2.0, Apoquindo 2.33, Alcántara 2.33
ESPERADO_B2 = [
    {"estacion": "Mapocho", "comuna": "Santiago", "salidas": 50, "capacidad": 10, "rotacion": 5.0},
    {"estacion": "Salvador", "comuna": "Providencia", "salidas": 45, "capacidad": 15, "rotacion": 3.0},
    {"estacion": "Bellas Artes", "comuna": "Santiago", "salidas": 50, "capacidad": 20, "rotacion": 2.5},
    {"estacion": "Tobalaba", "comuna": "Providencia", "salidas": 30, "capacidad": 12, "rotacion": 2.5},
    {"estacion": "Alcántara", "comuna": "Las Condes", "salidas": 14, "capacidad": 6, "rotacion": 2.33},
    {"estacion": "Apoquindo", "comuna": "Las Condes", "salidas": 7, "capacidad": 3, "rotacion": 2.33},
    {"estacion": "El Golf", "comuna": "Las Condes", "salidas": 50, "capacidad": 25, "rotacion": 2.0},
]


# ======================================================================= A.1
def test_c01_A1_carga_cantidad():
    viajes = cargar_viajes(VIAJES)
    assert isinstance(viajes, list), "A.1 debe retornar una lista"
    assert len(viajes) == 7200, f"A.1: se esperaban 7200 viajes y llegaron {len(viajes)}"
    assert all(isinstance(v, dict) for v in viajes), "A.1: cada viaje debe ser un dict"


def test_c02_A1_primera_fila():
    viajes = cargar_viajes(VIAJES)
    esperado = {"id_viaje": "V00001", "fecha": "2025-05-15", "hora_inicio": "8", "id_origen": "E903",
                "id_destino": "E132", "duracion_seg": "1893", "distancia_m": "8360", "tipo_usuario": "CASUAL"}
    assert viajes[0] == esperado, f"A.1: primera fila distinta (ojo con encoding='utf-8-sig'): {viajes[0]}"


# ======================================================================= A.2
def test_c03_A2_carga_catalogo():
    est = cargar_estaciones(ESTACIONES)
    assert isinstance(est, dict), "A.2 debe retornar un dict"
    assert len(est) == 44, f"A.2: se esperaban 44 estaciones y llegaron {len(est)}"
    assert est["E101"] == {"nombre": "Plaza de Armas", "comuna": "Santiago", "capacidad": 12}, est["E101"]


def test_c04_A2_strip_y_capacidad_int():
    est = cargar_estaciones(ESTACIONES)
    for id_est, info in est.items():
        assert info["nombre"] == info["nombre"].strip(), f"A.2: '{info['nombre']}' trae espacios extra"
        assert isinstance(info["capacidad"], int), f"A.2: capacidad de {id_est} debe ser int"
    assert est["E140"] == {"nombre": "Cementerio General", "comuna": "Recoleta", "capacidad": 0}, est["E140"]


# ======================================================================= A.3
def test_c05_A3_conversion_a_int():
    filas = limpiar_viajes([_fila(hora="7", dur="905", dist="3120")])
    f = filas[0]
    assert f["hora_inicio"] == 7 and isinstance(f["hora_inicio"], int), "A.3: hora_inicio debe ser int"
    assert f["duracion_seg"] == 905 and f["distancia_m"] == 3120, "A.3: duracion_seg y distancia_m deben ser int"
    assert f["fecha"] == "2025-03-10" and f["id_origen"] == "E1", "A.3: los demas campos quedan como string"


def test_c06_A3_tipo_usuario_normalizado():
    tipos = [" casual", "Suscrito ", "suscrito", "CASUAL ", "SUSCRITO"]
    filas = limpiar_viajes([_fila(tipo=t, i=i) for i, t in enumerate(tipos)])
    obtenido = [f["tipo_usuario"] for f in filas]
    assert obtenido == ["CASUAL", "SUSCRITO", "SUSCRITO", "CASUAL", "SUSCRITO"], f"A.3: tipo_usuario {obtenido}"


def test_c07_A3_duracion_min():
    filas = limpiar_viajes([_fila(dur="905"), _fila(dur="60"), _fila(dur="1893"), _fila(dur="29")])
    obtenido = [f["duracion_min"] for f in filas]
    assert obtenido == [15.1, 1.0, 31.6, 0.5], f"A.3: duracion_min esperada [15.1, 1.0, 31.6, 0.5] y llego {obtenido}"


def test_c08_A3_franja_bordes():
    horas = [0, 5, 6, 9, 10, 16, 17, 20, 21, 23]
    esperado = ["MADRUGADA", "MADRUGADA", "PUNTA_AM", "PUNTA_AM", "VALLE", "VALLE",
                "PUNTA_PM", "PUNTA_PM", "NOCHE", "NOCHE"]
    filas = limpiar_viajes([_fila(hora=str(h), i=i) for i, h in enumerate(horas)])
    obtenido = [f["franja"] for f in filas]
    for h, e, o in zip(horas, esperado, obtenido):
        assert e == o, f"A.3: la hora {h} deberia ser '{e}' y quedo '{o}'"


# ======================================================================= A.4
def test_c09_A4_claves():
    datos = _a4()
    assert isinstance(datos, dict), "A.4 debe retornar un dict"
    assert set(datos) == {"E1", "E2", "E3", "E9"}, (
        f"A.4: claves esperadas E1, E2, E3 (solo llegadas) y E9 (fuera del catalogo); "
        f"E4 no se usa en viajes y no va. Llego: {sorted(datos)}")
    for k in datos:
        assert set(datos[k]) == set(ESPERADO_A4["E1"]), f"A.4: {k} debe tener exactamente 7 campos"


def test_c10_A4_salidas_llegadas():
    datos = _a4()
    for k, e in ESPERADO_A4.items():
        assert (datos[k]["salidas"], datos[k]["llegadas"]) == (e["salidas"], e["llegadas"]), (
            f"A.4: {k} salidas/llegadas esperado {(e['salidas'], e['llegadas'])}")


def test_c11_A4_duracion_promedio():
    datos = _a4()
    for k, e in ESPERADO_A4.items():
        assert datos[k]["duracion_promedio_min"] == e["duracion_promedio_min"], (
            f"A.4: {k} duracion_promedio_min esperado {e['duracion_promedio_min']} "
            f"y llego {datos[k]['duracion_promedio_min']} (sin salidas = 0.0)")


def test_c12_A4_catalogo_y_punta():
    datos = _a4()
    assert datos == ESPERADO_A4, f"A.4: dict completo distinto.\nEsperado: {ESPERADO_A4}\nObtenido: {datos}"


# ======================================================================= B.1
def test_c13_B1_totales():
    r = resumen_por_comuna(copy.deepcopy(FIXTURE_DATOS))
    for c, e in ESPERADO_B1.items():
        assert (r[c]["estaciones"], r[c]["salidas"], r[c]["llegadas"]) == (
            e["estaciones"], e["salidas"], e["llegadas"]), f"B.1: totales de {c}"


def test_c14_B1_balance():
    r = resumen_por_comuna(copy.deepcopy(FIXTURE_DATOS))
    for c, e in ESPERADO_B1.items():
        assert r[c]["balance"] == e["balance"], f"B.1: balance de {c} = llegadas - salidas = {e['balance']}"


def test_c15_B1_estacion_top_desempate():
    r = resumen_por_comuna(copy.deepcopy(FIXTURE_DATOS))
    assert r["Santiago"]["estacion_top"] == "Bellas Artes", (
        "B.1: Mapocho y Bellas Artes empatan con 50 salidas; gana la primera alfabeticamente")
    assert r["Providencia"]["estacion_top"] == "Salvador"
    assert r["Las Condes"]["estacion_top"] == "El Golf"


def test_c16_B1_completo():
    r = resumen_por_comuna(copy.deepcopy(FIXTURE_DATOS))
    assert r == ESPERADO_B1, f"B.1: resultado distinto.\nEsperado: {ESPERADO_B1}\nObtenido: {r}"


# ======================================================================= B.2
def test_c17_B2_omite_capacidad_cero():
    lista = ranking_rotacion(copy.deepcopy(FIXTURE_DATOS))
    nombres = {d["estacion"] for d in lista}
    assert "Santa Lucía" not in nombres and "E906" not in nombres, "B.2: omite las de capacidad 0"
    assert len(lista) == 7, f"B.2: deben quedar 7 estaciones y quedaron {len(lista)}"


def test_c18_B2_rotacion_redondeada():
    lista = ranking_rotacion(copy.deepcopy(FIXTURE_DATOS))
    rot = {d["estacion"]: d["rotacion"] for d in lista}
    assert rot.get("Apoquindo") == 2.33 and rot.get("Mapocho") == 5.0, (
        f"B.2: rotacion = round(salidas / capacidad, 2). Obtenido: {rot}")


def test_c19_B2_orden_y_desempate():
    lista = ranking_rotacion(copy.deepcopy(FIXTURE_DATOS))
    orden = [d["estacion"] for d in lista]
    assert orden == [d["estacion"] for d in ESPERADO_B2], (
        f"B.2: orden de mayor a menor rotacion y, si empatan, alfabetico. Obtenido: {orden}")


def test_c20_B2_completo():
    lista = ranking_rotacion(copy.deepcopy(FIXTURE_DATOS))
    assert lista == ESPERADO_B2, f"B.2: lista distinta.\nEsperado: {ESPERADO_B2}\nObtenido: {lista}"
