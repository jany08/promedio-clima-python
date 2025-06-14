# Programa para calcular el promedio semanal del clima (POO)

class ClimaDia:
    def __init__(self, dia, temperatura):
        self.dia = dia
        self.temperatura = temperatura

    def get_temperatura(self):
        return self.temperatura

class SemanaClimatica:
    def __init__(self):
        self.dias = []

    def ingresar_datos(self):
        print("Ingrese la temperatura diaria (7 días):")
        for i in range(7):
            temp = float(input(f"Día {i+1}: "))
            self.dias.append(ClimaDia(i+1, temp))

    def calcular_promedio(self):
        total = sum(dia.get_temperatura() for dia in self.dias)
        return total / len(self.dias)

def main():
    semana = SemanaClimatica()
    semana.ingresar_datos()
    promedio = semana.calcular_promedio()
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
