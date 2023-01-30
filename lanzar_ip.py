import socket
import struct
import logging
logging.basicConfig(filename='logs/lanzar_ip.log', level=logging.DEBUG, mode='w')

myIP = socket.gethostbyname(socket.gethostname())
message = bytes(myIP, encoding="utf-8")
multicast_group = ('224.6.6.6', 6969)

# Creamos el socket
logging.debug('Creación de socket')
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Ponemos un tiempo maximo para recivir la info
# y asi no bloquear el socket
sock.settimeout(1)

# El time-to-live del paquete sera de 1
# para que no pase la difusion de red local
logging.debug('El time-to-live del paquete sera de 1')
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

try:

    # Envia los datos atraves del grupo de difusion
    logging.debug('Envio de los bytes')
    sent = sock.sendto(message, multicast_group)

    # Esperamos respuesta
    while True:
        try:
            data, server = sock.recvfrom(16)
        except socket.timeout:
            break
        else:
            print('received {!r} from {}'.format(
                data, server))

finally:
    sock.close()

def laun():
    return True, str