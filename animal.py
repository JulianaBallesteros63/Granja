class Animal:
    def __init__(self, id, especie, raza, edad, peso, produccion):
        self.__id = id
        self.__especie = especie
        self.__raza = raza
        self.__edad = edad
        self.__peso = peso
        self.__produccion = produccion

    def calcular_produccion(self):
        return self.__produccion

    def editar(self, especie=None, raza=None, edad=None, peso=None, produccion=None):
        if especie: self.__especie = especie
        if raza: self.__raza = raza
        if edad: self.__edad = edad
        if peso: self.__peso = peso
        if produccion: self.__produccion = produccion

    def get_id(self):
        return self.__id

    def __str__(self):
        return f"Animal(ID: {self.__id}, {self.__especie} {self.__raza}, Edad: {self.__edad}, Peso: {self.__peso}, Producción: {self.__produccion})"

