from tablero    import genera_tablero, imprimir_tablero, imprimir_tablero_IA
from barcos     import coloca_barcos
from os         import system
from sys        import platform
from os         import path, getcwd
import neat
import pickle
import numpy as np
import random


class Almirante:
    def __init__(self, nombre="Isoroku Yamamoto", entrenamiento=False):
        self.nombre = "Almirante " + nombre
        self.entrenamiento = entrenamiento
        self.barcos = ((1, 4), (2, 3), (3, 2), (4, 1))
        self.tablero_aliado  = genera_tablero()
        self.tablero_enemigo = genera_tablero()
        self.coordenadas_de_barcos_aliados = coloca_barcos(self.tablero_aliado, self.barcos)
        self.inicializar_posicions_conocidas()
        self.inicializar_la_red()

    def inicializar_posicions_conocidas(self):
        self.posicions_conocidas = [(i, j) for i in range(10) for j in range(10)]
        random.shuffle(self.posicions_conocidas)

    def inicializar_la_red(self):
        if not self.entrenamiento:
            self.config_path = path.join(getcwd(), 'hundir_la_flota/config-feedforward.txt')
            self.config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, self.config_path)
            try:
                with open("hundir_la_flota/red_mamadisima.pkl", "rb") as f:
                    self.archivo_de_IA = pickle.load(f)
                    self.red_neuronal_de_disparo = neat.nn.FeedForwardNetwork.create(self.archivo_de_IA, self.config)
            except:
                raise NameError("No se pudo importar el disparo IA")      

    def algun_hundido(self, fila, columna, coordenadas_de_barcos):
        for coordenadas in coordenadas_de_barcos:
            if (fila, columna) in coordenadas:
                coordenadas.remove((fila, columna))
            if len(coordenadas) == 0:
                return True
        return False

    def elegir_coordenada_aleatoria(self):
        fila, columna = self.posicions_conocidas[-1]
        self.posicions_conocidas.pop()
        return fila, columna

    def recibir_disparo(self, fila, columna):
        if self.tablero_aliado[fila][columna] == "0":
            return "A"
        if self.tablero_aliado[fila][columna] != "0":
            if self.algun_hundido(fila, columna, self.coordenadas_de_barcos_aliados):
                return "H"
            return "T"

    def actualizar_tras_disparo(self, resultado_del_disparo, fila, columna):
        if resultado_del_disparo == "A":
            self.tablero_enemigo[fila][columna] = "1"
            
        if resultado_del_disparo == "T":
            self.tablero_enemigo[fila][columna] = "2"

        if resultado_del_disparo == "H":
            self.tablero_enemigo[fila][columna] = "2"
            #print("Hundido!")

    def imprimir_tableros(self):
        if platform == "win32":
            system("cls")
        elif platform == "linux2":
            system("clear")
        else:
            system("clear")
        print(f"--- {self.nombre}")
        print()
        imprimir_tablero_IA(self.tablero_enemigo)
        print()
        imprimir_tablero(self.tablero_aliado)

    def soy_ganador(self):
        # Este bucle anidado recorre el tableo buscando
        # barcos "T" y si cuenta el maximo dice que ha gando
        win_counter = 0
        for numero in self.tablero_enemigo:
            for letra in numero:
                if letra == "2":
                    win_counter += 1
        if win_counter == 20:
            return True
        return False

    def tablero_enemigo_para_IA(self):
        # Modifica el tablero de str a float
        # para la red neuronal
        return np.array(list(map(lambda x: list(map(float, x)), self.tablero_enemigo)), dtype=np.float32).reshape(100)
    
    def salida_de_red_a_indice(self,salida_de_la_red):
        fila = salida_de_la_red // 10
        columna = salida_de_la_red % 10
        return fila, columna

    def elegir_coordenada_IA(self):
        tablero_enemigo_numpy = self.tablero_enemigo_para_IA()
        output = self.red_neuronal_de_disparo.activate(tablero_enemigo_numpy)
        fila, columna = self.salida_de_red_a_indice(np.argmax(output))
        if (fila, columna) in self.posicions_conocidas:
            self.posicions_conocidas.remove((fila, columna))
            return fila, columna
        else:
            fila, columna = self.elegir_coordenada_aleatoria()
            return fila, columna


def jugar(ganadas_RA:list, ganadas_IA:list, display=False):
    yo = Almirante("F")
    enemigo = Almirante("Manco")

    while (True):
        # Elegir una coordenada para disparar  
        fila, columna = yo.elegir_coordenada_IA()
        resultado_del_disparo = enemigo.recibir_disparo(fila, columna)

        fila, columna = enemigo.elegir_coordenada_aleatoria()
        resultado_del_disparo = yo.recibir_disparo(fila, columna)
    
        # Actualizar mapa con (Tocado, Hundido y Agua)
        yo.actualizar_tras_disparo(resultado_del_disparo, fila, columna)
        enemigo.actualizar_tras_disparo(resultado_del_disparo, fila, columna) 

        if display:
            # Impresión de los tableros
            yo.imprimir_tableros()      

        # Combrobar si hay ganador, 20 gana
        if yo.soy_ganador():
            if display:
                yo.imprimir_tableros()
                print(f"Gana {yo.nombre}")
            ganadas_IA.append("1")
            break

        if enemigo.soy_ganador():
            ganadas_RA.append("1")
            break
                
        # Velocidad del juego
        # sleep(0.1)

if __name__ == "__main__":
    ganadas_RA = []
    ganadas_IA = []
    n_juegos = 1000
    display  = False
    for _ in range(0, n_juegos):
        jugar(ganadas_RA, ganadas_IA, display)
    print(f"Ganadas IA        : {len(ganadas_IA)}")
    print(f"Ganadas Aleatorio : {len(ganadas_RA)}")
    print()
    print(f"Ganadas IA        : {round((len(ganadas_IA)/n_juegos)*100)}% de {n_juegos} partidas")