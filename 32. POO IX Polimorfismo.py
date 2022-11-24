# https://youtu.be/kV1cN_bqcSw

class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")
        
class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")


# miVehiculo = Moto()
# miVehiculo.desplazamiento()

# miVehiculo2 = Coche()
# miVehiculo2.desplazamiento()

# miVehiculo3 = Camion()
# miVehiculo3.desplazamiento()


def desplazamientoVehiculo(vehiculo): # creamos un procedimiento que recibe por parámetro que vehiculo queremos llamar
    vehiculo.desplazamiento() # con el vehiculo recibido llamaremos a la función "desplazamiento" de la clase que le corresponda

miVehiculo=Camion() # creamos una instancia con el vehículo escogido
desplazamientoVehiculo(miVehiculo) # finalmente llamamos al procedimiento anteriormente creado cuyo parámetro será el vehiculo que acabamos de instanciar, y nos devolverá el resultado del procedimiento correspondiente a la clase del vehículo instanciado