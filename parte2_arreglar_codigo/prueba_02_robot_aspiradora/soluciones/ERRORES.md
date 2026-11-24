# Pauta: los 5 errores del robot aspiradora

| Regla | Dónde | Código con error | Corrección | Por qué |
|---|---|---|---|---|
| R1 | `dentro` | `0 <= f < len(grilla) and c < len(grilla[0])` | agregar `0 <= c` | Con `c = -1` Python no falla: lee la última columna y el robot "ve" suciedad que no está al lado. |
| R2 | `DIRECCIONES` | `[(-1, 0), (1, 0), (0, 1), (0, -1)]` | `[(-1, 0), (0, 1), (1, 0), (0, -1)]` | El orden pedido es arriba, **derecha**, abajo, izquierda. |
| R3 | `es_sucia` | `valor != LIMPIA` | `valor == SUCIA` | "Distinto de limpia" incluye los obstáculos (2). |
| R4 | `distancia` | `max(abs(df), abs(dc))` | `abs(df) + abs(dc)` | `max` es la distancia de Chebyshev (permite diagonal). |
| R5 | `mas_cercana` | `d <= mejor_d` | `d < mejor_d` | Recorriendo por filas y columnas, el primer mínimo ya es el de menor fila/columna; con `<=` gana el último empatado. |

**Lección de examen:** en problemas de grilla los errores casi siempre están en (1) los bordes, (2) el orden de las direcciones, (3) qué valores cuentan, (4) la métrica de distancia y (5) el desempate `<` vs `<=`.
