"""
Programa Principal
Descripción:
Punto de entrada del sistema.
Ejecuta el servicio de cálculo de áreas.
"""

from servicios.calculadora_servicio import CalculadoraServicio


def main():
    app = CalculadoraServicio()
    app.ejecutar()


if __name__ == "__main__":
    main()
