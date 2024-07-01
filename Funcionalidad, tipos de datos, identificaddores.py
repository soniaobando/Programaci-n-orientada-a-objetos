# Programa para calcular el área de un rectángulo
# Este programa solicita al usuario la base y la altura de un rectángulo,
# y luego calcula y muestra el área del mismo.

def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.

    Parámetros:
    base (float): La base del rectángulo.
    altura (float): La altura del rectángulo.

    Retorna:
    float: El área del rectángulo.
    """
    area = base * altura
    return area


# Solicitar la base del rectángulo al usuario
base = float(input("15: "))

# Solicitar la altura del rectángulo al usuario
altura = float(input("12: "))

# Calcular el área del rectángulo
area_rectangulo = calcular_area_rectangulo(base, altura)

# Mostrar el área del rectángulo
print(f"El área del rectángulo es: {area_rectangulo}")

# Ejemplo de uso de booleano
es_grande = area_rectangulo > 100
if es_grande:
    print("El rectángulo es grande.")
else:
    print("El rectángulo no es grande.")
