# Programacion Tradicional
def ingresar_temperaturas():
    """Función para ingresar las temperaturas diarias."""
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    """Función para calcular el promedio de una lista de temperaturas."""
    return sum(temperaturas) / len(temperaturas)

def main():
    """Función principal del programa."""
    print("Programa para calcular el promedio semanal del clima (Programación Tradicional)")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}°C")





    # Programacion orientada a objetos (POO)
    class ClimaSemanal:
        def __init__(self):
            """Constructor de la clase ClimaSemanal."""
            self.temperaturas = []

        def ingresar_temperaturas(self):
            """Método para ingresar las temperaturas diarias."""
            for i in range(7):
                temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
                self.temperaturas.append(temp)

        def calcular_promedio(self):
            """Método para calcular el promedio de las temperaturas."""
            return sum(self.temperaturas) / len(self.temperaturas)

        def mostrar_promedio(self):
            """Método para mostrar el promedio de las temperaturas."""
            promedio = self.calcular_promedio()
            print(f"El promedio semanal de las temperaturas es: {promedio:.2f}°C")


    def main():
        """Función principal del programa."""
        print("Programa para calcular el promedio semanal del clima (POO)")
        clima_semanal = ClimaSemanal()
        clima_semanal.ingresar_temperaturas()
        clima_semanal.mostrar_promedio()




























