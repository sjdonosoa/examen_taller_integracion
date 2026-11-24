# Arreglar código 03 · Reportes de una tienda online

**Parte 2 – Detección y arreglo de problemas · 60 minutos · Dificultad: ⭐⭐⭐ (media)**
Procesamiento de datos con listas y diccionarios (el mismo tipo de código que escribes en la Parte 3), con 7 errores de lógica. 21 casos.

---

## Instrucciones

Abre `desafio.py`. Tiene 7 funciones y **cada una tiene exactamente un error de lógica**. No hay errores de sintaxis ni de espacios. Compara el código con el docstring de cada función, corrige y corre `python main.py`. No cambies nombres ni parámetros.

## El dominio

Un pedido es un diccionario:

```python
{"id": "P001", "email": "  Ana@Mail.com", "fecha": "2025-03-14",
 "items": [{"producto": "Polera", "cantidad": 2, "precio": 9990},
           {"producto": "Gorro", "cantidad": 1, "precio": 4990}]}
```

| Regla | Función | Qué debe hacer |
|---|---|---|
| R1 | `normalizar_email` | minúscula y sin espacios en los extremos |
| R2 | `total_pedido` | suma `cantidad × precio` de **todos** los ítems |
| R3 | `aplicar_cupon` | `DESC10` (−10 %, hacia abajo), `MENOS5000` (nunca bajo 0), otro → sin cambio |
| R4 | `clientes_frecuentes` | emails con **al menos** `minimo` pedidos, ordenados |
| R5 | `ranking_productos` | unidades desc; empate → nombre **A a Z** |
| R6 | `ventas_por_mes` | llave `"AAAA-MM"` (marzo 2024 ≠ marzo 2025) |
| R7 | `agregar_a_historial` | sin historial → lista **nueva** en cada llamada |

## Ejemplos

```python
total_pedido([{"producto": "Polera", "cantidad": 2, "precio": 9990},
              {"producto": "Gorro", "cantidad": 1, "precio": 4990}])   # 24970
aplicar_cupon(3000, "MENOS5000")                                      # 0
ranking_productos(...)  # [("Calcetines", 5), ("Bufanda", 3), ("Gorro", 3), ("Polera", 3), ...]
agregar_a_historial({"id": "P1"}); agregar_a_historial({"id": "P2"})  # la 2da retorna ["P2"]
```

## Tu nota

`nota = 1.0 + (casos aprobados / 21) * 6.0` · Cada arreglo suma 3 casos por su cuenta.

> 💡 Dos de estos errores son "trampas de Python" que no se ven a simple vista: mira la **indentación** de los `return` y los **valores por defecto** de los parámetros.
