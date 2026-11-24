"""Crea el esqueleto del estudiante a partir de la solucion resuelta.

Uso: python hacer_esqueleto.py <resuelta.py> <salida.py>

- Cada funcion top-level PUBLICA (no empieza con '_') queda solo con su firma
  y docstring, y el cuerpo pasa a ser '# TODO / pass'.
- Las funciones que ya vienen implementadas para el estudiante se marcan con
  un comentario '# YA IMPLEMENTADA' en la linea anterior al def: esas se dejan
  tal cual.
- El bloque if __name__ == "__main__": se deja comentado.
"""
import ast
import sys

origen, destino = sys.argv[1], sys.argv[2]
texto = open(origen, encoding="utf-8").read()
lineas = texto.splitlines()
arbol = ast.parse(texto)

reemplazos = []  # (inicio, fin, nuevas_lineas) en indices 0-based, fin exclusivo
for nodo in arbol.body:
    if isinstance(nodo, ast.FunctionDef):
        inicio = nodo.lineno - 1
        if nodo.decorator_list:
            inicio = nodo.decorator_list[0].lineno - 1
        if inicio > 0 and "YA IMPLEMENTADA" in lineas[inicio - 1]:
            continue
        fin = nodo.end_lineno
        if nodo.name.startswith("_"):
            reemplazos.append((inicio, fin, []))
            continue
        primero = nodo.body[0]
        tiene_doc = isinstance(primero, ast.Expr) and isinstance(getattr(primero, "value", None), ast.Constant) \
            and isinstance(primero.value.value, str)
        corte = primero.end_lineno if tiene_doc else nodo.body[0].lineno - 1
        sangria = " " * nodo.body[0].col_offset
        nuevas = lineas[inicio:corte] + [sangria + "# TODO", sangria + "pass"]
        reemplazos.append((inicio, fin, nuevas))
    elif isinstance(nodo, ast.If) and "__name__" in ast.get_source_segment(texto, nodo.test):
        inicio, fin = nodo.lineno - 1, nodo.end_lineno
        nuevas = ["# " + l if l.strip() else l for l in lineas[inicio:fin]]
        reemplazos.append((inicio, fin, nuevas))

for inicio, fin, nuevas in sorted(reemplazos, reverse=True):
    lineas[inicio:fin] = nuevas

salida = "\n".join(lineas).rstrip() + "\n"
while "\n\n\n\n" in salida:
    salida = salida.replace("\n\n\n\n", "\n\n\n")
open(destino, "w", encoding="utf-8").write(salida)
ast.parse(salida)  # valida que el esqueleto sea Python valido
print("esqueleto ->", destino)
