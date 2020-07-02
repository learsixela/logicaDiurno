#FOR : for variable IN lemento iterable ->(lista, cadena, rango) :
#cadena
for i in "TEMUCO":
    #print("i = ", i)
    print(f" valor de i en for {i}")

lista = ["a","e","i","o","u"]
for i in lista:
    print("i = ", i)

#rango
for x in range(5):
    print("range x = ", x)

rango = int(input("ingrese el rango de datos"))
for x in range(4,rango):
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