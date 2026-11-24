# Prueba 04 · Algoritmos con strings, listas, dicts y matrices

**Parte 3 – Implementación en código · 60 minutos · Dificultad: ⭐⭐ a ⭐⭐⭐**
Inspirada en los desafíos cortos de CoderByte que dejó el profe (prefijos palíndromos, números con frecuencia k) y en la lógica de grilla de los problemas Buscaminas y Dron.

---

No hay archivos: son **6 funciones independientes** en `solucion.py`, cada una con ejemplos en su docstring. Practica aquí lo que más se repite en el examen: recorrer strings, contar con diccionarios, ordenar con claves compuestas y moverse por una matriz sin salirse de los bordes.

| Grupo | Función | Tema | Casos |
|---|---|---|---|
| S1 | `recortar_sufijos(s)` | strings, slicing, palíndromos, ciclo `while` | 1–3 |
| L1 | `frecuentes(numeros, k)` | conteo con dict, `sorted` con clave `(-veces, numero)` | 4–6 |
| S2 | `comprimir(s)` | recorrer y agrupar consecutivos | 7–9 |
| M1 | `islas(grilla)` | matrices, vecinos en 4 direcciones, bordes, BFS/DFS | 10–13 |
| D1 | `agrupar_anagramas(palabras)` | dict de listas, `set`, ordenar grupos | 14–16 |
| S3 | `rut_valido(rut)` | limpieza de strings, módulo 11 | 17–20 |

`nota = 1.0 + (casos aprobados / 20) * 6.0` · Corre `python main.py`.

> 💡 Errores típicos que estos casos castigan: salirse de la matriz (`IndexError`) al mirar vecinos, olvidar el último bloque al comprimir, comparar con `>` cuando el enunciado dice "al menos", y no considerar el string vacío.
