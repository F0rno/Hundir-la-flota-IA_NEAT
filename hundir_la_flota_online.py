from lanzar_escucha_ip import *
from protocolo import *
from time import sleep

ipLanzada = lanzarIP()

if ipLanzada[0]:
    if ipLanzada[1] == "OK":
        print("OK")
        print("Abro socket TCP soy server")
else:
    escuchado = escucha()
    if escuchado[0]:
        print("Recibo IP soy cliente")
        print("Intento conectarme")
