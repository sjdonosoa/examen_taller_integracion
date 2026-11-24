# main_test.py - los 20 casos de la Prueba 04 (Algoritmos). NO lo modifiques.

import copy

from solucion import recortar_sufijos, frecuentes, comprimir, islas, agrupar_anagramas, rut_valido

GRUPOS = [
    ("S1", "Recortar sufijos palindromos", 3),
    ("L1", "Numeros frecuentes", 3),
    ("S2", "Comprimir string", 3),
    ("M1", "Islas en una grilla", 4),
    ("D1", "Agrupar anagramas", 3),
    ("S3", "Validar RUT", 4),
]


# ================================================================ Sufijos
def test_c01_S1_ejemplos():
    assert recortar_sufijos("codedocaaa") == "", "'aaa' se elimina y luego 'codedoc'"
    assert recortar_sufijos("coderbyte") == "coderbyte", "el unico sufijo palindromo es 'e' (1 letra)"


def test_c02_S1_vacio_y_una_letra():
    assert recortar_sufijos("") == ""
    assert recortar_sufijos("z") == "z", "un solo caracter no se elimina (menos de 2)"


def test_c03_S1_mas_largo_y_repetir():
    assert recortar_sufijos("xyzabba") == "xyz"
    assert recortar_sufijos("aabbab") == "aab", "'bab' es el sufijo palindromo mas largo; luego 'aab' termina en 'b'"
    assert recortar_sufijos("abacaba") == "", "todo el string es palindromo"


# ================================================================ Frecuentes
def test_c04_L1_ejemplo():
    assert frecuentes([4, 1, 2, 2, 4, 3, 4, 2], 2) == [(2, 3), (4, 3)]


def test_c05_L1_orden():
    assert frecuentes([5, -1, 5, -1, 7], 1) == [(-1, 2), (5, 2), (7, 1)], "veces desc, luego numero asc"
    assert frecuentes([9, 9, 9, 1, 1, 1, 1], 3) == [(1, 4), (9, 3)]


def test_c06_L1_vacios():
    assert frecuentes([], 1) == []
    assert frecuentes([1, 2, 3], 2) == [], "ninguno aparece 2 veces"


# ================================================================ Comprimir
def test_c07_S2_ejemplo():
    assert comprimir("aaabccdddd") == "a3bc2d4"


def test_c08_S2_sin_repeticiones_y_vacio():
    assert comprimir("abc") == "abc", "bloques de 1 van sin numero"
    assert comprimir("") == ""


def test_c09_S2_mayusculas_y_bloques_separados():
    assert comprimir("aAAa") == "aA2a", "distingue mayusculas"
    assert comprimir("aabaa") == "a2ba2", "bloques NO consecutivos se cuentan por separado"
    assert comprimir("zzzzzzzzzzzz") == "z12", "numeros de 2 digitos"


# ================================================================ Islas
EJEMPLO = [[1, 1, 0, 0],
           [0, 1, 0, 1],
           [1, 0, 0, 1],
           [1, 0, 1, 1]]


def test_c10_M1_ejemplo():
    assert islas(copy.deepcopy(EJEMPLO)) == (3, 4)


def test_c11_M1_diagonal_no_conecta():
    g = [[1, 0, 1],
         [0, 1, 0],
         [1, 0, 1]]
    assert islas(g) == (5, 1), "5 islas de 1 celda: en diagonal no se conectan"


def test_c12_M1_sin_tierra_y_no_rectangular_cuadrada():
    assert islas([[0, 0, 0], [0, 0, 0]]) == (0, 0)
    assert islas([[1, 1, 1, 1, 1]]) == (1, 5), "una sola fila"
    assert islas([[1], [1], [0], [1]]) == (2, 2), "una sola columna"


def test_c13_M1_no_modifica_y_forma_de_U():
    g = [[1, 0, 1],
         [1, 0, 1],
         [1, 1, 1],
         [0, 0, 0],
         [0, 1, 1]]
    copia = copy.deepcopy(g)
    assert islas(g) == (2, 7), "la U es una sola isla de 7 celdas"
    assert g == copia, "islas no debe modificar la grilla recibida"


# ================================================================ Anagramas
def test_c14_D1_ejemplo():
    entrada = ["Roma", "amor", "mora", "perro", "ramo", "AMOR", "saco", "cosa", "sol"]
    assert agrupar_anagramas(entrada) == [["amor", "mora", "ramo", "Roma"], ["cosa", "saco"]]


def test_c15_D1_sin_grupos():
    assert agrupar_anagramas(["uno", "dos", "tres"]) == []
    assert agrupar_anagramas([]) == []
    assert agrupar_anagramas(["Ala", "ALA", "ala"]) == [], "son la misma palabra repetida: no forman grupo"


def test_c16_D1_orden_de_grupos():
    entrada = ["lima", "mila", "nota", "tano", "malí", "Toña", "otan"]
    assert agrupar_anagramas(entrada) == [["nota", "otan", "tano"], ["lima", "mila"]], (
        "grupos por tamano desc; 'malí' (con tilde) y 'Toña' no son anagramas de nadie")


# ================================================================ RUT
def test_c17_S3_formatos():
    assert rut_valido("12.345.678-5") is True
    assert rut_valido("12345678-5") is True
    assert rut_valido("123456785") is True


def test_c18_S3_invalidos():
    assert rut_valido("12345678-4") is False
    assert rut_valido("abc-1") is False
    assert rut_valido("") is False
    assert rut_valido("-") is False


def test_c19_S3_digito_k():
    assert rut_valido("10.000.013-k") is True, "K minuscula tambien vale"
    assert rut_valido("12.345.670-K") is True
    assert rut_valido("6.000.000-k") is True
    assert rut_valido("6.000.000-0") is False


def test_c20_S3_digito_cero_y_ciclo():
    assert rut_valido("9.000.002-0") is True, "resto 11 -> DV '0'"
    assert rut_valido("5.126.663-3") is True
    assert rut_valido("20.000.001-3") is True, "8 digitos: los factores vuelven a partir en 2 despues del 7"
