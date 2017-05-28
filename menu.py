import sys
import copy
import route1			
from getch_py import getKey
from pokemon import *
from interfaz import *
from entrenador import guardarPartida
from fabulous.color import fg256, blink

help = 	[['*', "########################",'*'],
	 			 ['#', "w - paso hacia adelante ",'#'],
				 ['#', "s - paso hacia atrás    ",'#'],
				 ['#', "a - paso a la izquierda ",'#'],
				 ['#', "d - paso a la derecha   ",'#'], 
				 ['#', "e - interactuar         ",'#'],
				 ['#', "m - abrir el menú       ",'#'],
				 ['*', "########################",'*']]						

menu = 	[['*',  "#####################",'*'],
	 			 ['#',' ',"AYUDA              ",'#'],
				 ['#',' ',"POKÉDEX            ",'#'],
				 ['#',' ',"POKÉMON            ",'#'],
				 ['#',' ',"VOLVER A PARTIDA   ",'#'], 
				 ['#',' ',"GUARDAR PARTIDA    ",'#'], 
				 ['#',' ',"SALIR DEL JUEGO    ",'#'], 
				 ['*',  "#####################",'*']]



# opciones del menú principal
options = {'help': 1,
					 'pokedex': 2,
					 'pokemon': 3,
					 'bckgme': 4,
					 'save': 5,
					 'exit': 6}

# cursor's initial position
cx = 1
cy = 1
menu[cx][cy] = '>'

# cx = 5
# cy = 1
# menuPrincipal[cx][cy] = '>'


# imprimir menú o información en recuadro, por defecto el menú principal
# el menu ha de ser una lista de listas de cadenas de caracteres
def print_menu(menu = menu):
	limpiarPantalla()
	cmenu = copy.deepcopy(menu)
	for fila in cmenu:
		s = " ".join(fila)
		s = fg256('white', s)
		print(s)



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


def print_pokedex ():
	if (len(pokemon_db) <= 1):
		print ("No se ha descubierto ningún pokémon")
	else: # Imprimir todos los pokémon de la base de datos
		for i in range (1, MAX_POKEMON+1):
			if (str(i) in pokemon_db):
				limpiarPantalla()
				print(Pokemon(i))
				print("Pulse e para salir u otra tecla para siguiente Pokémon")
				if (getKey().lower() == 'e'):
					print("Pulse otra tecla para salir.")
					break;
	getKey()

# salir del juego
def exit_game ():
	sys.exit(0)


def next_move(Entrenador_e):
	global cx
	global cy

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
				route1.next_move(Entrenador_e)

			elif (menu[options['save']][1] == '>'):
				limpiarPantalla()
				print("Guardando la partida"+str(blink("...")))
				print("No apagues la consola.")
				guardarPartida(Entrenador_e)
				mecanografiar("Partida guardada correctamente.")
				
			elif (menu[options['exit']][1] == '>'):
				exit_game()

			


	





