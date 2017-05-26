import os
import sys
import copy
from termcolor import colored
import route1			
from getch_py import *
from pokemon import *

help = 	[['*', "########################",'*'],
	 			 ['#', "w - paso hacia adelante ",'#'],
				 ['#', "s - paso hacia atrás    ",'#'],
				 ['#', "a - paso a la izquierda ",'#'],
				 ['#', "d - paso a la derecha   ",'#'], 
				 ['#', "e - interactuar         ",'#'],
				 ['#', "m - abrir el menú       ",'#'],
				 ['*', "########################",'*']]						

menu = 	[['*',  "###################",'*'],
	 			 ['#',' ',"AYUDA            ",'#'],
				 ['#',' ',"POKÉDEX          ",'#'],
				 ['#',' ',"POKÉMON          ",'#'],
				 ['#',' ',"VOLVER A PARTIDA ",'#'], 
				 ['#',' ',"SALIR DEL JUEGO  ",'#'], 
				 ['*',  "###################",'*']]

menuPrincipal = [
	['*',  "###################",'*'],
	['#',' ',"                 ",'#'],
	['#',' ',"  PyOkEmOn ClI   ",'#'],
	['#',' ',"                 ",'#'],
	['#',' ',"Nueva Partida 	 ",'#'], 
	['#',' ',"Continuar        ",'#'], 
	['*',  "###################",'*']]

# opciones del menú principal
options = {'help': 1,
					 'pokedex': 2,
					 'pokemon': 3,
					 'bckgme': 4,
					 'exit': 5}

# cursor's initial position
cx = 1
cy = 1
menu[cx][cy] = '>'

# cx = 5
# cy = 1
# menuPrincipal[cx][cy] = '>'


# imprimir menú o información en recuadro, por defecto el menú principal
def print_menu(menu = menu):
	route1.clean_scr()
	cmenu = copy.deepcopy(menu)
	for fila in cmenu:
		s = " ".join(fila)
		s = colored(s, 'white')
		print(s)


# CAMBIAR
def print_pokemon ():
	print ("No hay pokémon que mostrar")

def print_pokedex ():
	if (len(pokemon_db) <= 1):
		print ("No se ha descubierto ningún pokémon")
	else: # Imprimir todos los pokémon de la base de datos
		for i in range (1, max_pokemon+1):
			if (str(i) in pokemon_db):
				route1.clean_scr()
				print(Pokemon(i))
				print("Pulse e para salir u otra tecla para siguiente Pokémon")
				if (getKey().lower() == 'e'):
					print("Pulse otra tecla para salir.")
					break;

# salir del juego
def exit_game ():
	sys.exit(1)


def next_move():
	global cx
	global cy

	while True:
		print_menu()
		pressedkey = getKey()
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
				input()

			elif (menu[options['pokedex']][1] == '>'):
				print_pokedex()
				input()

			elif (menu[options['pokemon']][1] == '>'):
				print_pokemon()
				input()

			elif (menu[options['bckgme']][1] == '>'):
				route1.next_move(route1.map)

			elif (menu[options['exit']][1] == '>'):
				exit_game()

			


	





