# CREAMOS UNA FUNCION CON RETURN QUE DEVUELVA NUMEROS PARES HASTA UN MÁXIMO DE DIGITOS QUE LE INDIQUEMOS
# def genenaPares(limite):
#     num=1
#     miLista=[]
#     while num<limite:
#         miLista.append(num*2)
#         num+=1
#     return miLista

# print(genenaPares(12))

# -----------------------------------------

# CREAMOS LA MISMA FUNCION CON YIELD

def generaPares(limite):
    num=1
    # miLista=[] -> al generar un objeto iterable (que se puede recorrer) ya no es necesario crear una lista
    while num<limite:
        # miLista.append(num*2)
        yield num*2
        num+=1
    # return miLista
devuelvePares=generaPares(10)

print(next(devuelvePares))

print("nueva línea de código")

print(next(devuelvePares))

print("nueva línea de código")

print(next(devuelvePares))