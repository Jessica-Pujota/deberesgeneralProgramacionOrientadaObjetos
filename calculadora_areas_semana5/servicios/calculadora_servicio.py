"""
Servicio: Calculadora de Áreas
Descripción:
Contiene la lógica del sistema, manejo del menú
y la interacción con el usuario.
"""

from modelos.figuras import Rectangulo, Circulo, Triangulo


class CalculadoraServicio:

    def mostrar_menu(self) -> int:
        print("\n--- CALCULADORA DE ÁREAS ---")
        print("1. Área del rectángulo")
        print("2. Área del círculo")
        print("3. Área del triángulo")
        print("4. Salir")

        try:
            return int(input("Seleccione una opción: "))
        except ValueError:
            return 0

    def ejecutar(self):
        while True:
            opcion = self.mostrar_menu()

            if opcion == 1:
                base = float(input("Ingrese la base: "))
                altura = float(input("Ingrese la altura: "))
                figura = Rectangulo(base, altura)

            elif opcion == 2:
                radio = float(input("Ingrese el radio: "))
                figura = Circulo(radio)

            elif opcion == 3:
                base = float(input("Ingrese la base: "))
                altura = float(input("Ingrese la altura: "))
                figura = Triangulo(base, altura)

            elif opcion == 4:
                print("Saliendo del programa...")
                break

            else:
                print("Opción inválida. Intente nuevamente.")
                continue

            area = figura.calcular_area()
            print(f"El área calculada es: {area:.2f}")
