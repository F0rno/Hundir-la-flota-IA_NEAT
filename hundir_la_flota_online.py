from lanzar_escucha_ip import *
from time import sleep

while (True):
    resultado = lanzarIP()
    print(resultado)
    if resultado[0]:
        if resultado[1].upper() == "OK":
            print("Eres server")
            break
        else:
            resultadoEscucha = escucha()
            if resultadoEscucha[0]:
                print("Te conectas")
                break