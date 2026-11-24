# Prueba 03 · Ventas de una cadena de supermercados 2025

**Parte 3 – Implementación en código · 60 minutos · Dificultad: ⭐⭐⭐⭐ (alta)**
Formato calcado de la práctica oficial "Ejercicios Parte 2" (9 funciones, 24 casos, partes A/B/C con exportación).

---

## Contexto

Una cadena de 12 supermercados quiere un pipeline que cruce su detalle de boletas con el catálogo de productos y la ficha de cada tienda. Debes **cargar, limpiar, consolidar por tienda, rankear, resumir por mes y por categoría, detectar tiendas con devoluciones anómalas y exportar un CSV**.

Abre `solucion.py` y completa sus **9 funciones**. `cargar_tiendas` ya viene implementada. Cada función trae su contrato en el docstring.

## Los datos (`archivos/`)

| Archivo | Formato | Trampas |
|---|---|---|
| `ventas.csv` | CSV, **separador `;`**, `utf-8-sig`, 9.000 líneas | fecha `DD/MM/AAAA`; cantidad **negativa** = devolución; tienda `T99` y sku `SKU9999` no están en los catálogos |
| `productos.json` | JSON **anidado por categoría** | hay que aplanarlo |
| `tiendas.json` | lista de tiendas | una tiene `metros2 = 0` |

## Parte A: carga, limpieza y diccionario (casos 1 a 10)

- **A.1** `cargar_ventas` (1–2) · **A.2** `cargar_productos` aplanado (3–4)
- **A.3** `limpiar_ventas`: int, `monto`, `es_devolucion`, `mes`, `tipo_dia` con `weekday()` (5–7)
- **A.4** `construir_stats_tiendas`: 9 campos por tienda, boletas **distintas** (usa `set`), ventas por mes (8–10)

## Parte B: análisis (casos 11 a 19)

- **B.1** `ranking_tiendas`: `venta_m2 = round(venta_neta / metros2, 1)`, desc, empate alfabético (11–13)
- **B.2** `stats_mensuales`: total nacional por mes + `mes_peak` (14–16)
- **B.3** `categorias_top`: unidades, venta, margen y producto estrella por categoría (17–19)

## Parte C: alertas y exportación (casos 20 a 24)

- **C.1** `alerta_devoluciones`: tasa de la tienda **>** tasa nacional y `boletas >= 100` (20–22)
- **C.2** `clasificar_y_exportar`: categoría A/B/C/D por umbrales con `>=` y escribir `ranking_tiendas.csv` (23–24)

## Nota

`nota = 1.0 + (casos aprobados / 24) * 6.0`

| Casos | 0 | 4 | 8 | 12 | 16 | 20 | 24 |
|---|---|---|---|---|---|---|---|
| Nota | 1.0 | 2.0 | 3.0 | 4.0 | 5.0 | 6.0 | 7.0 |

> 💡 Los casos 5 en adelante usan datos de control: puedes hacer B y C aunque A no te funcione. Llegar a 12/24 no es la meta: apunta a 24/24.
