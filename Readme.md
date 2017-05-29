## PyokemonCLI
Pequeño juego muy básico de línea de comandos inspirado en Pokémon creado con la intención de aprender programación orientada a objetos con el lenguaje de programación Python. Nace a partir del proyecto original **Pokémon CLI**, constituyendo una evolución lógica así como una expresión de la tecnología dominada actualmente por el autor. 


Utiliza exclusívamente la sintaxis de **Python 3** y actualmente sólo es compatible con OSX / macOS ejecutándose sobre una ventana de terminal a una resolucion de al menos 1600x900. 

- **Última versión:** 30 de Mayo de 2017.


## Librerías externas
+ **numpy**			(Para operaciones matemáticas y generación de números aleatorios)
+ **fabulous** 	(Mejores colores que "colored")
+ **colored**		(Más facilidad de uso para colorear matrices de caracteres)
+ **zmq**				(Comunicación externa)
+ **json**			(Para guardar las partidas y enviar datos de forma remota)
+ **copy** 			(Para permitir el paso de parámetros por copia)
+ **os** 				(Para invocar comandos externos como limpiar la pantalla o reproducir música)
+ **time** 			(Para dormir el programa cuando es necesario)
+ **platform** 	(Para detectar si el sitema es Windows)
+ **dropbox** 	(Para hacer uso de la plataforma)


## Dependencias de programas externos
+ **mpg123** (Unix, para reproducir música mp3 en bucle en segundo plano)
+ **afplay** (Solo OSX, para reproducir efectos de sonido en .wav)


## Menciones especiales
+ **img2txt** de @hit9 (http://github.com/hit9) Adapté este programa para poder imprimir las imágenes de los personajes en formato ascii en la terminal.
+ código rebautizado como **getch_py**, que saqué de un post de stackoverflow.


## Reconocimientos y agradecimientos
A todos los creadores de las librerías anteriormente mencionadas, que sin ellos este proyecto no hubiera sido posible.


## Instalación en OSX
0. Clonar este repositorio.
1. Instalar la última versión de [Python3](https://www.python.org/). 
2. Instalar con el comando **pip3 install** todas las librerías externas mencionadas en el apartado **Librerías externas**. Por ejemplo: 

+ **pip3 install numpy**. 


3. Instalar **mpg123**, para ello instale primero [Homebrew](https://brew.sh/index_es.html) y a continuación ejecute el comando:

+ **brew install mpg123**


4. Crear en el repositorio una carpeta llamada **img** e incluir en ella todo el contenido de la carpeta **static**, que contine las imágenes básicas para el correcto funcionamiento del juego.


Nota: En el caso de que se quiera utilizar el módulo de música, es necesario tener en el repositorio una carpeta llamada **sounds** con los gritos de todos los pokémon en formato .wav numerados del 1 al 386. Ejemplo: 1.wav, 28.wav, 128.wav... También deberá haber un archivo especial 0.wav para el grito del pokémon comodín MissignNo. que aparece cuando no se encuentra registrado el pokémon en dropbox o en la base de datos local.


## Configuración
Si su sistema no dispone de los programas **afplay** o **mpg123**, puede deshabilitar el módulo de música comentando la línea **musica.initMusica()**, situada al comienzo del fichero **main.py**. Si dispone de otros reproductores de audio, puede modificar el archivo **musica.py** para hacer uso de ellos y adaptarlos a su sistema. Igualmente, si no desea o no puede usar la funcionalidad de pokédex en la nube con dropbox, puede comentar la línea **modulo_dropbox.initDropbox()** al comienzo del mismo fichero **main.py**.



## Uso
Para ejecutar el programa, abra una terminal a pantalla completa en el directorio del repositorio y a continuación ejecute:

+ **python3 main.py**


Los controles son los siguientes:
+ w - Mover arriba
+ s - Mover abajo
+ a - Mover a la izquierda
+ d - Mover a la derecha
+ e - Interactuar (en el mapa)
+ m - Abrir el menú (en el mapa)

Para aceptar o saltar los diálogos (⏎) basta con pulsar cualquier tecla.