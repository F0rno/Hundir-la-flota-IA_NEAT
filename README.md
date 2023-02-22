# Hundir la flota (IA)

Este proyecto se basa en la creación de un juego de "Hundir la flota" que se juega de manera automatica con la característica de que el disparo (las coordenadas donde el jugador cree que está el barco enemigo) sean predichas por una red neuronal.

## Problema

Obviando la creación del juego base, tenemos el siguiente problema:
Necesitamos crear una red neuronal que decida donde deberíamos disparar en base a una entrada (input). La capas ocultas que tendra la red y la forma de la capa de salida que nos diga donde quiere disparar la red (el output de la red).

## Solución planteada

Para afrontar el problema la estructura de la red que he pensado es esta:

![This is an image](resources/red_img.png)

Con esta estructura lo que hacemos es dar como input a la red el tablero enemigo, que guarda la información que ya sabemos sobre las posiciones de barcos enemigos y como output tenemos otro "tablero" conformado por otras 100 neuronas de las cuales elegiremos la que más se active como coordenada deseada.

Aclarar que aunque en la ilustración las capas de entra/salida tienen la forma del tablero 10x10 en realidad tanto la capa de entrada como la de salida son 100 neuronas en fila, solo las represento así para que sea más visual.

Notar que no he representado la forma de las capas ocultas en la ilustración ya que para la generación de la red he usado el algoritmo [NEAT](https://neat-python.readthedocs.io/en/latest/neat_overview.html), lo que hace que no tenga mucho sentido dibujar la estructura oculta si de un entrenamiento a otro las capas ocultas pueden cambiar.

## Prueba de la solucíon

Ahora que tenemos la red para probar es hora de entrenarla, no lo he mencionado antes pero esta red sera entrenada mediante entrenamiento de refuerzo, lo que haremos sera ponerla a jugar para que consiga recompensas cuando hacierte a un barco o castigos cuando dispare al agua/repita disparo a una posición ya usada. Y asi lograr que encuentre la manera más optima para jugar, aunque ya os adelanto que en un juego tan limitado en acciones como este, junto a su gran componente de aleatoriedad no se le sacara todo el partido a nuestra red.

La podremos entrenar mediante el archivo ``entrenador.ipynb`` que es un jupyter Notebook.

Adicionalmente podemos cambiar una gran cantidad de los parametros de entrenamiento de nuestra red tales como: la función de activacion, el numero de individuos de cada población o el número de capas ocultas, junto a otros muchas más cosas en el archivo ``config-feedforward.txt``

## Resultados

Habiendo entrenado a 50 individuos en 200 generaciones estos son los resultados:

###### IA: La red entrenada

###### RA: Disparo aleatorio

![This is an image](resultado_de_partidas/10_partidas/0.png)

![This is an image](resultado_de_partidas/100_partidas/0.png)

![This is an image](resultado_de_partidas/1000_partidas/0.png)

![This is an image](resultado_de_partidas/10_000-partidas.png)

Con las graficas se pueden ver los resultados que tiene nuestra red en las partidas contra el jugador aleatorio. La efectividad en pequeñas muestras es practicamente aleatoria pero se estaviliza a medida que se aumenta el número de muestras. Eso si solo con una mejora de entorno al 6% frente al juego aleatorio.

Esto ocurre ya que en este juego en concreto el factor suerte/aleatorio esta muy presente, haciendo que  desaprovechemos la capacidad de encontrar patrones que superen al rival. Pero sigue consiguiendo que yo no tenga que trabajar con ``los malvados indices de un arreglo``, asi que para mi esto es un 10 en toda regla😁.

## Requisitos y dependencias

Este proyecto ha sido realizado usando Python 3.10, aunque puede ser utilizado por cualquier versión que pueda soportar las siguientes librerias:

neat-python
pickleshare
numpy
matplotlib

Estas pueden ser instaladas automaticamente utilizando el comando ``pip3 install -r .\requirements.txt``.

## Uso

Para probar el juego solo hay que ejecutar el archivo ``hundir_la_flota_con_clases.py``. Cuando termine las n partidas (default 100) y mostrara una grafica con las victorias.

Para jugarlo online en una misma red privada, solo hay que ejecutar ``hundir_la_flota_online.py`` en 2 equipos diferentes y mediante difusion se encontraran y empezaran a jugar.

## Licencia

## Enlaces
