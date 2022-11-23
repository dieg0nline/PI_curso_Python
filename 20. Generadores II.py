# cuando colocamos un * en el argumento de una función estamos indicando que va a recibir un número ilimitado de elementos
def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        # for subElemento in elemento:
            # yield subElemento
        yield from elemento

ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
