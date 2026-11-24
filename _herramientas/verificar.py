"""Verifica todas las pruebas de codigo del repo.

Para cada carpeta de prueba (las que tienen main.py y main_test.py):
  1. Corre los tests con el codigo tal como viene (esqueleto o codigo con
     errores): debe dar menos de 7.0 (idealmente 1.0).
  2. Copia la carpeta a un directorio temporal, reemplaza cada archivo X.py por
     soluciones/X_resuelta.py y vuelve a correr: debe dar 7.0.

Uso: python _herramientas/verificar.py [filtro]
"""
import glob
import os
import re
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
filtro = sys.argv[1] if len(sys.argv) > 1 else ""


def correr(carpeta):
    r = subprocess.run([sys.executable, "main.py"], cwd=carpeta, capture_output=True, text=True, timeout=600)
    m = re.search(r"CASOS APROBADOS: (\d+)/(\d+)", r.stdout)
    nota = re.search(r"NOTA ACTUAL: ([\d.]+)", r.stdout)
    return (m.group(0) if m else "??", float(nota.group(1)) if nota else -1, r.stdout + r.stderr)


ok_total = True
for main in sorted(glob.glob(os.path.join(RAIZ, "parte*", "*", "main.py"))):
    carpeta = os.path.dirname(main)
    if filtro not in carpeta:
        continue
    nombre = os.path.relpath(carpeta, RAIZ)
    casos0, nota0, _ = correr(carpeta)
    with tempfile.TemporaryDirectory() as tmp:
        copia = os.path.join(tmp, "p")
        shutil.copytree(carpeta, copia)
        for sol in glob.glob(os.path.join(copia, "soluciones", "*_resuelta.py")):
            destino = os.path.join(copia, os.path.basename(sol).replace("_resuelta", ""))
            shutil.copy(sol, destino)
        casos1, nota1, salida1 = correr(copia)
    estado = "OK" if (nota1 == 7.0 and nota0 < 7.0) else "FALLA"
    ok_total &= estado == "OK"
    print(f"[{estado}] {nombre:<55} inicial {casos0:<22} nota {nota0:<4} | resuelta {casos1:<22} nota {nota1}")
    if estado != "OK":
        print(salida1[-3000:])
sys.exit(0 if ok_total else 1)
