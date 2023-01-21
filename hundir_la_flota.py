from tablero import genera_tablero, imprimir_tablero
from barcos  import coloca_barcos
from os      import system
from sys     import platform
from time    import sleep
import random

def algun_hundido(fila, columna, coordenadas_de_barcos):
    for coordenadas in coordenadas_de_barcos:
        if len(coordenadas) == 0:
            return True
        if (fila, columna) in coordenadas:
            coordenadas.remove((fila, columna))
    return False

def elegir_coordenada(coordenadas_usadas):
    while (True):
        fila    = random.randint(0,9)
        columna = random.randint(0,9)
        if (fila, columna) not in coordenadas_usadas:
            coordenadas_usadas.append((fila, columna))
            break
    return fila, columna

def dispara(fila, columna, tablero_enemigo, coordenadas_de_barcos_jugador):
    if tablero_enemigo[fila][columna] == " ":
        return "A"
    if tablero_enemigo[fila][columna] != " ":
        if algun_hundido(fila, columna,coordenadas_de_barcos_jugador):
            return "H"
        return "T"

def es_ganador(tablero_enemigo):
    # Este bucle anidado recorre el tableo buscando
    # barcos "T" y si cuenta el maximo dice que ha gando
    win_counter = 0
    for letra in tablero_enemigo:
        for numero in letra:
            if numero == "T":
                win_counter += 1
    if win_counter == 20:
        return True
    return False

def imprimir_tableros(tableroEnemigo, tableroJugador, turno):
    if platform == "win32":
        system("cls")
    elif platform == "linux2":
        system("clear")
    print(f"--- Jugador {turno}")
    print()
    imprimir_tablero(tableroEnemigo)
    print()
    imprimir_tablero(tableroJugador)

if __name__ == "__main__":
    barcos = ((1, 4), (2, 3), (3, 2), (4, 1))

    # Generamos los tableros de los barcos aliados
    # y los enemigos
    jugador1_Tablero        = genera_tablero()
    jugador1_TableroEnemigo = genera_tablero()

    jugador2_Tablero        = genera_tablero()
    jugador2_TableroEnemigo = genera_tablero()

    # Inicializamos los barcos
    coordenadas_de_barcos_jugador1 = coloca_barcos(jugador1_Tablero, barcos)
    coordenadas_de_barcos_jugador2 = coloca_barcos(jugador2_Tablero, barcos)

    # Variables de juego
    turno = 1
    coordenadas_usadas_jugador1 = []
    coordenadas_usadas_jugador2 = []

    while (True):
        # Elegir una coordenada para disparar
        if turno == 1:
            fila, columna = elegir_coordenada(coordenadas_usadas_jugador1)
        if turno == 2:
            fila, columna = elegir_coordenada(coordenadas_usadas_jugador2)
        
        # Dispara y retorna (Tocado, Hundido y Agua)
        if turno == 1:
            resultado_del_disparo = dispara(fila, columna, jugador2_Tablero, coordenadas_de_barcos_jugador2)

        if turno == 2:
            resultado_del_disparo = dispara(fila, columna, jugador1_Tablero, coordenadas_de_barcos_jugador1)

        # Imprime el tablero enemigo actualizado
        if resultado_del_disparo == "A":
            if turno == 1:
                jugador1_TableroEnemigo[fila][columna] = "A"

            if turno == 2:
                jugador2_TableroEnemigo[fila][columna] = "A"
            
        if resultado_del_disparo == "T":
            if turno == 1:
                jugador1_TableroEnemigo[fila][columna] = "T"

            if turno == 2:
                jugador2_TableroEnemigo[fila][columna] = "T"

        if resultado_del_disparo == "H":
            if turno == 1:
                jugador1_TableroEnemigo[fila][columna] = "T"
                print("Hundido!")

            if turno == 2:
                jugador2_TableroEnemigo[fila][columna] = "T"
                print("Hundido!")

        # Impresión de los tableros
        if turno == 1:
            imprimir_tableros(jugador1_TableroEnemigo, jugador1_Tablero, turno)

        if turno == 2:
            imprimir_tableros(jugador2_TableroEnemigo, jugador2_Tablero, turno)

        # Combrobar si hay ganador, 20 gana
        if turno == 1:
            if es_ganador(jugador1_TableroEnemigo):
                print("Gana el jugador 1")
                break

        if turno == 2:
            if es_ganador(jugador2_TableroEnemigo):
                print("Gana el jugador 2")
                break

        # Cambio de turno
        if turno == 1:
            turno = 2
        elif turno == 2:
            turno = 1
                
        # Velocidad del juego
        #sleep(0.1)