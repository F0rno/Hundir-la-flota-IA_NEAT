from hundir_la_flota   import *

jugador1_Tablero        = genera_tablero()
jugador1_TableroEnemigo = genera_tablero()

jugador2_Tablero        = genera_tablero()
jugador2_TableroEnemigo = genera_tablero()

imprimir_tableros(jugador1_Tablero, jugador1_TableroEnemigo, 1)
# Inicializamos los barcos

coordenadas_de_barcos_jugador1 = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]  

def test_algun_hundido():
    coordenadas_barcos = [[(1,1)], [(2,2)]]
    assert algun_hundido(1,1, coordenadas_barcos) == True
    coordenadas_barcos = [[(1,1), (1,2)], [(2,2)]]
    assert algun_hundido(1,1, coordenadas_barcos) == False



