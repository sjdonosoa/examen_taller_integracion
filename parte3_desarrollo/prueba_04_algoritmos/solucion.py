# solucion.py
# Prueba 04 (Parte 3 - Desarrollo) - Algoritmos con strings, listas, dicts y matrices.
#
# Son 6 funciones INDEPENDIENTES (no hay archivos). 20 casos en total.
# nota = 1.0 + (casos aprobados / 20) * 6.0
#
# Este tipo de ejercicio aparece en los desafios "cortos" de CoderByte
# (palindromos, frecuencias) y en la logica de los problemas de grilla
# (Buscaminas, Dron de la batalla naval). Lee los ejemplos con calma: ahi
# estan los bordes que prueban los tests.
# Usa solo Python base.


def recortar_sufijos(s):
    """Caso 1 a 3. Recorte de sufijos palindromos.

    Repite este algoritmo sobre el string s:
      1. Entre todos los SUFIJOS de s (subcadenas que terminan en la ultima
         letra), busca el palindromo mas largo.
      2. Si ese sufijo tiene al menos 2 caracteres, eliminalo del FINAL de s
         y vuelve al paso 1. Si no, termina y retorna el s actual.

    Un palindromo se lee igual al derecho y al reves ("ana", "abba").

    Ejemplos:
        recortar_sufijos("codedocaaa") -> ""      ("aaa" se va, luego "codedoc")
        recortar_sufijos("coderbyte")  -> "coderbyte"   (solo "e" es palindromo)
        recortar_sufijos("xyzabba")    -> "xyz"
        recortar_sufijos("")           -> ""
    """
    # TODO
    pass


def frecuentes(numeros, k):
    """Caso 4 a 6. Numeros que aparecen AL MENOS k veces.

    Retorna una lista de tuplas (numero, veces) SIN duplicados, ordenada por
    veces de mayor a menor y, si empatan, por numero de menor a mayor.
    Si ninguno cumple, retorna [].

    Ejemplos:
        frecuentes([4, 1, 2, 2, 4, 3, 4, 2], 2) -> [(2, 3), (4, 3)]
        frecuentes([5, -1, 5, -1, 7], 1)        -> [(-1, 2), (5, 2), (7, 1)]
        frecuentes([], 1)                        -> []
    """
    # TODO
    pass


def comprimir(s):
    """Caso 7 a 9. Compresion por repeticion (run-length).

    Recorre s y reemplaza cada bloque de letras IGUALES CONSECUTIVAS por la
    letra seguida de cuantas veces se repite. Si el bloque tiene una sola
    letra, va solo la letra (sin el 1). Distingue mayusculas.

    Ejemplos:
        comprimir("aaabccdddd") -> "a3bc2d4"
        comprimir("abc")        -> "abc"
        comprimir("aAAa")       -> "aA2a"
        comprimir("")           -> ""
    """
    # TODO
    pass


def islas(grilla):
    """Caso 10 a 13. Islas en un mapa.

    grilla es una matriz (lista de listas, todas las filas del mismo largo)
    con 1 = tierra y 0 = agua. Una isla es un grupo de celdas de tierra
    conectadas por los 4 lados (arriba, abajo, izquierda, derecha). La
    diagonal NO conecta.

    Retorna una tupla (cantidad_de_islas, tamano_de_la_isla_mas_grande).
    Si no hay tierra retorna (0, 0). No debe modificar la grilla recibida.

    Ejemplo:
        [[1, 1, 0, 0],
         [0, 1, 0, 1],
         [1, 0, 0, 1],
         [1, 0, 1, 1]]   -> (3, 4)
    Islas: {(0,0),(0,1),(1,1)} de 3, {(2,0),(3,0)} de 2 y
    {(1,3),(2,3),(3,3),(3,2)} de 4. Ojo: (1,1) y (2,0) estan en diagonal,
    asi que NO forman una sola isla.
    """
    # TODO
    pass


def agrupar_anagramas(palabras):
    """Caso 14 a 16. Agrupa palabras que son anagramas entre si.

    Dos palabras son anagramas si tienen exactamente las mismas letras la
    misma cantidad de veces, sin importar mayusculas ("Roma" y "amor").
    Las palabras repetidas (ignorando mayusculas) se cuentan una sola vez,
    quedandose con la primera forma que aparece.

    Retorna una lista de grupos (listas), solo con los grupos de 2 o mas
    palabras:
    - Dentro de cada grupo, las palabras conservan su forma original y se
      ordenan por palabra.lower().
    - Los grupos se ordenan por tamano de mayor a menor y, si empatan, por
      su primera palabra en minuscula.

    Ejemplo:
        ["Roma", "amor", "mora", "perro", "ramo", "AMOR", "saco", "cosa", "sol"]
        -> [["amor", "mora", "ramo", "Roma"], ["cosa", "saco"]]
    ("AMOR" es repeticion de "amor" y se ignora; "perro" y "sol" no tienen pareja.)
    """
    # TODO
    pass


def rut_valido(rut):
    """Caso 17 a 20. Valida un RUT chileno.

    El rut viene como string y puede traer puntos y guion en cualquier
    formato: "12.345.678-5", "12345678-5", "123456785". El digito
    verificador (ultimo caracter) puede ser un numero o 'K' / 'k'.

    Algoritmo (modulo 11):
      1. Quita puntos y guion. El ultimo caracter es el DV; el resto el cuerpo.
         Si el cuerpo no son solo digitos o esta vacio, retorna False.
      2. Recorre el cuerpo de DERECHA a IZQUIERDA multiplicando cada digito
         por 2, 3, 4, 5, 6, 7, y vuelve a 2, 3, ... Suma los productos.
      3. resto = 11 - (suma % 11).  Si resto == 11 el DV es '0'; si
         resto == 10 el DV es 'K'; si no, el DV es str(resto).
      4. Retorna True si el DV calculado coincide con el entregado
         (sin importar mayuscula/minuscula de la K).

    Ejemplos:
        rut_valido("12.345.678-5") -> True
        rut_valido("12345678-4")   -> False
        rut_valido("10.000.013-k") -> True
        rut_valido("abc-1")        -> False
    """
    # TODO
    pass
