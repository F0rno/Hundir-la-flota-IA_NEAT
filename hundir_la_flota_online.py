from hundir_la_flota_con_clases import Almirante
from net.lanzar_escucha_ip import *
from net.protocolo import *
from time import sleep
logging.basicConfig(level=print)


def coordenada_con_letra(fila, columna):
    diccionario_de_numeros = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J'}
    return diccionario_de_numeros[fila], columna


def letras_a_coordenadas(fila, columna):
    diccionario_de_letras = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
    return diccionario_de_letras[fila], int(columna)


def coordenadas_a_bytes(fila, columna):
    return bytes(f"{fila}{columna}", encoding="utf-8")


def bytes_a_coordenadas(mensaje_en_bytes: bytes):
    coordenadas_str = mensaje_en_bytes.decode("utf-8")
    return letras_a_coordenadas(coordenadas_str[0], coordenadas_str[1])


def comprobar_si_ganamos_y_avisamos(socket: socket, barco_local: Almirante):
    if barco_local.soy_ganador():
        socket.sendall(bytes("WIN", encoding="utf-8"))
        return True
    return False
        

def jugarComoServer(server_socket: socket):
    barco_local  = Almirante("Servidor")
    ganamos = False
    end = False

    while (True):
        # Comprobamos si hemos ganado
        if comprobar_si_ganamos_y_avisamos(server_socket, barco_local):
            ganamos = True
            break
        # Disparamos primero porque somos el server
        fila, columna = barco_local.elegir_coordenada_IA()
        filaLetra, columnaInt = coordenada_con_letra(fila, columna)
        server_socket.sendall(coordenadas_a_bytes(filaLetra, columnaInt))
        # Esperamos respuesta
        respuesta_del_enemigo = bytes(server_socket.recv(16)).decode("utf-8")
        # Comprobamos si perdemos
        if respuesta_del_enemigo == "WIN":
            ganamos = False
            break
        # Actualizamos el tablero y imprimimos
        barco_local.actualizar_tras_disparo(respuesta_del_enemigo, fila, columna)
        barco_local.imprimir_tableros()

        # Mientras que acertemos seguimos disparando
        while (respuesta_del_enemigo == "T" or respuesta_del_enemigo == "H"):
            if comprobar_si_ganamos_y_avisamos(server_socket, barco_local):
                ganamos = True
                end = True
                break
            # Disparamos de nuevo
            fila, columna = barco_local.elegir_coordenada_IA()
            filaLetra, columnaInt = coordenada_con_letra(fila, columna)
            server_socket.sendall(coordenadas_a_bytes(filaLetra, columnaInt))
            # Esperamos respuesta
            respuesta_del_enemigo = bytes(server_socket.recv(16)).decode("utf-8")
            barco_local.actualizar_tras_disparo(respuesta_del_enemigo, fila, columna)

        # Si detectamos que ganamos terminamos el bucle del juego aqui
        if end:
            break
        # Recibimos el disparo enemigo y comprobamos si nos a ganado
        disparo_enemigo = server_socket.recv(16)
        if bytes(disparo_enemigo).decode("utf-8") == "WIN":
            ganamos = False
            break
        # Vemos que ha hecho su disparo en nuestro tablero
        # y enviamos el resultado
        fila, columna = bytes_a_coordenadas(disparo_enemigo)
        respuesta_aliada = barco_local.recibir_disparo(fila, columna)
        server_socket.sendall(bytes(respuesta_aliada, encoding="utf-8"))

        # Mientras que acierten nos siguen disparando 
        while (respuesta_aliada == "T" or respuesta_aliada == "H"):
            disparo_enemigo = server_socket.recv(16)
            if bytes(disparo_enemigo).decode("utf-8") == "WIN":
                ganamos = False
                end = True
                break
            fila, columna = bytes_a_coordenadas(disparo_enemigo)
            respuesta_aliada = barco_local.recibir_disparo(fila, columna)
            server_socket.sendall(bytes(respuesta_aliada, encoding="utf-8"))
        
        # Terminamos si nos han ganado esperando su disparo
        if end:
            break
        sleep(0.1)

    # Por si no lo ha recivido
    try:
        sleep(0.5)
        if ganamos:
            server_socket.sendall(bytes("WIN", encoding="utf-8"))
    except:
        pass

    server_socket.close()

    if ganamos:
        barco_local.imprimir_tableros()
        print(f"{barco_local.nombre} gano!!!")
    else:
        barco_local.imprimir_tableros()        
        print(f"{barco_local.nombre} perdio!!!")


def jugarComoCliente(cliente_socket: socket):
    barco_local  = Almirante("Cliente")
    end = False

    while (True):
        # Esperamos el primer disparo porque somos el cliente
        disparo_enemigo = cliente_socket.recv(16)
        # Comprobamos si perdemos
        if bytes(disparo_enemigo).decode("utf-8") == "WIN":
            ganamos = False
            break
        # Comprobamos si hemos ganado
        if comprobar_si_ganamos_y_avisamos(cliente_socket, barco_local):
            ganamos = True
            break
        # Al recivir disparo damos el resultado y se actualiza el tablero
        fila, columna = bytes_a_coordenadas(disparo_enemigo)
        respuesta_aliada = barco_local.recibir_disparo(fila, columna)
        # Enviamos el resultado
        cliente_socket.sendall(bytes(respuesta_aliada, encoding="utf-8"))
        barco_local.imprimir_tableros()

        # Mientras que acierten nos siguen disparando 
        while (respuesta_aliada == "T" or respuesta_aliada == "H"):
            disparo_enemigo = cliente_socket.recv(16)
            if bytes(disparo_enemigo).decode("utf-8") == "WIN":
                ganamos = False
                end = True
                break
            fila, columna = bytes_a_coordenadas(disparo_enemigo)
            respuesta_aliada = barco_local.recibir_disparo(fila, columna)
            cliente_socket.sendall(bytes(respuesta_aliada, encoding="utf-8"))

        # Terminamos si nos han ganado esperando su disparo
        if end:
            break
        # Disparamos porque el servidor fallo
        fila, columna = barco_local.elegir_coordenada_IA()
        filaLetra, columnaInt = coordenada_con_letra(fila, columna)
        cliente_socket.sendall(coordenadas_a_bytes(filaLetra, columnaInt))
        # Esperamos respuesta
        respuesta_del_enemigo = bytes(cliente_socket.recv(16)).decode("utf-8")
        # Comprobamos si hemos perdido
        if respuesta_del_enemigo == "WIN":
            ganamos = False
            break
        barco_local.actualizar_tras_disparo(respuesta_del_enemigo, fila, columna)
        barco_local.imprimir_tableros()

        # Mientras que acertemos seguimos disparando
        while (respuesta_del_enemigo == "T" or respuesta_del_enemigo == "H"):
            if comprobar_si_ganamos_y_avisamos(cliente_socket, barco_local):
                ganamos = True
                end = True
                break
            # Disparamos de nuevo
            fila, columna = barco_local.elegir_coordenada_IA()
            filaLetra, columnaInt = coordenada_con_letra(fila, columna)
            cliente_socket.sendall(coordenadas_a_bytes(filaLetra, columnaInt))
            # Esperamos respuesta
            respuesta_del_enemigo = bytes(cliente_socket.recv(16)).decode("utf-8")
            barco_local.actualizar_tras_disparo(respuesta_del_enemigo, fila, columna)
            if bytes(disparo_enemigo).decode("utf-8") == "WIN":
                ganamos = False
                end = True
                break
        
        if end:
            break
        sleep(0.1)

    # Por si no lo ha recivido
    try:
        sleep(0.5)
        if ganamos:
            cliente_socket.sendall(bytes("WIN", encoding="utf-8"))
    except:
        pass

    cliente_socket.close()
    
    if ganamos:
        barco_local.imprimir_tableros()
        print(f"{barco_local.nombre} gano!!!")
    else:
        barco_local.imprimir_tableros() 
        print(f"{barco_local.nombre} perdio!!!")


def main():
    IP = socket.gethostbyname(socket.gethostname())
    maximo_de_intentos = 1
    numero_de_intentos = 1

    while (numero_de_intentos <= maximo_de_intentos):
        print("Lanzando IP")
        # Bolean, Str
        ipLanzada = lanzarIP()

        if ipLanzada[0]:
            # Bolean, Str
            if ipLanzada[1] == "OK":
                print("OK")
                print("Abro socket TCP soy server")
                hayCliente, socket_server = levantar_server(IP)
                if hayCliente:
                    jugarComoServer(socket_server)
                else:
                    print("No se a conectado ningun cliente")
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
                    jugarComoCliente(socket_server)
                else:
                    print("No es posible conectarse")
        numero_de_intentos += 1


if __name__ == "__main__":
    main()