pares= [2, 4, 6, 8, 10]
impares= [1, 3, 5, 7, 9]

#temp = pares
#pares = impares
#impares = temp

lista_total= pares+impares #[2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
pares=lista_total[5:]
impares = lista_total[:5]

print(pares," - ",impares)

vacia = []

vacia = pares
pares=impares
impares=vacia

print(pares)
print(impares)

#funciones, retorno, for y listas, if elif else
lista_numeros= [1,2,3,4,5,6,7,8,9,10]
lista_vocales= [a,e,i,o,u]
#reemplace los pares con vocales, retornar lista modificada e imprimirla