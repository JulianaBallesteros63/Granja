from granja import Granja
from cultivo import Cultivo
from animal import Animal

def mostrar_menu():
    print("\n=== SISTEMA DE GESTIÓN AGRÍCOLA Y GANADERA ===")
    print("1. Agregar cultivo")
    print("2. Agregar animal")
    print("3. Editar cultivo")
    print("4. Editar animal")
    print("5. Eliminar cultivo")
    print("6. Eliminar animal")
    print("7. Mostrar reporte de producción")
    print("8. Salir")


def main():
    granja = Granja()
    id_animal = 1

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del cultivo: ")
            tipo = input("Tipo de cultivo: ")
            area = float(input("Área (ha): "))
            rendimiento = float(input("Rendimiento por ha: "))
            cultivo = Cultivo(nombre, tipo, area, rendimiento)
            granja.agregar_cultivo(cultivo)

        elif opcion == "2":
            especie = input("Especie: ")
            raza = input("Raza: ")
            edad = int(input("Edad: "))
            peso = float(input("Peso (kg): "))
            produccion = float(input("Producción esperada: "))
            animal = Animal(id_animal, especie, raza, edad, peso, produccion)
            granja.agregar_animal(animal)
            id_animal += 1

        elif opcion == "3":
            nombre = input("Nombre del cultivo a editar: ")
            nuevos = {
                "tipo": input("Nuevo tipo (dejar vacío para mantener): ") or None,
                "area": float(input("Nueva área (dejar en blanco para mantener): ") or 0) or None,
                "rendimiento": float(input("Nuevo rendimiento (dejar en blanco para mantener): ") or 0) or None,
            }
            granja.editar_cultivo(nombre, nuevos)

        elif opcion == "4":
            id = int(input("ID del animal a editar: "))
            nuevos = {
                "especie": input("Nueva especie: ") or None,
                "raza": input("Nueva raza: ") or None,
                "edad": int(input("Nueva edad: ") or 0) or None,
                "peso": float(input("Nuevo peso: ") or 0) or None,
                "produccion": float(input("Nueva producción: ") or 0) or None,
            }
            granja.editar_animal(id, nuevos)

        elif opcion == "5":
            nombre = input("Nombre del cultivo a eliminar: ")
            granja.eliminar_cultivo(nombre)

        elif opcion == "6":
            id = int(input("ID del animal a eliminar: "))
            granja.eliminar_animal(id)

        elif opcion == "7":
            granja.generar_reporte_produccion()

        elif opcion == "8":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()

