import random

def comprueba_barco(tablero, fila, columna, orientacion, posiciones):
    for i in range(posiciones):
        if columna+i*(orientacion==0) >= len(tablero[0]):
            return False
        if fila+i*orientacion >= len(tablero):
            return False
        if tablero[fila+i*orientacion][columna+i*(orientacion==0)] != "0":
            return False
    return True

def coloca_barco(tablero, fila, columna, orientacion, posiciones):
    coordenada  = []
    coordenadas = []
    for i in range(posiciones):
        tablero[fila+i*orientacion][columna+i*(orientacion==0)] = str(posiciones)
        coordenada.append((fila+i*orientacion, columna+i*(orientacion==0)))
    coordenadas.append(coordenada)
    return tuple(coordenadas)

def coloca_barcos(tablero, barcos):
    coordenadas_de_barcos = []
    for numero_barcos, posiciones in barcos:
        for _ in range(numero_barcos):
            while True:
                fila = random.randint(1,10)
                columna = random.randint(1,10)
                orientacion = random.randint(0,1)
                if comprueba_barco(tablero, fila, columna, orientacion, posiciones):
                    break
            coordenadas_de_barcos += coloca_barco(tablero, fila, columna, orientacion, posiciones)
    return coordenadas_de_barcos

