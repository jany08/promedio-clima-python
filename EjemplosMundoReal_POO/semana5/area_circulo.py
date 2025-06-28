# Programa: Calculadora del área de un círculo
# Descripción: Este programa solicita al usuario el radio de un círculo y calcula su área.
# Utiliza distintos tipos de datos como float, string, boolean e integer.

import math  # Importamos la biblioteca para usar pi


def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    area = math.pi * radio ** 2
    return area


# Solicita el nombre del usuario (tipo string)
nombre_usuario = input("Hola, ¿cuál es tu nombre? ")

# Muestra un mensaje de saludo
print("¡Hola", nombre_usuario + "! Vamos a calcular el área de un círculo.")

# Solicita el radio (tipo float)
radio_circulo = float(input("Por favor, ingresa el radio del círculo en cm: "))

# Verifica que el radio sea positivo (tipo boolean)
radio_valido = radio_circulo > 0

if radio_valido:
    # Llama a la función para calcular el área
    area_resultado = calcular_area_circulo(radio_circulo)

    # Imprime el resultado (area_resultado es float)
    print("El área del círculo es:", round(area_resultado, 2), "cm²")
else:
    print("El radio debe ser un número positivo.")
