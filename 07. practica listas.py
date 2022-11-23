miLista=["María","Pepe","Marta","Antonio"]

print(miLista[:])

# AGREGAR ELEMENTOS A UNA LISTA -> "append"

miLista.append("Sandra")

print(miLista[:])

# AGREGAR EN UNA POSICIÓN DETERMINADA -> "insert"

miLista.insert(2,"Diego")

print(miLista[:])

# AGREGAR VARIOS ELEMENTOS AL FINAL -> "extend"

miLista.extend(["Susana","Mitu","Pi"])

print(miLista[:])

# LOCALIZAR LA POSICIÓN DE UN ELMENTO -> "index"

print(miLista.index("Susana"))

# COMPROBAR SI UN ELEMENTO SE ENCUENTRA

print("Pepe" in miLista)

# ELIMINAR ELEMENTO -> "remove"

miLista.remove("Pepe")
print(miLista[:])

# ELIMINAR EL ULTIMO ELEMENTO -> "pop"

miLista.pop()
print(miLista[:])

# AÑADIR UNA LISTA A OTRA 

miLista2=["Pi","Lila"]

miLista3=miLista+miLista2

print(miLista3[:])

# PODEMOS HACER QUE UNA LISTA REPITA ELEMENTOS

miLista2=["Pi","Lila"] * 3

print(miLista2[:])