print("Programa de evaluación de notas de alumnos")

nota_alumno=input("introduce la nota")
#nota_num = int(nota_alumno)


def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspenso"
    return valoracion

print(evaluacion(int(nota_alumno)))
#print(evaluacion(nota_num))

