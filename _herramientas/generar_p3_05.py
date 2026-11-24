"""Genera los datos de parte3_desarrollo/prueba_05_avance_curricular (deterministico)."""
import csv
import json
import os
import random
import sys

DESTINO = sys.argv[1]
os.makedirs(DESTINO, exist_ok=True)
rnd = random.Random(2162)

RAMOS = [
    ("IIC1103", "Introducción a la Programación", 10, []),
    ("MAT1610", "Cálculo I", 10, []),
    ("MAT1203", "Álgebra Lineal", 10, []),
    ("FIS1503", "Física I", 10, []),
    ("MAT1620", "Cálculo II", 10, ["MAT1610"]),
    ("IIC2233", "Programación Avanzada", 10, ["IIC1103"]),
    ("IIC1253", "Matemáticas Discretas", 10, ["IIC1103"]),
    ("EYP1113", "Probabilidad y Estadística", 10, ["MAT1620"]),
    ("IIC2133", "Estructuras de Datos y Algoritmos", 10, ["IIC2233", "IIC1253"]),
    ("IIC2343", "Arquitectura de Computadores", 10, ["IIC1103"]),
    ("IIC2413", "Bases de Datos", 10, ["IIC2233"]),
    ("IIC2143", "Ingeniería de Software", 10, ["IIC2233"]),
    ("ICS1513", "Introducción a la Economía", 10, []),
    ("ICS2523", "Microeconomía", 10, ["ICS1513", "MAT1620"]),
    ("IIC3113", "Gestión de Proyectos TI", 10, ["IIC2143"]),
    ("IIC3703", "Gestión de Operaciones TI", 10, ["IIC2413"]),
    ("IIC2513", "Tecnologías y Aplicaciones Web", 10, ["IIC2413", "IIC2143"]),
    ("IIC3143", "Desarrollo de Software", 10, ["IIC2143", "IIC2513"]),
    ("IIC3752", "Tecnologías para Inteligencia de Negocios", 10, ["IIC2413", "EYP1113"]),
    ("IIC3800", "Taller de Integración", 15, ["IIC3143", "IIC3113", "IIC3703"]),
    ("FIL188", "Ética para Ingenieros", 5, []),
]
with open(os.path.join(DESTINO, "ramos.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["sigla", "nombre", "creditos", "prerrequisitos"])
    for s, n, c, pre in RAMOS:
        w.writerow([s, n, c, "|".join(pre)])

info = {s: pre for s, _, _, pre in RAMOS}
orden = [s for s, *_ in RAMOS]
SEMESTRES = ["2022-1", "2022-2", "2023-1", "2023-2", "2024-1", "2024-2", "2025-1", "2025-2"]
NOMBRES = ["Sofía", "Matías", "Valentina", "Benjamín", "Isidora", "Vicente", "Florencia", "Agustín", "Josefa",
           "Tomás", "Catalina", "Joaquín", "Antonia", "Martín", "Emilia", "Lucas", "Trinidad", "Diego", "Javiera",
           "Cristóbal"]
APELLIDOS = ["González", "Muñoz", "Rojas", "Díaz", "Pérez", "Soto", "Contreras", "Silva", "Martínez", "Sepúlveda",
             "Morales", "Rodríguez", "López", "Fuentes", "Hernández"]
CARRERAS = ["Ingeniería Civil", "Ingeniería Civil", "Licenciatura en Ingeniería", "College"]


def nota_str():
    if rnd.random() < 0.04:
        return "NP"
    n = round(min(7.0, max(1.0, rnd.gauss(4.9, 1.1))), 1)
    return f"{n:.1f}".replace(".", ",")


alumnos = []
for i in range(80):
    numero = f"{21600000 + rnd.randint(1, 99999):08d}"[:-1] + rnd.choice("0123456789J")
    aprobados = set()
    historial = []
    nivel = rnd.randint(2, 8)
    for sem in SEMESTRES[:nivel]:
        posibles = [s for s in orden if s not in aprobados and all(p in aprobados for p in info[s])]
        rnd.shuffle(posibles)
        for s in posibles[:rnd.randint(3, 5)]:
            nota = nota_str()
            historial.append({"sigla": s, "semestre": sem, "nota": nota})
            if nota != "NP" and float(nota.replace(",", ".")) >= 4.0:
                aprobados.add(s)
    alumnos.append({
        "numero": numero,
        "nombre": f"{rnd.choice(NOMBRES)} {rnd.choice(APELLIDOS)}",
        "carrera": rnd.choice(CARRERAS),
        "historial": historial,
    })

with open(os.path.join(DESTINO, "alumnos.json"), "w", encoding="utf-8") as f:
    json.dump({"universidad": "UC", "alumnos": alumnos}, f, ensure_ascii=False, indent=2)
print("ok")
