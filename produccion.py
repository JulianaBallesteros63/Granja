class Produccion:
    def __init__(self, origen, cantidad, tipo):
        self.__origen = origen  # nombre del cultivo o id del animal
        self.__cantidad = cantidad
        self.__tipo = tipo      # "cultivo" o "animal"

    def __str__(self):
        return f"Producción({self.__tipo} - {self.__cantidad} unidades, origen: {self.__origen})"

    def get_cantidad(self):
        return self.__cantidad
