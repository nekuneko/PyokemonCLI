import sys
import copy
import route1			
import modulo_dropbox
from getch_py import getKey
from pokemon import *
from interfaz import *
from entrenador import guardarPartida
from fabulous.color import fg256, blink

help = [
	['*', "########################",'*'],
	['#', "w - Paso hacia adelante ",'#'],
	['#', "s - Paso hacia atrás    ",'#'],
	['#', "a - Paso a la izquierda ",'#'],
	['#', "d - Paso a la derecha   ",'#'], 
	['#', "e - Interactuar         ",'#'],
	['#', "m - Abrir el menú       ",'#'],
	['*', "########################",'*']]						

menu = [
	['*',  "#####################",'*'],
	['#',' ',"AYUDA              ",'#'],
	['#',' ',"POKéDEX            ",'#'],
	['#',' ',"POKéMON            ",'#'],
	['#',' ',"GUARDAR PARTIDA    ",'#'], 
	['#',' ',"OPCIONES           ",'#'],
	['#',' ',"VOLVER A PARTIDA   ",'#'], 
	['#',' ',"SALIR DEL JUEGO    ",'#'], 
	['*',  "#####################",'*']]

dropbox = [
	['*',  "#####################",'*'],
	['#',	 "                     ",'#'],
	['#',	 "       DropBox       ",'#'],
	['#',	 "                     ",'#'],
	['#',' ',"ACTIVAR            ",'#'],
	['#',' ',"DESACTIVAR         ",'#'],
	['#',' ',"VOLVER             ",'#'], 
	['*',  "#####################",'*']]


# opciones del menú principal
options = {
	'help': 1,
	'pokedex': 2,
	'pokemon': 3,
	'save': 4,
	'dropbox': 5,
	'bckgme': 6,
	'exit': 7}
					 


# imprimir menú o información en recuadro, por defecto el menú principal
# el menu ha de ser una lista de listas de cadenas de caracteres
# colorea el menú en blanco
def print_menu(menu = menu):
	limpiarPantalla()
	cmenu = copy.deepcopy(menu)
	for fila in cmenu:
		s = " ".join(fila)
		s = fg256('white', s)
		print(s)



# Imprime el equipo pokémon del eentrenador
def imprimirEquipo (Entrenador_e):
	#print ("No hay pokémon que mostrar")
	seleccion = 0
	while(seleccion != -1):
		limpiarPantalla()
		print(Entrenador_e.listarEquipo())

		try:
			seleccion = int(getKey())
		except Exception as e:
			seleccion = -1

		if (0 <= seleccion and seleccion <= len(Entrenador_e.equipo)):
			limpiarPantalla()
			print(Entrenador_e.equipo[seleccion])
			getKey()


# Imprime todos los pokémon de la base de datos local
def print_pokedex ():
	limpiarPantalla()
	if (len(pokemon_db) <= 1):
		print ("No se ha descubierto ningún pokémon")
	else: # Imprimir todos los pokémon de la base de datos
		for i in range (1, MAX_POKEMON+1):
			if (str(i) in pokemon_db):
				limpiarPantalla()
				print(Pokemon(i))
				print("Pulse 'e' para salir u otra tecla para siguiente Pokémon")
				if (getKey().lower() == 'e'):
					print("Pulse otra tecla para salir.")
					break;
	getKey()



# salir del juego
def exit_game ():
	sys.exit(0)

def print_dropbox ():
	# cursor's initial position
	cx = 4
	cy = 1
	dropbox[cx][cy] = '>'

	k = 's'
	while (k == 'w' or k == 's'):
		limpiarPantalla()
		print_menu(dropbox)
		k = str(getKey()).lower()

		if (k == 'w'):
			if dropbox[cx-1][cy] == ' ': # hay opción arriba
				# restore empty space
				dropbox[cx][cy] = ' '
				# update menu with new cursor's position
				cx = cx-1
				dropbox[cx][cy] = '>'


		elif (k == 's'):
			if dropbox[cx+1][cy] == ' ': # hay opción abajo
				# restore empty space
				dropbox[cx][cy] = ' '
				# update menu with new cursor's position
				cx = cx+1
				dropbox[cx][cy] = '>'

		else: # Se pulsa una tecla
			# ACTIVAR
			if dropbox[4][1] == '>':
				limpiarPantalla()
				print("Activando Dropbox...")
				modulo_dropbox.initDropbox()
				mecanografiar("Dropbox activado.")

				k = 's' # No se sale del menú

			# DESACTIVAR
			elif dropbox[5][1] == '>':
				limpiarPantalla()
				print("Desactivando Dropbox...")
				try:
					modulo_dropbox.bool_usaDropbox = False
				except Exception as e:
					pass

				mecanografiar("Dropbox desactivado.")

				k = 's' # No se sale del menú

			# SALIR
			elif dropbox[6][1] == '>':
				dropbox[cx][cy] = ' '
				limpiarPantalla()

	


def next_move(Entrenador_e):
	# cursor's initial position
	cx = 1
	cy = 1
	menu[cx][cy] = '>'
	
	while True:
		print_menu()
		pressedkey = str(getKey()).lower()
		if pressedkey == 'w':
			if menu[cx-1][cy] == ' ': # hay opción arriba
				# restore empty space
				menu[cx][cy] = ' '
				# update menu with new cursor's position
				cx = cx-1
				menu[cx][cy] = '>'
				print_menu()

		elif pressedkey == 's':
			if menu[cx+1][cy] == ' ': # hay opción abajo
				# restore empty space
				menu[cx][cy] = ' '
				# update menu with new cursor's position
				cx = cx+1
				menu[cx][cy] = '>'
				print_menu()

		else: # pressedkey == '\n':
			if (menu[options['help']][1] == '>'):
				print_menu(help)
				getKey()

			elif (menu[options['pokedex']][1] == '>'):
				print_pokedex()

			elif (menu[options['pokemon']][1] == '>'):
				imprimirEquipo(Entrenador_e)

			elif (menu[options['bckgme']][1] == '>'):
				menu[cx][cy] = ' '
				route1.next_move(Entrenador_e)

			elif (menu[options['save']][1] == '>'):
				limpiarPantalla()
				print("Guardando la partida"+str(blink("...")))
				print("No apagues la consola.")
				guardarPartida(Entrenador_e)
				mecanografiar("Partida guardada correctamente.")
				
			elif (menu[options['exit']][1] == '>'):
				limpiarPantalla()
				print("Fin de la Partida")
				print("Gracias por jugar :D")

				# Guardar base de datos de pokemon y salir
				guardarBaseDatosPkm()
				exit_game()

			elif (menu[options['dropbox']][1] == '>'):
				print_dropbox()

			


	





