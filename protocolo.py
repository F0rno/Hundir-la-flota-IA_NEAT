import socket
import struct
import logging
logging.basicConfig(level=logging.DEBUG)

def conectar(ip):
    logging.debug("Crear un socket TCP, para connectarse")
    socket_con_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #socket_con_server.settimeout()
    server_address = (ip, 6969)
    logging.debug("Intentando conectarse")
    try:
        socket_con_server.connect(server_address)
        conexion = True
    except Exception as err:
        conexion = False
        logging.debug(err)
        socket_con_server.close()
    return conexion, socket_con_server


def levantar_server(ip):
    # Crear un socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.settimeout(4)
    # Obtener la dirección IP y el puerto del servidor
    server_address = (ip, 6969)
    # Vincular el socket a la dirección y puerto del servidor
    server_socket.bind(server_address)
    # Escuchar solicitudes de conexión
    server_socket.listen(1)
    logging.debug('Servidor escuchando en {}:{}'.format(*server_address))
    try:
        logging.debug('Esperando una conexión...')
        client_socket, client_address = server_socket.accept()
        # Aceptar una conexión entrante
        logging.debug('Conexión desde {}:{}'.format(*client_address))
        conexion = True
        return conexion, client_socket 
    except Exception as err:
        conexion = False
        logging.debug(err)
        server_socket.close()
        return conexion, socket 
       

"""
    Recibir datos del cliente
    data = client_socket.recv(1024)

    Enviar una respuesta al cliente
    response = b'Mensaje recibido: ' + data
    client_socket.sendall(response)

    Cerrar la conexión con el cliente
    client_socket.close()
    break

"""