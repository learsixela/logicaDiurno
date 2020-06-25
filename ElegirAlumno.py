import random
print("****************************************")
print("Realizar la selección de alumno a presentar ejercicio")
print("****************************************")

def obtenerNumero(alumnosTotales):
    numero = random.randint(1,alumnosTotales)
    return numero

print()
print("****************************************")
cantAlumnos = int(input("Ingrese total de alumnos asistentes a clases hoy"))
print("****************************************")
numElegido= obtenerNumero(cantAlumnos)
print()
print("****************************************")
print("*                                      *")
print("* El o La afortunada es:", numElegido,"  *")
print("*                                      *")
print("****************************************")