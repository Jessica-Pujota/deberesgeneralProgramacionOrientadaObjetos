"""
Programa: Calculadora de áreas de figuras geométricas
Descripción: Aplicativo desarrollado con Programación
Orientada a Objetos y patrón de diseño MVC.
"""

from controlador.controlador_figuras import ControladorFiguras


def main():
    app = ControladorFiguras()
    app.ejecutar()


if __name__ == "__main__":
    main()
