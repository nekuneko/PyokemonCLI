## PyokemonCLI

Pequeño juego muy básico de línea de comandos inspirado en Pokémon creado con la intención de aprender programación orientada a objetos con el lenguaje de programación Python. Nace a partir del proyecto original "Pokémon CLI", constituyendo una evolución lógica así como una expresión de la tecnología dominada actualmente por el autor. 


Utiliza exclusívamente la sintaxis de Python 3. Actualmente sólo es compatible con OSX / macOS ejecutándose sobre una ventana de terminal a una resolucion de al menos 1600x900. 

- Última versión: 30 de Mayo de 2017.

## Librerías externas

+ numpy			(Para operaciones matemáticas y generación de números aleatorios)
+ fabulous 	(Mejores colores que "colored")
+ colored		(Más facilidad de uso para colorear matrices de caracteres)
+ zmq				(Comunicación externa)
+ json			(Para guardar las partidas y enviar datos de forma remota)
+ copy 			(Para permitir el paso de parámetros por copia)
+ os 				(Para invocar comandos externos como limpiar la pantalla o reproducir música)
+ time 			(Para dormir el programa cuando es necesario)
+ platform 	(Para detectar si el sitema es Windows)
+ dropbox 	(Para hacer uso de la plataforma)

## Dependencias de programas externos

+ mpg123 (Unix, para reproducir música mp3 en bucle en segundo plano)
+ afplay (Solo OSX, para reproducir efectos de sonido en .wav)


## Menciones especiales

+ img2txt de @hit9 (http://github.com/hit9) Adapté este programa para poder imprimir las imágenes de los personajes en formato ascii en la terminal.
+ código rebautizado como "getch_py", que saqué de un post de stackoverflow.

## Reconocimientos y agradecimientos

A todos los creadores de las librerías anteriormente mencionadas, que sin ellos este proyecto no hubiera sido posible.


## Instalación en OSX
Instalar la última versión de [Python3](https://www.python.org/). Instalar con el comando "pip3 install" todas las librerías externas mencionadas en el apartado "Librerías externas". Ejemplo: "pip3 install numpy", sin las comillas. Para instalar mpg123 instale primero [Homebrew](https://brew.sh/index_es.html) y a continuación ejecute el comando:

+ brew install mpg123


Crear en el repositorio una carpeta llamada "img" e incluir en ella el contenido de la carpeta "static".


Nota: Es necesario tener en el repositorio una carpeta llamada "sounds" con los gritos de todos los pokémon en formato .wav numerados del 1 al 386. Ejemplo: 1.wav, 28.wav, 128.wav...

## Uso

Para ejecutar el programa, abra una terminal a pantalla completa en el directorio del repositorio y a continuación ejecute:

+ python3 main.py


Los controles son los siguientes:
+ w - Mover arriba
+ s - Mover abajo
+ a - Mover a la izquierda
+ d - Mover a la derecha
+ e - Interactuar (en el mapa)
+ m - Abrir el menú (en el mapa)

Para aceptar o saltar los diálogos (⏎) basta con pulsar cualquier tecla.