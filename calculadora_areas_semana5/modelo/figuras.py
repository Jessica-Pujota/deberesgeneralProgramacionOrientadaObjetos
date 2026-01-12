"""
Modelo: FigurasGeométricas
Descripción: Contiene las clases para calcular el área
de distintas figuras geométricas.
"""

import math


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base        # float
        self.altura = altura    # float

    def calcular_area(self):
        return self.base * self.altura


class Circulo:
    def __init__(self, radio):
        self.radio = radio      # float

    def calcular_area(self):
        return math.pi * self.radio ** 2


class Triangulo:
    def __init__(self, base, altura):
        self.base = base        # float
        self.altura = altura    # float

    def calcular_area(self):
        return (self.base * self.altura) / 2
