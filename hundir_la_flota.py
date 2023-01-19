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

def elegir_coordenada():
    fila = random.randint(0,9)
    columna = random.randint(0,9)
    return fila, columna

def dispara(fila, columna, tablero_enemigo, coordenadas_de_barcos_jugador):
    if tablero_enemigo[fila][columna] == " ":
        return "A"
    if tablero_enemigo[fila][columna] != " ":
        if algun_hundido(fila, columna,coordenadas_de_barcos_jugador):
            return "H"
        return "T"

def imprimir_tableros(tableroEnemigo, tableroJugador):
    if platform == "win32":
        system("cls")
    elif platform == "linux2":
        system("clear")

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
    contador_de_hundidos_juagor1 = 0
    contador_de_hundidos_juagor2 = 0

    while (True):
        # Elegir una coordenada para disparar
        fila, columna = elegir_coordenada()
        
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
                contador_de_hundidos_juagor1 += 1
                print("Hundido!")

            if turno == 2:
                jugador2_TableroEnemigo[fila][columna] = "T"
                contador_de_hundidos_juagor2 += 1
                print("Hundido!")

        # Combrobar si hay ganador, 10 gana
        if contador_de_hundidos_juagor1 == 10:
            print("Gana el jugador 1")
            break

        if contador_de_hundidos_juagor2 == 10:
            print("Gana el jugador 2")
            break

        # Impresión de los tableros
        if turno == 1:
            imprimir_tableros(jugador1_TableroEnemigo, jugador1_Tablero)

        if turno == 2:
            imprimir_tableros(jugador1_TableroEnemigo, jugador1_Tablero)

        # Cambio de turno
        if turno == 1:
            turno = 2
        
        if turno == 2:
            turno = 1
        
        # Velocidad del juego
        sleep(0.5)