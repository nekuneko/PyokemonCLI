import os
import sys
import copy
from termcolor import colored
import route1			


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
	print ("No se ha descubierto ningún pokémon")

# salir del juego
def exit_game ():
	sys.exit(1)


def next_move():
	global cx
	global cy

	while True:
		print_menu()
		pressedkey = input() 
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

		elif pressedkey == '':
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

			


	





