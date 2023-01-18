from tablero import genera_tablero, imprimir_tablero

def main():

    BARCOS = ((1, 4), (2, 3), (3, 2), (4, 1))
    miTablero = genera_tablero()
    imprimir_tablero(miTablero)

if __name__ == "__main__":
    main()