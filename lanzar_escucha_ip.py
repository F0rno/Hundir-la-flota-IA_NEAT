import socket
import struct
import logging
logging.basicConfig(level=logging.DEBUG)

def escucha():
    multicast_group = '224.6.6.6'
    server_address = ('', 6969)

    # Creamos el socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Le ponemos la ip al socket
    sock.bind(server_address)

    # Avisamos al sistema operativo para que inicie el socket
    # en el grupo de multi cast en todas las interfaces de red
    group = socket.inet_aton(multicast_group)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    # Recive y envia
    logging.debug("Escuchando")
    while True:
        try:
            data, address = sock.recvfrom(1024)
            logging.debug("Datos recibidos", data.decode('utf-8'))
            sock.sendto(b'OK', address)
            logging.debug("Enviando ok")
            sock.close()
            return True, data.decode('utf-8')
        except socket.timeout:
            logging.debug("Socket timeout")
            return False, str


def lanzarIP():

    myIP = socket.gethostbyname(socket.gethostname())
    message = bytes(myIP, encoding="utf-8")
    multicast_group = ('224.6.6.6', 6969)

    # Creamos el socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Ponemos un tiempo maximo para recivir la info
    # y asi no bloquear el socket
    sock.settimeout(2)

    # El time-to-live del paquete sera de 1
    # para que no pase la difusion de red local
    ttl = struct.pack('b', 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

    try:
        # Envia los datos atraves del grupo de difusion
        logging.debug("Enviando datos")
        sent = sock.sendto(message, multicast_group)

        # Esperamos respuesta
        logging.debug("Esperando respuesta")
        while True:
            try:
                data, server = sock.recvfrom(16)
                return True, data.decode('utf-8')
                logging.debug("Respuesta recibida")
            except socket.timeout:
                logging.debug("Socket timeout")
                break
    finally:
        logging.debug("Cerrando socket")
        sock.close()
    return False, str

if __name__ == "__main__":
    print(lanzarIP())