#key, o palabra clave

#Diccionarios
numeros = {
    "uno": 1,
    "doscientos":200,
    "gato":1234,
}

print(numeros["uno"])
print(numeros["doscientos"])
print(numeros["gato"])
print()

#agregar contenido a numeros
#crear variable para diccionario numeros
print(numeros)
numeros["cuatro"] = 4
print(numeros["cuatro"])
print(numeros)
#tamaño del diccionario
print(len(numeros))

numeros["cuatro"] = 5
print(numeros)

#si no existe y consultamos =>error (impresion)
#si no existe  lo crea, asignacion
#si existe lo reemplaza

#matriz de diccionarios
matriz =[
    [{"uno":"casa","dos":2},{"tres":3,"cuatro":4}],#0
    #[a,b,c,d] #1, a=>{key:valor,key:valor}; b=>{key:valor,key:valor}
    #[] #2,
    #[] #3,
    #[] #4,
]
print()
print(matriz)
print(matriz[0])#[{"uno":1,"dos":2},{"tres":3,"cuatro":4}]
print(matriz[0][0])#{'uno': 1, 'dos': 2}
print(matriz[0][0]["uno"])#casa


#matriz de diccionarios con :
# 5 arreglos internos
# cada arreglo debe tener 4 elementos
# cada elemento debe tener 2 key


#como imprimir con for de for
matriz2=[
    [{"nombre":"israel"},{"apellido":"palma"},{"edad":40}],
    [{"nombre":"Juan"},{"apellido":"Perez"},{"edad":30}],
    [{"nombre":"Juan2"},{"apellido":"Perez2"},{"edad":20}],
    [{"nombre":"Juan3"},{"apellido":"Perez3"},{"edad":25}],
]
## israel palma 40
## juan perez 30

