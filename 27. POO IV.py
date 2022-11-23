# https://youtu.be/x5CY8fVyYLo


# creamos una clase
class Coche():
    # añadimos propiedades en un constructor
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha=False

    # creamos métodos (comportamientos)
    def arrancar(self, arrancamos): # añadimos un segundo parámetro, que le pasaremos para evaluar el estado del coche
        self.__enmarcha = arrancamos
        if(self.__enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"

    def estado(self):
        print ("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

miCoche=Coche() # creamos el primer objeto de la clase, es decir, instanciamos la clase

# comprobamos el estado del coche
miCoche.estado() # como el método ya devuelve un print, no hace falta imprimirlo

# Accedemos al método
print(miCoche.arrancar(True)) #ponemos en marcha el coche. Al devolver el método un "return" debemos imprimir el resultado

# volvemos a comprobar el estado del coche
# print (miCoche.estado())

print ("--------------- A continuación creamos el segundo ojbjeto -------------------------")

miCoche2=Coche() #creamos una segunda instancia de la clase "Coche"

miCoche2.estado()
print (miCoche2.arrancar(False))

miCoche2.__ruedas=5 # al estar encapsulada la variable no se modifica el valor
miCoche2.estado()