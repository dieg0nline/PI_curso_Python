# https://youtu.be/t93x-vnFvP4

# creamos una carpeta /modulos dentro del proyecto en la que almacenaremos los modulos que vamos a usar
# al estar el módulo en una subcarpeta no consigo hacerlo funcionar, hay que configurar algo para que reconozca las subcarpetas, pero no doy como.
# la solución que he encontrado es la siguiente: carpeta.modulo, y para abreviar lo combino con un "as" para crearle un alias

# -------------------------------

# esta sería una de las formulas para importar un módulo pero vamos a ver otra opción
# import modulos.funciones_matematicas as fun_mat 

# fun_mat.sumar(7,5)

# continuar en https://youtu.be/t93x-vnFvP4?t=514

# Otra opción sería importar únicamente el método que vamos a usar:
from modulos.funciones_matematicas import sumar

sumar(3,2)

# una tercera opción, para usar todos los metodos, sería sustituir el metodo a importar por un asterisco, aunque no se que diferencia hay entre hacer eso e importar el modulo entero con import en vez de hacer un "from *"
# from modulos.funciones_matematicas import *