# PYTHON

_No es hasta la lección 27 cuando comienzo a crear este archivo .md para tomar mis apuntes de clase. Anteriormente anotaba en el fichero_ **notas.md**.

_En lo sucesivo lo haré así con todas las clases y cursos lo cual me permitirá, por un lado tener organizados y localizados mis apuntes y por otro practicar el lenguaje markdown._

## Recursos

[Libros para estudiar](https://www.programaenpython.com/miscelanea/mejores-libros-de-python-en-espanol/)

[Clases online](https://es.py4e.com/lessons)

[documentación](https://pyspanishdoc.sourceforge.net/lib/lib.html)

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

~~~ py
# Creamos una clase, que será la clase "padre"
class Vehiculos():
    # Establecemos unos atributos (propiedades)
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    # Creamos unos métodos
    def arrancar(self):
        self.enmarcha = True

    def acelearar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print ("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena )

class Moto(Vehiculos): # Creamos una nueva clase "Moto" que hereda atributos y métodos de la clase "Vehiculos"
    pass

miMoto=Moto("honda","shadow") # Instaciamos la clase "Moto" pasandole los 2 parámetros requeridos

miMoto.estado() # Ahora podemos ejecutar en la clase "moto" uno de los métodos heredados de la clase "vehiculos"
~~~

### 30. POO VII Herencia II

#### Sobre escritura de métodos

#### Herencia simple y múltiple

Cuando hay herencia múltiple se da preferencia a la primera clase que pasamos como parámetro y, en caso de que distintas clases tengan métodos con el mismo nombre se usarán los métodos de dicha primera clase.

### 31. POO VIII Herencia III

#### super()

La función super, allá donde la coloquemos, llamará al método de la clase padre

### isinstance()

Se usa para comprobar si una instancia es hija de una clase en concreto, y nos devuelve True o False

~~~ py
isinstance(instancia, clase_padre)
~~~

[ejemplo](https://www.discoduroderoer.es/isinstance-en-python/)

### 32 POLIMORFISMO

Es cuando objetos de diferentes clases pueden ser accedidos utilizando el mismo interfaz, mostrando un comportamiento distinto (tomando diferentes formas) según cómo sean accedidos.

[Poliformismo en Python](https://ellibrodepython.com/polimorfismo-en-programacion)

### [33.Métodos de cadenas](https://youtu.be/zH0VsRuD2ok)

+ Uso de métodos de cadenas (string)
  + upper() - Pasa a mayúsculas un string
  + lower() - Pasa a minúsculas un string
  + capitalize() - Pone la primera letra en mayúscula
  + count() - Cuenta cuantas veces aparece una letra o grupo de caracteres dentro de un texto
  + find() - Representa la posición en la cual aparece un carácter o grupo de caracteres en un texto
  + isdigit() - Devuelve un booleando dependiendo si el texto es un valor numérico o no
  + isalum() - Comprueba si es alfanumérico
  + isalpha() - Comprueba si hay solo letras
  + split() - Separa por palabras utilizando espácios
  + strip() - Elimina los espacios sobrantes tanto al principio como al final
  + replace() - Cambia una palabra por otra dentro de un string
  + rfind() - Representa la posición en la cual aparece un carácter, pero contando desde el final

### [34. Módulos](https://youtu.be/t93x-vnFvP4)

Módulos son archivos con extensión .py .pyc (Python compliado) o archivo escrito en C para CPython, que posee su propio espacio de nombres y que puede contener variables, funciones, clases e incluso otros módulos.

Sirven para organizar y reutilizar el código (modularización y reutilización)
