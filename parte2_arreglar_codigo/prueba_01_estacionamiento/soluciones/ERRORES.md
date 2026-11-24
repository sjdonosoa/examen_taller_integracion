# Pauta: los 7 errores del estacionamiento

| Regla | Función | Código con error | Corrección | Por qué |
|---|---|---|---|---|
| R1 | `a_minutos` | `horas, minutos = hhmm.strip().split(":")` | `partes = ...split(":")` y usar `partes[0]`, `partes[1]` | Con segundos el split da 3 partes y el desempaquetado a 2 variables lanza `ValueError`. |
| R2 | `duracion` | `if s < e: e, s = s, e` | `if s < e: s += 1440` | Intercambiar calcula el tiempo "al revés" dentro del mismo día; cruzar medianoche es sumar 24 h. |
| R3 | `es_gratis` | `minutos < MINUTOS_GRATIS` | `minutos <= MINUTOS_GRATIS` | "15 o menos" es inclusivo. |
| R4 | `bloques` | `minutos // 30 + 1` | `(minutos + 29) // 30` (o `math.ceil(minutos / 30)`) | `//30 + 1` sobra un bloque justo en los múltiplos de 30. |
| R5 | `tarifa` | `TARIFAS.get(t, TARIFAS["auto"])` | `TARIFAS.get(t, max(TARIFAS.values()))` | Desconocido debe cobrar la tarifa más alta. |
| R6 | `aplicar_tope` | `max(monto, TOPE_DIARIO)` | `min(monto, TOPE_DIARIO)` | El tope es un máximo a cobrar → `min`. |
| R7 | `aplicar_convenio` | `int(round(con_desc, -1))` | `int(con_desc) // 10 * 10` | `round` redondea al más cercano (1568 → 1570); se pide hacia abajo (1560). |

**Patrones típicos que aparecen en el examen:** `<` vs `<=`, `min` vs `max`, redondeo hacia arriba/abajo/cercano, división entera vs techo, valor por defecto de `dict.get`, desempaquetado que asume un formato fijo.
