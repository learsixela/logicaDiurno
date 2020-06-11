print(">>>Como hacer amigos>>>")
print("Hacer una llamada de telefonica")
print("________________________________")
#Respuesta
print("¿Hay respuesta ? Y/N")
respuesta = input()
if respuesta.upper()== "Y":
        respuesta = input("¿Quieres compartir una merienda conmigo? Y/N")
        if respuesta.upper()== "Y":
                print("Cenar juntos y comenzar una amistad")
        elif respuesta.upper()== "N":
                respuesta = input("¿Disfrutarias un bebida caliente? Y/N")
                if respuesta.upper() == "Y":
                        bebida = input("Elije 1.- Cafe 2.- Té 3.- Cocoa")
                        if bebida == "1":
                                print("Tomaremos café y comenzaremos una amistad")
                        elif bebida == "2":
                                print("Tomaremos Té y comenzaremos una amistad")
                        elif bebida == "3":
                                print("Tomaremos Cocoa y comenzaremos una amistad")
                elif respuesta.upper() == "N":
                        print("...REBATIR")
                        respuesta = input("¿Compartimos algun interes? Y/N")
                        if respuesta.upper()== "Y":
                                print("¿Que tal si hacemos algo juntos? y comenzar amistad")
                        else:
                                print("Actividad menos objetable")
elif respuesta.upper()== "N":
        print("Deja un mensaje")
        print("Espera que que devuelva la llamda")