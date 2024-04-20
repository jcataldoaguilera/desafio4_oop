# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-04-18
# RLAB-23-02-09-0044-2
#

# Librerias
from error import DimensionError

# Desarollo
class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        while ancho:
            try:
                if ancho < 1 or ancho > self.MAX:
                    DimensionError("Error: El alto ingresado no es valido", ancho, self.MAX)
                else:
                    self.__alto = ancho
            except DimensionError as dy:
                exit(dy)

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        while alto:
            try:
                if alto < 1 or alto > self.MAX:
                    DimensionError("Error: El alto ingresado no es valido", alto, self.MAX)
                else:
                    self.__alto = alto
            except DimensionError as dy:
                exit(dy)


if __name__ == '__main__':
    Foto(0, 10, "foto.png")