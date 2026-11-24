# Prueba 01 · Pipeline de bicicletas compartidas (Santiago 2025)

**Parte 3 – Implementación en código · 60 minutos · Dificultad: ⭐⭐ (base)**
Formato calcado del Examen 2026-01 (Pregunta 2, "Pipeline de siniestros").

---

## 1. Contexto del problema

Una empresa de bicicletas compartidas opera 44 estaciones en 8 comunas de Santiago. Te entregan el registro de viajes de marzo a mayo de 2025 y el catálogo de estaciones. Tu tarea es construir un pipeline en Python: **cargar datos, limpiar campos, consolidar métricas por estación, resumir por comuna y calcular un ranking de rotación**.

El código se completa en `solucion.py`. Ahí está el contrato exacto de cada función: parámetros, retorno, campos esperados y reglas de desempate.

## 2. Datasets entregados (carpeta `archivos/`)

**Dataset A – Viajes** · `viajes.csv` · separador coma · encoding `utf-8-sig` · 7.200 filas × 8 columnas

| Columna | Qué trae |
|---|---|
| id_viaje | `V00001` … |
| fecha | `AAAA-MM-DD` |
| hora_inicio | `0` a `23` |
| id_origen / id_destino | id de la estación (`E101`…) |
| duracion_seg | segundos del viaje |
| distancia_m | metros recorridos |
| tipo_usuario | `SUSCRITO` o `CASUAL`, **a veces con espacios o en minúscula** |

**Dataset B – Estaciones** · `estaciones.csv` · 44 filas × 4 columnas: `id_estacion, nombre, comuna, capacidad`. Algunos nombres vienen con espacios extra. Hay estaciones con capacidad `0` (en mantención).

Unos pocos viajes usan **estaciones piloto** (`E901`, `E902`, `E903`) que **no están en el catálogo**.

## PARTE A

**A.1 Carga de viajes (casos 1 y 2).** Lee `viajes.csv` y retorna una lista de diccionarios, una fila por viaje, con todo como string.

**A.2 Carga de estaciones (casos 3 y 4).** Retorna un dict indexado por `id_estacion` con `nombre` (sin espacios extra), `comuna` y `capacidad` (int).

**A.3 Limpieza y franja (casos 5 a 8).** Convierte números, normaliza `tipo_usuario`, agrega `duracion_min` y clasifica cada viaje en una `franja` (MADRUGADA, PUNTA_AM, VALLE, PUNTA_PM, NOCHE). Los bordes son inclusivos (ver docstring).

**A.4 Diccionario consolidado por estación (casos 9 a 12).** Construye `datos_estaciones` con salidas, llegadas, duración promedio y salidas en hora punta. Aparecen todas las estaciones que salen **o llegan** en algún viaje; las que no están en el catálogo quedan con comuna `DESCONOCIDA` y capacidad 0.

## PARTE B

**B.1 Resumen por comuna (casos 13 a 16).** Totales por comuna, `balance = llegadas − salidas` y la estación líder (más salidas; empate → alfabético).

**B.2 Ranking de rotación (casos 17 a 20).** Para estaciones con capacidad > 0: `rotacion = round(salidas / capacidad, 2)`. Lista completa ordenada de mayor a menor; empate → alfabético por nombre.

## Instrucciones de trabajo

- Completa solo las 6 funciones de `solucion.py` y no cambies sus nombres ni parámetros.
- Cada función se prueba por separado: puedes avanzar aunque otra quede pendiente.
- Lo que evalúan los tests es el **valor retornado**, no los `print`.
- Si usas pandas, retorna estructuras nativas (listas, dicts, int, float, str).
- Si una función queda incompleta, deja código válido (`pass` sirve). Un error de sintaxis anula todos los casos.
- Corre `python main.py` para ver el **RESUMEN POR SUBDESAFÍO** y la **NOTA ACTUAL**.

## Nota

`nota = 1.0 + (casos aprobados / 20) * 6.0`

| Casos | Nota |
|---|---|
| 0 | 1.0 |
| 5 | 2.5 |
| 10 | 4.0 |
| 15 | 5.5 |
| 20 | 7.0 |

> 💡 Estrategia de examen: A.1 + A.2 + A.3 = 8 casos (3.4). Con A.4 llegas a 12 (4.6). Las funciones de la parte B se prueban con datos de control, así que puedes hacerlas aunque A.4 no te funcione.
