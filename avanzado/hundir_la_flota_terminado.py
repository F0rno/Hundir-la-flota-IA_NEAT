import random
import time

# Dimensiones del tablero
BOARD_WIDTH = 10
BOARD_HEIGHT = 10

# Número de barcos por jugador
NUM_SHIPS = 5

# Nombres de los barcos
SHIP_NAMES = ['Portaaviones', 'Acorazado', 'Crucero', 'Submarino', 'Destructor']

# Valor para representar el agua en el tablero
WATER = ' '

# Valor para representar un barco tocado en el tablero
HIT = 'X'

# Valor para representar un fallo en el tablero
MISS = 'O'


def init_board(width, height):
    """Crea un tablero vacío con las dimensiones especificadas"""
    board= [[" " for _ in range(width)] for _ in range(height)]
    return board

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
    for i in range(posiciones):
        tablero[fila+i*orientacion][columna+i*(orientacion==0)] = str(posiciones)
        #print(f"fila:{fila+i*orientacion}, columna:{columna+i*(orientacion==0)}")

def coloca_barcos(tablero, barcos):
    for numero_barcos, posiciones in barcos:
        for _ in range(numero_barcos):
            while True:
                fila = random.randint(1,10)
                columna = random.randint(1,10)
                orientacion = random.randint(0,1)
                if comprueba_barco(tablero, fila, columna, orientacion, posiciones):
                    break
            coloca_barco(tablero, fila, columna, orientacion, posiciones)

def attack(board, row, col):
    """Realiza un ataque a la posición especificada del tablero y devuelve el resultado"""
    if board[row][col] != WATER:
        board[row][col] = HIT
        return True
    else:
        board[row][col] = MISS
        return False


def check_sunk(board, ship_positions):
    """Verifica si un barco ha sido hundido"""
    for row, col in ship_positions:
        if board[row][col] != HIT:
            return False
    return True


def check_win(boards):
    """Verifica si un jugador ha ganado"""
    for board in boards:
        for row in board:
            if WATER in row:
                return False
    return True


def print_board(board):
    """Muestra el tablero por pantalla"""
    columnas = " ABCDEFGHIJ"
    print(" ", end="")
    for letra in columnas:
        print(letra, end=" ")
    print()
    for orden, fila in enumerate(board):
        #print(orden+1, end=" "+(" " if orden+1<10 else ""))
        print(orden+1, end=" ")
        if orden+1<10:
            print(" ", end="")
        for celda in fila:
            print(celda, end=" ")
        print()


def main():
    # Inicializar tableros
    board1 = init_board(BOARD_WIDTH, BOARD_HEIGHT)
    board2 = init_board(BOARD_WIDTH, BOARD_HEIGHT)

    # Barcos
    barcos = ((1, 4), (2, 3), (3, 2), (4, 1))

    # Colocar barcos
    ships1 = coloca_barcos(board1, barcos)
    ships2 = coloca_barcos(board2, barcos)

    # Column dictionary
    colDictionary = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 10
    }

    # Bucle principal del juego
    current_player = 1
    while True:
        try:
            # Mostrar tablero del oponente
            print(f'Tablero del jugador {current_player}:')
            print_board(board1 if current_player == 1 else board2)

            # Solicitar ataque
            print(f'Turno del jugador {current_player}')
            row = int(input('Ingrese fila: ')) - 1
            if row < 1 or row > 10:
                raise NameError("Fila no valida")
            col = input('Ingrese columna: ').upper()
            if col not in colDictionary:
                raise NameError("Columna no valida")
            col = colDictionary[col]

            # Realizar ataque y mostrar resultado
            board = board1 if current_player == 2 else board2
            result = attack(board, row, col)
            if result:
                print('¡Tocado!')
                sunk = check_sunk(board, ships1 if current_player == 2 else ships2)
                if sunk:
                    print(f'¡Has hundido el {SHIP_NAMES[board[row][col]]}!')
            else:
                print('¡Agua!')

            # Verificar si algún jugador ha ganado
            if check_win([board1, board2]):
                print(f'¡El jugador {current_player} ha ganado!')
                break

            # Cambiar turno
            current_player = 1 if current_player == 2 else 2
            print()
            time.sleep(1)
        except Exception as error:
            print(error)


# Iniciar juego
main()