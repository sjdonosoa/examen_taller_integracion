# Examen Taller de Integración · Pruebas de práctica

Pruebas de práctica para el **Examen de Proyecto de Título – Taller de Integración (UC, 2026-02)**, con el mismo formato que CoderByte: enunciado, archivo a completar o arreglar, tests ocultos-pero-visibles y un `main.py` que te muestra el **resumen por subdesafío y tu NOTA**, igual que el botón *Run Code* de la plataforma.

Todo se resuelve en **Python 3.11** y se puede hacer completo desde **VS Code**.

| Parte | Carpeta | Qué hay | Duración en el examen |
|---|---|---|---|
| 1 · Selección múltiple | `parte1_seleccion_multiple/` | 2 pruebas de 18 preguntas (IS, GPTI, GOTI) con corrector en la terminal | 30 min |
| 2 · Arreglar código | `parte2_arreglar_codigo/` | 3 pruebas con errores de lógica | 60 min |
| 3 · Implementación | `parte3_desarrollo/` | 5 pruebas de pipeline de datos y algoritmos | 60 min |

En [`GUIA_DEL_EXAMEN.md`](GUIA_DEL_EXAMEN.md) está el resumen de qué trae cada parte según los exámenes liberados.

---

## Instalación (una vez)

1. Instala **Python 3.11** ([python.org](https://www.python.org/downloads/release/python-3119/)). Otras versiones 3.x también funcionan, pero el examen usa 3.11.
2. Clona el repo y ábrelo en VS Code:
   ```bash
   git clone https://github.com/sjdonosoa/examen_taller_integracion.git
   cd examen_taller_integracion
   code .
   ```
3. Instala pytest (lo usa `main.py` para correr los casos):
   ```bash
   python -m pip install -r requirements.txt
   ```
4. En VS Code instala la extensión **Python** (te la sugiere sola) y elige el intérprete 3.11 (`Ctrl/Cmd+Shift+P` → *Python: Select Interpreter*).

## Cómo practicar

1. Elige una prueba, por ejemplo `parte3_desarrollo/prueba_01_bicicletas/`.
2. Lee `ENUNCIADO.md` (en VS Code: clic derecho → *Open Preview*).
3. Pon un cronómetro de **60 minutos**.
4. Completa `solucion.py` (Parte 3) o corrige `desafio.py` (Parte 2).
5. Para ver tu nota, con el archivo abierto aprieta **F5** (configuración "Correr los casos de esta prueba"), o en la terminal:
   ```bash
   cd parte3_desarrollo/prueba_01_bicicletas
   python main.py
   ```
   Verás algo así:
   ```
   Caso 01 [A1] OK
   Caso 05 [A3] FALLA -> A.3: la hora 9 deberia ser 'PUNTA_AM' y quedo 'VALLE'
   ...
   ===== RESUMEN POR SUBDESAFIO =====
   OK A1    A.1 Carga de viajes          2/2
      A3    A.3 Limpieza y franja         3/4
   CASOS APROBADOS: 11/20
   NOTA ACTUAL: 4.3
   ```
6. Recién al terminar, compara con `soluciones/`.

Para la Parte 1:
```bash
cd parte1_seleccion_multiple
python quiz.py 1            # rinde la prueba 1
python quiz.py 2 --mezclar  # orden aleatorio
python quiz.py 1 --pauta    # ver todas las respuestas explicadas
```

## Las pruebas

### Parte 3 · Implementación (la más importante)

| Prueba | Tema | Lo que entrena | Casos | Dificultad |
|---|---|---|---|---|
| `prueba_01_bicicletas` | 2 CSV, viajes y estaciones | cargar, limpiar, franja horaria, dict por estación, resumen por comuna, ranking con desempate | 20 | ⭐⭐ |
| `prueba_02_resenas` | JSON anidado + CSV léxico | filtros, fechas ISO, `weekday()`, tokenizar texto, quitar tildes, negaciones, ranking | 16 | ⭐⭐⭐ |
| `prueba_03_retail` | CSV con `;` + 2 JSON | aplanar JSON, devoluciones, `set` de boletas, venta por m², alertas vs promedio nacional, **exportar CSV** | 24 | ⭐⭐⭐⭐ |
| `prueba_04_algoritmos` | sin archivos | strings, conteo, compresión, islas en matriz (BFS), anagramas, RUT | 20 | ⭐⭐–⭐⭐⭐ |
| `prueba_05_avance_curricular` | JSON + CSV de ramos | notas con coma, promedio ponderado, prerrequisitos, orden con 3 claves, cadena transitiva | 20 | ⭐⭐⭐⭐ |

### Parte 2 · Arreglar código

| Prueba | Tema | Errores | Casos | Dificultad |
|---|---|---|---|---|
| `prueba_01_estacionamiento` | cobro por bloques, medianoche, tope, convenios | 7 | 21 | ⭐⭐ |
| `prueba_02_robot_aspiradora` | grilla: vecinos, bordes, prioridad, Manhattan, empates | 5 | 15 | ⭐⭐⭐ |
| `prueba_03_pedidos` | dicts y listas con trampas clásicas de Python | 7 | 21 | ⭐⭐⭐ |

Cada error arreglado suma sus casos **por su cuenta** (está verificado), así que puedes ir de a uno.

## Reglas para practicar como en el examen

- **Sin IA.** Este repo trae `.vscode/settings.json` con Copilot y las sugerencias automáticas apagadas. En el examen usar IA es 1,0 directo.
- Solo apuntes de **sintaxis de Python**.
- No modifiques `main.py` ni `main_test.py` (igual que en CoderByte).
- Si te queda una función a medias, deja `pass`: un error de sintaxis anula todos los casos.

## Estructura de cada prueba

```
prueba_XX_nombre/
├── ENUNCIADO.md          # el enunciado (léelo entero primero)
├── solucion.py           # Parte 3: lo que completas   |  desafio.py: Parte 2, lo que arreglas
├── archivos/             # datos CSV / JSON (si la prueba los usa)
├── main.py               # corre los casos y muestra tu NOTA
├── main_test.py          # los casos (puedes leerlos: ahí están los datos de control)
└── soluciones/           # ⚠️ spoilers: solución resuelta (y ERRORES.md en la Parte 2)
```

## Si algo falla

- `No module named pytest` → `python -m pip install pytest`.
- `FileNotFoundError` → corre `main.py` de la carpeta de la prueba (F5 con un archivo de esa prueba abierto, o `cd` a la carpeta).
- Windows: usa `py -3.11 main.py` si `python` apunta a otra versión.

---

`_herramientas/` contiene los generadores de datos y los verificadores (cada prueba da 1,0 con el código inicial y 7,0 con la solución). No necesitas tocarla.
