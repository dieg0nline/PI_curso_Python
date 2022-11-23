# https://youtu.be/OU-e2uhoGxE

class Coche():
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha=False


    def arrancar(self, arrancamos): 
        self.__enmarcha = arrancamos

        if(self.__enmarcha): # al no especificar nada le estamos pidiendo que compruebe si es True
            chequeo=self.__chequeo_interno() # guardamos en una variable "chequeo" el resultado del método "__chequeo_interno"

        if(self.__enmarcha and chequeo): #comprobamos que, tanto "__enmarcha" como "chequeo" seean True
            return "El coche está en marcha"
        elif(self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo, no podemos arrancar"
        else:
            return "El coche está parado"


    def estado(self):
        print ("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)


    def __chequeo_interno(self): # encapsulamos el método para que no pueda ser ejecutado fuera de la clase
        print ("realizando chequeo interno")
        
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False



miCoche=Coche()

print(miCoche.arrancar(True)) 

miCoche.estado() 

print ("--------------- A continuación creamos el segundo ojbjeto -------------------------")

miCoche2=Coche() 

print (miCoche2.arrancar(False))

miCoche2.estado()