# solucion.py
# Prueba 05 (Parte 3 - Desarrollo) - Avance curricular y toma de ramos.
#
# Completa las 7 funciones. 20 casos en total.
# nota = 1.0 + (casos aprobados / 20) * 6.0
#
# DATOS (carpeta archivos/):
#
#   ramos.csv (separado por coma, encoding 'utf-8'), 21 ramos:
#       sigla           str  'IIC2233'
#       nombre          str
#       creditos        str  numerico
#       prerrequisitos  str  siglas separadas por '|' ('IIC2233|IIC1253'),
#                            o string VACIO si el ramo no tiene prerrequisitos
#
#   alumnos.json:
#   {"universidad": "UC",
#    "alumnos": [
#       {"numero": "21672349", "nombre": "Vicente Silva", "carrera": "College",
#        "historial": [{"sigla": "IIC1103", "semestre": "2022-1", "nota": "4,8"}, ...]},
#       ...]}
#   OJO con las notas: vienen como STRING con COMA decimal ("4,8") y algunas
#   son "NP" (no se presento), que vale 1.0.
#   Un alumno puede tener el mismo ramo varias veces (lo reprobo y lo repitio).
#
# REGLA UC: un ramo esta aprobado si la nota es >= 4.0.

import csv
import json


# ============================================================ PARTE A
def cargar_ramos(ruta):
    """A.1 (casos 1 y 2). Retorna:
        {"IIC2133": {"nombre": "Estructuras de Datos y Algoritmos", "creditos": 10,
                     "prerrequisitos": ["IIC2233", "IIC1253"]}, ...}
    - creditos como int.
    - prerrequisitos como LISTA de siglas en el mismo orden del archivo;
      lista vacia [] si el campo viene vacio (ojo: "".split("|") da [""]).
    """
    # TODO
    pass


def cargar_alumnos(ruta):
    """A.2 (casos 3 a 5). Lee alumnos.json y retorna un dict por numero de
    alumno:
        {"21672349": {"nombre": "Vicente Silva", "carrera": "College",
                      "historial": [{"sigla": "IIC1103", "semestre": "2022-1", "nota": 4.8}, ...]}, ...}
    - La nota pasa a float: "4,8" -> 4.8 y "NP" -> 1.0.
    - El historial mantiene el orden del archivo.
    """
    # TODO
    pass


def estado_alumno(alumno, ramos):
    """A.3 (casos 6 a 9). Resume la situacion de UN alumno (un valor del dict
    de A.2). Retorna un dict con exactamente estas 5 llaves:

      aprobados           list  siglas aprobadas (al menos un intento con nota >= 4.0),
                                SIN repetir, ordenadas alfabeticamente.
      reprobaciones       int   cantidad de INTENTOS con nota < 4.0 (si reprobo un
                                ramo dos veces, cuenta 2).
      creditos_aprobados  int   suma de creditos de los ramos aprobados (cada ramo
                                una sola vez).
      ppa                 float promedio ponderado por creditos de TODOS los
                                intentos (aprobados y reprobados):
                                round(sum(nota * creditos) / sum(creditos), 2).
                                Si el historial esta vacio, 0.0.
      ultimo_semestre     str   el semestre mas reciente del historial ("2025-1"),
                                o None si el historial esta vacio.
    Los intentos de siglas que no estan en ramos se ignoran por completo.
    """
    # TODO
    pass


# ============================================================ PARTE B
def puede_tomar(alumno, sigla, ramos):
    """B.1 (casos 10 a 12). True si el alumno puede inscribir `sigla`:
      - la sigla existe en ramos,
      - el alumno NO la tiene aprobada, y
      - tiene aprobados TODOS sus prerrequisitos directos.
    En cualquier otro caso, False. (Reprobar un ramo no impide volver a tomarlo.)
    """
    # TODO
    pass


def ramos_disponibles(alumno, ramos):
    """B.2 (casos 13 y 14). Lista ordenada alfabeticamente de TODAS las siglas
    que el alumno puede tomar segun la regla de B.1.
    """
    # TODO
    pass


def ranking_carrera(alumnos, ramos, carrera):
    """B.3 (casos 15 a 17). Ranking de los alumnos de una carrera.

    Considera solo los alumnos cuya carrera es exactamente `carrera` y que
    tengan al menos un intento de un ramo existente. Para cada uno arma:
        {"numero": str, "nombre": str, "ppa": float, "creditos": int}
    usando ppa y creditos_aprobados de A.3.
    Orden: ppa de MAYOR a menor; si empatan, mas creditos primero; si siguen
    empatados, numero de alumno ascendente (como string).
    """
    # TODO
    pass


# ============================================================ PARTE C
def cadena_prerrequisitos(sigla, ramos):
    """C.1 (casos 18 a 20). Todos los prerrequisitos de `sigla`, directos e
    INDIRECTOS (los prerrequisitos de sus prerrequisitos, y asi hasta el fondo).

    Retorna una lista ordenada alfabeticamente y sin repetidos. No incluye la
    propia sigla. Si la sigla no existe o no tiene prerrequisitos, retorna [].

    Ejemplo: IIC2133 requiere IIC2233 e IIC1253, y ambos requieren IIC1103:
        cadena_prerrequisitos("IIC2133", ramos) -> ["IIC1103", "IIC1253", "IIC2233"]
    Tip: una pila/cola de pendientes o una funcion recursiva.
    """
    # TODO
    pass


# if __name__ == "__main__":
#     ramos = cargar_ramos("archivos/ramos.csv")
#     alumnos = cargar_alumnos("archivos/alumnos.json")
#     for fila in ranking_carrera(alumnos, ramos, "College")[:3]:
#         print(fila)
