#listas
# conjunto de datos, ordenados segun su ingreso, separados por coma ","
alumnos = [
    ["israel","palma","40"],
    ["alexander","soto", "16"],
    ["daniela","loncomil","15"],
    ["madeleine","colicheo","27"], # 4-1
    ["andrea","melillan","17"]
]
lista_datos_distintos = ["uno",2,"tres",4,"cinco"]
len(lista_datos_distintos) #5
print()
#len se utiliza para saber cantidad de elemento de una lista
print("tamaño de lista alumno:",len(alumnos))
print()
#acceder a dato por posicion o indice, lista alumnos tiene 4 elementos,
print(alumnos[0]) #['israel', 'palma', '40']
len(alumnos[0])
print(alumnos[1]) #['alexander', 'soto', '16']
print(alumnos[2])#['daniela', 'loncomil', '15']
print(alumnos[3])#['madeleine', 'colicheo', '27']
print(alumnos[4])#['andrea', 'melillan', '17']
print()
#alumnos[0] = ['israel', 'palma', '40']
print(alumnos[0][0])
print(alumnos[0][1])
print(alumnos[0][2])
print()
print(alumnos[1][0])
print(alumnos[1][1])
print(alumnos[1][2])
print()
print(alumnos[2][0])
print(alumnos[2][1])
print(alumnos[2][2])
print()
print(alumnos[3][0])
print(alumnos[3][1])
print(alumnos[3][2])
print()
#['andrea', 'melillan', '17']
print(alumnos[4][0])#andrea
print(alumnos[4][1])#melillan
print(alumnos[4][2])#17

#reemplazar lo anterior de forma mas optima
range(2) # 0,1
range(3) # 0,1,2
range(4) # 0,1,2,3
range(20)# 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19
range(500) #0,1,2,3...498,499

for x in range(5):#0,1,2,3,4
    print("************")
    print("fila:",x)
print()

#tamaño de la lista alumnos
tamanio= len(alumnos)# tamaño o cantidad de elementos de la lista es 5
print()
for posicion in range(tamanio):#0,1,2,...(tamaño-1)
    print("************")
    print("posicion ",posicion)
    print("alumno :",alumnos[posicion]) #alumnos[0],alumnos[1]...
    print(len(alumnos[posicion])) #len(alumnos[0]),len(alumnos[1])...

#['israel', 'palma', '40'] alumnos[0][2] =>40
alumnos = [
    ["israel","palma","40"],
    ["alexander","soto", "16"],
    ["daniela","loncomil","15"],
    ["madeleine","colicheo","27"], # 4-1
    ["andrea","melillan","17"]
]
print()
for posicion in range(tamanio):#0,1,2,3,4... posicion (5)
    for columna in range(len(alumnos[posicion])): #len(alumnos[0])= 3
        #range(3) => 0,1,2
        print(alumnos[posicion][columna]) #alumnos[0][0]=>Israel

    #    posicion      columna
    #    0               0           #israel
    #    0               1           #palma
    #    0               2           #40
    #    1               0           #alexander
    #    1               1           #soto
