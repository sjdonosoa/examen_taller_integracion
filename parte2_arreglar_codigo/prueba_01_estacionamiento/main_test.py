# main_test.py - 21 casos de la Prueba 01 de Arreglar Codigo (Estacionamiento).
# NO lo modifiques. Cada grupo de 3 casos verifica UNA regla del enunciado y
# llama directamente a la funcion que implementa esa regla.

from desafio import a_minutos, duracion, es_gratis, bloques, tarifa, aplicar_tope, aplicar_convenio

GRUPOS = [
    ("R1", "Hora a minutos (con o sin segundos)", 3),
    ("R2", "Duracion cruzando medianoche", 3),
    ("R3", "Primeros 15 minutos gratis", 3),
    ("R4", "Se cobra cada bloque iniciado", 3),
    ("R5", "Tarifa por tipo (desconocido = la mas alta)", 3),
    ("R6", "Tope diario", 3),
    ("R7", "Convenio y redondeo a la decena", 3),
]


def _ok(obtenido, esperado, regla, entrada):
    assert obtenido == esperado, f"{regla}: con {entrada} se esperaba {esperado!r} y se obtuvo {obtenido!r}"


# R1 ----------------------------------------------------------------------
def test_c01_R1_con_segundos():
    _ok(a_minutos("23:59:59"), 1439, "R1", "'23:59:59'")


def test_c02_R1_mezcla():
    _ok([a_minutos("08:05:30"), a_minutos("08:05")], [485, 485], "R1", "'08:05:30' y '08:05'")


def test_c03_R1_espacios_y_segundos():
    _ok(a_minutos(" 00:01:00 "), 1, "R1", "' 00:01:00 '")


# R2 ----------------------------------------------------------------------
def test_c04_R2_medianoche():
    _ok(duracion("23:30", "00:10"), 40, "R2", "entrada 23:30, salida 00:10")


def test_c05_R2_casi_un_dia():
    _ok(duracion("10:00", "09:59"), 1439, "R2", "entrada 10:00, salida 09:59 (del dia siguiente)")


def test_c06_R2_normal_y_noche():
    _ok([duracion("10:00", "11:15"), duracion("22:45", "01:15")], [75, 150], "R2", "10:00->11:15 y 22:45->01:15")


# R3 ----------------------------------------------------------------------
def test_c07_R3_quince_exactos():
    _ok(es_gratis(15), True, "R3", "15 minutos")


def test_c08_R3_bordes():
    _ok([es_gratis(0), es_gratis(15), es_gratis(16)], [True, True, False], "R3", "0, 15 y 16 minutos")


def test_c09_R3_lista():
    _ok([m for m in range(10, 20) if es_gratis(m)], [10, 11, 12, 13, 14, 15], "R3", "10 a 19 minutos")


# R4 ----------------------------------------------------------------------
def test_c10_R4_media_hora_justa():
    _ok(bloques(30), 1, "R4", "30 minutos")


def test_c11_R4_multiplos():
    _ok([bloques(60), bloques(90), bloques(1440)], [2, 3, 48], "R4", "60, 90 y 1440 minutos")


def test_c12_R4_mezcla():
    _ok([bloques(16), bloques(31), bloques(120), bloques(121)], [1, 2, 4, 5], "R4", "16, 31, 120 y 121 minutos")


# R5 ----------------------------------------------------------------------
def test_c13_R5_desconocido():
    _ok(tarifa("bus"), 900, "R5", "'bus' (tipo desconocido)")


def test_c14_R5_normalizado_y_desconocido():
    _ok([tarifa(" Moto "), tarifa("CAMIONETA"), tarifa("tractor")], [400, 900, 900], "R5",
        "' Moto ', 'CAMIONETA' y 'tractor'")


def test_c15_R5_vacio():
    _ok([tarifa("auto"), tarifa("")], [700, 900], "R5", "'auto' y '' (vacio = desconocido)")


# R6 ----------------------------------------------------------------------
def test_c16_R6_bajo_el_tope():
    _ok(aplicar_tope(2100), 2100, "R6", "2100")


def test_c17_R6_sobre_el_tope():
    _ok([aplicar_tope(33600), aplicar_tope(12000)], [12000, 12000], "R6", "33600 y 12000")


def test_c18_R6_cero():
    _ok([aplicar_tope(0), aplicar_tope(11999)], [0, 11999], "R6", "0 y 11999")


# R7 ----------------------------------------------------------------------
def test_c19_R7_redondeo_hacia_abajo():
    _ok(aplicar_convenio(1960, "UC"), 1560, "R7", "1960 con convenio UC (1568 -> 1560)")


def test_c20_R7_mayusculas_y_clinica():
    _ok([aplicar_convenio(1999, "clinica"), aplicar_convenio(12000, "uc")], [990, 9600], "R7",
        "1999 'clinica' (999.5 -> 990) y 12000 'uc'")


def test_c21_R7_sin_o_desconocido():
    _ok([aplicar_convenio(1500, None), aplicar_convenio(1500, "XYZ"), aplicar_convenio(2970, "UC")],
        [1500, 1500, 2370], "R7", "None, 'XYZ' y 2970 'UC' (2376 -> 2370)")
