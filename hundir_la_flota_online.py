from hundir_la_flota_con_clases import *
from lanzar_escucha_ip import *
from protocolo import *
from time import sleep
logging.basicConfig(level=logging.DEBUG)

def coordenada_con_letra(fila, columna):
    diccionario_de_letras = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J'}
    return diccionario_de_letras[fila], columna

def jugarComoServer(server_socket: socket):
    barco_local  = Almirante()
    barco_online = Almirante("Tomas Coronado")

    while (True):
        fila, columna = barco_local.elegir_coordenada_IA()
        fila, columna = coordenada_con_letra(fila, columna)
        coordenadas_de_disparo = bytes(f"{fila}{columna}", encoding='utf-8')
        server_socket.sendall(coordenadas_de_disparo)
        server_socket.close()
        break

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