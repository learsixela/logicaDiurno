#listas
# conjunto de datos, ordenados segun su ingreso, separados por coma ","

lista_numeros = [0,1,2,3,4,5,6,7,8,9] #tamaño es 10
print(lista_numeros)

#las listas comienza por la posicion(indice) 0 (cero)()
lista_datos_distintos = ["uno",2,"tres",4]
print(lista_datos_distintos)
#cantidad de elementos = 4 elementos  -> tamaño
#el ultimo elemento = tamaño - 1 (4-1 = 3)


#acceder a dato por posicion o indice
print(lista_datos_distintos[0])
print(lista_datos_distintos[1])
print(lista_datos_distintos[2])
print(lista_datos_distintos[3])
print(lista_numeros[9])
print(lista_numeros[-1])
print("*********")
#"uno",2,"tres",4,"uno",2,"tres",4
print(lista_datos_distintos[-1])
print(lista_datos_distintos[-2])
print(lista_datos_distintos[-3])
print("*********")
#imprimir seccion segun posicion, hacia la izquierda no considela el valor del indice
print(" desde indice 1",lista_datos_distintos[1:] )
print(" desde indice 2",lista_datos_distintos[2:] )
print("* hacia la izquierda*")
print(" desde indice 1",lista_datos_distintos[:1] )
print(" desde indice 2",lista_datos_distintos[:2] )

print("")
#suma de lista (conctatenacion de listas)
lista_uno= [1,2,3,4]
lista_dos= [5,6,7,8]
lista_tres=[] #lista vacia
lista_tres= lista_dos + lista_uno
print("Lista tres ",lista_tres)#Lista tres  [5, 6, 7, 8, 1, 2, 3, 4]
print("")
# append ,. permite agregar elementos a las listas
lista_uno.append(9)
print(lista_uno)#[1, 2, 3, 4, 9]
lista_dos.append(9)
print(lista_dos)#[5, 6, 7, 8, 9]

#reemplazar contenido segun indice
lista_uno[4] = 0
print(lista_uno)


#lista con los meses del año
#signos del zodiaco
#dia semana
#abecedario
#vocales

#crearlas con los elementos correspondientes
#dividir todas las listas en 2 sub listas

lista_vocales=[]
lista_vocales.append('a')
lista_vocales.append('e')
lista_vocales.append('a')

lista_vocales[2]='i'