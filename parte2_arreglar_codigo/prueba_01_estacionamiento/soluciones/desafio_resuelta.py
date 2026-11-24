# desafio.py
# Parte 2: arreglar codigo - Cobro de un estacionamiento.
#
# Este programa calcula cuanto paga un vehiculo al salir del estacionamiento,
# pero tiene SIETE errores de logica (no de sintaxis): cobra mal. Cada funcion
# tiene un docstring que describe lo que DEBERIA hacer. El error de cada
# funcion esta en su codigo, no en su docstring: compara una cosa con la otra.
#
# Puedes reescribir lo que quieras, pero no cambies el nombre ni los
# parametros de las funciones: los tests llaman a cada una por separado.
# Usa solo Python base.

TARIFAS = {"auto": 700, "moto": 400, "camioneta": 900}
TOPE_DIARIO = 12000
MINUTOS_GRATIS = 15
CONVENIOS = {"UC": 0.20, "CLINICA": 0.50}


def a_minutos(hhmm):
    """Convierte una hora (24 h) en minutos desde la medianoche.

    Algunas barreras registran la hora con segundos ('HH:MM:SS') y otras sin
    ellos ('HH:MM'); los segundos se ignoran. Puede traer espacios alrededor.
    '00:00' -> 0, '01:30' -> 90, '23:59:59' -> 1439, ' 07:05 ' -> 425.
    """
    partes = hhmm.strip().split(":")
    return int(partes[0]) * 60 + int(partes[1])


def duracion(entrada, salida):
    """Minutos que el vehiculo estuvo estacionado.

    entrada y salida vienen como 'HH:MM'. El estacionamiento atiende de noche:
    si la hora de salida es MENOR que la de entrada, el vehiculo paso la
    medianoche, y hay que sumarle 24 horas (1440 minutos) a la salida.
    Nunca se queda mas de 24 horas.

    duracion('10:00', '11:15') -> 75
    duracion('23:30', '00:10') -> 40
    """
    e, s = a_minutos(entrada), a_minutos(salida)
    if s < e:
        s += 1440
    return s - e


def es_gratis(minutos):
    """Los primeros 15 minutos son gratis: una estadia de 15 minutos o menos
    no paga nada (15 exactos todavia es gratis; 16 ya paga).
    """
    return minutos <= MINUTOS_GRATIS


def bloques(minutos):
    """Cantidad de bloques de 30 minutos a cobrar. Se cobra cada bloque
    INICIADO, contando desde el minuto 0 (los 15 gratis no se descuentan si la
    estadia supera los 15 minutos).

    bloques(16) -> 1, bloques(30) -> 1, bloques(31) -> 2, bloques(90) -> 3
    """
    return (minutos + 29) // 30


def tarifa(tipo):
    """Valor de un bloque segun el tipo de vehiculo.

    El tipo puede venir con mayusculas o espacios (' Moto ' es 'moto').
    Si el tipo no esta en TARIFAS (por ejemplo 'bus'), se cobra la tarifa MAS
    ALTA de la tabla, para no perder plata.
    """
    t = tipo.strip().lower()
    return TARIFAS.get(t, max(TARIFAS.values()))


def aplicar_tope(monto):
    """Ninguna estadia paga mas que el TOPE_DIARIO. Si el monto lo supera, se
    cobra el tope; si no, el monto tal cual.
    """
    return min(monto, TOPE_DIARIO)


def aplicar_convenio(monto, convenio):
    """Descuento por convenio, que se aplica DESPUES del tope.

    convenio puede ser None, o un nombre en CONVENIOS (sin importar
    mayusculas: 'uc' es 'UC'). Un convenio desconocido no hace descuento.
    El resultado se redondea HACIA ABAJO a la decena (no existen monedas de 1
    ni de 5 pesos): 1568 -> 1560, 1599 -> 1590, 1600 -> 1600.
    Retorna un int.
    """
    if convenio is None:
        return monto
    desc = CONVENIOS.get(convenio.upper(), 0)
    con_desc = monto * (1 - desc)
    return int(con_desc) // 10 * 10


def solution(entrada, salida, tipo, convenio=None):
    """Monto final a pagar (int).

    1. Calcula la duracion. 2. Si es gratis, paga 0. 3. Si no, bloques * tarifa.
    4. Aplica el tope. 5. Aplica el convenio.
    """
    m = duracion(entrada, salida)
    if es_gratis(m):
        return 0
    monto = bloques(m) * tarifa(tipo)
    monto = aplicar_tope(monto)
    return aplicar_convenio(monto, convenio)
