"""
Archivo principal para ejecutar la aplicación.
"""

from modelos.vehiculos import Vehiculo
from modelos.automoviles import Automovil
from servicios.gestor_de_vehiculos import GestorVehiculos

def main():
    print("=== DEMOSTRACIÓN DE CONCEPTOS DE POO ===\n")

    vehiculo_base = Vehiculo("Toyota", "Generic", 2020)
    print(vehiculo_base.obtener_informacion())

    auto1 = Automovil("Toyota", "Corolla", 2022, "Gasolina")
    auto2 = Automovil("Ford", "Mustang", 2023, "Eléctrico")

    gestor = GestorVehiculos()
    gestor.agregar_vehiculo(vehiculo_base)
    gestor.agregar_vehiculo(auto1)
    gestor.agregar_vehiculo(auto2)

    print(gestor.listar_vehiculos())
    print(gestor.realizar_viaje_todos(50))
    print(gestor.obtener_estadisticas())

    print(auto1.tocar_bocina())
    print(auto1.abrir_maletero())
    print(auto1.cargar_combustible(30))

if __name__ == "__main__":
    main()
