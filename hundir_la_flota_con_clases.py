"""
Este modulo ejecuta n partidas el juego de hundir la flota 
y muestra los resultados por una grafica
"""
from hundir_la_flota.tablero    import genera_tablero, imprimir_tablero, imprimir_tablero_IA
from hundir_la_flota.barcos     import coloca_barcos
from os         import system, path, getcwd
from sys        import platform, path
import matplotlib.pyplot as plt
import numpy as np
import pickle
import random
import neat


class Almirante:
    """
    Representa a un jugador de hundir la flota con sus tablero
    y la capacidad de elegir donde disparar
    """
    def __init__(self, nombre="Isoroku Yamamoto", entrenamiento=False, nombre_archivo_red_entrenada="red_entrenada"):
        """
        La clase de normal se instancia para jugar haciendo que se abra el archivo entrenado predeterminado,
        pero si se la quire usar para entrenar no cargara el archivo inhabilitando el disparo IA
        """
        self.nombre = "Almirante " + nombre
        self.nombre_archivo_red_entrenada = nombre_archivo_red_entrenada
        self.entrenamiento = entrenamiento
        self.barcos = ((1, 4), (2, 3), (3, 2), (4, 1))
        self.tablero_aliado  = genera_tablero()
        self.tablero_enemigo = genera_tablero()
        self.coordenadas_de_barcos_aliados = coloca_barcos(self.tablero_aliado, self.barcos)
        self.inicializar_posicions_conocidas()
        self.inicializar_la_red()

    def inicializar_posicions_conocidas(self):
        """Inicializamos las posibles coordenadas donde disparar"""
        self.posicions_conocidas = [(i, j) for i in range(10) for j in range(10)]
        random.shuffle(self.posicions_conocidas)

    def inicializar_la_red(self):
        """Abrimos el archivo donde esta la red neuronal entrenada para disparar"""
        if not self.entrenamiento:
            self.config_path = 'config-feedforward.txt'
            self.config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, self.config_path)
            try:
                with open(f"{self.nombre_archivo_red_entrenada}.pkl", "rb") as f:
                    self.archivo_de_IA = pickle.load(f)
                    self.red_neuronal_de_disparo = neat.nn.FeedForwardNetwork.create(self.archivo_de_IA, self.config)
            except:
                raise NameError("No se pudo importar el archivo con la red entrenada")      

    def algun_hundido(self, fila, columna, coordenadas_de_barcos):
        """Comprobamos si nos han hundido un barco"""
        for coordenadas in coordenadas_de_barcos:
            if (fila, columna) in coordenadas:
                coordenadas.remove((fila, columna))
            if len(coordenadas) == 0:
                return True
        return False

    def elegir_coordenada_aleatoria(self):
        """
        Elegimos una coordenada de manera aleatoria y la devolvemos la fila y columna
        """
        fila, columna = self.posicions_conocidas[-1]
        self.posicions_conocidas.pop()
        return fila, columna

    def recibir_disparo(self, fila, columna):
        """Devolvemos si nos han dado en agua o en un barco"""
        if self.tablero_aliado[fila][columna] == "0":
            return "A"
        if self.tablero_aliado[fila][columna] != "0":
            return "T"

    def actualizar_tras_disparo(self, resultado_del_disparo, fila, columna):
        """Actualizamos la matriz del tablero enemigo para saber como vamos"""
        if resultado_del_disparo == "A":
            self.tablero_enemigo[fila][columna] = "1"
            
        if resultado_del_disparo == "T":
            self.tablero_enemigo[fila][columna] = "2"

        if resultado_del_disparo == "H":
            self.tablero_enemigo[fila][columna] = "2"

    def imprimir_tableros(self):
        """Imprimimos el tablero por terminal"""
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
        """Recorremos el tablero enemigo para saber si hemos tocado todos los barcos"""
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
        """Convertimos el tablero a un formato que la red neuronal pueda procesar"""
        # Modifica el tablero de str a float
        # para la red neuronal
        return np.array(list(map(lambda x: list(map(float, x)), self.tablero_enemigo)), dtype=np.float32).reshape(100)
    
    def salida_de_red_a_indice(self,salida_de_la_red):
        """
        Convertimos una posición de un vector de 100 elementos
        a unas coordenadas para una matriz de 10x10
        """
        fila = salida_de_la_red // 10
        columna = salida_de_la_red % 10
        return fila, columna

    def elegir_coordenada_IA(self):
        """
        Pasamos el tablero enemigo por la red neuronal para
        que haga la predicción del siguiente disparo
        """
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
    """Ejecutamos una partida con 2 almirantes 1 con IA y otro Aelatroio y vemos el resultado"""
    yo = Almirante("IA")
    enemigo = Almirante("Ramdon")
    # Variable de juego
    turno = 1
    global ganadas_IA_contador, ganadas_RA_contador

    while (True):

        # Combrobar si hay ganador, 20 gana
        if turno == 1:
            if yo.soy_ganador():
                if display:
                    yo.imprimir_tableros()
                    print(f"Gana {yo.nombre}")
                ganadas_IA_contador += 1
                ganadas_IA.append(ganadas_IA_contador)
                ganadas_RA.append(ganadas_RA_contador)
                break
        
        if turno == 2:
            if enemigo.soy_ganador():
                ganadas_RA_contador += 1
                ganadas_RA.append(ganadas_RA_contador)
                ganadas_IA.append(ganadas_IA_contador)
                break

        # Elegir una coordenada para disparar
        if turno == 1:
            fila, columna = yo.elegir_coordenada_IA()
            resultado_del_disparo = enemigo.recibir_disparo(fila, columna)

        if turno == 2:
            fila, columna = enemigo.elegir_coordenada_aleatoria()
            resultado_del_disparo = yo.recibir_disparo(fila, columna)
    
        # Actualizar mapa con (Tocado, Hundido y Agua)
        if turno == 1:
            yo.actualizar_tras_disparo(resultado_del_disparo, fila, columna)
            # Si tocamos un barco seguimos disparando
            if resultado_del_disparo == "T":
                continue

        if turno == 2:
            enemigo.actualizar_tras_disparo(resultado_del_disparo, fila, columna)
            # Si tocamos un barco seguimos disparando
            if resultado_del_disparo == "T":
                continue

        if display:
            # Impresión de los tableros
            yo.imprimir_tableros()      

        # Cambio de turno    
        if turno == 1:
            turno = 2
        elif turno == 2:
            turno = 1

        # Velocidad del juego
        # sleep(0.1)


global ganadas_IA_contador, ganadas_RA_contador


def pintarGrafica(ganadas_IA, ganadas_RA, numero_de_partidas):
    """Pintamos la grafica con los datos de la partida"""
    x = [_ for _ in range(0,numero_de_partidas)]
    y1 = ganadas_IA
    y2 = ganadas_RA

    # Graficar dos líneas en la misma figura
    plt.plot(x, y1, label="IA")
    plt.plot(x, y2, label="RA")

    # Titulo de la grafica
    plt.title(f"Ganadas IA {round((ganadas_IA[-1]/numero_de_partidas)*100)}% de {numero_de_partidas} partidas")

    # Agregar la leyenda
    plt.legend()

    # Agregar etiquetas a los ejes
    plt.xlabel("Partidas")
    plt.ylabel("Victorias")

    plt.show()


def main():
    """Ejecutamos n juegos y guardamos los resultados para graficarlos"""
    global ganadas_IA_contador, ganadas_RA_contador
    ganadas_IA_contador = 0
    ganadas_RA_contador = 0
    ganadas_RA = []
    ganadas_IA = []
    n_juegos = 100
    display  = False

    for _ in range(0, n_juegos):
        jugar(ganadas_RA, ganadas_IA, display)

    pintarGrafica(ganadas_IA, ganadas_RA, n_juegos)


if __name__ == "__main__":
    main()
