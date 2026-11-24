# Guía del examen: qué trae cada parte (según las evaluaciones liberadas)

Resumen de lo que se ve en las 9 evaluaciones públicas de CoderByte que entrega el profesor en las instrucciones (2025-02, 2026-01, prácticas y demos). Sirve para saber **qué tipo de ejercicio esperar**; los ejercicios de este repo son originales, construidos con ese mismo formato.

> Recordatorio de las instrucciones: Python 3.11, sin IA (reprobación inmediata), solo apuntes de sintaxis Python en partes 2 y 3, la plataforma detecta copy/paste desde otras pestañas. En 2026-02 **la Parte 2 es arreglar código y la Parte 3 es el desafío de implementación** (antes era al revés).

---

## Parte 1 · Selección múltiple (30 min, 20 %)

| Evaluación | Preguntas | Qué traía |
|---|---|---|
| Examen 2026-01 | 18 | ~6 de Gestión de Operaciones TI (evolución soporte→colaboración→diferenciación→negocio, posicionamiento de un caso, catálogo de servicios, mejores prácticas vs estándares, presupuesto centralizado vs distribuido, incidente recurrente = gestión de problemas), ~6 de Ingeniería de Software (baja cohesión, Sprint Review, **código Python** para identificar Strategy, Observer, SOA, Adapter) y ~6 de Gestión de Proyectos (casos de interesados, conflicto, comunicaciones, riesgos con proveedores). |
| Examen 2025-02 | 12 | **Código Python** para distinguir Strategy vs Factory, caso largo para elegir SOA, 4 fragmentos de código para elegir el Adapter correcto, agilidad (cambios tardíos), CI, ITSM, BI, migración lift-and-shift, y las mismas preguntas de interesados/conflicto. |

**Patrón:** los enunciados son casos ("Caso: la empresa X…") y varias preguntas son **leer código y reconocer el patrón**. Las de GPTI del temario incluyen cálculos (EVM, PERT, reservas), por eso la calculadora es obligatoria.

→ En este repo: `parte1_seleccion_multiple/` (2 pruebas de 18, mismo reparto por ramo, con explicación de cada respuesta).

---

## Parte 2 · Arreglar código (60 min, 40 %)

| Evaluación | Problema | Formato |
|---|---|---|
| Ejercicio 2026-01 "Ascensor" | Algoritmo SCAN: elegir la próxima parada según dirección, llamadas de subida/bajada | 7 errores de lógica, 21 casos (3 por regla), "RESUMEN POR REGLA" |
| Examen 2026-01 "Dron" | Batalla naval: buscar fila por fila o rematar alrededor de un tocado | 5 errores, 15 casos; uno provoca `IndexError` (salirse del tablero) |
| Examen 2025-02 "Buscaminas" | Revelar celdas; si hay 0 minas alrededor se expande (flood fill) | errores de sintaxis y/o lógica |
| Demo "Viernes" | Números que aparecen exactamente k veces | función corta |

**Patrón de los errores:** `<` vs `<=`, `min` vs `max`, mínimo vs máximo al invertir dirección, revisar bordes de una matriz, orden de prioridad, desempates, unión de conjuntos equivocada (incluir lo que no corresponde). Cada función trae un docstring correcto: **el error está en el código, nunca en el docstring.**

→ En este repo: `parte2_arreglar_codigo/` (3 pruebas: 7 + 5 + 7 errores, cada arreglo suma sus casos de forma independiente).

---

## Parte 3 · Implementación (60 min, 40 %)

| Evaluación | Problema | Formato |
|---|---|---|
| Examen 2026-01 "Siniestros de tránsito" | CSV de siniestros CONASET + CSV de población INE | 6 funciones, 20 casos: cargar → agrupar población → limpiar y franja horaria → dict por comuna con cruce de nombres normalizados → resumen por región con líder (desempate alfabético) → ranking de tasa por 100.000 hab. |
| Práctica oficial (pipeline siniestros) | Mismos datos, más largo | 9 funciones, 24 casos: además `weekday()` para fin de semana, conteo por mes en un dict anidado, filtro contra tasa nacional, índice ponderado y **exportar un CSV** |
| Examen 2025-02 "Análisis de sentimientos" | JSON de publicaciones (anidado) + CSV léxico | 3 archivos `desafio_N.py`, 12 casos: filtros por seguidores e interacciones, fecha de la última interacción, distribución por hora, rango temporal, puntaje de sentimiento, palabras más frecuentes con desempate |
| Demo "Jueves" | Eliminar prefijos palíndromos repetidamente | strings |

**Patrón:** leer CSV/JSON → convertir tipos (todo llega como string) → normalizar texto (`strip().lower()`) → construir **diccionarios de agregación** → cruzar dos fuentes (y decidir qué hacer si no calza) → ordenar con **claves compuestas** y desempates → redondear con `round(x, 2)`. Los tests usan **datos de control** además del archivo real, así que cada función se puede hacer por separado.

→ En este repo: `parte3_desarrollo/` (5 pruebas, de dificultad base a alta).

---

## Consejos para el día

1. Lee el enunciado **entero** antes de escribir código: los bordes (`>` vs `>=`, empates) están ahí y son los casos que fallan.
2. Corre el código seguido. Arregla de a una función y vuelve a correr.
3. Nunca dejes un error de sintaxis: **anula todos los casos**. Si algo queda a medias, deja `pass`.
4. Retorna estructuras nativas (`list`, `dict`, `int`, `float`, `str`), nunca un DataFrame.
5. Ojo con `encoding="utf-8-sig"` en los CSV (si no, la primera columna trae `﻿`).
6. 12/24 da un 4,0, pero no te quedes ahí: apunta a todos los casos.
