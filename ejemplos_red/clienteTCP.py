import socket

# Crear un socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Obtener la dirección IP y el puerto del servidor
server_address = ('172.26.3.156', 6969)

# Conectarse al servidor
sock.connect(server_address)

# Enviar datos al servidor
message = b'Mensaje de prueba'
sock.sendall(message)

# Recibir datos del servidor
data = sock.recv(1024)

# Cerrar la conexión
sock.close()

print('Recibido: {!r}'.format(data))