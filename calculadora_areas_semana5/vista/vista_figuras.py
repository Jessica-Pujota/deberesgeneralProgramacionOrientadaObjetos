"""
Vista: VistaFiguras
Descripción: Maneja la interacción con el usuario.
"""

class VistaFiguras:

    def mostrar_menu(self):
        print("\n--- CALCULADORA DE ÁREAS ---")
        print("1. Área del rectángulo")
        print("2. Área del círculo")
        print("3. Área del triángulo")
        print("4. Salir")

        return int(input("Seleccione una opción: "))

    def solicitar_datos_rectangulo(self):
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        return base, altura

    def solicitar_datos_circulo(self):
        radio = float(input("Ingrese el radio: "))
        return radio

    def solicitar_datos_triangulo(self):
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        return base, altura

    def mostrar_resultado(self, area):
        print(f"El área calculada es: {area}")
