from lanzar_escucha_ip import *
from protocolo import *
from time import sleep

def jugar(socket_comunicacion, es_server):
    pass

def main():
    maximo_de_intentos = 5

    while (maximo_de_intentos <= 5):
        ipLanzada = lanzarIP()

        if ipLanzada[0]:
            # Bolean, Str
            if ipLanzada[1] == "OK":
                print("OK")
                print("Abro socket TCP soy server")
        else:
            # Bolean, Socket
            escuchado = escucha()
            if escuchado[0]:
                print("Recibo IP soy cliente")
                print("Intento conectarme")
                if conectar(escuchado[0]):
                    # Lanza el juego con el 
                    # socket recibido para envir los paquetes
                    jugar(escuchado[1])
        maximo_de_intentos += 1
