print("Programa de becas año 2022")

distancia_escuela=int(input("Introduce la distancia a la escuela en km: " ))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el número de hermanos en el centro: "))
print(numero_hermanos)

salario_familiar=int(input("Introduce salario anual bruto: "))
print(salario_familiar)

min_distancia = 40
min_hermanos = 2
max_salario = 20000

if distancia_escuela>min_distancia and numero_hermanos>min_hermanos and salario_familiar<max_salario:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")


# OPERADOR IN
print("Asignaturas optativas:")

print("informática gráfica - pruebas de sofware - usabilidad y accesibilidad")

opcion=input("Escribe la asignatura escogida: ")

asignatura=opcion.lower()

if asignatura in ("informática gráfica","pruebas de software","usabilidad y accesibilidad"):
    print("Asignatura elegida: " + asignatura)
else:
    print(asignatura + " no está incluída en el plan de estúdios")

