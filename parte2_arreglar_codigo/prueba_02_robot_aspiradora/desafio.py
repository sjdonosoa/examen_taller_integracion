# desafio.py
# Parte 2: arreglar codigo - El cerebro de un robot aspiradora.
#
# El robot mira el mapa de la pieza y decide a que celda ir. Este programa
# tiene CINCO errores de logica (no de sintaxis): el robot elige mal su
# objetivo. Cada funcion trae un docstring con lo que DEBERIA hacer; el error
# esta en el codigo, no en el docstring.
#
# Puedes reescribir lo que quieras, pero la primera linea de
# solution(grilla, pos) (nombre y parametros) debe quedar igual.
# Usa solo Python base.

LIMPIA = 0
SUCIA = 1
OBSTACULO = 2

DIRECCIONES = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def solution(grilla, pos):
    """Decide el objetivo del robot y lo retorna como lista [fila, columna].

    grilla: matriz rectangular (lista de listas) con 0 = limpia, 1 = sucia y
            2 = obstaculo (un mueble: nunca es objetivo).
    pos:    [fila, columna] donde esta el robot (esa celda nunca esta sucia).

    1. Si alguna celda VECINA (arriba, derecha, abajo o izquierda, dentro del
       tablero) esta sucia, va a la primera segun ese orden de prioridad.
    2. Si no, va a la celda sucia mas cercana de todo el mapa (distancia
       Manhattan). Si hay empate, la de menor fila y, si sigue el empate, la
       de menor columna.
    3. Si no queda nada sucio, retorna su propia posicion.
    No modifica la grilla.
    """
    vecina = vecina_sucia(grilla, pos)
    if vecina is not None:
        return vecina
    cercana = mas_cercana(grilla, pos)
    if cercana is not None:
        return cercana
    return [pos[0], pos[1]]


# ----------------------------------------------------------- Situacion 1
def dentro(grilla, f, c):
    """True si [f, c] es una celda del tablero: fila entre 0 y alto-1 y columna
    entre 0 y ancho-1. Ojo: en Python grilla[0][-1] NO da error (es la ultima
    columna), asi que hay que revisar los bordes a mano.
    """
    return 0 <= f < len(grilla) and c < len(grilla[0])


def es_sucia(valor):
    """True solo si la celda esta sucia (valor 1). Una celda limpia (0) o un
    obstaculo (2) NO son sucias.
    """
    return valor != LIMPIA


def vecina_sucia(grilla, pos):
    """Primera celda vecina sucia en este orden de prioridad (como el reloj):
    ARRIBA, DERECHA, ABAJO, IZQUIERDA. Retorna [f, c] o None si no hay.
    Solo considera celdas dentro del tablero.
    """
    for df, dc in DIRECCIONES:
        f, c = pos[0] + df, pos[1] + dc
        if dentro(grilla, f, c) and es_sucia(grilla[f][c]):
            return [f, c]
    return None


# ----------------------------------------------------------- Situacion 2
def distancia(a, b):
    """Distancia Manhattan entre dos celdas: |fila_a - fila_b| + |col_a - col_b|.
    El robot se mueve solo en horizontal y vertical, nunca en diagonal.
    """
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))


def mas_cercana(grilla, pos):
    """Celda sucia mas cercana a pos. Empate: menor fila; si sigue, menor
    columna. Retorna [f, c] o None si no hay ninguna sucia.
    """
    mejor = None
    mejor_d = None
    for f in range(len(grilla)):
        for c in range(len(grilla[0])):
            if es_sucia(grilla[f][c]):
                d = distancia(pos, [f, c])
                if mejor is None or d <= mejor_d:
                    mejor, mejor_d = [f, c], d
    return mejor
