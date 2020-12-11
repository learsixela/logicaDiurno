
opcion= 1
while (opcion !=0):
    numero1 = int(input("INGRESA UN NUMERO 1: "))
    numero2 = int(input("Ingresa un numero 2: "))

    print("Seleccione una opcion del menu")
    print("1.-Suma")   
    print("2.-Resta")   
    print("3.Dividir")   
    print("4.-Multiplicacion")   
    print("0.-Salir")

    opcion=int(input("Ingrese la opcion: "   ))

    if(opcion ==1):
        suma = numero1 + numero2
        print("**********")
        print("Su Resultado es de la suma es:", suma)
        print("**********")
    elif(opcion ==2):
        Resta = numero1 - numero2
        print("**********")
        print("Su resultado de la resta es: ", Resta)
        print("**********")
    elif(opcion ==3):
        if(numero2==0):
            print("**********")
            print("No se puede Dividir por cero")
            print("**********")
        else:
            Division = numero1 / numero2
            print("**********")
            print("Su resultado es de dividir; ", Division)
            print("**********")
    elif(opcion ==4):
        Multiplicacion = numero1 * numero2
        print("**********")
        print("Su resultado es de multiplicar ", Multiplicacion)
        print("**********")
    else:
        print("Saliste del programa")