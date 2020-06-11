print("**********************")
print("Ejercicio calculadora")
print("**********************")
numero1 = int(input("ingrese un numero "))
numero2 = int(input("ingrese un segundo numero "))
print("**********************")
print("ingrese su opción:")
print("(1) sumar")
print("(2) restar")
print("(3) multiplicar")
print("(4) dividir")
opcion= input()
print("**********************")

if opcion == "1":
    print(f" el resultado de la suma es {numero1+numero2}")
elif opcion == "2":
    print(f" el resultado de la resta es {numero1-numero2}")
elif opcion == "3":
    print(f" el resultado de la multiplicación es {numero1 * numero2}")
elif opcion == "4":
    if numero2 == 0:
        print("No se puede dividir por cero")
    else:
        print(f" el resultado de la division es {numero1 / numero2}")
else:
    print("Ops! opcion ingresada no es valida.")
print("**********************")