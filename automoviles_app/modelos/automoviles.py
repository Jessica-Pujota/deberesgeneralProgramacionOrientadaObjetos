"""
Clase derivada Automovil que hereda de Vehiculo.
Demuestra herencia, polimorfismo y agrega funcionalidades específicas.
"""

from modelos.vehiculos import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, tipo_combustible):
        super().__init__(marca, modelo, año)
        self.__tipo_combustible = tipo_combustible
        self.__nivel_combustible = 50

    # GETTERS
    def get_tipo_combustible(self):
        return self.__tipo_combustible

    def get_nivel_combustible(self):
        return self.__nivel_combustible

    def cargar_combustible(self, cantidad):
        if 0 <= cantidad <= 100:
            self.__nivel_combustible = min(100, self.__nivel_combustible + cantidad)
            return f"Combustible cargado. Nivel actual: {self.__nivel_combustible}%"
        return "Cantidad inválida"

    # POLIMORFISMO
    def obtener_informacion(self):
        info_base = super().obtener_informacion()
        return f"{info_base} | Combustible: {self.__tipo_combustible}"

    def viajar(self, distancia):
        consumo = distancia * 0.1
        if consumo <= self.__nivel_combustible:
            self.__nivel_combustible -= consumo
            resultado_base = super().viajar(distancia)
            return f"{resultado_base} | Combustible restante: {self.__nivel_combustible:.1f}%"
        return "Combustible insuficiente para el viaje"

    # MÉTODOS ESPECÍFICOS
    def abrir_maletero(self):
        return "Maletero abierto"

    def tocar_bocina(self):
        return "¡Beep! ¡Beep!"
