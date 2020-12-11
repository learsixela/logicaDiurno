matriz2= [
    [{"nombre":"Israel"},{"apellido":"Palma"},{"edad":40}],
    [{"nombre":"Alexander"},{"apellido":"Soto"},{"edad":18}],
    [{"nombre":"Elias"},{"apellido":"Rodríguez"},{"edad":17}],
    [{"nombre":"Angel"},{"apellido":"Muñoz"},{"edad":52}],
]
print("---Hola Bienvenido a la base de datos---")
print("Lista de los nombres de personas con sus respectivas edades:")

for i in range(len(matriz2)):
    for x in range(len(matriz2[i])):
        print(matriz2[i][x])

print("--------------------------------------------------------------")