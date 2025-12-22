from modelos.medico import Medico

class Clinica:
    def __init__(self):
        self.medicos = []

    def agregar_medico(self, medico):
        self.medicos.append(medico)

    def mostrar_medicos(self):
        print("\n👨‍⚕️ Médicos disponibles:")
        for i, medico in enumerate(self.medicos, start=1):
            print(f"{i}. ", end="")
            medico.mostrar_info()

    def obtener_medico(self, indice):
        if 0 <= indice < len(self.medicos):
            return self.medicos[indice]
        return None
