def divide():
    try:
        op1=(float(input("introduce el primer número: ")))
        op2=(float(input("introduce el segundo número: ")))
        print("El resultado de la división es: " + str(op1/op2))

    except ValueError:
        print("El valor introducido es erróneo")

    except ZeroDivisionError:
        print("No se puede dividir entre 0")

    finally:
        print("Operación finalizada")

divide()