"""Genera los datos de parte3_desarrollo/prueba_01_bicicletas (deterministico)."""
import csv
import os
import random
import sys
from datetime import date, timedelta

DESTINO = sys.argv[1]
os.makedirs(DESTINO, exist_ok=True)
rnd = random.Random(2026)

COMUNAS = {
    "Santiago": ["Plaza de Armas", "Bellas Artes", "Santa Lucía", "Barrio Lastarria", "La Moneda",
                 "Parque Almagro", "Santa Isabel", "Barrio Brasil", "Estación Central Norte", "Mapocho"],
    "Providencia": ["Pedro de Valdivia", "Manuel Montt", "Los Leones", "Salvador", "Baquedano",
                    "Inés de Suárez", "Tobalaba", "Parque Bustamante"],
    "Las Condes": ["El Golf", "Escuela Militar", "Apoquindo", "Manquehue", "Alcántara",
                   "Parque Araucano", "Rotonda Atenas"],
    "Ñuñoa": ["Plaza Ñuñoa", "Irarrázaval", "Villa Frei", "Estadio Nacional", "Chile España",
              "Suecia Sur"],
    "Vitacura": ["Parque Bicentenario", "Alonso de Córdova", "Nueva Costanera", "Lo Curro"],
    "La Reina": ["Príncipe de Gales", "Plaza Egaña", "Parque Mahuida"],
    "Recoleta": ["Patronato", "Cementerio General", "Vega Central"],
    "San Miguel": ["Gran Avenida", "El Llano", "Lo Vial"],
}

estaciones = []
n = 101
for comuna, nombres in COMUNAS.items():
    for nombre in nombres:
        estaciones.append({
            "id_estacion": f"E{n}",
            "nombre": nombre,
            "comuna": comuna,
            "capacidad": rnd.choice([0, 12, 15, 15, 18, 20, 20, 24, 30]) if nombre != "Lo Curro" else 0,
        })
        n += 1

# Estaciones que existen en los viajes pero NO en el catalogo (estaciones piloto nuevas)
fantasmas = ["E901", "E902", "E903"]
ids = [e["id_estacion"] for e in estaciones]
pesos = [rnd.uniform(0.3, 3.0) for _ in ids]

with open(os.path.join(DESTINO, "estaciones.csv"), "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["id_estacion", "nombre", "comuna", "capacidad"])
    for e in estaciones:
        # algunos nombres vienen con espacios extra
        nombre = e["nombre"] if rnd.random() > 0.1 else "  " + e["nombre"] + " "
        w.writerow([e["id_estacion"], nombre, e["comuna"], e["capacidad"]])


def hora_aleatoria():
    r = rnd.random()
    if r < 0.05:
        return rnd.randint(0, 5)
    if r < 0.35:
        return rnd.randint(6, 9)
    if r < 0.65:
        return rnd.randint(10, 16)
    if r < 0.92:
        return rnd.randint(17, 20)
    return rnd.randint(21, 23)


inicio = date(2025, 3, 1)
with open(os.path.join(DESTINO, "viajes.csv"), "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["id_viaje", "fecha", "hora_inicio", "id_origen", "id_destino",
                "duracion_seg", "distancia_m", "tipo_usuario"])
    for i in range(1, 7201):
        origen = rnd.choices(ids, pesos)[0] if rnd.random() > 0.01 else rnd.choice(fantasmas)
        destino = rnd.choices(ids, pesos)[0] if rnd.random() > 0.01 else rnd.choice(fantasmas)
        dist = rnd.randint(300, 9000)
        dur = int(dist / rnd.uniform(2.5, 5.5)) + rnd.randint(30, 200)
        tipo = rnd.choice(["SUSCRITO"] * 7 + ["CASUAL"] * 3)
        if rnd.random() < 0.08:
            tipo = rnd.choice([" casual", "Suscrito ", "suscrito", "CASUAL "])
        fecha = inicio + timedelta(days=rnd.randint(0, 91))
        w.writerow([f"V{i:05d}", fecha.isoformat(), hora_aleatoria(), origen, destino, dur, dist, tipo])
print("ok")
