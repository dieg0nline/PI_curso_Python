import pandas as pd
from pandas import ExcelWriter

consultar=""
nombre=[]
apellido=[]

while consultar !="N":
    nuevo_nombre=input("introduce tu nombre: ")
    nombre.append(nuevo_nombre)

    nuevo_apellido=input("introduce tu apellido: ")
    apellido.append(nuevo_apellido)

    consultar=input("crear otro registro?: ")

    data = {'nombre': nombre,
        'apellido': apellido}

# print(data)

df = pd.DataFrame(data)

escritor = pd.ExcelWriter('/home/dieg0nline/Dropbox/Estudiar/prueba.xlsx', engine='xlsxwriter')
df.to_excel(escritor, sheet_name="hojaPrueba", index=False)

escritor.save()
print("registro creado")