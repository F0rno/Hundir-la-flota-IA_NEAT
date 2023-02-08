import random

def imprimir_tablero(tablero):
    columnas = " ABCDEFGHIJ"
    print(" ", end="")
    for letra in columnas:
        print(letra, end=" ")
    print()
    for orden, fila in enumerate(tablero):
        #print(orden+1, end=" "+(" " if orden+1<10 else ""))
        print(orden+1, end=" ")
        if orden+1<10:
            print(" ", end="")
        for celda in fila:
            if celda == "0":
                print(" ", end=" ")
            else:
                print(celda, end=" ")
        print()

def imprimir_tablero_IA(tablero):
    columnas = " ABCDEFGHIJ"
    print(" ", end="")
    for letra in columnas:
        print(letra, end=" ")
    print()
    for orden, fila in enumerate(tablero):
        #print(orden+1, end=" "+(" " if orden+1<10 else ""))
        print(orden+1, end=" ")
        if orden+1<10:
            print(" ", end="")
        for celda in fila:
            if celda == "0":
                print("~", end=" ")
            elif celda == "1":
                print(" ", end=" ")
            else:
                print("T", end=" ")
        print()

# Crea tablero 10x10
# versión con listas por comprensión
def genera_tablero(filas = 10, columnas = 10):
    return [ [ "0" for _ in range(columnas) ] for _ in range(filas) ]


if __name__ == "__main__":
    # versión loser
    tablero = []
    for _ in range(10):
        fila = []
        for _ in range(10):
            fila.append(" ")
        tablero.append(fila)

    tablero[9][9] = "x"
    print(tablero[9][9])
    imprimir_tablero(tablero)
