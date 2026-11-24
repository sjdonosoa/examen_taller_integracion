# main_test.py - 15 casos de la Prueba 02 de Arreglar Codigo (Robot aspiradora).
# NO lo modifiques. Todos los casos llaman a solution(grilla, pos) y revisan
# UN objetivo del robot. Estan agrupados por la regla que verifican.

import copy

from desafio import solution

GRUPOS = [
    ("R1", "Vecinas: dentro del tablero", 3),
    ("R2", "Vecinas: prioridad arriba-derecha-abajo-izq", 3),
    ("R3", "Un obstaculo nunca es objetivo", 3),
    ("R4", "Distancia Manhattan", 3),
    ("R5", "Empate: menor fila, luego menor columna", 3),
]


def _caso(grilla, pos, esperado, regla):
    original = copy.deepcopy(grilla)
    obtenido = solution(grilla, pos)
    assert grilla == original, f"{regla}: solution no debe modificar la grilla"
    assert obtenido == esperado, (
        f"{regla}: grilla={original}, pos={pos} -> se esperaba {esperado} y se obtuvo {obtenido}")


# R1 -------------------------------------------------------------- dentro
def test_c01_R1_columna_cero():
    _caso([[0, 0, 1]], [0, 0], [0, 2], "R1")


def test_c02_R1_columna_cero_fila_1():
    _caso([[0, 0, 0, 0],
           [0, 0, 0, 1]], [1, 0], [1, 3], "R1")


def test_c03_R1_esquina():
    _caso([[0, 0, 0],
           [0, 0, 0],
           [0, 0, 1]], [2, 0], [2, 2], "R1")


# R2 ----------------------------------------------------------- prioridad
def test_c04_R2_derecha_antes_que_abajo():
    _caso([[0, 0, 0],
           [0, 0, 1],
           [0, 1, 0]], [1, 1], [1, 2], "R2")


def test_c05_R2_tres_vecinas():
    _caso([[1, 0, 1],
           [0, 1, 0]], [0, 1], [0, 2], "R2")


def test_c06_R2_borde_izquierdo():
    _caso([[0, 0],
           [0, 1],
           [1, 0]], [1, 0], [1, 1], "R2")


# R3 ---------------------------------------------------------- obstaculos
def test_c07_R3_obstaculo_vecino():
    _caso([[0, 0, 2, 0, 1]], [0, 1], [0, 4], "R3")


def test_c08_R3_rodeado_sin_suciedad():
    _caso([[2, 2, 2],
           [2, 0, 2],
           [2, 2, 2]], [1, 1], [1, 1], "R3")


def test_c09_R3_obstaculo_mas_cerca():
    _caso([[0, 0, 0, 0],
           [0, 0, 2, 0],
           [0, 0, 0, 1]], [0, 1], [2, 3], "R3")


# R4 ----------------------------------------------------------- Manhattan
def test_c10_R4_diagonal_no_es_atajo():
    _caso([[0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0]], [0, 1], [0, 4], "R4")


def test_c11_R4_cinco_por_cinco():
    _caso([[0, 0, 0, 0, 0],
           [0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0]], [1, 1], [1, 4], "R4")


def test_c12_R4_misma_fila_gana():
    _caso([[1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 1]], [2, 2], [2, 5], "R4")


# R5 -------------------------------------------------------------- empate
def test_c13_R5_empate_fila():
    _caso([[0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0]], [2, 2], [0, 2], "R5")


def test_c14_R5_empate_columna():
    _caso([[0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0]], [2, 2], [2, 0], "R5")


def test_c15_R5_triple_empate():
    _caso([[0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 1],
           [0, 1, 0, 0, 0]], [2, 2], [0, 3], "R5")
