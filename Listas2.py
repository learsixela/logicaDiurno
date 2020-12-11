#matrices
#lista anidadas
animales = [
    ["Perro","domestico","12"],#0
    ["Gato","domestico","10"],#1
    ["Raton","silvestre","3"] #2 #len-1
]
print("len o tamaño de lista",len(animales))

print("ingreso a lista por indice 1",animales[1])
print("accediendo a elemento de la lista interna por indice 2:",animales[1][2])

print(animales[0][0],animales[0][1],animales[0][2])
print(animales[1][0],animales[1][1],animales[1][2])
print(animales[2][0],animales[2][1],animales[2][2])

#print("mati",animales[0][0,1,2])

print("***********************************")
tamanioLista = len(animales)
for variable in range(tamanioLista):#3 # valores 0,1,2
    print("variable:",variable," lista:",animales[variable])

#for anidados
print("**************** for anidados *******************")
for fila in range(tamanioLista):
    print("fila n:",fila," lista:",animales[fila])
    for elemento in range(len(animales[fila])):
        print("variable2", elemento,"-  valor interno:",animales[fila][elemento])

#diccionarios de lista

print("**************** diccionarios de lista *******************")
fecha = {
    "dia": 9,
    "mes": 7,
    "mes_palabras": "Julio",
    "año": 2020,
    2: "esto es un numero de key",
    "covid": {"19":"enfermedad", "20":"pandemia"},

}

print("fecha", fecha)
print("acceder al elemento:",fecha["mes_palabras"],fecha["año"], fecha[2])

print(fecha["covid"])
print(fecha["covid"]["20"])

#crea una matriz de diccionarios de 2X2

Matris = [
    {"uno": 1,"dos": 2},{"tres":3}

]
print("tamaño de la matriz", len(Matris))
print(Matris[0])
print(len(Matris[0]))

Matris.append({"cinco":5})
print(Matris)

#agregar a diccionario
Matris[1]["cuatro"] = 4
#si no existe el elemento, lo agrega, y si existe lo reemplaza

print("agregando cuatro ",Matris)
Matris[2]["cinco"] = 6
print("si existe lo reemplaza ",Matris)


fecha["prueba"]="Proximo Jueves a las 14:10 horas"
print(fecha)