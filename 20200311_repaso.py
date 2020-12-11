print("Hola clase")
#el contenido define el tipo de variable
numero = "uno"
numero2= 2
numero= 2
print("el contenido de la variable es", numero2)

if( numero > numero2) :
    print("numero es mayor a numero2")
elif (numero < numero2):
    print("numero es menor que numero2")
else:
    print("Ambos son iguales")

#listas
#la primera posicion es en el indice cero
lista1 = []
lista1.append(2)
lista1.append("dos")
print(lista1)
#tamaño
texto="tamaño"
print(len(lista1))
print(len(texto))
#acceso a elementos
print(lista1[0])
print(lista1[1])
#print(lista1[2])
print()
print(texto[2])
#lista1.append()
#lista1[3] = 4
lista2 = lista1 + [9,6]
print(lista2)
print("*****")
#matriz
matriz1 = [
    [1,3,5,7,9],
    [2,4,6,8,0]
]

print(matriz1[0])
print(matriz1[0][2])#5
print(matriz1[0][4])#9
print(matriz1[1])
print(matriz1[1][3])#8
print("*** key diccionarios ***")
#key de Diccionarios
matriz2= [
    [{"nombre": "Israel","Edad":"40"},{"nombres": "Alexis", "Edads": "27"}]
],
print("matriz 2 ",matriz2[0][0])#{'nombre': 'Israel'}
#print("matriz 2 ",matriz2[0][0]["edad"])#{'nombre': 'Israel'}
#print(matriz2[0][0])#Israel
print()
#print(matriz2[0]["Israel"])#Erroneo
#print(matriz2[1])
#print(matriz2[1]["Edad"])

print("+++ diccionarios++")
diccionario1={
    "nombre": "Israel",
    "Edad": 40
}

#print(diccionario1[0])#error
print(diccionario1["nombre"])#

matriz3=[
    ["Israel",30]
]
#resto de la division
if(7%2==0):
    print("numero par")
else:
    print("impar")

#elevado
print(4**2)
print(4**3)

# // arroja la parte entera y el resrto es con %
print(7//3)
print()
opcion = int(input("ingrese un numero"))
print(opcion)

nombre  = input("ingrese su nombre")

print(nombre.upper()) ##mayuscula
print(nombre.lower())##minuscula

opcion = input("Esta de acuerdo [SI/NO]")
if(opcion.upper() =="SI"): #sI,SI,si
    print("su opcion es SI")
else:
    print("su opcion es NO")

print("******")

edad = int(input("ingrese su edad"))
def funcion1():
    if(edad >= 18 ):
        print("usuario  mayor de edad")
    else:
        print("usuario menor de edad")

funcion1()#llamado a la funcion

def funcion2(variable):

    return variable *2

retorno1= funcion2(edad)
print("retorno** ",retorno1)