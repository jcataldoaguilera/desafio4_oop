# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-04-18
# RLAB-23-02-09-0044-2
#

# Desarollo
class DimensionError(Exception):
    def __init__(self, mensaje:str, dimension:int, maximo:int) -> None:
        super().__init__(mensaje)
        self.dimension = dimension
        self.maximo = maximo
    
    def __str__(self) -> str:
        if self.dimension or self.maximo:
            return f"Error: {self.dimension} las dimensiones deben ser mayor a 1 y menor a {self.maximo}"
        else:
            return super().__str__