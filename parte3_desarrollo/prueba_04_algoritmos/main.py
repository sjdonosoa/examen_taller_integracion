# main.py - corre los casos de esta prueba y muestra tu NOTA.
# Es el equivalente al boton "Run Code" de CoderByte. NO lo modifiques.
#
# Uso (desde cualquier carpeta):
#     python main.py
# o en VS Code: abre este archivo y aprieta el boton "Run Python File" (triangulo).

import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
os.chdir(AQUI)
if AQUI not in sys.path:
    sys.path.insert(0, AQUI)

if sys.version_info[:2] != (3, 11):
    print(
        "AVISO: el examen corre Python 3.11 y tu estas usando Python "
        + ".".join(map(str, sys.version_info[:3]))
        + ". Casi todo funciona igual, pero practica con 3.11 si puedes.\n"
    )

try:
    import pytest
except ImportError:
    print("Falta pytest. Instalalo con:  python -m pip install pytest")
    sys.exit(1)


def _leer_grupos():
    """Lee la lista GRUPOS del archivo de tests sin importar tu codigo."""
    import ast

    with open(os.path.join(AQUI, "main_test.py"), encoding="utf-8") as f:
        arbol = ast.parse(f.read())
    for nodo in arbol.body:
        if isinstance(nodo, ast.Assign) and getattr(nodo.targets[0], "id", "") == "GRUPOS":
            return ast.literal_eval(nodo.value)
    return []


def _total_casos():
    with open(os.path.join(AQUI, "main_test.py"), encoding="utf-8") as f:
        return f.read().count("\ndef test_")


GRUPOS = _leer_grupos()


class ReporteNota:
    def __init__(self):
        self.aprobados = 0
        self.por_grupo = {}

    def pytest_collectreport(self, report):
        if report.failed:
            print("\n*** TU CODIGO NO SE PUEDE IMPORTAR: todos los casos quedan en 0 ***")
            print("(en el examen pasa lo mismo: un error de sintaxis anula TODOS los casos)\n")
            print(str(report.longrepr)[-1500:])

    def pytest_runtest_logreport(self, report):
        if report.when != "call" and not report.failed:
            return
        nombre = report.nodeid.split("::")[-1]
        partes = nombre.split("_")          # test_c07_A3_duracion_min
        caso = partes[1][1:] if len(partes) > 2 else nombre
        grupo = partes[2] if len(partes) > 2 else ""
        if report.passed:
            print(f"Caso {caso} [{grupo}] OK")
            self.aprobados += 1
            self.por_grupo[grupo] = self.por_grupo.get(grupo, 0) + 1
        elif report.failed:
            msg = ""
            crash = getattr(report.longrepr, "reprcrash", None)
            if crash is not None:
                msg = crash.message
            else:
                msg = str(report.longrepr).strip().splitlines()[-1]
            msg = msg.split("\nassert ")[0].replace("AssertionError: ", "").strip()
            if len(msg) > 600:
                msg = msg[:600] + " ..."
            print(f"Caso {caso} [{grupo}] FALLA -> {msg}")


reporte = ReporteNota()
argumentos = [os.path.join(AQUI, "main_test.py"), "-p", "no:terminal", "-p", "no:cacheprovider", "-s"]
pytest.main(argumentos, plugins=[reporte])

total = _total_casos()
es_regla = GRUPOS and all(c.startswith("R") and c[1:].isdigit() for c, _, _ in GRUPOS)
print("\n===== RESUMEN POR " + ("REGLA" if es_regla else "SUBDESAFIO") + " =====")
for codigo, nombre, n in GRUPOS:
    ok = reporte.por_grupo.get(codigo, 0)
    marca = "OK " if ok == n else "   "
    print(f"{marca}{codigo:<5} {nombre:<45} {ok}/{n}")

nota = 1.0 + (reporte.aprobados / total) * 6.0 if total else 1.0
print(f"\nCASOS APROBADOS: {reporte.aprobados}/{total}")
print(f"NOTA ACTUAL: {nota:.1f}")
