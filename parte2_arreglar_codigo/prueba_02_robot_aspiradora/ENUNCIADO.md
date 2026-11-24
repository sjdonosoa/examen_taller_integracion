# Arreglar código 02 · El cerebro de un robot aspiradora

**Parte 2 – Detección y arreglo de problemas · 60 minutos · Dificultad: ⭐⭐⭐ (media)**
Formato calcado de "El dron de la batalla naval" (Examen 2026-01): grilla, vecinos, bordes y desempates. 5 errores, 15 casos.

---

## Instrucciones

Abre `desafio.py` y corrígelo. No tiene errores de sintaxis, pero sí **cinco errores de lógica**: el robot elige mal a qué celda ir. Puedes reescribir lo que quieras, pero la primera línea de `solution(grilla, pos)` debe quedar igual. Corre `python main.py` después de cada arreglo.

## La pieza y el robot

`grilla` es una matriz rectangular (lista de listas). Cada celda vale:

| Valor | Significado |
|---|---|
| 0 | Limpia |
| 1 | **Sucia** |
| 2 | Obstáculo (un mueble): nunca es objetivo |

Una celda se ubica como `[fila, columna]` desde 0: `[0, 0]` es arriba a la izquierda, la fila crece hacia abajo y la columna hacia la derecha. `pos` es la celda donde está el robot.

## Qué debe hacer `solution(grilla, pos)`

Devuelve **una lista** `[fila, columna]` con el objetivo del robot, sin modificar la grilla.

**Situación 1 – hay suciedad al lado.** Mira las 4 vecinas en este orden, como un reloj: **arriba, derecha, abajo, izquierda**. Una vecina fuera del tablero no existe. Va a la primera vecina sucia.

**Situación 2 – no hay suciedad al lado.** Va a la celda sucia **más cercana** de todo el mapa, con distancia **Manhattan** `|Δfila| + |Δcol|` (el robot no se mueve en diagonal; ignora los obstáculos para medir). Empate → menor fila; si sigue el empate → menor columna.

**Situación 3 – no queda nada sucio.** Devuelve su propia posición.

## Ejemplos

```
solution([[0, 0, 1]], [0, 0])            -> [0, 2]   # la "izquierda" de [0,0] no existe
solution([[0,0,0],[0,0,1],[0,1,0]], [1,1]) -> [1, 2] # derecha antes que abajo
solution([[0,0,2,0,1]], [0, 1])          -> [0, 4]   # el 2 es un mueble, no suciedad
solution([[0,0,0,0,1],
          [0,0,0,0,0],
          [0,0,0,1,0]], [0, 1])          -> [0, 4]   # Manhattan 3 vs 4 (en diagonal parecería más cerca)
```

> ⚠️ Pista Python: `grilla[0][-1]` **no** lanza error: devuelve la última columna. Revisar solo `c < ancho` no basta.

## Tu nota

15 casos, 3 por regla. `nota = 1.0 + (casos aprobados / 15) * 6.0`

| Casos | 0 | 3 | 6 | 9 | 12 | 15 |
|---|---|---|---|---|---|---|
| Nota | 1.0 | 2.2 | 3.4 | 4.6 | 5.8 | 7.0 |

Si obtienes un número que no está en la tabla (por ejemplo 7/15), un arreglo quedó a medias o agregaste un error nuevo: el grupo con 1/3 o 2/3 en el resumen te dice dónde.
