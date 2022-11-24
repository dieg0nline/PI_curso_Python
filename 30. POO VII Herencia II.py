# https://youtu.be/jMQQN9OxwVc

class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelearar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print ("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena )

class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado = cargar
        if(self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta está vacía"

class Moto(Vehiculos): 

    # Creamos un constructor y mediante "super()" llamamos al constructor de la clase padre para heredar sus parámetros (marca y modelo) y añadimos los nuevos (tipo y hcaballito)
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo
        self.hcaballito = ""

    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"

    def estado(self):
        print ("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nTipo: ", self.tipo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito )        

class VElectricos():

    # Creamos su constructor
    def __init__(self): 
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True

class BicicletaElectrica(VElectricos, Vehiculos): # Al heredar de dos clases distintas los parámetros que nos pedirá son los que marque la primera herencia indicada (Vehiculos) por lo que, en este caso, no pasaremos parámetros
    pass


miMoto=Moto("honda","shadow","custom") 

miMoto.caballito()
miMoto.estado()

print("----- Siguiente vehículo----")

miFurgoneta=Furgoneta("fiat","vitto")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

print("----- Siguiente vehículo----")

miBici = BicicletaElectrica()