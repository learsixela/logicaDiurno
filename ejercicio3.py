nombre = input("digame su nombre")
apellido = input(f"digame su apellido {nombre}")


#apellido = input("digame su apellido ",nombre)

edad = int(input(f" indique su edad {nombre} {apellido}"))
print(f"usted tiene {edad} años")
print("usted tiene", edad,"años")
peso= float(input("ingrese su peso corporal"))
print(f"don {nombre} {apellido} tiene un peso de : {peso}")


mayoriaEdad= 18

#if - elif- else
#if(edad >= mayoriaEdad){}
#operadores de comparacion
print("********************")
if edad >= mayoriaEdad:
    print("la edad ingresada del la persona indica que es mayor de edad")
else:
    print("es menor de edad segun edad ingresada")
print("********************")

if edad >= mayoriaEdad:
    print("la edad ingresada del la persona indica que es mayor de edad")
elif edad >= 1:
    print("es menor de edad segun edad ingresada")
elif edad == 0:
    print("edad ingresada es cero")
else:
    print("no puede ingresar edad negativa")

print("********************")

if edad >= mayoriaEdad:
    print("la edad ingresada del la persona indica que es mayor de edad")
else:
    if edad >= 1:
        print("es menor de edad segun edad ingresada")
    else:
        print("edad ingresada es erronea")