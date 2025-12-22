class Paciente:
    def __init__(self, nombre):
        self.nombre = nombre

    def agendar_cita(self, medico):
        if medico.disponible:
            medico.disponible = False
            print(f"✅ Cita agendada con el Dr. {medico.nombre}")
        else:
            print("❌ El médico no está disponible")
