def mensaje ():
    print("Estamos aprendiendo Python")
    print("Estamos aprendiendo las instrucciones básicas")
    print("Poco a poco iremos avanzando")

mensaje()

#--------------------

def suma():
    num1=5
    num2=7
    print(num1+num2)

suma()

# FUNCIONES CON PARAMETROS

def suma(num1,num2):
    print(num1+num2)

suma(5,7)

suma(2,3)

suma(35,358)

# FUNCIONES QUE DEVUELVEN UN VALOR "RETURN"

def suma():
    num1=5
    num2=7
    resultado = num1+num2
    return(resultado)

num3=suma()
num4=3
print (num3+num4)

#---------------------------

def suma(num1,num2):
    resultado=num1+num2
    return resultado

print(suma(5,7))
print(suma(2,3))
print(suma(35,358))