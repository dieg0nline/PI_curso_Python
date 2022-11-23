# for i in range(5):
#     print(f"valor de la variable {i}")

# un range admite 3 pámetros - inicio del conteo - número de valores - intervalo de salto

# for i in range(3,18,2):
#     print(f"valor de la variable {i}")

valido=False

email=input("introducie tu email: ")

for i in range(len(email)):
    if email[i]=="@":
        valido=True

if valido:
    print("email correcto")

else:
    print("email incorrecto")

    # print (email[i])

