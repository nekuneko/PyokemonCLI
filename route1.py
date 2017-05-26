import os
import platform
import copy
import menu
from numpy import random
from fabulous.color import blink, plain
from colored import fg, bg, attr
import modulo_zmq
import modulo_dropbox
from pokemon import *
from getch_py import *
from interfaz import *

						
				# 0   1   2   3   4   5   6   7   8   9  10   11  
map = {	0:	['#',' ',' ',' ','#','x','x','#',' ',' ',' ','#'], 
				1:	['#','#','#','#','#',' ',' ','#','#','#','#','#'],
				2:	['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
				3:	['#',' ',' ',' ','*',' ',' ',' ',' ',' ',' ','#'],
				4:	['#','-','-','-','*','-','-','-',' ',' ',' ','#'],
				5:	['*',' ',' ',' ','*','w','w','w','w','w','w','*'],
				6:	['*',' ',' ',' ','*','w','w','w','w','w','w','*'],
				7:	['*','-','-','-','*','w','w','w','w','w','w','*'],
				8:	['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
				9:	['*',' ',' ',' ',' ',' ',' ',' ','w','w','w','*'],
				10:	['*','#','-','-','-','#','#','#','w','w','w','*'],	# ^
				11:	['#',' ',' ',' ',' ',' ',' ',' ','w','w','w','#'],	# |
				12:	['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],	# x
				13:	['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],	# |
				14:	['#',' ','-','-',' ','-','-','-','-','-','-','#'],	# v
				15:	['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
				16:	['#',' ',' ',' ',' ',' ',' ','w','w','w',' ','#'],
				17:	['#','*','*','*','*','*','*','w','w','w','-','#'],
				18:	['#',' ',' ',' ',' ',' ',' ','w','w','w',' ','#'],
				19:	['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
				20:	['#','-',' ',' ','i','-','-','-','-','-','-','#'],
				21:	['*',' ','w','w','w',' ',' ',' ','w','w','w','*'],
				22:	['*','w','w','w',' ',' ',' ','w','w','w',' ','*'],
				23:	['*','#','#','#','#','w','w','#','#','#','#','*'],
				24:	['*',' ',' ',' ','#','w','w','#',' ',' ',' ','*'],
				25:	['*',' ',' ',' ','#','x','x','#',' ',' ',' ','*']}
				# <-------------------------y------------------------>

# casillas que no puede pisar el personaje
forbidden_cell = {'wall':		'#',
									'tree': 	'*',
									'close':  'x',
									'jump':   '-',
									'post':		'i',
									'player': '@'}

# casillas que puede pisar el personaje mas todas las demás
element = {'empty': 	' ', 
					 'herb':		'w',
					 **forbidden_cell}


# last element stepped by player
last_step = element['empty']


# player's initial coordinates
px = 22
py = 6
map[px][py] = element['player']


# colorear un mapa según los elementos, el color por defecto es el de la terminal
def color_map (map):
	cmap = copy.deepcopy(map)
	for i in range(len(map)): # range(de 0 a 25)
		for j in range(len(map[0])): # range(0 a 11)
			if (map[i][j] == element['wall']):
				cmap[i][j] = fg('white') + map[i][j] + attr(0)
			elif (map[i][j] == element['tree']):
				cmap[i][j] = fg('light_green') + map[i][j] + attr(0)
			elif (map[i][j] == element['herb']):
				cmap[i][j] = fg('dark_green') + map[i][j] + attr(0)
			elif (map[i][j] == element['jump']):
				cmap[i][j] = fg('light_gray') + map[i][j] + attr(0)
			elif (map[i][j] == element['close']):
				cmap[i][j] = fg('red') + map[i][j] + attr(0)
			elif (map[i][j] == element['post']):
				cmap[i][j] = fg('yellow_1') + map[i][j] + attr(0)
			elif (map[i][j] == element['player']):
				cmap[i][j] = fg('blue') + map[i][j] + attr(0)

	return cmap


# imprimir un mapa
def print_map (map):
	for i in range(len(map)):
		print(" ".join(map[i]))


# limpiar la pantalla
def clean_scr():
	if platform.system() == 'Windows':
		os.system('cls')
	else: # Linux || OSX
		os.system('clear')


# limpiar la pantalla e imprimir mapa coloreado
def update_map (map):
	clean_scr()
	print_map(color_map(map))


# siguiente movimiento del mapa
def next_move (map):
	global px
	global py
	global last_step
	last_battle = False

	while True:
		pressedkey = getKey()
		player_moves = False

		if pressedkey == 'w':
			if map[px-1][py] in (element['empty'], element['herb']):
				# restore element in map
				map[px][py] = last_step
				# save element of next step
				last_step = map[px-1][py]
				# update map with new player's position
				px = px-1
				map[px][py] = element['player']
				# indicate that player has made a movement
				player_moves = True

		elif pressedkey == 's':
			if map[px+1][py] in (element['empty'], element['herb']):
				# restore element in map
				map[px][py] = last_step
				# save element of next step
				last_step = map[px+1][py]
				# update map with new player's position
				px = px+1
				map[px][py] = element['player']
				# indicate that player has made a movement
				player_moves = True

			elif map[px+1][py] is element['jump']:
				# restore element in map
				map[px][py] = last_step
				# save element of next step
				last_step = map[px+2][py]
				# update map with new player's position
				px = px+2
				map[px][py] = element['player']
				# indicate that player has made a movement
				player_moves = True


		elif pressedkey == 'a':
			if map[px][py-1] in (element['empty'], element['herb']):
				# restore element in map
				map[px][py] = last_step
				# save element of next step
				last_step = map[px][py-1]
				# update map with new player's position
				py = py-1
				map[px][py] = element['player']
				player_moves = True


		elif pressedkey == 'd':
			if map[px][py+1]  in (element['empty'], element['herb']):
				# restore element in map
				map[px][py] = last_step
				# save element of next step
				last_step = map[px][py+1]
				# update map with new player's position
				py = py+1
				map[px][py] = element['player']
				player_moves = True


		elif pressedkey == 'e':
			cell = map[px-1][py] # valdosa que haya en frente
			if cell is element['post']:
				print("¡Pistas para Entrenadores!", end="")
				input()
				print("Para entrar en el menú, pulsa M.", end="")
				input()

			elif cell is element['herb']:
				print("Es una zona de hierba alta.", end="")
				input()
				print("¡Pueden aparecer pokémon salvajes!", end="")
				input()

			elif cell is element['wall']:
				print("Hay una pared delante.", end="")
				input()

			elif cell is element['jump']:
				print("Puedo saltar esto desde el otro lado.", end="")
				input()

			elif cell is element['tree']:
				print("Es un arbol.", end="")
				input()

			elif cell is element['close']:
				print("El camino está cortado. Disculpen las molestias.", end="")
				input()

			update_map(map)


		elif pressedkey == 'm':
			menu.next_move()

		else:
			pass

		# print map
		update_map(map)

		# si el entrador se mueve a una zona de hierba alta, 
		# hay un 20% de probabilidad de que aparezca un pokémon salvaje
		if (player_moves and last_step is element['herb']):
			probability = random.randint(0,10)
			if (probability < 2):
				if (last_battle is True): # impedir enfrentamiento nada mas acabar un enfrentamiento
					last_battle = False
				else:
					# generar pokémon aleatorio
					int_numero = random.randint(1, 384)
					int_nivel = random.randint(5, 100)

					print("Un pokémon salvaje apareció ⏎")
					getKey()

					print("Identificando Pokemon" + blink("..."))
					pkm = Pokemon(int_numero, int_nivel)
					
					print(pkm)
					getKey()

					modulo_zmq.publicarTwitter(pkm)

					

					algoritmoCombate(Pokemon(25, 100), pkm)

					last_battle = True

