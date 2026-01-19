# Clase base Vehiculo que demuestra encapsulación y define la estructura base para todos los vehículos del sistema.

class Vehiculo:
    def __init__(self, marca, modelo, año):
        """Constructor de la clase base Vehiculo."""
        self._marca = marca
        self._modelo = modelo
        self.__año = año
        self.__kilometraje = 0

    # GETTERS Y SETTERS
    def get_marca(self):
        return self._marca

    def set_marca(self, nueva_marca):
        self._marca = nueva_marca

    def get_modelo(self):
        return self._modelo

    def get_año(self):
        return self.__año

    def get_kilometraje(self):
        return self.__kilometraje

    def set_kilometraje(self, km):
        if km >= self.__kilometraje:
            self.__kilometraje = km
        else:
            print("Error: El kilometraje no puede disminuir")

    # MÉTODOS COMUNES
    def obtener_informacion(self):
        return f"{self._marca} {self._modelo} ({self.__año})"

    def viajar(self, distancia):
        if distancia > 0:
            self.__kilometraje += distancia
            return f"Viaje de {distancia} km realizado. Kilometraje total: {self.__kilometraje} km"
        return "Distancia debe ser positiva"

    def estado_vehiculo(self):
        if self.__kilometraje == 0:
            return "Nuevo"
        elif self.__kilometraje < 50000:
            return "Poco uso"
        elif self.__kilometraje < 150000:
            return "Uso moderado"
        else:
            return "Alto kilometraje"
