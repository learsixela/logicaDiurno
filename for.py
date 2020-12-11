#FOR : for variable IN lemento iterable ->(lista, cadena, rango) :
#cadena
print("********** cadenas ***********")
for i in "TEMUCO":
    print("i = ", i)
    #print(f" valor de i en for {i}")

print("********** Listas ***********")
lista = ["a","e","i","o","u"]
for i in lista:
    print("i = ", i)

#rango
print("********** rango ***********")
for x in range(5):#0,1,2,3,4
    print("range x = ", x)

print("")
rango = int(input("ingrese el rango de datos"))
for x in range(4,rango):#4,5,6
    print("range x = ", x)

numero_pares = []
numero_impares = []
for num in range(1, 11):
    if (num%2 ==0):
        numero_pares.append(num)
    else:
        numero_impares.append(num)

print(" numeros pares",numero_pares)
print(" numeros impares",numero_impares)

pares= [2, 4, 6, 8, 10]
impares= [1, 3, 5, 7, 9]

temp = pares
pares = impares
impares = temp

print(pares," - ",impares)