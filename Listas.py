#conjunto de elementos, ordenados segun su ingreso, son separados por coma
lista_numeros= [1,2,3,4,5,6,7,8,9,0]
print(lista_numeros)

#las listas comienzan con indice o posición cero (0), y termina n-1 donde "n" es el tamaño de la lista
lista_distintos_datos = ["uno",2,"tres",4]
print(lista_distintos_datos) #['uno', 2, 'tres', 4]
lista_vacia= []
print(lista_vacia)

#acceder a un datos de la lista, por posicion
print(lista_distintos_datos[0])
print(lista_distintos_datos[-4])
#print(lista_distintos_datos[4])#fuera de indice

#bloque o porcion del arreglo
print("acceso por porcion",lista_distintos_datos[2:]) #hacia la derecha, incluyendo el valor en el indice
print("acceso por porcion 2",lista_distintos_datos[:2])#hacia la izquierda excluyendo el valor en el indice

#suma de listas (concatenar/unir listas)
lista_uno= [1,2,3,4]
lista_dos= [5,6,7,8]
lista_tres = lista_uno +lista_dos
print("lista tres",lista_tres)

#lista de listas
lista_lista = [lista_uno,lista_dos]
print("lista lista",lista_lista)

#MUTABILIDAD
#cambiar el contenido de la lista
lista_numeros[6] = "a" #7 ->"a"  [1,2,3,4,5,6,7,8,9,0]
print("mutabilidad",lista_numeros) #[1, 2, 3, 4, 5, 6, 'a', 8, 9, 0]

#agrgrear mas contenido a la lista append()
lista_numeros.append(7)
print("agregar contenido con append",lista_numeros) #[1, 2, 3, 4, 5, 6, 'a', 8, 9, 0, 7]

#reemplazar bloques
lista_numeros[:6] = ["b","c","d"]
print("reemplazar bloque de contenido",lista_numeros) #['b', 'c', 'd', 'a', 8, 9, 0, 7]

#tamaño de la lista
print("tamaño lista",len(lista_numeros)) #tamaño 8

nombre = "Temuco"
print(len(nombre))