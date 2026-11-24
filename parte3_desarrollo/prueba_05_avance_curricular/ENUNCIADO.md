# Prueba 05 · Avance curricular y toma de ramos

**Parte 3 – Implementación en código · 60 minutos · Dificultad: ⭐⭐⭐⭐ (alta)**

---

## Contexto

La Dirección de Docencia quiere una herramienta que, a partir del historial académico, diga **qué ramos tiene aprobados cada alumno, su PPA, qué puede inscribir el próximo semestre y cuál es la cadena completa de prerrequisitos** de un ramo. Completa las 7 funciones de `solucion.py`.

## Datos (`archivos/`)

- `ramos.csv` → `sigla, nombre, creditos, prerrequisitos`. Los prerrequisitos vienen como **siglas separadas por `|`** o como string **vacío**.
- `alumnos.json` → `{"alumnos": [{"numero", "nombre", "carrera", "historial": [{"sigla", "semestre", "nota"}]}]}`.
  Las notas vienen como **string con coma decimal** (`"4,8"`) y algunas son `"NP"` (= 1.0). Un ramo puede aparecer varias veces (reprobado y repetido).

**Regla UC:** aprobado si nota ≥ 4.0.

## Funciones

| | Función | Casos | Qué practica |
|---|---|---|---|
| A.1 | `cargar_ramos` | 1–2 | `split("|")` y el caso del string vacío |
| A.2 | `cargar_alumnos` | 3–5 | JSON anidado, `replace(",", ".")`, valores especiales |
| A.3 | `estado_alumno` | 6–9 | `set` de aprobados, contar intentos, promedio ponderado, ignorar siglas inexistentes |
| B.1 | `puede_tomar` | 10–12 | `all()` sobre prerrequisitos |
| B.2 | `ramos_disponibles` | 13–14 | reutilizar B.1 |
| B.3 | `ranking_carrera` | 15–17 | ordenar con **3 claves** (ppa desc, créditos desc, número asc) |
| C.1 | `cadena_prerrequisitos` | 18–20 | recorrido transitivo (pila/cola o recursión) sin repetidos |

`nota = 1.0 + (casos aprobados / 20) * 6.0` · Corre `python main.py`.

> 💡 Cuidado con `round(x, 2)` en promedios: el test usa exactamente `round(sum(nota * creditos) / sum(creditos), 2)`.
