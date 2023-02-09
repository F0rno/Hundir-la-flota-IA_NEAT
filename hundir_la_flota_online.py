from lanzar_escucha_ip import *
from protocolo import *
from time import sleep

def jugar(socket_comunicacion: socket, es_server=False):
    if not es_server:
        print("Conectado, cerrando")
        socket_comunicacion.close()

def main():
    maximo_de_intentos = 5

    while (maximo_de_intentos <= 5):
        print("Lanzando IP")
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
                conexion, socket_server = conectar(escuchado[1])
                if conexion:
                    # Lanza el juego con el 
                    # socket recibido para envir los paquetes
                    jugar(socket_server)
                else:
                    print("No es posible conectarse")
        maximo_de_intentos += 1
        break

if __name__ == "__main__":
    main()