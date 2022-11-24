# https://youtu.be/zH0VsRuD2ok

nombreUsuario=input("Intrudouce tu nombre de Usuario: ")

print ("El nombre es: ", nombreUsuario.upper())
print ("El nombre es: ", nombreUsuario.capitalize())

edad=input("introduce tu edad: ")
print(edad.isdigit())

while(edad.isdigit()==False):
    print("por favor, introduce un valor numérico")
    edad=input("introduce tu edad: ")
    print(edad.isdigit())


if (int(edad)<18):
    print("no puede pasar")
else:
    print("puede pasar")
    