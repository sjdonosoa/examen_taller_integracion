# desafio.py
# Parte 2: arreglar codigo - Reportes de una tienda online.
#
# Este modulo procesa los pedidos de una tienda online, pero tiene SIETE
# errores de logica (no de sintaxis). Cada funcion tiene un docstring con lo
# que DEBERIA hacer: compara el codigo con el docstring.
# No cambies nombres ni parametros. Usa solo Python base.
#
# Un pedido es un dict como este:
# {"id": "P001", "email": "  Ana@Mail.com", "fecha": "2025-03-14",
#  "items": [{"producto": "Polera", "cantidad": 2, "precio": 9990},
#            {"producto": "Gorro", "cantidad": 1, "precio": 4990}]}


def normalizar_email(email):
    """Deja el email en minuscula y sin espacios al inicio ni al final:
    '  Ana@Mail.com ' -> 'ana@mail.com'.
    """
    return email.strip().lower()


def total_pedido(items):
    """Suma cantidad * precio de TODOS los items del pedido (int).
    Una lista vacia suma 0.
    """
    total = 0
    for item in items:
        total += item["cantidad"] * item["precio"]
    return total


def aplicar_cupon(total, cupon):
    """Aplica un cupon al total y retorna el nuevo total (int):
      'DESC10'    -> 10% de descuento, redondeando hacia abajo: total * 90 // 100
      'MENOS5000' -> resta 5000, pero el total NUNCA queda negativo (minimo 0)
      None o un cupon desconocido -> el total sin cambios
    El cupon no distingue mayusculas ('desc10' vale).
    """
    if cupon is None:
        return total
    c = cupon.upper()
    if c == "DESC10":
        return total * 90 // 100
    if c == "MENOS5000":
        return max(total - 5000, 0)
    return total


def clientes_frecuentes(pedidos, minimo=3):
    """Emails (normalizados con normalizar_email) que tienen AL MENOS `minimo`
    pedidos. Retorna una lista ordenada alfabeticamente, sin repetidos.
    """
    conteo = {}
    for p in pedidos:
        e = normalizar_email(p["email"])
        conteo[e] = conteo.get(e, 0) + 1
    return sorted(e for e, n in conteo.items() if n >= minimo)


def ranking_productos(pedidos):
    """Unidades vendidas por producto, sumando todos los pedidos.
    Retorna una lista de tuplas (producto, unidades) ordenada por unidades de
    MAYOR a menor y, si empatan, por nombre de producto alfabetico (A a Z).
    """
    conteo = {}
    for p in pedidos:
        for item in p["items"]:
            conteo[item["producto"]] = conteo.get(item["producto"], 0) + item["cantidad"]
    return sorted(conteo.items(), key=lambda x: (-x[1], x[0]))


def ventas_por_mes(pedidos):
    """Total vendido (total_pedido) por mes. La llave es 'AAAA-MM' sacada de la
    fecha 'AAAA-MM-DD': marzo de 2024 y marzo de 2025 son meses DISTINTOS.
    Retorna {'2025-03': 34970, ...}.
    """
    meses = {}
    for p in pedidos:
        clave = p["fecha"][:7]
        meses[clave] = meses.get(clave, 0) + total_pedido(p["items"])
    return meses


def agregar_a_historial(pedido, historial=None):
    """Agrega el id del pedido al historial y retorna el historial.
    Si no se entrega historial, parte con uno NUEVO y vacio en cada llamada
    (dos llamadas sin historial no deben compartir la lista).
    """
    if historial is None:
        historial = []
    historial.append(pedido["id"])
    return historial
