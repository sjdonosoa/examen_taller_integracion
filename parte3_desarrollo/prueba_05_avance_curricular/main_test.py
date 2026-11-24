# main_test.py - los 20 casos de la Prueba 05 (Avance curricular). NO lo modifiques.

import copy
import os

from solucion import (cargar_ramos, cargar_alumnos, estado_alumno, puede_tomar, ramos_disponibles,
                      ranking_carrera, cadena_prerrequisitos)

GRUPOS = [
    ("A1", "A.1 Carga de ramos", 2),
    ("A2", "A.2 Carga de alumnos", 3),
    ("A3", "A.3 Estado del alumno", 4),
    ("B1", "B.1 Puede tomar", 3),
    ("B2", "B.2 Ramos disponibles", 2),
    ("B3", "B.3 Ranking por carrera", 3),
    ("C1", "C.1 Cadena de prerrequisitos", 3),
]

RAMOS_CSV = os.path.join("archivos", "ramos.csv")
ALUMNOS_JSON = os.path.join("archivos", "alumnos.json")

FIXTURE_RAMOS = {
    "A": {"nombre": "Ramo A", "creditos": 10, "prerrequisitos": []},
    "B": {"nombre": "Ramo B", "creditos": 5, "prerrequisitos": ["A"]},
    "C": {"nombre": "Ramo C", "creditos": 10, "prerrequisitos": ["A"]},
    "D": {"nombre": "Ramo D", "creditos": 15, "prerrequisitos": ["B", "C"]},
    "E": {"nombre": "Ramo E", "creditos": 10, "prerrequisitos": ["D"]},
    "F": {"nombre": "Ramo F", "creditos": 5, "prerrequisitos": []},
}


def _h(sigla, nota, sem):
    return {"sigla": sigla, "semestre": sem, "nota": nota}


ALUMNO = {"nombre": "Ana", "carrera": "X", "historial": [
    _h("A", 3.5, "2023-1"), _h("F", 1.0, "2023-1"), _h("A", 4.0, "2023-2"),
    _h("B", 6.2, "2024-1"), _h("C", 3.9, "2024-1"), _h("Z", 7.0, "2024-2"),   # Z no existe en ramos
]}
VACIO = {"nombre": "Nuevo", "carrera": "X", "historial": []}

FIXTURE_ALUMNOS = {
    "200": {"nombre": "Beto", "carrera": "X", "historial": [_h("A", 5.0, "2024-1"), _h("C", 5.0, "2024-2")]},
    "100": {"nombre": "Ana", "carrera": "X", "historial": [_h("C", 5.0, "2024-1"), _h("A", 5.0, "2024-1")]},
    "300": {"nombre": "Caro", "carrera": "X", "historial": [_h("A", 5.0, "2024-1"), _h("C", 5.0, "2024-1"),
                                                           _h("B", 5.0, "2024-2"), _h("F", 5.0, "2024-2")]},
    "400": {"nombre": "Dani", "carrera": "X", "historial": [_h("A", 6.0, "2024-1")]},
    "500": {"nombre": "Eli", "carrera": "Y", "historial": [_h("A", 7.0, "2024-1")]},
    "600": {"nombre": "Feña", "carrera": "X", "historial": []},
}


# ======================================================================= A.1
def test_c01_A1_carga():
    r = cargar_ramos(RAMOS_CSV)
    assert isinstance(r, dict) and len(r) == 21, "A.1: se esperaban 21 ramos"
    assert r["IIC2133"] == {"nombre": "Estructuras de Datos y Algoritmos", "creditos": 10,
                            "prerrequisitos": ["IIC2233", "IIC1253"]}, r["IIC2133"]


def test_c02_A1_sin_prerrequisitos():
    r = cargar_ramos(RAMOS_CSV)
    assert r["IIC1103"]["prerrequisitos"] == [], "A.1: campo vacio -> lista vacia (no [''])"
    assert r["IIC3800"]["creditos"] == 15 and r["IIC3800"]["prerrequisitos"] == ["IIC3143", "IIC3113", "IIC3703"]


# ======================================================================= A.2
def test_c03_A2_cantidad():
    a = cargar_alumnos(ALUMNOS_JSON)
    assert isinstance(a, dict) and len(a) == 80, "A.2: se esperaban 80 alumnos indexados por numero"
    assert a["21672349"]["nombre"] == "Vicente Silva" and a["21672349"]["carrera"] == "Licenciatura en Ingeniería"


def test_c04_A2_nota_coma():
    a = cargar_alumnos(ALUMNOS_JSON)
    assert a["21672349"]["historial"][:2] == [
        {"sigla": "IIC1103", "semestre": "2022-1", "nota": 4.8},
        {"sigla": "ICS1513", "semestre": "2022-1", "nota": 3.9}], "A.2: '4,8' -> 4.8 (float)"


def test_c05_A2_np():
    a = cargar_alumnos(ALUMNOS_JSON)
    h = [x for x in a["21636139"]["historial"] if x["sigla"] == "MAT1620" and x["semestre"] == "2023-2"]
    assert h and h[0]["nota"] == 1.0, "A.2: 'NP' vale 1.0"
    assert all(isinstance(x["nota"], float) for al in a.values() for x in al["historial"]), "todas las notas float"


# ======================================================================= A.3
def test_c06_A3_aprobados():
    e = estado_alumno(copy.deepcopy(ALUMNO), FIXTURE_RAMOS)
    assert e["aprobados"] == ["A", "B"], "A.3: A se aprueba en el 2do intento (4.0 es aprobado); C con 3.9 no"


def test_c07_A3_reprobaciones_y_creditos():
    e = estado_alumno(copy.deepcopy(ALUMNO), FIXTURE_RAMOS)
    assert e["reprobaciones"] == 3, "A.3: intentos < 4.0: A(3.5), F(1.0), C(3.9). Z no existe y se ignora"
    assert e["creditos_aprobados"] == 15, "A.3: A (10) + B (5), cada ramo una vez"


def test_c08_A3_ppa_y_ultimo():
    e = estado_alumno(copy.deepcopy(ALUMNO), FIXTURE_RAMOS)
    assert e["ppa"] == 3.75, "A.3: (3.5*10 + 1.0*5 + 4.0*10 + 6.2*5 + 3.9*10) / 40 = 3.75"
    assert e["ultimo_semestre"] == "2024-1", "A.3: Z (2024-2) no existe en ramos y se ignora"


def test_c09_A3_vacio_y_real():
    assert estado_alumno(copy.deepcopy(VACIO), FIXTURE_RAMOS) == {
        "aprobados": [], "reprobaciones": 0, "creditos_aprobados": 0, "ppa": 0.0, "ultimo_semestre": None}
    r = cargar_ramos(RAMOS_CSV)
    a = cargar_alumnos(ALUMNOS_JSON)
    e = estado_alumno(a["21672349"], r)
    assert (e["reprobaciones"], e["creditos_aprobados"], e["ppa"], e["ultimo_semestre"]) == (9, 115, 4.47, "2024-1"), e


# ======================================================================= B.1
def test_c10_B1_ya_aprobado_y_reprobado():
    al = copy.deepcopy(ALUMNO)
    assert puede_tomar(al, "A", FIXTURE_RAMOS) is False, "B.1: A ya esta aprobado"
    assert puede_tomar(al, "C", FIXTURE_RAMOS) is True, "B.1: C se reprobo y se puede repetir (A aprobado)"
    assert puede_tomar(al, "F", FIXTURE_RAMOS) is True


def test_c11_B1_prerrequisitos():
    al = copy.deepcopy(ALUMNO)
    assert puede_tomar(al, "D", FIXTURE_RAMOS) is False, "B.1: D requiere B y C, y C no esta aprobado"
    assert puede_tomar(al, "E", FIXTURE_RAMOS) is False


def test_c12_B1_sigla_inexistente():
    assert puede_tomar(copy.deepcopy(ALUMNO), "ZZZ999", FIXTURE_RAMOS) is False
    assert puede_tomar(copy.deepcopy(VACIO), "B", FIXTURE_RAMOS) is False
    assert puede_tomar(copy.deepcopy(VACIO), "A", FIXTURE_RAMOS) is True


# ======================================================================= B.2
def test_c13_B2_fixture():
    assert ramos_disponibles(copy.deepcopy(ALUMNO), FIXTURE_RAMOS) == ["C", "F"]
    assert ramos_disponibles(copy.deepcopy(VACIO), FIXTURE_RAMOS) == ["A", "F"]


def test_c14_B2_real():
    r = cargar_ramos(RAMOS_CSV)
    a = cargar_alumnos(ALUMNOS_JSON)
    assert ramos_disponibles(a["21672349"], r) == ["EYP1113", "IIC2143", "IIC2413"]


# ======================================================================= B.3
def test_c15_B3_filtro():
    lista = ranking_carrera(copy.deepcopy(FIXTURE_ALUMNOS), FIXTURE_RAMOS, "X")
    numeros = [d["numero"] for d in lista]
    assert "500" not in numeros, "B.3: 500 es de otra carrera"
    assert "600" not in numeros, "B.3: 600 no tiene intentos"
    assert len(lista) == 4


def test_c16_B3_orden_desempates():
    lista = ranking_carrera(copy.deepcopy(FIXTURE_ALUMNOS), FIXTURE_RAMOS, "X")
    assert [d["numero"] for d in lista] == ["400", "300", "100", "200"], (
        "B.3: ppa desc; 300, 100 y 200 empatan en 5.0 -> mas creditos primero (300); 100 y 200 empatan -> numero asc")
    assert lista[0] == {"numero": "400", "nombre": "Dani", "ppa": 6.0, "creditos": 10}, lista[0]


def test_c17_B3_real():
    r = cargar_ramos(RAMOS_CSV)
    a = cargar_alumnos(ALUMNOS_JSON)
    lista = ranking_carrera(a, r, "College")
    assert len(lista) == 21
    assert lista[0] == {"numero": "21633812", "nombre": "Emilia Rodríguez", "ppa": 5.45, "creditos": 55}, lista[0]


# ======================================================================= C.1
def test_c18_C1_directo_e_indirecto():
    assert cadena_prerrequisitos("D", FIXTURE_RAMOS) == ["A", "B", "C"], "C.1: A llega por dos caminos y va una vez"
    assert cadena_prerrequisitos("E", FIXTURE_RAMOS) == ["A", "B", "C", "D"]


def test_c19_C1_vacios():
    assert cadena_prerrequisitos("A", FIXTURE_RAMOS) == []
    assert cadena_prerrequisitos("NOEXISTE", FIXTURE_RAMOS) == []


def test_c20_C1_real():
    r = cargar_ramos(RAMOS_CSV)
    assert cadena_prerrequisitos("IIC3800", r) == ["IIC1103", "IIC2143", "IIC2233", "IIC2413", "IIC2513",
                                                  "IIC3113", "IIC3143", "IIC3703"]
    assert cadena_prerrequisitos("IIC3752", r) == ["EYP1113", "IIC1103", "IIC2233", "IIC2413", "MAT1610", "MAT1620"]
