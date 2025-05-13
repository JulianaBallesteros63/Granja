from cultivo import Cultivo
from animal import Animal
from produccion import Produccion

class Granja:
    def __init__(self):
        self.__cultivos = []
        self.__animales = []
        self.__producciones = []

    def agregar_cultivo(self, cultivo):
        self.__cultivos.append(cultivo)

    def eliminar_cultivo(self, nombre):
        self.__cultivos = [c for c in self.__cultivos if c.get_nombre() != nombre]

    def editar_cultivo(self, nombre, nuevos_datos):
        for cultivo in self.__cultivos:
            if cultivo.get_nombre() == nombre:
                cultivo.editar(**nuevos_datos)

    def agregar_animal(self, animal):
        self.__animales.append(animal)

    def eliminar_animal(self, id):
        self.__animales = [a for a in self.__animales if a.get_id() != id]

    def editar_animal(self, id, nuevos_datos):
        for animal in self.__animales:
            if animal.get_id() == id:
                animal.editar(**nuevos_datos)

    def calcular_produccion_total(self):
        self.__producciones.clear()
        for cultivo in self.__cultivos:
            cantidad = cultivo.calcular_produccion()
            self.__producciones.append(Produccion(cultivo.get_nombre(), cantidad, "cultivo"))
        for animal in self.__animales:
            cantidad = animal.calcular_produccion()
            self.__producciones.append(Produccion(f"Animal ID {animal.get_id()}", cantidad, "animal"))
        return sum(p.get_cantidad() for p in self.__producciones)

    def generar_reporte_produccion(self):
        print("\n--- Reporte de Producción Total de la Granja ---")
        total = self.calcular_produccion_total()
        for prod in self.__producciones:
            print(f"- {prod}")
        print(f"\nProducción total de la granja: {total}\n")

