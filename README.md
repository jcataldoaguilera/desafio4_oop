# Descripción
Usted trabaja para una empresa que se encuentra desarrollando una aplicación de galería de
fotos. Le han solicitado controlar que no sea posible modificar el alto o el ancho de una foto
creada, en caso de que se esté intentando modificar alguno de estos atributos por un valor
menor a 1, o mayor al valor máximo determinado por el atributo de clase MAX de la clase Foto.
Le solicitan además hacer este control mediante una excepción propia, ya que se desea
utilizar la misma excepción en otro sector del programa que recibe los valores de ancho y
alto, y desea validarlos antes de crear nuevas fotos.
Se le proporciona el código que permite crear instancias de Foto, donde usted debe agregar
el lanzamiento de la excepción en los métodos setter de ancho y alto, según las condiciones
indicadas.