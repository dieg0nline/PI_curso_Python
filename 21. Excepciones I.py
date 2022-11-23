def suma(num1, num2):
    return num1+num2

def resta(num1, num2):
    return num1-num2

def multiplica(num1, num2):
    return num1*num2

def divide(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return "Operación errónea"

try:
    op1=(int(input("introduce el primer número: ")))
except ValueError:
    print("El dato introducido no es un número")

try:
    op2=(int(input("introduce el segundo número: ")))
except ValueError:
    print("El dato introducido no es un número")

operacion=input("Introduce la operación a realizar (suma, resta, multiplica, divide): ")

if operacion=="suma":
    print(suma(op1,op2))

elif operacion=="resta":
    print(resta(op1,op2))

elif operacion=="multiplica":
    print(multiplica(op1,op2))

elif operacion=="divide":
    print(divide(op1,op2))

else:
    print("operación no válida")

print("Operación ejecutada. Continuación de ejecución del programa ")