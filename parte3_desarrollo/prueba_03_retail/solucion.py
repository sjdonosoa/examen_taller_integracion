# solucion.py
# Prueba 03 (Parte 3 - Desarrollo) - Ventas de una cadena de supermercados 2025.
#
# Completa las 9 funciones (partes A, B y C). Cada una se prueba por separado
# con 24 casos en total. Mantén nombres y parametros: los tests las importan.
#
# PUNTAJE: nota = 1.0 + (casos aprobados / 24) * 6.0
#
# DATOS (carpeta archivos/):
#
#   ventas.csv  -> OJO: separado por PUNTO Y COMA (';'), encoding='utf-8-sig'.
#                  9.000 lineas de detalle de boletas. Una boleta tiene 1 a 4 lineas.
#       id_boleta        str  'B000001' (se repite en las lineas de la misma boleta)
#       fecha            str  'DD/MM/AAAA'  (formato chileno, no ISO)
#       id_tienda        str  'T01'... (hay una tienda 'T99' que NO esta en tiendas.json)
#       sku              str  'SKU0001'... (hay un 'SKU9999' que NO esta en productos.json)
#       cantidad         str  entero; NEGATIVO si la linea es una devolucion
#       precio_unitario  str  entero, en pesos
#
#   productos.json -> {"categorias": [{"nombre": "Lácteos",
#                        "productos": [{"sku": "SKU0001", "nombre": "...", "costo": 990}, ...]}, ...]}
#
#   tiendas.json   -> [{"id": "T01", "nombre": "Express Providencia",
#                       "region": "Metropolitana", "metros2": 180}, ...]
#                     (una tienda tiene metros2 = 0: esta en remodelacion)
#
# Puedes usar csv, json, datetime (ya importados) o pandas. Lo que retornas
# debe ser estructura nativa de Python.

import csv
import json
from datetime import datetime


# YA IMPLEMENTADA
def cargar_tiendas(ruta):
    """Lee tiendas.json y retorna {id: {"nombre", "region", "metros2"}}.
    Ya esta implementada: usala tal cual.
    """
    with open(ruta, encoding="utf-8") as f:
        return {t["id"]: {"nombre": t["nombre"], "region": t["region"], "metros2": t["metros2"]}
                for t in json.load(f)}


# ============================================================ PARTE A
def cargar_ventas(ruta):
    """A.1 (casos 1 y 2) - Carga de ventas.csv.

    Lee el archivo (separado por ';', encoding 'utf-8-sig') y retorna una
    lista de dicts, una por linea, con todos los valores como string.
    """
    # TODO
    pass


def cargar_productos(ruta):
    """A.2 (casos 3 y 4) - Aplanar el catalogo de productos.

    productos.json viene anidado por categoria. Retorna un dict plano:
        {"SKU0001": {"nombre": "Leche Entera 1L", "categoria": "Lácteos", "costo": 990}, ...}
    con un elemento por producto (31 en total).
    """
    # TODO
    pass


def limpiar_ventas(ventas):
    """A.3 (casos 5 a 7) - Limpieza linea a linea.

    Modifica cada dict:
    - cantidad y precio_unitario a int.
    - Agrega 'monto' = cantidad * precio_unitario (negativo en devoluciones).
    - Agrega 'es_devolucion' = True si cantidad < 0, si no False.
    - Agrega 'mes' (int, 1 a 12) sacado de la fecha 'DD/MM/AAAA'.
    - Agrega 'tipo_dia': usa datetime.strptime(fecha, '%d/%m/%Y').weekday();
      si es >= 5 (sabado o domingo) es 'FIN_DE_SEMANA', si no 'DÍA_HÁBIL'.
    La fecha queda como string. Retorna la misma lista.

    Ejemplo: {'fecha': '15/03/2025', 'cantidad': '-2', 'precio_unitario': '990', ...}
    queda {..., 'cantidad': -2, 'precio_unitario': 990, 'monto': -1980,
           'es_devolucion': True, 'mes': 3, 'tipo_dia': 'FIN_DE_SEMANA'}
    (el 15/03/2025 fue sabado).
    """
    # TODO
    pass


def construir_stats_tiendas(ventas, tiendas):
    """A.4 (casos 8 a 10) - Diccionario de estadisticas por tienda.

    A partir de las ventas limpias, construye un dict cuya clave es id_tienda
    y el valor un dict con EXACTAMENTE estos 9 campos:

      nombre            str  de tiendas (o el mismo id si la tienda no esta, ej. 'T99')
      region            str  de tiendas (o 'SIN REGIÓN' si no esta)
      metros2           int  de tiendas (o 0 si no esta)
      venta_bruta       int  suma de 'monto' de las lineas que NO son devolucion
      devoluciones      int  suma del valor ABSOLUTO de 'monto' de las devoluciones
      venta_neta        int  venta_bruta - devoluciones
      boletas           int  cantidad de id_boleta DISTINTOS de la tienda
      venta_fin_semana  int  suma de 'monto' (con signo) de las lineas de FIN_DE_SEMANA
      ventas_por_mes    dict {mes int: suma de 'monto' con signo de ese mes}

    Solo aparecen tiendas que tengan al menos una linea en ventas.

    Ejemplo: dos lineas de la boleta B1 (lunes de enero, montos 1000 y 500) y
    una devolucion de la boleta B2 (sabado de febrero, monto -300) dan:
      {'nombre': ..., 'region': ..., 'metros2': ..., 'venta_bruta': 1500,
       'devoluciones': 300, 'venta_neta': 1200, 'boletas': 2,
       'venta_fin_semana': -300, 'ventas_por_mes': {1: 1500, 2: -300}}
    """
    # TODO
    pass


# ============================================================ PARTE B
def ranking_tiendas(stats):
    """B.1 (casos 11 a 13) - Ranking por venta por metro cuadrado.

    Omite las tiendas con metros2 == 0. Para las demas:
        venta_m2 = round(venta_neta / metros2, 1)
    Retorna una lista de dicts con exactamente: tienda (nombre), region,
    venta_neta, metros2, venta_m2. Orden: venta_m2 de MAYOR a menor; si
    empatan, por tienda alfabetico.
    """
    # TODO
    pass


def stats_mensuales(stats):
    """B.2 (casos 14 a 16) - Venta neta nacional por mes.

    Junta los ventas_por_mes de todas las tiendas. Retorna:
        {mes int: {"venta_neta": int, "mes_peak": bool}}
    con exactamente esas dos llaves por mes. mes_peak es True SOLO para el
    mes con mayor venta_neta nacional (si hubiera empate, True para todos los
    meses empatados en el maximo).
    """
    # TODO
    pass


def categorias_top(ventas, productos):
    """B.3 (casos 17 a 19) - Resumen por categoria de producto.

    Usa las ventas LIMPIAS y el catalogo plano de A.2. Ignora las lineas cuyo
    sku no esta en el catalogo. Por cada categoria calcula:
      unidades           int  suma de cantidad (con signo: las devoluciones restan)
      venta_neta         int  suma de monto (con signo)
      margen             int  suma de (precio_unitario - costo) * cantidad
      producto_estrella  str  nombre del producto de la categoria con MAS
                              unidades netas; si empatan, el primero alfabetico.
    Retorna una lista de dicts con exactamente: categoria, unidades,
    venta_neta, margen, producto_estrella. Orden: venta_neta de mayor a menor.
    """
    # TODO
    pass


# ============================================================ PARTE C
def alerta_devoluciones(stats):
    """C.1 (casos 20 a 22) - Tiendas con devoluciones sobre el promedio.

    1. tasa_nacional = suma de devoluciones / suma de venta_bruta * 100,
       sumando TODAS las tiendas de stats.
    2. Una tienda entra en alerta si cumple las dos condiciones:
       - boletas >= 100
       - tasa_devolucion = devoluciones / venta_bruta * 100 es ESTRICTAMENTE
         mayor que tasa_nacional (compara sin redondear).
    3. Cada tienda en alerta va con exactamente: tienda (nombre), region,
       tasa_devolucion (redondeada con round(..., 2)) y
       pct_fin_semana = round(venta_fin_semana / venta_neta * 100, 2).
    Orden: tasa_devolucion de mayor a menor; empate -> tienda alfabetico.
    """
    # TODO
    pass


def clasificar_y_exportar(ranking):
    """C.2 (casos 23 y 24) - Clasificacion y exportacion.

    Recibe la lista de B.1 y agrega a cada tienda el campo 'categoria' segun
    venta_m2 (bordes con mayor o igual):
        venta_m2 >= 15000           -> 'A'
        8000 <= venta_m2 < 15000    -> 'B'
        6000 <= venta_m2 < 8000     -> 'C'
        venta_m2 < 6000             -> 'D'
    O sea, 15000.0 exacto es 'A', 8000.0 es 'B' y 6000.0 es 'C'.
    Luego escribe 'ranking_tiendas.csv' en la carpeta de trabajo (separado por
    coma, encoding 'utf-8', con csv.writer o DictWriter): un encabezado y una
    fila por tienda en el mismo orden de la lista, con estas 6 columnas:
        tienda,region,venta_neta,metros2,venta_m2,categoria
    Retorna la misma lista con 'categoria' agregada.
    """
    # TODO
    pass


# if __name__ == "__main__":
#     ventas = limpiar_ventas(cargar_ventas("archivos/ventas.csv"))
#     productos = cargar_productos("archivos/productos.json")
#     tiendas = cargar_tiendas("archivos/tiendas.json")
#     stats = construir_stats_tiendas(ventas, tiendas)
#     for fila in ranking_tiendas(stats)[:3]:
#         print(fila)
