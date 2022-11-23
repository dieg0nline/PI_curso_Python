# https://youtu.be/u_VbLsIyzRk

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

miMoto=Moto("honda","shadow")

miMoto.estado()