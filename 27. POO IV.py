# https://youtu.be/x5CY8fVyYLo


# creamos una clase
class Coche():
    # añadimos propiedades en un constructor
    def __init__(self):
        self.largoChasis = 250
        self.anchoChasis = 120
        self.ruedas = 4
        self.enmarcha=False

    # creamos métodos (comportamientos)
    def arrancar(self, arrancamos): # añadimos un segundo parámetro, que le pasaremos para evaluar el estado del coche
        self.enmarcha = arrancamos
        if(self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"

    def estado(self):
        print ("El coche tiene ", self.ruedas, " ruedas. Un ancho de ", self.anchoChasis, " y un largo de ", self.largoChasis)

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

# https://youtu.be/x5CY8fVyYLo