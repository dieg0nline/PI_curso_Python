# PRIMER EJERCICIO

# i=1

# while i<=10:
#     # print(f"ejecución {i}")
#     print("Ejecución " + str(i))
#     i=i+1


# SEGUNDO EJERCICIO

# edad=int(input("introduce tu edad: "))

# while edad<0 or edad>100:
#     print("Edad incorrecta. Vuelve a intentarlo")
#     edad=int(input("vuelve a introducir tu edad: "))

# print("Edad correcta " + str(edad))


# TERCER EJERCICIO

import math
print ("programa de cálculo de raíz cuadrada")
numero=int(input("introduce un número: "))

intentos=0

while numero<0:
    print ("No se puede hallar la raíz de un número negativo")

    if intentos==2:
        print ("Has fallado demasiadas veces")
        break;

    numero=int(input("introduce un número: "))
    if numero<0:
        intentos=intentos+1

if intentos<2:
    solucion=math.sqrt(numero)
    print ("La raíz cuadrada de " + str(numero) + " es " + str(solucion))
