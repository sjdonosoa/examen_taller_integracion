"""Genera los datos de parte3_desarrollo/prueba_02_resenas (deterministico)."""
import csv
import json
import os
import random
import sys
from datetime import datetime, timedelta

DESTINO = sys.argv[1]
os.makedirs(DESTINO, exist_ok=True)
rnd = random.Random(20252)

LEXICO = [
    ("excelente", "positivo", 3), ("increible", "positivo", 3), ("delicioso", "positivo", 3),
    ("buenisimo", "positivo", 3), ("bueno", "positivo", 2), ("rico", "positivo", 2),
    ("amable", "positivo", 2), ("rapido", "positivo", 1), ("limpio", "positivo", 1),
    ("recomendable", "positivo", 2), ("agradable", "positivo", 1), ("barato", "positivo", 1),
    ("pesimo", "negativo", 3), ("horrible", "negativo", 3), ("asqueroso", "negativo", 3),
    ("malo", "negativo", 2), ("lento", "negativo", 2), ("frio", "negativo", 1),
    ("caro", "negativo", 1), ("sucio", "negativo", 2), ("grosero", "negativo", 2),
    ("demora", "negativo", 1), ("decepcionante", "negativo", 2), ("ruidoso", "negativo", 1),
]

with open(os.path.join(DESTINO, "lexico.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["palabra", "polaridad", "intensidad"])
    for p, pol, i in LEXICO:
        w.writerow([p, pol, i])

# formas con tilde / mayuscula que aparecen en los textos
FORMA = {"increible": "increíble", "buenisimo": "buenísimo", "rapido": "rápido", "pesimo": "pésimo",
         "frio": "frío"}

FRASES_POS = ["El servicio fue {p} y la comida {p2}", "Todo muy {p}, volvería sin duda",
              "Atención {p}, el lugar {p2}", "{P} experiencia, súper {p2}", "Un local {p} y {p2}",
              "La cazuela estaba {p}"]
FRASES_NEG = ["La atención fue {n}, esperé mucho", "Muy {n} y además {n2}", "{N} todo, el café {n2}",
              "El plato llegó {n} y {n2}", "Nada {p}: {n}", "No fue {p}, más bien {n}",
              "Local {n}, no {p}"]
FRASES_NEU = ["Fui un martes a almorzar", "Queda cerca del metro", "Pedí el menú del día",
              "Tienen estacionamiento", "No fue {p} ni {n}"]

POS = [p for p, pol, _ in LEXICO if pol == "positivo"]
NEG = [p for p, pol, _ in LEXICO if pol == "negativo"]


def forma(palabra, mayus=False):
    s = FORMA.get(palabra, palabra) if rnd.random() < 0.7 else palabra
    return s.capitalize() if mayus else s


def frase():
    t = rnd.random()
    plantilla = rnd.choice(FRASES_POS if t < 0.45 else FRASES_NEG if t < 0.85 else FRASES_NEU)
    return plantilla.format(p=forma(rnd.choice(POS)), p2=forma(rnd.choice(POS)), P=forma(rnd.choice(POS), True),
                            n=forma(rnd.choice(NEG)), n2=forma(rnd.choice(NEG)), N=forma(rnd.choice(NEG), True))


USUARIOS = [f"user_{i:03d}" for i in range(1, 61)]
SEGUIDORES = {u: rnd.choice([rnd.randint(5, 900), rnd.randint(900, 1100), rnd.randint(1000, 25000)])
              for u in USUARIOS}
SEGUIDORES["user_007"] = 1000   # borde exacto
LOCALES = ["L01", "L02", "L03", "L04", "L05", "L06", "L07", "L08"]

base = datetime(2025, 10, 1, 0, 0)
data = []
for i in range(1, 241):
    creado = base + timedelta(minutes=rnd.randint(0, 60 * 24 * 45))
    autor = rnd.choice(USUARIOS)
    likes = sorted(creado + timedelta(minutes=rnd.randint(1, 5000)) for _ in range(rnd.choice([0, 0, 3, 10, 30, 60, 90])))
    rnd.shuffle(likes)   # NO vienen ordenados
    respuestas = [{"autor": rnd.choice(USUARIOS),
                   "fecha": (creado + timedelta(minutes=rnd.randint(1, 8000))).strftime("%Y-%m-%dT%H:%M:%SZ")}
                  for _ in range(rnd.choice([0, 0, 1, 2, 5, 12]))]
    data.append({
        "id": f"R{1000 + i}",
        "texto": " ".join(frase() for _ in range(rnd.choice([1, 1, 2]))),
        "local_id": rnd.choice(LOCALES[:-1]) if i != 240 else "L08",
        "creado": creado.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "autor": {"usuario": autor, "seguidores": SEGUIDORES[autor], "verificado": rnd.random() < 0.3},
        "interacciones": {
            "likes": [l.strftime("%Y-%m-%dT%H:%M:%SZ") for l in likes],
            "respuestas": respuestas,
            "reportes": rnd.choice([0, 0, 0, 1, 2]),
        },
    })

with open(os.path.join(DESTINO, "resenas.json"), "w", encoding="utf-8") as f:
    json.dump({"meta": {"fuente": "app de reseñas", "total": len(data)}, "data": data}, f, ensure_ascii=False, indent=2)
print("ok")
