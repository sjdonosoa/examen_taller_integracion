# main_test.py - los 24 casos de la Prueba 03 (Retail). NO lo modifiques.
#
# - Los casos 1 a 4 usan los archivos reales de archivos/.
# - Los demas prueban cada funcion con datos de control (FIXTURE_*) que estan
#   aqui a la vista, con sus valores esperados.

import copy
import csv
import os

from solucion import (  # noqa: E402
    cargar_ventas, cargar_productos, cargar_tiendas, limpiar_ventas, construir_stats_tiendas,
    ranking_tiendas, stats_mensuales, categorias_top, alerta_devoluciones, clasificar_y_exportar,
)

GRUPOS = [
    ("A1", "A.1 Carga de ventas", 2),
    ("A2", "A.2 Catalogo plano", 2),
    ("A3", "A.3 Limpieza", 3),
    ("A4", "A.4 Stats por tienda", 3),
    ("B1", "B.1 Ranking venta por m2", 3),
    ("B2", "B.2 Ventas por mes", 3),
    ("B3", "B.3 Categorias", 3),
    ("C1", "C.1 Alerta de devoluciones", 3),
    ("C2", "C.2 Clasificar y exportar", 2),
]

ARCH = "archivos"


def _cruda(fecha="17/03/2025", cant="2", precio="990", boleta="B1", tienda="T1", sku="SKU0001"):
    return {"id_boleta": boleta, "fecha": fecha, "id_tienda": tienda, "sku": sku,
            "cantidad": cant, "precio_unitario": precio}


def _limpia(boleta, tienda, mes, tipo, cant, precio, sku="SKU0001"):
    return {"id_boleta": boleta, "fecha": "01/01/2025", "id_tienda": tienda, "sku": sku, "cantidad": cant,
            "precio_unitario": precio, "monto": cant * precio, "es_devolucion": cant < 0, "mes": mes,
            "tipo_dia": tipo}


H, F = "DÍA_HÁBIL", "FIN_DE_SEMANA"

# ---------------------------------------------------------------- A.4
FIXTURE_TIENDAS = {"T1": {"nombre": "Centro", "region": "RM", "metros2": 100},
                   "T2": {"nombre": "Costa", "region": "Valparaíso", "metros2": 50},
                   "T3": {"nombre": "Sin Ventas", "region": "RM", "metros2": 80}}
FIXTURE_VENTAS_A4 = [
    _limpia("B1", "T1", 1, H, 2, 500), _limpia("B1", "T1", 1, H, 1, 500), _limpia("B2", "T1", 2, F, -1, 300),
    _limpia("B3", "T2", 2, F, 4, 200), _limpia("B3", "T2", 2, F, 1, 200), _limpia("B4", "T9", 3, H, 2, 200),
]
ESPERADO_A4 = {
    "T1": {"nombre": "Centro", "region": "RM", "metros2": 100, "venta_bruta": 1500, "devoluciones": 300,
           "venta_neta": 1200, "boletas": 2, "venta_fin_semana": -300, "ventas_por_mes": {1: 1500, 2: -300}},
    "T2": {"nombre": "Costa", "region": "Valparaíso", "metros2": 50, "venta_bruta": 1000, "devoluciones": 0,
           "venta_neta": 1000, "boletas": 1, "venta_fin_semana": 1000, "ventas_por_mes": {2: 1000}},
    "T9": {"nombre": "T9", "region": "SIN REGIÓN", "metros2": 0, "venta_bruta": 400, "devoluciones": 0,
           "venta_neta": 400, "boletas": 1, "venta_fin_semana": 0, "ventas_por_mes": {3: 400}},
}


def _a4():
    return construir_stats_tiendas(copy.deepcopy(FIXTURE_VENTAS_A4), copy.deepcopy(FIXTURE_TIENDAS))


# ---------------------------------------------------------------- B y C
def _st(nombre, region, m2, bruta, dev, boletas, fin, por_mes):
    return {"nombre": nombre, "region": region, "metros2": m2, "venta_bruta": bruta, "devoluciones": dev,
            "venta_neta": bruta - dev, "boletas": boletas, "venta_fin_semana": fin, "ventas_por_mes": por_mes}


FIXTURE_STATS = {
    "S1": _st("Alfa", "RM", 100, 1600000, 100000, 300, 450000, {1: 600, 3: 2000}),
    "S2": _st("Beta", "Valparaíso", 200, 1700000, 100000, 99, 400000, {1: 6, 2: 7}),
    "S3": _st("Gamma", "RM", 300, 1899970, 100000, 100, 600000, {3: -100, 12: 8}),
    "S4": _st("Delta", "Biobío", 50, 320000, 20000, 150, 75000, {}),
    "S5": _st("Epsilon", "RM", 0, 1000000, 0, 500, 0, {}),
    "S6": _st("Celta", "Valparaíso", 100, 840000, 40000, 120, 200000, {}),
}
ESPERADO_B1 = [
    {"tienda": "Alfa", "region": "RM", "venta_neta": 1500000, "metros2": 100, "venta_m2": 15000.0},
    {"tienda": "Beta", "region": "Valparaíso", "venta_neta": 1600000, "metros2": 200, "venta_m2": 8000.0},
    {"tienda": "Celta", "region": "Valparaíso", "venta_neta": 800000, "metros2": 100, "venta_m2": 8000.0},
    {"tienda": "Delta", "region": "Biobío", "venta_neta": 300000, "metros2": 50, "venta_m2": 6000.0},
    {"tienda": "Gamma", "region": "RM", "venta_neta": 1799970, "metros2": 300, "venta_m2": 5999.9},
]
# tasa nacional = 360000 / 7359970 * 100 = 4.89...
ESPERADO_C1 = [
    {"tienda": "Alfa", "region": "RM", "tasa_devolucion": 6.25, "pct_fin_semana": 30.0},
    {"tienda": "Delta", "region": "Biobío", "tasa_devolucion": 6.25, "pct_fin_semana": 25.0},
    {"tienda": "Gamma", "region": "RM", "tasa_devolucion": 5.26, "pct_fin_semana": 33.33},
]

FIXTURE_PRODUCTOS = {"P1": {"nombre": "Leche", "categoria": "Lácteos", "costo": 600},
                     "P2": {"nombre": "Yogurt", "categoria": "Lácteos", "costo": 300},
                     "P3": {"nombre": "Pan", "categoria": "Panadería", "costo": 100}}
FIXTURE_VENTAS_B3 = [
    _limpia("B1", "T1", 1, H, 2, 1000, "P1"), _limpia("B1", "T1", 1, H, 2, 500, "P2"),
    _limpia("B2", "T1", 1, H, -1, 500, "P2"), _limpia("B3", "T1", 1, H, 1, 500, "P2"),
    _limpia("B3", "T1", 1, H, 5, 200, "P3"), _limpia("B4", "T1", 1, H, 10, 100, "PX"),
]
ESPERADO_B3 = [
    {"categoria": "Lácteos", "unidades": 4, "venta_neta": 3000, "margen": 1200, "producto_estrella": "Leche"},
    {"categoria": "Panadería", "unidades": 5, "venta_neta": 1000, "margen": 500, "producto_estrella": "Pan"},
]


# ======================================================================= A.1
def test_c01_A1_cantidad():
    v = cargar_ventas(os.path.join(ARCH, "ventas.csv"))
    assert isinstance(v, list) and len(v) == 9000, "A.1: se esperaban 9000 lineas (ojo: separador ';')"


def test_c02_A1_primera_fila():
    v = cargar_ventas(os.path.join(ARCH, "ventas.csv"))
    assert v[0] == {"id_boleta": "B000001", "fecha": "17/11/2025", "id_tienda": "T03", "sku": "SKU0001",
                    "cantidad": "2", "precio_unitario": "1490"}, f"A.1: primera fila: {v[0]}"


# ======================================================================= A.2
def test_c03_A2_plano():
    p = cargar_productos(os.path.join(ARCH, "productos.json"))
    assert isinstance(p, dict) and len(p) == 31, f"A.2: se esperaban 31 productos y llegaron {len(p) if p else p}"
    assert p["SKU0001"] == {"nombre": "Leche Entera 1L", "categoria": "Lácteos", "costo": 787}, p["SKU0001"]


def test_c04_A2_categorias():
    p = cargar_productos(os.path.join(ARCH, "productos.json"))
    cats = {}
    for info in p.values():
        cats[info["categoria"]] = cats.get(info["categoria"], 0) + 1
    assert cats == {"Lácteos": 5, "Panadería": 5, "Bebidas": 5, "Limpieza": 5, "Despensa": 6,
                    "Frutas y Verduras": 5}, cats


# ======================================================================= A.3
def test_c05_A3_tipos_y_monto():
    f = limpiar_ventas([_cruda(cant="3", precio="1290")])[0]
    assert f["cantidad"] == 3 and f["precio_unitario"] == 1290, "A.3: cantidad y precio a int"
    assert f["monto"] == 3870 and f["es_devolucion"] is False, "A.3: monto = cantidad * precio"
    d = limpiar_ventas([_cruda(cant="-2", precio="990")])[0]
    assert d["monto"] == -1980 and d["es_devolucion"] is True, "A.3: devolucion con monto negativo"


def test_c06_A3_mes():
    filas = limpiar_ventas([_cruda(fecha="05/01/2025"), _cruda(fecha="31/12/2025"), _cruda(fecha="12/03/2025")])
    assert [f["mes"] for f in filas] == [1, 12, 3], "A.3: el mes sale de 'DD/MM/AAAA' (no confundir dia con mes)"
    assert filas[0]["fecha"] == "05/01/2025", "A.3: la fecha queda como string"


def test_c07_A3_tipo_dia():
    fechas = ["14/03/2025", "15/03/2025", "16/03/2025", "17/03/2025"]   # vie, sab, dom, lun
    filas = limpiar_ventas([_cruda(fecha=x) for x in fechas])
    assert [f["tipo_dia"] for f in filas] == [H, F, F, H], [f["tipo_dia"] for f in filas]


# ======================================================================= A.4
def test_c08_A4_montos():
    s = _a4()
    for t in ESPERADO_A4:
        for campo in ("venta_bruta", "devoluciones", "venta_neta"):
            assert s[t][campo] == ESPERADO_A4[t][campo], f"A.4: {t} {campo} esperado {ESPERADO_A4[t][campo]}"


def test_c09_A4_boletas_distintas_y_fin_semana():
    s = _a4()
    assert s["T1"]["boletas"] == 2 and s["T2"]["boletas"] == 1, "A.4: boletas = id_boleta DISTINTOS (usa un set)"
    assert s["T1"]["venta_fin_semana"] == -300 and s["T2"]["venta_fin_semana"] == 1000


def test_c10_A4_completo():
    s = _a4()
    assert s == ESPERADO_A4, f"A.4: dict distinto (T3 no tiene ventas y no va; T9 no esta en tiendas).\n" \
                             f"Esperado: {ESPERADO_A4}\nObtenido: {s}"


# ======================================================================= B.1
def test_c11_B1_omite_m2_cero():
    r = ranking_tiendas(copy.deepcopy(FIXTURE_STATS))
    assert len(r) == 5 and all(x["tienda"] != "Epsilon" for x in r), "B.1: omite metros2 == 0"


def test_c12_B1_orden_empate():
    r = ranking_tiendas(copy.deepcopy(FIXTURE_STATS))
    assert [x["tienda"] for x in r] == ["Alfa", "Beta", "Celta", "Delta", "Gamma"], [x["tienda"] for x in r]


def test_c13_B1_completo():
    r = ranking_tiendas(copy.deepcopy(FIXTURE_STATS))
    assert r == ESPERADO_B1, f"B.1:\nEsperado: {ESPERADO_B1}\nObtenido: {r}"


# ======================================================================= B.2
def test_c14_B2_totales():
    r = stats_mensuales(copy.deepcopy(FIXTURE_STATS))
    assert {m: d["venta_neta"] for m, d in r.items()} == {1: 606, 2: 7, 3: 1900, 12: 8}


def test_c15_B2_peak():
    r = stats_mensuales(copy.deepcopy(FIXTURE_STATS))
    assert [m for m, d in r.items() if d["mes_peak"]] == [3], "B.2: solo el mes con maxima venta es peak"
    assert all(set(d) == {"venta_neta", "mes_peak"} for d in r.values()), "B.2: exactamente 2 llaves por mes"


def test_c16_B2_completo():
    r = stats_mensuales(copy.deepcopy(FIXTURE_STATS))
    assert r == {1: {"venta_neta": 606, "mes_peak": False}, 2: {"venta_neta": 7, "mes_peak": False},
                 3: {"venta_neta": 1900, "mes_peak": True}, 12: {"venta_neta": 8, "mes_peak": False}}, r


# ======================================================================= B.3
def test_c17_B3_unidades_venta():
    r = categorias_top(copy.deepcopy(FIXTURE_VENTAS_B3), copy.deepcopy(FIXTURE_PRODUCTOS))
    assert [(x["categoria"], x["unidades"], x["venta_neta"]) for x in r] == [
        ("Lácteos", 4, 3000), ("Panadería", 5, 1000)], "B.3: ignora sku fuera del catalogo; devoluciones restan"


def test_c18_B3_margen():
    r = categorias_top(copy.deepcopy(FIXTURE_VENTAS_B3), copy.deepcopy(FIXTURE_PRODUCTOS))
    assert [x["margen"] for x in r] == [1200, 500], "B.3: margen = suma (precio - costo) * cantidad"


def test_c19_B3_estrella_empate():
    r = categorias_top(copy.deepcopy(FIXTURE_VENTAS_B3), copy.deepcopy(FIXTURE_PRODUCTOS))
    assert r == ESPERADO_B3, f"B.3: Leche y Yogurt empatan con 2 unidades netas -> gana Leche.\nObtenido: {r}"


# ======================================================================= C.1
def test_c20_C1_filtro_boletas():
    r = alerta_devoluciones(copy.deepcopy(FIXTURE_STATS))
    nombres = [x["tienda"] for x in r]
    assert "Beta" not in nombres, "C.1: Beta tiene 99 boletas (< 100) y no entra"
    assert "Gamma" in nombres, "C.1: Gamma tiene 100 boletas exactas y SI entra"


def test_c21_C1_tasa_nacional():
    r = alerta_devoluciones(copy.deepcopy(FIXTURE_STATS))
    assert sorted(x["tienda"] for x in r) == ["Alfa", "Delta", "Gamma"], (
        "C.1: tasa nacional 4.89% (Celta 4.76% queda fuera)")


def test_c22_C1_completo():
    r = alerta_devoluciones(copy.deepcopy(FIXTURE_STATS))
    assert r == ESPERADO_C1, f"C.1:\nEsperado: {ESPERADO_C1}\nObtenido: {r}"


# ======================================================================= C.2
def test_c23_C2_categorias(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    r = clasificar_y_exportar(copy.deepcopy(ESPERADO_B1))
    assert [x["categoria"] for x in r] == ["A", "B", "B", "C", "D"], (
        "C.2: 15000.0 es A, 8000.0 es B, 6000.0 es C y 5999.9 es D")


def test_c24_C2_csv(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    clasificar_y_exportar(copy.deepcopy(ESPERADO_B1))
    assert os.path.isfile("ranking_tiendas.csv"), "C.2: no se encontro ranking_tiendas.csv en la carpeta de trabajo"
    with open("ranking_tiendas.csv", encoding="utf-8") as f:
        filas = list(csv.reader(f))
    assert filas[0] == ["tienda", "region", "venta_neta", "metros2", "venta_m2", "categoria"], filas[0]
    assert filas[1] == ["Alfa", "RM", "1500000", "100", "15000.0", "A"], filas[1]
    assert len(filas) == 6 and filas[-1][0] == "Gamma", "C.2: una fila por tienda, mismo orden"
