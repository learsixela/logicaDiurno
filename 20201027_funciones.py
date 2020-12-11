#funciones, se ejecutan cuando son llamadas
#2 tipos, reciben o no parametros; retornan o no un valor
# def nombre_de_la_funcion(parametro):
#(javascript) function nombre(){
# }
def saludos():
    print("Hola clase")

#llamado a la funcion o invocacion
saludos()

def mensaje():
    print("mensaje 1")
    print("mensaje 2")
    print("mensaje 3")

mensaje()
saludos()
print()

def suma(x,y):
    print(x+y)

suma(2,3)
suma(5,7)
suma(100,1200)

def restar(a,b):
    print(a-b)
print()
restar(3,7)
suma(3,7)
print("********")

#las variables a ser utilizadas en una funcion, deben ser declaradas antes del llamado a la función
numero1= 6
#numero2= 5

def sumar_2_Numeros():
    print(numero1+numero2)
numero2=4
#llamado a la funcion
sumar_2_Numeros()
#numero2=3 #error

print("**** multiplicar sobre escritura de funciones***")

def multiplicacion():
    print("el resultado de la multiplicacion es 1:",numero1*numero2)
multiplicacion()
print()
def multiplicacion(num1,num2):
    print("el resultado de la multiplicacion es 2:", num1 * num2)
multiplicacion(5,7)

print()
#en caso de no enviar el parametro , considera el valor por defecto
def multiplicacion(num1,num2=6):
    print("el resultado de la multiplicacion es 3:", num1 * num2)
multiplicacion(8)
multiplicacion(2,3)
#multiplicacion() este llamado es a la ultima definicion de la funcion

print("**** Retorno de valores ***")
def division(dividendo,divisor):
    #no podemos dividir por cero
    if(divisor!=0):
        print("El resultado de la division es:",dividendo/divisor)
        return dividendo/divisor
    else:
        print("No se puede dividir por cero")
        return "No se puede dividir por cero"

resultado = division(8,4)
print(resultado)

resultado = division(8,0)
print(resultado)

