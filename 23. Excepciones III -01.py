# https://www.youtube.com/watch?v=dLH-oay4Bts&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=23

def evaluaEdad(edad):

    if edad<0:
        raise TypeError("No se permiten edades negativas") #forzamos una excepción de error personalizada

    if edad<20:
        return "Eres muy joven"
    elif edad<40:
        return "Eres joven"
    elif edad<65:
        return "Eres maduro"
    elif edad<100:
        return "Cuídate..."

# print (evaluaEdad(18))
print (evaluaEdad(int(input("introduce tu edad: "))))