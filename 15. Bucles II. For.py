# for i in ["enero", "febrero", 3]:
#     print("hola", end=" ")

#----------------------------------------------------

# email=False
# miEmail=input("intruduce tu dirección de email: ")

# for i in "diego@datalisis.es":
#     if(i=="@"):
#         email=True

# if email==True:
#     print("Email correcto")
# else:
#     print("Email incorrecto")

#----------------------------------------------------

contador=0
miEmail=input("introduce tu dirección de email: ")

for i in miEmail:
    if(i=="@" or i=="."):
        contador=contador+1

if contador==2:
    print("Email correcto")
else:
    print("Email incorrecto")

#----------------------------------------------------


