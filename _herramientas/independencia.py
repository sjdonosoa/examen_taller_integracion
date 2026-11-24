"""Comprueba que en una prueba de 'arreglar codigo' cada error es independiente:
al corregir SOLO el error i, deben pasar exactamente los casos de su regla.

Uso: python independencia.py <carpeta_prueba>
Compara desafio.py (con errores) contra soluciones/desafio_resuelta.py linea a
linea: cada bloque distinto del diff es un "error".
"""
import difflib
import os
import re
import shutil
import subprocess
import sys
import tempfile

carpeta = os.path.abspath(sys.argv[1])
malo = open(os.path.join(carpeta, "desafio.py"), encoding="utf-8").read().splitlines(keepends=True)
bueno = open(os.path.join(carpeta, "soluciones", "desafio_resuelta.py"), encoding="utf-8").read().splitlines(keepends=True)
bloques = [op for op in difflib.SequenceMatcher(None, malo, bueno).get_opcodes() if op[0] != "equal"]
print(f"{len(bloques)} errores encontrados")
for i, (tag, a1, a2, b1, b2) in enumerate(bloques):
    texto = malo[:a1] + bueno[b1:b2] + malo[a2:]
    with tempfile.TemporaryDirectory() as tmp:
        copia = os.path.join(tmp, "p")
        shutil.copytree(carpeta, copia)
        open(os.path.join(copia, "desafio.py"), "w", encoding="utf-8").write("".join(texto))
        out = subprocess.run([sys.executable, "main.py"], cwd=copia, capture_output=True, text=True).stdout
    grupos = re.findall(r"^(OK |   )(R\d+)\s.*?(\d+)/(\d+)$", out, re.M)
    pasan = [g for _, g, ok, n in grupos if ok != "0"]
    completos = [g for _, g, ok, n in grupos if ok == n]
    print(f"  arreglo {i + 1} ({''.join(bueno[b1:b2]).strip()[:60]!r}): grupos con casos = {pasan}, completos = {completos}")
