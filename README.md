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

Con las graficas se puede ver de una manera visual la efectividad de nuestra red, que aunque en pequeñas muestras es practicamente aleatoria a medida que se aumenta el número de muestras se estaviliza. Pero solo con una mejora del 6% frente al juego aleatorio.

Aunque cabe destacar que mientras hacia las graficas me di cuenta de que el archivo que ejecuta las pruebas ``hundir_la_flota_con_clases.py`` se salta una regla importante del juego original y es que: cuando haciertas en el juego original puedes seguir disparando hasta que falles, cosa que aqui no se contempla y no importa, el turno siempre cambia.

Esto seguramente haga que las estadisticas de la red pueda mejorar frente al rival aleatorio, pero como el punto de este repositorio no es conseguir la red más eficiente si no un "hundir la flota" que se juegue automatico haciendo uso de redes neuronales y asi hacer que yo no tenga que trabajar con malvados indices😨. Pues sera una cosa que tenga en cuenta para mis proximos proyectos y asi ver la mejora😁.

Requisitos del sistema: Si el proyecto requiere ciertos requisitos del sistema para funcionar correctamente, como una versión específica del lenguaje de programación o un sistema operativo en particular, asegúrese de incluir esa información.

Instalación: Proporcione instrucciones detalladas para instalar y configurar el proyecto en un ambiente de desarrollo. Es recomendable incluir comandos de terminal necesarios para instalar cualquier dependencia y cualquier otra configuración requerida.

Uso: Proporcione instrucciones claras sobre cómo utilizar el proyecto. Si el proyecto tiene una interfaz de usuario, proporcione capturas de pantalla y / o vídeos de demostración.

Contribución: Si está permitido, indique cómo la comunidad puede contribuir al proyecto. Incluya información sobre cómo presentar solicitudes de cambio y cómo colaborar en el desarrollo del proyecto.

Licencia: Proporcione información sobre la licencia del proyecto y cómo se puede utilizar el código.

Enlaces: Proporcione enlaces a documentación adicional, recursos útiles o cualquier otro enlace relevante relacionado con el proyecto.
