midiccionario={"Alemania":"Berlín", "Francia":"París", "Reino Unido":"Londres", "España":"Madrid"}

print(midiccionario["Francia"])


# Agregar elementos

midiccionario["Italia"]="Lisboa"

print (midiccionario)


# Modificar un valor

midiccionario["Italia"]="Roma"

print(midiccionario)


# Eliminar un elemento

del midiccionario["Reino Unido"]

print(midiccionario)


# Asignar elementos en un diccionario desde una tupla

mitupla=["España", "Francia", "Reino Unido", "Alemania"]

midiccionario2={mitupla[0]:"Madrid", mitupla[1]:"Paris", mitupla[2]:"Londres", mitupla[3]:"Berlín"}

print(midiccionario2)


# Podemos guardar una tupla dentro de un diccionario

midiccionario3={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":[1991,1992,1993,1996,1997,1998]}

print(midiccionario3)
print(midiccionario3["Equipo"])
print(midiccionario3["anillos"])


# Imprimir las claves de un diccionario

print(midiccionario3.keys())


# Imprimir los valores de un diccionario

print(midiccionario3.values())