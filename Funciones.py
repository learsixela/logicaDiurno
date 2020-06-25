
#funcion
def funcionSaludo():
    mensaje()
    print("Esta es un mensaje desde otra funcion")


def mensaje():
    print("mensaje")
    print("mensaje2")
    print("mensaje3")
    print("***********")

#llamado a la funcion
#mensaje()
#funcionSaludo()
#mensaje()


def funcionSuma():
    numero3 = 3
    numero4 = 4
    print("Resultado de la suma",numero1+numero2)
    print("Resultado de la 2 suma", numero3 + numero4)

numero1 = int(input("Ingrese numero 1 "))
numero2 = int(input("Ingrese numero 2 "))
print(numero1+ numero2)

funcionSuma()

#definiendo un funcion que recibe parametros
def resta(num1, num2):
    print("el resultado de la resta es :", num1-num2)

#llamar a la funcion con parametros
resta(numero1,numero2)
resta(8,4)
resta(numero2,numero2)

print("****** multiplicacion ******")
#funcion sin parametros
def multiplicacion():
    print("Resultado de la multiplicacion es: ", numero1*numero2)
multiplicacion()

#sobre carga de un metodo o funcion
def multiplicacion(var1,var2):
    print("Resultado de la multiplicacion 2 es: ", var1 * var2)

multiplicacion(numero2,numero1)

print("****** division ******")
def division(dividendo, divisor):
    if divisor ==0 :
        print("Error, no se puede dividir por cero")
    else:
        print("Resultado de la division es :", dividendo/divisor)

division(numero1,numero2)

print("****** funciones con retorno ******")

# funciones que retornan un valor
def funcionRetorno():
    return "17"

valorRespuesta = funcionRetorno()
print(" el valor de retorno es: ",valorRespuesta)

print("llamado directo ",funcionRetorno())

if(funcionRetorno() ==1):
    print("recibi un uno")