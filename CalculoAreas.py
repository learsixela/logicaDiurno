print("programa para calcular el area de una figura, elija la opcion")
print("area de un cuadrado=1")
print("area de un triangulo=2")
print("area de un rectangulo=3")

respuesta=int(input())

def resultado():
    if respuesta==1:
        print("ingrese el lado")
        altura = int(input())
        resultado=altura*altura
        print("el area del cuadrado es ",resultado)
        return resultado
    elif respuesta==2:
        altura=int(input("ingrese altura"))
        base = int(input("ingrese la base"))
        resultado=base*altura/2
        print("el area del triangulo es ", resultado)
        return resultado
    elif respuesta==3:
        altura = int(input("ingrese lado a"))
        base = int(input("ingrese lado b"))
        resultado=base*altura
        print("el area del rectangulo es ", resultado)
        return resultado
    else:
        print("la opcion ingresada no es valida")

print("area total: ",resultado())

resultado()