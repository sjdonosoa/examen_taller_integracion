# Arreglar código 01 · El cobro del estacionamiento

**Parte 2 – Detección y arreglo de problemas · 60 minutos · Dificultad: ⭐⭐ (base)**
Formato calcado de "El cerebro de un ascensor" (Ejercicio Parte 3, 2026-01): 7 errores de lógica, 21 casos agrupados por regla.

---

## Instrucciones para resolver

Abre `desafio.py` y corrígelo ahí. El código **no tiene errores de sintaxis**, pero sí **siete errores de lógica**: el estacionamiento cobra mal. Los descubres comparando lo que hace el código con las reglas y los ejemplos de este enunciado.

- Puedes reescribir lo que quieras de `desafio.py`, pero **no cambies el nombre ni los parámetros** de las funciones.
- Usa solo Python base. No modifiques `main.py` ni `main_test.py`.
- Cada función trae un docstring que describe lo que **debería** hacer. El error de cada función está en su código, no en su docstring.
- Corre `python main.py`: verás cada caso y al final el **RESUMEN POR REGLA** y la **NOTA ACTUAL**.

## El estacionamiento

Un estacionamiento de un mall cobra al salir según estas reglas:

| Regla | Descripción |
|---|---|
| R1 | Las barreras registran la hora como `HH:MM` o `HH:MM:SS` (los segundos se ignoran). |
| R2 | Atiende de noche: si la salida es "menor" que la entrada, pasó la medianoche (sumar 24 h a la salida). |
| R3 | Los primeros **15 minutos son gratis** (15 exactos todavía es gratis). |
| R4 | Pasados los 15 minutos, se cobra cada **bloque de 30 minutos iniciado**, contando desde el minuto 0. |
| R5 | Valor del bloque: auto $700, moto $400, camioneta $900. Tipo desconocido → la tarifa **más alta**. |
| R6 | Ninguna estadía paga más de **$12.000** (tope diario). |
| R7 | Convenios (después del tope): UC 20 %, CLINICA 50 %. Resultado **redondeado hacia abajo a la decena**. |

## Ejemplos

| Llamada | Resultado | Por qué |
|---|---|---|
| `solution("10:00", "10:15", "auto")` | `0` | 15 minutos: gratis |
| `solution("10:00", "10:30", "auto")` | `700` | 30 min = 1 bloque |
| `solution("10:00", "10:31", "moto")` | `800` | 31 min = 2 bloques iniciados |
| `solution("23:30", "01:00:45", "auto")` | `2100` | 90 min (cruza medianoche) = 3 bloques |
| `solution("08:00", "22:00", "camioneta")` | `12000` | 28 bloques × 900 = 25.200 → tope |
| `solution("09:00", "11:20", "auto", "uc")` | `2800` | 140 min = 5 bloques = 3.500 → −20 % = 2.800 |
| `solution("09:00", "10:10", "bus", "UC")` | `2160` | 3 bloques × 900 = 2.700 → −20 % = 2.160 |

## Tu nota

21 casos (3 por regla). `nota = 1.0 + (casos aprobados / 21) * 6.0`. Cada error que arregles suma sus 3 casos por su cuenta: **corrige de a uno y vuelve a correr**.

| Casos | 0 | 6 | 9 | 12 | 15 | 21 |
|---|---|---|---|---|---|---|
| Nota | 1.0 | 2.7 | 3.6 | 4.4 | 5.3 | 7.0 |

> La pauta con los 7 errores está en `soluciones/ERRORES.md`. No la abras hasta terminar.
