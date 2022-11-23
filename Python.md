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
+ Para crear un método constructor se utiliza la palabra reservada **def** y la plabra reservada **\_\_init__**, y una vez declarado dicho método constructor metemos las propiedades dentro de este método precedidas de la plabra **self.**

~~~ py
class Coche():
    def __init__(self):
        self.largoChasis = 250
        self.anchoChasis = 120
        self.ruedas = 4
        self.enmarcha=False
~~~

#### [Encapsulamiento](https://ellibrodepython.com/encapsulamiento-poo)

+ Protege una propiedad para que no se pueda modificar desde fuera de la clase. Para encapsular se precede al nombre de la variable con dos guiones bajos **\_\_variable**

~~~ py
class Coche():
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha=False
~~~

### 28 POO V

#### Encapsulación de objetos

+ Es el mismo concepto que la encapsulación de las propiedades. Pero aplicada a los métodos.

### 29. POO VI. HERENCIA

#### [Herencia](https://ellibrodepython.com/herencia-en-python)

Es el mecanismo por el cual una clase permite heredar las características (atributos y métodos) de otra clase.

Terminología importante:

1. Superclase: la clase cuyas características se heredan se conoce como superclase (o una clase base o una clase principal).
2. Subclase: la clase que hereda la otra clase se conoce como subclase (o una clase derivada, clase extendida o clase hija). La subclase puede agregar sus propios campos y métodos, además de los campos y métodos de la superclase.
3. Reutilización: la herencia respalda el concepto de “reutilización”, es decir, cuando queremos crear una clase nueva y ya hay una clase que incluye parte del código que queremos, podemos derivar nuestra nueva clase de la clase existente. Al hacer esto, estamos reutilizando los campos/atributos y métodos de la clase existente.
