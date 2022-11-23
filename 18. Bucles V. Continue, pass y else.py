# INSTRUCCIÓN CONTINUE

#  for letra in "Python":
#     if letra=="h":
#         continue
#     print ("Viendo la letra " + letra)

# ---------------------------

# nombre="Pildoras informáticas"

# print(str(len(nombre)) + " contando espacios en blanco")

# contador=0

# for i in nombre:
#     if i==" ":
#         continue
#     contador+=1

# print(str(contador) + " sin contar espacios en blanco")

# ---------------------------

# INSTRUCCIÓN ELSE -> se ejecuta cuando el bucle termina, si no llega a terminar no se ejecuta

email = input("Intruduce tu email: ")

for i in email:
    if i=="@":
        arroba=True

        break;

else:
    arroba=False

print(arroba)