# Pauta: los 7 errores de la tienda online

| Regla | Función | Código con error | Corrección | Por qué |
|---|---|---|---|---|
| R1 | `normalizar_email` | `email.lower()` | `email.strip().lower()` | Faltaba quitar espacios, tabs y saltos de línea. |
| R2 | `total_pedido` | `return total` **dentro** del `for` | sacar el `return` del ciclo | Retornaba después del primer ítem. Con 1 ítem "funciona", por eso cuesta verlo. |
| R3 | `aplicar_cupon` | `return total - 5000` | `return max(total - 5000, 0)` | El total no puede quedar negativo. |
| R4 | `clientes_frecuentes` | `n > minimo` | `n >= minimo` | "Al menos" es inclusivo. |
| R5 | `ranking_productos` | `key=lambda x: (x[1], x[0]), reverse=True` | `key=lambda x: (-x[1], x[0])` | `reverse=True` invierte **las dos** claves: el desempate queda Z→A. Para orden mixto se niega solo la numérica. |
| R6 | `ventas_por_mes` | `p["fecha"][5:7]` | `p["fecha"][:7]` | `[5:7]` es solo el mes ("03") y mezcla años distintos. |
| R7 | `agregar_a_historial` | `historial=[]` | `historial=None` (+ el `if historial is None`) | Un default mutable se crea **una sola vez** y se comparte entre llamadas. |

**Para el examen:** R2, R5 y R7 son errores clásicos de Python que aparecen seguido en ejercicios de "arreglar código".
