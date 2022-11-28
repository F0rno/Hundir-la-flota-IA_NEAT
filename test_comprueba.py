import aleatorio
from matrices import genera_tablero


def test_comprueba_barcos():
    tablero = genera_tablero(3,3)
    tablero[0][0] = "B"

    # Barco tamaño 1 horizontal
    assert aleatorio.comprueba_barco(tablero, fila=1, columna=1, 
                                     orientacion=0, posiciones=1) == True
    assert aleatorio.comprueba_barco(tablero, fila=0, columna=0, 
                                     orientacion=0, posiciones=1) == False

    # Barco tamaño 2 horizontal
    assert aleatorio.comprueba_barco(tablero, fila=1, columna=1, 
                                     orientacion=0, posiciones=2) == True

    tablero = genera_tablero(3,3)    
    tablero[0][1] = "B"
    assert aleatorio.comprueba_barco(tablero, fila=0, columna=0, 
                                     orientacion=0, posiciones=2) == False

    # Barco fuera tablero
    assert aleatorio.comprueba_barco(tablero, fila=0, columna=2, 
                                     orientacion=0, posiciones=2) == False
    assert aleatorio.comprueba_barco(tablero, fila=2, columna=0, 
                                     orientacion=1, posiciones=2) == False
