import menu
import route1
import modulo_dropbox
from pokemon_t import *
from entrenador import *
from interfaz import limpiarPantalla, mecanografiar
from fabulous.color import blink, fg256
from getch_py import getKey
from imagenToString import imgToStr
from pokemon import MAX_POKEMON, cargarBaseDatosPkm

ancho = 19
portadaJuego = [
	['*','#'*ancho,'*'],
	['#',' '*ancho,'#'],
	['#',"PYoKéMoN ".center(ancho),'#'],
	['#',"Edición cli".center(ancho),'#'],
	['#',' '*ancho,'#'],
	['# ',' ',"Nueva Partida".ljust(ancho-3),'#'], 
	['# ',' ',"Continuar".ljust(ancho-3),'#'], 
	['# ',' ',"Salir".ljust(ancho-3),'#'], 
	['*','#'*ancho,'*']]


# Imprime la portada del juego, por defecto
# el cursor se situa en "continuar"
def imprimePortadaJuego (cx = 6, cy = 1):
	limpiarPantalla()

	# Situar Cursor
	c = []
	# Colorear todo de blanco
	for fila in portadaJuego:
		fila = " ".join(fila)
		fila = str(fg256("white", fila))
		c.append(fila)

	c[2] = c[2].replace("PYoKéMoN", str(fg256('yellow', "PYoKéMoN")))
	c[2] = c[2].replace("#", str(fg256('white', '#')))
	c = "\n".join(c)
	print(c)
	


def introducirNombre ():
	k = "n"
	while (k != "s"):
		limpiarPantalla()
		print("Ahora dime...")
		print("¿Cómo te llamas?")
		str_nombre = input()



		if (str_nombre != "" and str_nombre != " " and str_nombre != "null"):
			limpiarPantalla()
			print("Así que te llamas " + str_nombre + ".")
			print("¿Es correcto?")
			print(" s - Sí")
			print(" n - No")
			k = str(getKey()).lower()

	limpiarPantalla()

	return str_nombre


def introducirGenero ():
	
	k = 2
	while (k not in ["0", "1"]):
		limpiarPantalla()
		print("¿Eres un chico o una chica?")
		print(" 0 - Chica")
		print(" 1 - Chico")
		k = str(getKey()).lower()

	limpiarPantalla()

	if (k == "0"):
		return CHICA
	else:
		return CHICO


def elegirPokemon ():
	int_numero = 0
	while (int_numero <= 0 or int_numero > MAX_POKEMON):
		limpiarPantalla()
		print("¿Con qué pokémon te gustaría iniciar tu aventura?")
		print("(Introduce un número del 1 al " + str(MAX_POKEMON) + ")")

		try:
			int_numero = int(input())
		except Exception as e:
			int_numero = 0
		
	limpiarPantalla()

	return int(int_numero)



def oak ():
	int_tab = 3
	limpiarPantalla()
	str_imagen = "\n" + imgToStr("oak.png", 30)
	str_imagen = str_imagen.replace("\n", "\n" + '\t'*int_tab)
	print(str_imagen)
	print("¡Hola a todos!")
	mecanografiar("¡Bienvenidos al mundo de POKéMON!")
	
	limpiarPantalla()
	str_imagen = "\n" + imgToStr("oak.png", 30)
	str_imagen = str_imagen.replace("\n", "\n" + '\t'*int_tab)
	print(str_imagen)
	print("¡Me llamo Oak!")
	mecanografiar("¡Pero la gente me llama PROFESOR POKéMON!")
	
	limpiarPantalla()
	str_imagen = "\n" + imgToStr((str(25) + ".png").lower(), 50)
	str_imagen = str_imagen.replace("\n", "\n" + '\t'*int_tab)
	print(str_imagen)
	mecanografiar("¡Este mundo está habitado por unas criaturas llamadas POKéMON!")

	limpiarPantalla()
	str_imagen = "\n" + imgToStr((str(25) + ".png").lower(), 50)
	str_imagen = str_imagen.replace("\n", "\n" + '\t'*int_tab)
	print(str_imagen)
	mecanografiar("Para algunos, los POKéMON son mascotas. Pero otros los usan para pelear")

	limpiarPantalla()
	str_imagen = "\n" + imgToStr((str(25) + ".png").lower(), 50)
	str_imagen = str_imagen.replace("\n", "\n" + '\t'*int_tab)
	print(str_imagen)
	mecanografiar("En cuanto a mi...")

	limpiarPantalla()
	str_imagen = "\n" + imgToStr((str(25) + ".png").lower(), 50)
	str_imagen = str_imagen.replace("\n", "\n" + '\t'*int_tab)
	print(str_imagen)
	mecanografiar("Estudio a los POKéMON como profesión.")





			
#### MAIN
# Iniciar el módulo dropbox
limpiarPantalla()
print("Iniciando Dropbox...")
modulo_dropbox.initDropbox()
print("Dropbox iniciado.")

# Cargar base de datos de pokémon Local
cargarBaseDatosPkm()

# Situar el cursor en la portada
portadaJuego[6][1] = '>'


# ELECCIÓN, NUEVA PARTIDA O CONTINUAR
NUEVAPARTIDA 	= 0
CONTINUAR 		= 1
eleccion = -1
cx = 6
cy = 1
while (eleccion == -1):
	imprimePortadaJuego()
	k = str(getKey()).lower()

	if (k == 'w'):
		if portadaJuego[cx-1][cy] == ' ': # hay opción arriba
			# restore empty space
			portadaJuego[cx][cy] = ' '
			# update menu with new cursor's position
			cx = cx-1
			portadaJuego[cx][cy] = '>'

	elif (k == 's'):
		if portadaJuego[cx+1][cy] == ' ': # hay opción abajo
			# restore empty space
			portadaJuego[cx][cy] = ' '
			# update menu with new cursor's position
			cx = cx+1
			portadaJuego[cx][cy] = '>'

	else: # Pulsa cualquier tecla, aceptar
		# NUEVA PARTIDA
		if (portadaJuego[5][1] == '>'):
			eleccion = NUEVAPARTIDA

		# CONTINUAR
		if (portadaJuego[6][1] == '>'):
			eleccion = CONTINUAR

		# SALIR
		if (portadaJuego[7][1] == '>'):
			menu.exit_game()


limpiarPantalla()


# EJECUTAR ELECCIÓN
Entrenador_e = ""
if (eleccion == NUEVAPARTIDA):
	oak()
	str_nombre 		= introducirNombre()
	int_genero 		= introducirGenero()
	int_pokemon 	= elegirPokemon()
	Entrenador_e 	= Entrenador(str_nombre, int_genero)
	Entrenador_e.equipar(Pokemon(int_pokemon, 75))

	guardarPartida(Entrenador_e) 


if (eleccion == CONTINUAR):
	# En realidad hay que cargar el archivo genérico, cargamos este para la demo
	print("Cargando partida " + str(blink("...")))
	#Entrenador_e = cargarPartida("chica.json")
	Entrenador_e = cargarPartida()
	mecanografiar("Partida cargada correctamente.")


limpiarPantalla()
print("Datos de la partida:")
print(Entrenador_e)
getKey()


# A la ruta 1
route1.next_move(Entrenador_e)






