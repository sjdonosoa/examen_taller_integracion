"""Prueba de seleccion multiple en la terminal (Parte 1 del examen).

Uso:
    python quiz.py              -> te deja elegir la prueba
    python quiz.py 1            -> rinde prueba_1.json
    python quiz.py 2 --mezclar  -> preguntas y alternativas en orden aleatorio
    python quiz.py 1 --pauta    -> muestra todas las preguntas con su respuesta

Responde con la letra (a, b, c, ...). Puedes escribir 's' para saltar una
pregunta. Al final ves tu nota y la explicacion de las que fallaste.
En el examen real tienes 30 minutos, sin apuntes y con calculadora.
"""
import json
import os
import random
import sys
import time

AQUI = os.path.dirname(os.path.abspath(__file__))
LETRAS = "abcdefgh"


def cargar(numero):
    ruta = os.path.join(AQUI, f"prueba_{numero}.json")
    with open(ruta, encoding="utf-8") as f:
        return json.load(f)


def mostrar(i, total, p, alternativas):
    print("\n" + "=" * 78)
    print(f"Pregunta {i}/{total}  [{p['ramo']}]")
    print("-" * 78)
    print(p["enunciado"])
    if p.get("codigo"):
        print()
        for linea in p["codigo"].splitlines():
            print("    " + linea)
    print()
    for letra, alt in zip(LETRAS, alternativas):
        print(f"  {letra}) {alt}")


def rendir(datos, mezclar):
    preguntas = list(datos["preguntas"])
    if mezclar:
        random.shuffle(preguntas)
    print(f"\n{datos['titulo']} - {len(preguntas)} preguntas - {datos['duracion_min']} minutos")
    input("Aprieta Enter para comenzar (el reloj parte ahora)...")
    inicio = time.time()
    correctas, fallidas = 0, []
    for i, p in enumerate(preguntas, 1):
        orden = list(range(len(p["alternativas"])))
        if mezclar:
            random.shuffle(orden)
        alternativas = [p["alternativas"][k] for k in orden]
        mostrar(i, len(preguntas), p, alternativas)
        while True:
            r = input("Tu respuesta: ").strip().lower()
            if r == "s" or (len(r) == 1 and r in LETRAS[:len(alternativas)]):
                break
            print("  Escribe una letra valida (o 's' para saltar).")
        elegida = None if r == "s" else orden[LETRAS.index(r)]
        if elegida == p["correcta"]:
            correctas += 1
        else:
            fallidas.append((i, p, elegida))
        minutos = (time.time() - inicio) / 60
        print(f"  [{minutos:.1f} de {datos['duracion_min']} min]")

    minutos = (time.time() - inicio) / 60
    nota = 1.0 + 6.0 * correctas / len(preguntas)
    print("\n" + "#" * 78)
    print(f"Correctas: {correctas}/{len(preguntas)}   Tiempo: {minutos:.1f} min   NOTA: {nota:.1f}")
    if minutos > datos["duracion_min"]:
        print("(Te pasaste del tiempo del examen: practica la velocidad.)")
    por_ramo = {}
    for p in preguntas:
        por_ramo.setdefault(p["ramo"], [0, 0])[1] += 1
    for _, p, _ in fallidas:
        por_ramo[p["ramo"]][0] += 1
    for ramo, (malas, total) in por_ramo.items():
        print(f"  {ramo:<28} {total - malas}/{total}")
    for i, p, elegida in fallidas:
        print("\n" + "-" * 78)
        print(f"Pregunta {i}: {p['enunciado'][:110]}...")
        tu = "(sin responder)" if elegida is None else p["alternativas"][elegida]
        print(f"  Tu respuesta:   {tu}")
        print(f"  Correcta:       {p['alternativas'][p['correcta']]}")
        print(f"  Por que:        {p['explicacion']}")


def pauta(datos):
    for i, p in enumerate(datos["preguntas"], 1):
        mostrar(i, len(datos["preguntas"]), p, p["alternativas"])
        print(f"\n  RESPUESTA: {LETRAS[p['correcta']]}) {p['alternativas'][p['correcta']]}")
        print(f"  {p['explicacion']}")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    numero = args[0] if args else input("¿Que prueba quieres rendir? (1 o 2): ").strip()
    datos = cargar(numero)
    if "--pauta" in sys.argv:
        pauta(datos)
    else:
        rendir(datos, "--mezclar" in sys.argv)
