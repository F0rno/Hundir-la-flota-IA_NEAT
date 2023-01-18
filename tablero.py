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
            print(celda, end=" ")
        print()

# Crea tablero 10x10
# versión con listas por comprensión
def genera_tablero(filas = 10, columnas = 10):
    return [ [ " " for _ in range(columnas) ] for _ in range(filas) ]


if __name__ == "__main__":
    # versión loser
    tablero = []
    for _ in range(10):
        fila = []
        for _ in range(10):
            fila.append(" ")
        tablero.append(fila)


    imprimir_tablero(tablero)
