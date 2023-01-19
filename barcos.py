import random
from tablero import genera_tablero, imprimir_tablero

def comprueba_barco(tablero, fila, columna, orientacion, posiciones):
    for i in range(posiciones):
        if columna+i*(orientacion==0) >= len(tablero[0]):
            return False
        if fila+i*orientacion >= len(tablero):
            return False
        if tablero[fila+i*orientacion][columna+i*(orientacion==0)] != " ":
            return False
    return True

def coloca_barco(tablero, fila, columna, orientacion, posiciones):
    coordenada  = []
    coordenadas = []
    for i in range(posiciones):
        tablero[fila+i*orientacion][columna+i*(orientacion==0)] = str(posiciones)
        coordenada.append((fila+i*orientacion, columna+i*(orientacion==0)))
        #print(f"{posiciones}: fila: {fila+i*orientacion}, columna: {columna+i*(orientacion==0)}")
    #print()
    coordenadas.append(coordenada)
    return tuple(coordenadas)

def coloca_barcos(tablero, barcos):
    coordenas_de_barcos = ()
    for numero_barcos, posiciones in barcos:
        for _ in range(numero_barcos):
            while True:
                fila = random.randint(1,10)
                columna = random.randint(1,10)
                orientacion = random.randint(0,1)
                if comprueba_barco(tablero, fila, columna, orientacion, posiciones):
                    break
            coordenas_de_barcos += coloca_barco(tablero, fila, columna, orientacion, posiciones)
    return coordenas_de_barcos

def algun_hundido(coordenas_de_barcos):
    for coordenadas in coordenas_de_barcos:
        if len(coordenadas) == 0:
            return True
    return False

if __name__ == "__main__":
    barcos = ((1, 4), (2, 3), (3, 2), (4, 1))

    miTablero = genera_tablero()
    coordenas_de_barcos = coloca_barcos(miTablero, barcos)
    algun_hundido(coordenas_de_barcos)
    imprimir_tablero(miTablero)