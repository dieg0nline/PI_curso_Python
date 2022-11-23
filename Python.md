# PYTHON

## Programación orientada a objetos

### 27. POO IV

~~~ py
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

~~~

#### CONSTRUCTORES

+ Un **constructor** es un método especial que le da el estado inicial a los objetos
+ Para crear un método constructor se utiliza la palabra reservada **def** y la plabra reservada **\_\_init__**, y una vez declarado dicho método constructor metemos las propiedades dentro de este método precedidas de la plabra **.self**

~~~ py
class Coche():
    def __init__(self):
        self.largoChasis = 250
        self.anchoChasis = 120
        self.ruedas = 4
        self.enmarcha=False
~~~
