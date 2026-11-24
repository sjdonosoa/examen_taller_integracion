# main_test.py - 21 casos de la Prueba 03 de Arreglar Codigo (Pedidos).
# NO lo modifiques. Cada grupo de 3 casos prueba UNA funcion.

from desafio import (normalizar_email, total_pedido, aplicar_cupon, clientes_frecuentes,
                     ranking_productos, ventas_por_mes, agregar_a_historial)

GRUPOS = [
    ("R1", "Email normalizado", 3),
    ("R2", "Total del pedido", 3),
    ("R3", "Cupones", 3),
    ("R4", "Clientes frecuentes (al menos)", 3),
    ("R5", "Ranking de productos y empates", 3),
    ("R6", "Ventas por mes (AAAA-MM)", 3),
    ("R7", "Historial nuevo en cada llamada", 3),
]


def _it(producto, cantidad, precio):
    return {"producto": producto, "cantidad": cantidad, "precio": precio}


def _p(id_, email, fecha, items):
    return {"id": id_, "email": email, "fecha": fecha, "items": items}


def _ok(obtenido, esperado, regla, contexto):
    assert obtenido == esperado, f"{regla}: {contexto} -> se esperaba {esperado!r} y se obtuvo {obtenido!r}"


# R1 -----------------------------------------------------------------------
def test_c01_R1_espacios():
    _ok(normalizar_email("  Ana@Mail.com "), "ana@mail.com", "R1", "'  Ana@Mail.com '")


def test_c02_R1_tab_y_salto():
    _ok(normalizar_email("\tBETO@uc.cl\n"), "beto@uc.cl", "R1", "tab y salto de linea")


def test_c03_R1_lista():
    _ok([normalizar_email(e) for e in ["x@y.cl", " X@Y.CL", "x@y.cl  "]], ["x@y.cl"] * 3, "R1", "tres variantes")


# R2 -----------------------------------------------------------------------
def test_c04_R2_dos_items():
    _ok(total_pedido([_it("Polera", 2, 9990), _it("Gorro", 1, 4990)]), 24970, "R2", "2 poleras + 1 gorro")


def test_c05_R2_varios_y_vacio():
    _ok([total_pedido([_it("A", 1, 100), _it("B", 2, 200), _it("C", 3, 300)]), total_pedido([])],
        [1400, 0], "R2", "tres items y lista vacia")


def test_c06_R2_cantidad_cero():
    _ok(total_pedido([_it("A", 0, 5000), _it("B", 4, 250)]), 1000, "R2", "primer item con cantidad 0")


# R3 -----------------------------------------------------------------------
def test_c07_R3_menos5000_no_negativo():
    _ok(aplicar_cupon(3000, "MENOS5000"), 0, "R3", "total 3000 con MENOS5000")


def test_c08_R3_varios():
    _ok([aplicar_cupon(9999, "desc10"), aplicar_cupon(4999, "menos5000"), aplicar_cupon(8000, "MENOS5000")],
        [8999, 0, 3000], "R3", "DESC10 sobre 9999, MENOS5000 sobre 4999 y 8000")


def test_c09_R3_borde_y_desconocido():
    _ok([aplicar_cupon(5000, "MENOS5000"), aplicar_cupon(100, "MENOS5000"), aplicar_cupon(100, "XX"),
         aplicar_cupon(100, None)], [0, 0, 100, 100], "R3", "5000, 100, cupon desconocido y None")


# R4 -----------------------------------------------------------------------
PEDIDOS_R4 = [_p(f"P{i}", e, "2025-01-01", [_it("A", 1, 100)]) for i, e in enumerate(
    ["ana@x.cl", "ana@x.cl", "ana@x.cl", "beto@x.cl", "beto@x.cl", "caro@x.cl", "dani@x.cl", "dani@x.cl",
     "dani@x.cl", "dani@x.cl"])]


def test_c10_R4_minimo_por_defecto():
    _ok(clientes_frecuentes(PEDIDOS_R4), ["ana@x.cl", "dani@x.cl"], "R4", "minimo=3 (ana tiene exactamente 3)")


def test_c11_R4_minimo_2():
    _ok(clientes_frecuentes(PEDIDOS_R4, 2), ["ana@x.cl", "beto@x.cl", "dani@x.cl"], "R4", "minimo=2")


def test_c12_R4_minimo_1_y_4():
    _ok([clientes_frecuentes(PEDIDOS_R4, 1), clientes_frecuentes(PEDIDOS_R4, 4)],
        [["ana@x.cl", "beto@x.cl", "caro@x.cl", "dani@x.cl"], ["dani@x.cl"]], "R4", "minimo=1 y minimo=4")


# R5 -----------------------------------------------------------------------
PEDIDOS_R5 = [
    _p("P1", "a@x.cl", "2025-01-01", [_it("Polera", 2, 1), _it("Gorro", 3, 1)]),
    _p("P2", "a@x.cl", "2025-01-02", [_it("Bufanda", 3, 1), _it("Polera", 1, 1)]),
    _p("P3", "a@x.cl", "2025-01-03", [_it("Calcetines", 5, 1), _it("Anteojos", 1, 1)]),
]


def test_c13_R5_empate_alfabetico():
    _ok(ranking_productos(PEDIDOS_R5)[1:4], [("Bufanda", 3), ("Gorro", 3), ("Polera", 3)], "R5",
        "Bufanda, Gorro y Polera empatan con 3 (orden A a Z)")


def test_c14_R5_completo():
    _ok(ranking_productos(PEDIDOS_R5), [("Calcetines", 5), ("Bufanda", 3), ("Gorro", 3), ("Polera", 3),
                                        ("Anteojos", 1)], "R5", "ranking completo")


def test_c15_R5_dos_empatados():
    pedidos = [_p("P1", "a@x.cl", "2025-01-01", [_it("Zapato", 2, 1), _it("Abrigo", 2, 1)])]
    _ok(ranking_productos(pedidos), [("Abrigo", 2), ("Zapato", 2)], "R5", "Abrigo y Zapato empatan")


# R6 -----------------------------------------------------------------------
PEDIDOS_R6 = [
    _p("P1", "a@x.cl", "2024-03-10", [_it("A", 1, 1000)]),
    _p("P2", "a@x.cl", "2025-03-01", [_it("A", 2, 1000)]),
    _p("P3", "a@x.cl", "2025-03-31", [_it("A", 1, 500)]),
    _p("P4", "a@x.cl", "2025-12-24", [_it("A", 3, 100)]),
]


def test_c16_R6_mismo_mes_distinto_anio():
    _ok(ventas_por_mes(PEDIDOS_R6[:2]), {"2024-03": 1000, "2025-03": 2000}, "R6", "marzo 2024 y marzo 2025")


def test_c17_R6_completo():
    _ok(ventas_por_mes(PEDIDOS_R6), {"2024-03": 1000, "2025-03": 2500, "2025-12": 300}, "R6", "cuatro pedidos")


def test_c18_R6_llave_formato():
    _ok(sorted(ventas_por_mes(PEDIDOS_R6)), ["2024-03", "2025-03", "2025-12"], "R6", "llaves 'AAAA-MM'")


# R7 -----------------------------------------------------------------------
def test_c19_R7_dos_llamadas_sin_historial():
    agregar_a_historial({"id": "P1"})
    _ok(agregar_a_historial({"id": "P2"}), ["P2"], "R7", "segunda llamada sin historial")


def test_c20_R7_con_historial():
    h = ["P0"]
    r = agregar_a_historial({"id": "P9"}, h)
    _ok((r, agregar_a_historial({"id": "P7"})), (["P0", "P9"], ["P7"]), "R7",
        "con historial ['P0'] y luego otra llamada sin historial")


def test_c21_R7_independientes():
    a = agregar_a_historial({"id": "A"})
    b = agregar_a_historial({"id": "B"})
    _ok((a, b, a is b), (["A"], ["B"], False), "R7", "dos llamadas deben retornar listas distintas")
