from modelos.medico import Medico
from modelos.paciente import Paciente
from servicios.clinica import Clinica

def main():
    print("🏥 Sistema de Gestión de Citas Médicas\n")

    clinica = Clinica()
    clinica.agregar_medico(Medico("Juan Pérez", "Medicina General"))
    clinica.agregar_medico(Medico("Ana López", "Pediatría"))

    nombre = input("Ingrese nombre del paciente: ")
    paciente = Paciente(nombre)

    while True:
        print("\nMENÚ")
        print("1. Ver médicos")
        print("2. Agendar cita")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            clinica.mostrar_medicos()

        elif opcion == "2":
            clinica.mostrar_medicos()
            try:
                num = int(input("Seleccione el médico: ")) - 1
                medico = clinica.obtener_medico(num)
                if medico:
                    paciente.agendar_cita(medico)
                else:
                    print("❌ Médico inválido")
            except ValueError:
                print("❌ Ingrese un número válido")

        elif opcion == "3":
            print("👋 Gracias por usar el sistema")
            break

        else:
            print("❌ Opción no válida")

if __name__ == "__main__":
    main()
