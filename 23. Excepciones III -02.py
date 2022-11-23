# https://youtu.be/dLH-oay4Bts?t=599

import math

def calculaRaiz(num1): #creamos una función que esperal un parámetro
    if num1<0:
        raise ValueError ("El número no puede ser negativo") #forzamos una excepción personalizada
    else:
        return math.sqrt(num1)

op1 = (int(input("introduce un número: "))) #capturamos el número del cual queremos calcular la raiz cuadrada

try:
    print(calculaRaiz(op1)) #Llamamos a la función creada, pasandole como parámetro el número que introducirá el usuario y mandamos el resultado por pantalla   
except ValueError as ErrorDeNumeroNegativo: #creamos un alias con la excepción de error capturado
    print(ErrorDeNumeroNegativo)


print("fin del programa")
