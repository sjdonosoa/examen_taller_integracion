# Prueba 02 · Análisis de reseñas de restaurantes

**Parte 3 – Implementación en código · 60 minutos · Dificultad: ⭐⭐⭐ (media)**
Formato calcado del Examen 2025-02 ("Análisis de sentimientos": JSON + CSV, tres archivos `desafio_N.py`).

---

## Contexto

Una app de reseñas de restaurantes necesita entender la percepción de sus usuarios. Te entregan un archivo **JSON** con 240 reseñas (texto, autor, fecha, likes y respuestas anidadas) y un **CSV** con un léxico de palabras clasificadas por polaridad.

*Para todos los desafíos puedes crear tus propias funciones auxiliares y copiar código entre archivos, pero debes mantener el nombre y los parámetros de las funciones pedidas.*

## Archivos

- `archivos/resenas.json` → `{"meta": {...}, "data": [reseña, ...]}`. Cada reseña trae `id`, `texto`, `local_id`, `creado` (ISO `AAAA-MM-DDTHH:MM:SSZ`), `autor` (dict con `usuario`, `seguidores`, `verificado`) e `interacciones` (dict con lista `likes` **desordenada**, lista `respuestas` de dicts y `reportes`).
- `archivos/lexico.csv` → `palabra,polaridad,intensidad` (palabras en minúscula y **sin tildes**). Ya tienes `cargar_lexico()` implementada en `cargar_csv.py`.

## Desafío 1: Extracción y preparación (`desafio_1.py`, casos 1 a 5)

1. `autores_influyentes` – reseñas cuyo autor tiene **más de** 1000 seguidores (casos 1 y 2).
2. `con_interacciones` – reseñas con **al menos** `minimo` interacciones (likes + respuestas; los reportes no cuentan) (casos 3 y 4).
3. `ultimas_interacciones` – fecha del like y de la respuesta **más recientes** de cada reseña, o `None` (caso 5).

Formato de 1 y 2: `[{"id": "R1001", "texto": "...", "autor": "user_020"}]`, en el mismo orden del JSON.

## Desafío 2: Análisis temporal (`desafio_2.py`, casos 6 a 9)

1. `distribucion_por_hora` → `{"distribucion": {"9": 3, "15": 1, ...}}` (casos 6 y 7).
2. `distribucion_por_dia` → las 7 llaves `"Lunes"` … `"Domingo"` (con tilde), incluso si valen 0 (caso 8).
3. `rango_temporal` → `{"rango": {"inicio": ..., "fin": ...}}` (caso 9).

## Desafío 3: Análisis de sentimiento (`desafio_3.py`, casos 10 a 16)

**Regla de tokenización:** minúscula → quitar tildes → `re.findall(r"[a-zñ]+", texto)`.
**Puntaje:** suma de intensidades del léxico (+ positivo, − negativo), contando repeticiones.

1. `clasificacion` → positivo / negativo / neutro (caso 10).
2. `puntaje_sentimiento` → puntaje por reseña + resumen de totales (casos 11 y 12).
3. `palabras_frecuentes` → top N palabras del léxico, frecuencia desc y luego alfabético (caso 13).
4. `puntaje_con_negacion` → si "no" o "nada" está en alguna de las **2 palabras anteriores**, la palabra suma invertida (casos 14 y 15).
5. `ranking_locales` → promedio de puntaje por local (mínimo de reseñas), desc y luego `local_id` (caso 16).

Ejemplo del enunciado: *"Terrible experiencia, el producto llegó malo y nadie responde"* → con este léxico, solo `malo` (−2) cuenta: **negativo, −2**.

## Nota

`nota = 1.0 + (casos aprobados / 16) * 6.0` · Corre `python main.py`.

> 💡 Los tests usan **otros archivos JSON** además del real: abre siempre el archivo con el parámetro que recibe la función, nunca con una ruta fija.
