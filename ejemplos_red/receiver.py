"""
Sacado de https://rico-schmidt.name/pymotw-3/socket/multicast.html
"""
import socket
import struct

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
while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(1024)

    print('received {} bytes from {}'.format(
        len(data), address))
    print(data)

    print('sending acknowledgement to', address)
    sock.sendto(b'ack', address)
    sock.close()
    break
