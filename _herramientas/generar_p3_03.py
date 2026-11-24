"""Genera los datos de parte3_desarrollo/prueba_03_retail (deterministico)."""
import csv
import json
import os
import random
import sys
from datetime import date, timedelta

DESTINO = sys.argv[1]
os.makedirs(DESTINO, exist_ok=True)
rnd = random.Random(3913)

CATEGORIAS = {
    "Lácteos": ["Leche Entera 1L", "Yogurt Frutilla", "Queso Gauda 250g", "Mantequilla 250g", "Leche Descremada 1L"],
    "Panadería": ["Marraqueta kg", "Pan de Molde", "Hallulla kg", "Queque Marmoleado", "Tostadas"],
    "Bebidas": ["Bebida Cola 3L", "Agua Mineral 1.5L", "Jugo Naranja 1L", "Bebida Light 1.5L", "Néctar Durazno"],
    "Limpieza": ["Detergente 3L", "Lavalozas 750ml", "Cloro 2L", "Esponja x3", "Papel Higiénico x12"],
    "Despensa": ["Arroz 1kg", "Fideos Spaghetti", "Aceite Maravilla 1L", "Azúcar 1kg", "Harina 1kg", "Atún Lata"],
    "Frutas y Verduras": ["Palta Hass kg", "Tomate kg", "Plátano kg", "Manzana kg", "Lechuga"],
}
productos = {"categorias": []}
skus = []
precio = {}
n = 1
for cat, nombres in CATEGORIAS.items():
    lista = []
    for nom in nombres:
        sku = f"SKU{n:04d}"
        p = rnd.choice([590, 790, 990, 1290, 1490, 1990, 2490, 2990, 3990, 4990, 6990])
        costo = int(p * rnd.uniform(0.5, 0.8))
        lista.append({"sku": sku, "nombre": nom, "costo": costo})
        skus.append(sku)
        precio[sku] = p
        n += 1
    productos["categorias"].append({"nombre": cat, "productos": lista})
with open(os.path.join(DESTINO, "productos.json"), "w", encoding="utf-8") as f:
    json.dump(productos, f, ensure_ascii=False, indent=2)

TIENDAS = [
    ("T01", "Express Providencia", "Metropolitana", 180), ("T02", "Express Ñuñoa", "Metropolitana", 150),
    ("T03", "Hiper Maipú", "Metropolitana", 1200), ("T04", "Hiper La Florida", "Metropolitana", 1100),
    ("T05", "Mercado Viña", "Valparaíso", 420), ("T06", "Mercado Valparaíso", "Valparaíso", 380),
    ("T07", "Hiper Concepción", "Biobío", 950), ("T08", "Express Talcahuano", "Biobío", 160),
    ("T09", "Mercado Temuco", "La Araucanía", 400), ("T10", "Mercado La Serena", "Coquimbo", 450),
    ("T11", "Express Antofagasta", "Antofagasta", 200), ("T12", "Mercado Rancagua", "O'Higgins", 0),
]
with open(os.path.join(DESTINO, "tiendas.json"), "w", encoding="utf-8") as f:
    json.dump([{"id": t, "nombre": nom, "region": reg, "metros2": m2} for t, nom, reg, m2 in TIENDAS],
              f, ensure_ascii=False, indent=2)

ids_t = [t[0] for t in TIENDAS] + ["T99"]
pesos_t = [3, 2.5, 6, 5.5, 3, 2.5, 4.5, 1.5, 2.5, 3, 1.8, 2, 0.5]
tasa_dev = {t: rnd.uniform(0.01, 0.07) for t in ids_t}
filas = []
boleta = 1
inicio = date(2025, 1, 1)
while len(filas) < 9000:
    t = rnd.choices(ids_t, pesos_t)[0]
    dia = inicio + timedelta(days=int(rnd.triangular(0, 364, 330)))
    for _ in range(rnd.randint(1, 4)):
        sku = rnd.choice(skus) if rnd.random() > 0.01 else "SKU9999"
        cant = rnd.choice([1, 1, 1, 2, 2, 3, 4, 6])
        if rnd.random() < tasa_dev[t]:
            cant = -cant
        p = precio.get(sku, 1500)
        filas.append([f"B{boleta:06d}", dia.strftime("%d/%m/%Y"), t, sku, cant, p])
    boleta += 1

with open(os.path.join(DESTINO, "ventas.csv"), "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f, delimiter=";")
    w.writerow(["id_boleta", "fecha", "id_tienda", "sku", "cantidad", "precio_unitario"])
    w.writerows(filas)
print("ok", len(filas))
