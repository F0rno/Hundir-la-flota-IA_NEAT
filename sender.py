"""
Sacado de https://rico-schmidt.name/pymotw-3/socket/multicast.html
"""
import socket
import struct

message = b'Quien unos barquitos?'
multicast_group = ('224.3.29.71', 10000)

# Creamos el socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Ponemos un tiempo maximo para recivir la info
# y asi no bloquear el socket
sock.settimeout(0.2)

# El time-to-live del paquete sera de 1
# para que no pase la difusion de red local
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

try:

    # Envia los datos atraves del grupo de difusion
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, multicast_group)

    # Esperamos respuesta
    while True:
        print('waiting to receive')
        try:
            data, server = sock.recvfrom(16)
        except socket.timeout:
            print('timed out, no more responses')
            break
        else:
            print('received {!r} from {}'.format(
                data, server))

finally:
    print('closing socket')
    sock.close()