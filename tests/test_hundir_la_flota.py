from hundir_la_flota.hundir_la_flota   import *

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



