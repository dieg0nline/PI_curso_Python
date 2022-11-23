from os import system


mitupla=["Susana", "Diego", "Mitu", "Pi"]
print(mitupla[1])

milista=list(mitupla)
mitupla2=tuple(milista)

print(mitupla2)
print(milista)
print(len(mitupla))


mitupla3=("Diego", 1, 5, 1969) 
nombre, dia, mes, year = mitupla3

print(year)
print(nombre)
