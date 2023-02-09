from lanzar_escucha_ip import *
from protocolo import *
from time import sleep
logging.basicConfig(level=logging.DEBUG)

def jugarComoServer(server_socket: socket):
    message = b'Se acabaron los barquitos'
    server_socket.sendall(message)
    server_socket.close()

def jugarComoCliente(server_cliente: socket):
    data = server_cliente.recv(1024)
    print(data)
    server_cliente.close()

def main():
    IP = socket.gethostbyname(socket.gethostname())
    maximo_de_intentos = 5

    while (maximo_de_intentos <= 5):
        logging.debug("Lanzando IP")
        # Bolean, Str
        ipLanzada = lanzarIP()

        if ipLanzada[0]:
            # Bolean, Str
            if ipLanzada[1] == "OK":
                logging.debug("OK")
                logging.debug("Abro socket TCP soy server")
                hayCliente, socket_server = levantar_server(IP)
                if hayCliente:
                    jugarComoServer(socket_server)
                else:
                    logging.debug("No se a conectado ningun cliente")

        else:
            # Bolean, Socket
            escuchado = escucha()
            if escuchado[0]:
                logging.debug("Recibo IP soy cliente")
                logging.debug("Intento conectarme")
                conexion, socket_server = conectar(escuchado[1])
                if conexion:
                    # Lanza el juego con el 
                    # socket recibido para envir los paquetes
                    jugarComoCliente(socket_server)
                else:
                    logging.debug("No es posible conectarse")
        maximo_de_intentos += 1
        break

if __name__ == "__main__":
    main()