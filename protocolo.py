import socket
import struct
import logging
logging.basicConfig(level=logging.DEBUG)

def conectar(ip):
    logging.debug("Crear un socket TCP, para connectarse")
    socket_con_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_con_server.settimeout(2)
    server_address = (ip, 6969)
    logging.debug("Intentando conectarse")
    try:
        socket_con_server.connect(server_address)
        conexion = True
    except Exception as err:
        conexion = False
        logging.debug(err)
    return conexion, socket_con_server

