"""
Modelo: Figuras Geométricas
Descripción:
Define las clases de las figuras geométricas y
sus métodos para el cálculo de áreas.
"""

import math


class Rectangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return self.base * self.altura


class Circulo:
    def __init__(self, radio: float):
        self.radio = radio

    def calcular_area(self) -> float:
        return math.pi * self.radio ** 2


class Triangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return (self.base * self.altura) / 2
