#
# Ejercicio nro 1
#
def mcd(a, b):
    """
    Esta función calcula el máximo común divisor (MCD) entre dos números utilizando el algoritmo de Euclides.
    """
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

#
# Ejercicio nro 2
#
def mcm(a, b):
    """
    Esta función calcula el mínimo común múltiplo (MCM) entre dos números utilizando el máximo común divisor (MCD) y la
    fórmula MCM(a, b) = (a * b) / MCD(a, b).
    """
    return (a * b) // mcd(a, b)


def mcm_factorizacion(a, b):
    """
    Esta función calcula el mínimo común múltiplo (MCM) entre dos números utilizando la factorización en factores primos.
    """
    # Obtenemos los factores primos de ambos números
    factores_a = factorizar(a)
    factores_b = factorizar(b)

    # Multiplicamos los factores primos comunes en la mayor potencia encontrada
    mcm = 1
    for factor, potencia in factores_a.items():
        if factor in factores_b:
            mcm *= factor ** max(potencia, factores_b[factor])
        else:
            mcm *= factor ** potencia

    # Multiplicamos los factores primos que no son comunes en ambos números
    for factor, potencia in factores_b.items():
        if factor not in factores_a:
            mcm *= factor ** potencia

    return mcm


def factorizar(n):
    """
    Esta función devuelve un diccionario con los factores primos de un número y sus respectivas potencias.
    """
    factores = {}
    i = 2
    while i <= n:
        if n % i == 0:
            if i in factores:
                factores[i] += 1
            else:
                factores[i] = 1
            n //= i
        else:
            i += 1
    return factores
	
	
	
#
# Ejercicio nro 3
#
def contar_palabras(cadena):
    """
    Esta función recibe una cadena de caracteres y devuelve un diccionario con la frecuencia de cada palabra.
    """
    # Separamos la cadena en palabras
    palabras = cadena.split()

    # Creamos un diccionario vacío
    frecuencia = {}

    # Contamos la frecuencia de cada palabra
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    return frecuencia

#
# Ejercicio nro 4
#
def palabra_mas_repetida(frecuencia):
    """
    Esta función recibe un diccionario con la frecuencia de cada palabra y devuelve una tupla con la palabra más repetida y su frecuencia.
    """
    # Inicializamos la palabra más repetida y su frecuencia
    palabra_max = None
    frecuencia_max = 0

    # Buscamos la palabra más repetida y su frecuencia
    for palabra, frec in frecuencia.items():
        if frec > frecuencia_max:
            palabra_max = palabra
            frecuencia_max = frec

    return (palabra_max, frecuencia_max)


#
# Ejercicio nro 5
#
def get_int_iter():
    while True:
        try:
            valor = int(input("Ingrese un valor entero: "))
            return valor
        except ValueError:
            print("El valor ingresado no es un entero. Intente nuevamente.")

			
def get_int_recur():
    try:
        valor = int(input("Ingrese un valor entero: "))
        return valor
    except ValueError:
        print("El valor ingresado no es un entero. Intente nuevamente.")
        return get_int_recur()

