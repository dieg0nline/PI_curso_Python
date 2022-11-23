# https://youtu.be/Y_SiIgxc-xI

# creamos una clase
class Coche():
    # añadimos propiedades
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha=False

    # creamos métodos (comportamientos)
    def arrancar(self):
        self.enmarcha = True
        print("Arrancamos el coche")

    def estado(self):
        if(self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"

miCoche=Coche() # creamos el primer objeto de la clase, es decir, instanciamos la clase

# Accedemos a las propiedades
print("el largo del coche es de : ", miCoche.largoChasis)
print("El coche tiene ", miCoche.ruedas, " ruedas")

# comprobamos el estado del coche
print (miCoche.estado())

# Accedemos al método
miCoche.arrancar() #ponemos en marcha el coche

# volvemos a comprobar el estado del coche
print (miCoche.estado())