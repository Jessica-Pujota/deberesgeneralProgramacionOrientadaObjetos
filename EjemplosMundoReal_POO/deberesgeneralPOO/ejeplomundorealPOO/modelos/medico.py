class Medico:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
        self.disponible = True

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "Ocupado"
        print(f"{self.nombre} - {self.especialidad} | {estado}")
