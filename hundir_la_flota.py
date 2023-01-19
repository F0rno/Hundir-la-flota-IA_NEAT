from tablero import genera_tablero, imprimir_tablero, coloca_barcos

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

    turno = 1

    while (True):

        # Elegir una coordenada para disparar

        elegir_coordenada()

        # Dispara y retorna (Tocado, Hundido y Agua)
        # Imprime el tablero enemigo actualizado
        break

    imprimir_tablero(jugador1_Tablero)
    imprimir_tablero(jugador2_Tablero)