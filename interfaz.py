import os
import platform # necesario para detectar windows
import time
import sys
from pokemon import *
from pokemon_t import *
from imagenToString import imgToStr
from getch_py import getKey
from fabulous.color import blink, fg256

VOLVERAMENUANTERIOR = 10

# limpiar la pantalla
def limpiarPantalla():
	if platform.system() == 'Windows':
		os.system('cls')
	else: # Linux || OSX
		os.system('clear')


def mecanografiar(texto, velocidad=0.10):
	lista = texto.split()
	for palabra in lista:
		sys.stdout.write(palabra + " ")
		sys.stdout.flush()
		time.sleep(velocidad)
	print()



def imprimeRival (Pokemon_r, tab_len=10):
	# Calcular barra de vida
	b_max = 30-4-8
	b = int(Pokemon_r.ps * b_max / Pokemon_r.ps_max)
	str_vida = ('#' * b) + ('_' * (b_max-b))

	# Obtener imagen delantera del pokemon, se supone que está en el directorio local
	str_imagen = "\n" + imgToStr((str(Pokemon_r.numero) + ".png").lower(), 35)

	# Indentar imagen
	str_imagen = str_imagen.replace("\n", "\n" + '\t'*tab_len)

	char_capturado = '@' 	# Pokémon Capturado
	char_capturado = ' ' 	# Pokémon no Capturado

	# El nombre y el nivel ocupan como maximo 30 caracteres
	print('#'* 32)
	print('# ' + (Pokemon_r.nombre+' '+dic_genero[Pokemon_r.sexo]).ljust(20) + ("Nv: "+str(Pokemon_r.nivel)).ljust(8) + ' ##')
	print('# ' + char_capturado + '   PS: (' + str_vida + ') ####')
	print('#'* 37)
	print(str_imagen)


def imprimePokemon (Pokemon_p, tab_len=10):
	# Calcular barra de vida
	b_max = 30-4-8
	b = int(Pokemon_p.ps * b_max / Pokemon_p.ps_max)
	str_vida = ('#' * b) + ('_' * (b_max-b))

	# Obtener imagen trasera del pokemon, se supone que está en el directorio local
	str_imagen = imgToStr((str(Pokemon_p.numero) + "_t.png").lower(), 35)

	# El nombre y el nivel ocupan como maximo 30 caracteres
	str_box = (
		'\n     '+ ('#'* 32) +
		'\n    ## ' + (Pokemon_p.nombre+' '+dic_genero[Pokemon_p.sexo]).ljust(20) + ("Nv: "+str(Pokemon_p.nivel)).ljust(8) + ' #' +
		'\n  ####     PS: (' + str_vida + ') #' +
		'\n' + '#'* 37)
	print(str_imagen)
	print(str_box.replace("\n", ("\n" + '\t'*tab_len)))


def imprimeEntrenador (Entrenador_e, tab_len=0):
	str_imagen = imgToStr((dic_genero[Entrenador_e.genero] + ".png").lower())
	str_imagen = str_imagen.replace("\n", "\n" + '\t'*tab_len)
	print(str_imagen)


def imprimeEntrenadorBack (Entrenador_e, tab_len=0):
	str_imagen = imgToStr((dic_genero[Entrenador_e.genero] + "_t.png").lower())
	str_imagen = str_imagen.replace("\n", "\n" + '\t'*tab_len)
	print(str_imagen)




def charPokemon (Pokemon_e):
	char_pkm = '@'

	if (Pokemon_e.nombre == '-'):
		char_pkm = 'O'
	elif (Pokemon_e.ps <= 0):
		char_pkm = 'X'
	
	return str(char_pkm)



def strBoxEntrenador (Entrenador_e, orientacion=0, tab_len=0):
	e = Entrenador_e


	str_balls = ""

	for i in range (0, len(e.equipo)):
		str_balls += charPokemon(e.equipo[i]) + '  '

	str_ballf =""
	# rellenar las balls que falten
	for i in range (0, 6-len(e.equipo)):
		str_ballf += 'O  '

	str_balls = str_ballf + str_balls

	if orientacion == 0:
		str_box = ('\n# ' + str_balls.center(30) + 
						 '\n' + ('#'* 32))
	else:
		"".join(reversed(str_balls))
		str_box = ('\n' + str_balls.center(31) + '#'
						 '\n' + ('#'* 32))
		
	str_box = str_box.replace("\n", "\n" + '\t'*tab_len)

	# Colorear
	str_box = str_box.replace('@', str(fg256('red', '@')))
	str_box = str_box.replace('O', str(fg256('white', '@')))
	str_box = str_box.replace('X', str(fg256('black', '#')))
	return str_box



# devuelve eleccion valida: 0, 1, 2, 3, o eleccion invalida: -1
def imprimeMenuCombate (ancho=70):
	print("#"*ancho)
	print('#' + (' '*int(ancho/2-2)) + '#' + (' '*int(ancho/2-1)) + '#')
	print('#' + " 0) LUCHAR".center(int(ancho/2-2)) + '#' + " 1) MOCHILA".center(int(ancho/2-1)) + '#') 
	print('#' + (' '*int(ancho/2-2)) + '#' + (' '*int(ancho/2-1)) + '#')
	print("#"*ancho)
	print('#' + (' '*int(ancho/2-2)) + '#' + (' '*int(ancho/2-1)) + '#')
	print('#' + " 2) CAMBIAR POKEMON".center(int(ancho/2-2))  + '#' + " 3) ESCAPAR".center(int(ancho/2-1)) + '#') 
	print('#' + (' '*int(ancho/2-2)) + '#' + (' '*int(ancho/2-1)) + '#')
	print("#"*ancho)

	#print("Su elección: ", end="")
	eleccion = getKey()
	
	try:
		eleccion = int(eleccion)
	except Exception as e:
		eleccion = -1

	return eleccion



# devuelve eleccion valida: 0, 1, 2, 3, o eleccion invalida: -1
def imprimeMenuLuchar (Pokemon_p, ancho=70):
	p = Pokemon_p
	print("#"*ancho)
	print('#' + (' '*int(ancho/2-2)) + '#' + (' '*int(ancho/2-1)) + '#')
	print('#' + ("  0) " + p.movimientos[0].nombre).ljust(int(ancho/2-2)) + '#' + ("  1) " + p.movimientos[1].nombre).ljust(int(ancho/2-1)) + '#') 
	print('#' + ("     " + dic_tipo[p.movimientos[0].tipo].ljust(12) + " PP: " + str(p.movimientos[0].pp) + '/' + str(p.movimientos[0].pp_max)).ljust(int(ancho/2-2)) + '#' + ("     " + dic_tipo[p.movimientos[1].tipo].ljust(12) + " PP: " + str(p.movimientos[1].pp) + '/' + str(p.movimientos[1].pp_max)).ljust(int(ancho/2-1)) + '#') 
	print('#' + (' '*int(ancho/2-2)) + '#' + (' '*int(ancho/2-1)) + '#')
	print("#"*ancho)
	print('#' + (' '*int(ancho/2-2)) + '#' + (' '*int(ancho/2-1)) + '#')
	print('#' + ("  2) " + p.movimientos[2].nombre).ljust(int(ancho/2-2)) + '#' + ("  3) " + p.movimientos[3].nombre).ljust(int(ancho/2-1)) + '#') 
	print('#' + ("     " + dic_tipo[p.movimientos[2].tipo].ljust(12) + " PP: " + str(p.movimientos[2].pp) + '/' + str(p.movimientos[2].pp_max)).ljust(int(ancho/2-2)) + '#' + ("     " + dic_tipo[p.movimientos[3].tipo].ljust(12) + " PP: " + str(p.movimientos[3].pp) + '/' + str(p.movimientos[3].pp_max)).ljust(int(ancho/2-1)) + '#') 
	print('#' + (' '*int(ancho/2-2)) + '#' + (' '*int(ancho/2-1)) + '#')
	print("#"*ancho)

	#print("Su elección: ", end="")
	eleccion = getKey()
	
	try:
		eleccion = int(eleccion)
	except Exception as e:
		eleccion = -1

	return eleccion


def imprimeCombate (Pokemon_p, Pokemon_r):
	p = Pokemon_p
	r = Pokemon_r
	limpiarPantalla()
	imprimeRival(r)
	imprimePokemon(p)



# Imprime la escena de lucha completa y devuelve el ataque seleccionado:
# 0: atq0, 1: atq1, 2: atq2, 3: ataq3, -1 combate, VOLVERAMENUANTERIOR: volver a menú anterior
def imprimeEscenaLuchar (Pokemon_p, Pokemon_r):
	p = Pokemon_p
	r = Pokemon_r

	limpiarPantalla()
	imprimeCombate(Pokemon_p, Pokemon_r)
	print("¿Qué debería hacer " + str(Pokemon_p.nombre) + "?")
	sel_atk = imprimeMenuLuchar(p)

	# Si ataque no es válido, indicar que se desea volver al menú anterior
	if (sel_atk == -1):
		return VOLVERAMENUANTERIOR

	# Si el ataque seleccionado no tiene PP
	if (Pokemon_p.movimientos[sel_atk].pp <= 0):	
		# Comprobar que el pokémon tenga PP en al menos un ataque
		ataques_con_pp = [0, 1, 2, 3]
		for i in range(0, 4):
			if (Pokemon_p.movimientos[i].pp <= 0):
				ataques_con_pp.remove(i)

		# Si ningún ataque del pokémon tiene PP
		if (len(ataques_con_pp) == 0):
			return -1 # el pokémon usará "combate"
		else: 
			mecanografiar("¡No quedan PP para este movimiento! " + str(blink('⏎')))
			getKey()
			# Llamada recursiva, volvemos a empezar
			return imprimeEscenaLuchar (Pokemon_p, Pokemon_r)

	# El movimiento seleccionado tiene suficientes PP
	else:
		return sel_atk # el pokémon usará el ataque seleccionado






# devuelve eleccion valida: 0: luchar, 1: mochila, 2: equipo, 3: huir, o eleccion invalida: -1
def imprimeEscenaCombate (Pokemon_p, Pokemon_r):

	# Imprime a los dos combatientes y el menu de combate
	imprimeCombate(Pokemon_p, Pokemon_r)
	print("¿Qué debería de hacer " + str(Pokemon_p.nombre) + "?")
	eleccion = imprimeMenuCombate()
	
	try:
		eleccion = int(eleccion)
	except Exception as e:
		# Elección inválida, volver a empezar
		return imprimeEscenaCombate(Pokemon_p, Pokemon_r)

	return eleccion









# Imprime al rival, que puede ser un pokemon salvaje o un entrenador 
# y al entrenador de espaldas con sus pokeballs.
# Devuelve el pokémon elegido por el entrenador para luchar
def imprimeEscenaInicial (Entrenador_e, PokemonEntrenador):
	bool_esPokemon = False
	bool_esEntrenador = False

	limpiarPantalla()
	# Si el objeto tiene el atributo movimientos, es un pokemon
	try:
		PokemonEntrenador.movimientos
		# El pokémon grita cuando sale a combatir
		imprimeRival(PokemonEntrenador)
		PokemonEntrenador.gritar()
		bool_esPokemon = True
	except Exception as e:
		# Sino, el objeto es un entrenador
		print(strBoxEntrenador(PokemonEntrenador))
		imprimeEntrenador(PokemonEntrenador, 10)
		bool_esEntrenador = True

	# Imprime la parte de abajo, entrenador y barrra de pokébals
	imprimeEntrenadorBack(Entrenador_e)
	print(strBoxEntrenador(Entrenador_e, 1, 10))

	# INCOMPLETO, IMPLEMENTAR CLASES DE ENTRENADORES Y DESCARGAR IMAGENES
	if (bool_esEntrenador):
		mecanografiar("\n¡Entrenador Guay " + PokemonEntrenador.nombre + " quiere luchar! "+ str(blink('⏎')))
		getKey();

	if (bool_esPokemon):
		mecanografiar("\n¡Pokémon " + PokemonEntrenador.nombre + " salvaje apareció! "+ str(blink('⏎')))
		getKey();


	# Entrenador saca a su primer pokémon no nulo no debilitado
	Pokemon_p = Entrenador_e.sacarPokemon()
	mecanografiar("\n¡Adelante, " + Pokemon_p.nombre + "! " + str(blink('⏎')))
	getKey();


	if (bool_esPokemon):
		limpiarPantalla()
		imprimeCombate(Pokemon_p, PokemonEntrenador)
		# Pokemon elegido del entrenador grita cuando sale a combatir
		Pokemon_p.gritar()
		time.sleep(2)
		
	return Pokemon_p

	


# Devuelve True si el Pokemon del jugador fue el primero en atacar,
# devuelve False en caso contrario
def primeroEnAtacar (Pokemon_p, Pokemon_r):

	if (Pokemon_p.velocidad > Pokemon_r.velocidad):
		return True
	elif (Pokemon_p.velocidad < Pokemon_r.velocidad):
		return False
	else: # Los dos tienen la misma velocidad así que se echa a suertes, 50% probabilidad
		if (random.randint(0, 2) == 0):
			return True
		else:
			return False


def imprimeEfectividad (int_efectividad = 1):
	efectividad = int(int_efectividad)	

	if (efectividad == 2):
		os.system("afplay music/superdamage.wav &");
		mecanografiar("¡Es muy eficaz! "+ str(blink('⏎')))
		getKey()
	elif (efectividad == 0.5):
		os.system("afplay music/notverydamage.wav &");
		mecanografiar("No es muy eficaz..." + str(blink('⏎')))
		getKey()
	elif (efectividad == 1):
		os.system("afplay music/normaldamage.wav &");
		pass
	elif (efectividad == 0):
		mecanografiar("No afecta a " + Pokemon_r.nombre + " enemigo... "+ str(blink('⏎')))
		getKey()

	


AUTOMATICO = 10
# Ataca el pokémon del entrenador, con el movimiento int_ataque
def turnoPokemon (Pokemon_p, Pokemon_r, int_ataque=AUTOMATICO):
		int_ataque = int(int_ataque)

		# Imprime el combate para limpiar la interfaz
		imprimeCombate(Pokemon_p, Pokemon_r)

		if (int_ataque == AUTOMATICO):
			dic_resultado = Pokemon_p.atacarIA(Pokemon_r)
		else:
			dic_resultado = Pokemon_p.atacar(Pokemon_r, int_ataque)

		mecanografiar(str(Pokemon_p.nombre) + " usó " + str(dic_resultado['ataque']) + 
									" contra pokémon " + str(Pokemon_r.nombre) + " enemigo. "+ str(blink('⏎')))
		getKey()

		# Imprime el combate para ver el efecto del ataque
		imprimeCombate(Pokemon_p, Pokemon_r)

		if (bool(dic_resultado['acierto'])):
			imprimeEfectividad(int(dic_resultado['efectividad']))
		else:
			mecanografiar("Pero falló. " + str(blink('⏎')))
			getKey()


AUTOMATICO = 10
# Ataca el pokémon rival, con el movimiento int_ataque
def turnoRival (Pokemon_r, Pokemon_p, int_ataque=AUTOMATICO):
		int_ataque = int(int_ataque)

		if (int_ataque == AUTOMATICO):
			dic_resultado = Pokemon_r.atacarIA(Pokemon_p)
		else:
			dic_resultado = Pokemon_r.atacar(Pokemon_p, int_ataque)

		mecanografiar("Pokemon " + str(Pokemon_r.nombre) + " enemigo usó " + 
									str(dic_resultado['ataque']) + ". " + str(blink('⏎')))
		getKey()

		# Imprime el combate para ver el efecto del ataque
		imprimeCombate(Pokemon_p, Pokemon_r)

		if (bool(dic_resultado['acierto'])):
			imprimeEfectividad(int(dic_resultado['efectividad']))
		else:
			mecanografiar("Pero falló. "+ str(blink('⏎')))
			getKey()



# devuelve -1 si gana rival, 0 si empate, 1 si gana entrenador
def algoritmoCombate (Pokemon_p, Pokemon_r):
	finCombate = False
	intentosHuida = 0
	while (not finCombate):
		
		# Escena de Combate: imprimeRival, imprimePokemon y menuCombate
		# Devolverá una opción válida: 0 luchar, 1, mochila, 2 pkm, 3 huir
		int_queHacer = int(imprimeEscenaCombate(Pokemon_p, Pokemon_r))

		# 0 LUCHAR - SELECCIONADO
		if (int_queHacer == 0):

			# Elección del ataque a realizar
			int_ataque = imprimeEscenaLuchar(Pokemon_p, Pokemon_r)

			if (int_ataque != VOLVERAMENUANTERIOR):
				# ACCIÓN DE LUCHA
				# Si el pokemon del entrenador realiza un movimiento, se resetea el contador de huidas
				intentosHuida = 0

				# El pokémon del entrenador es más veloz
				if (primeroEnAtacar(Pokemon_p, Pokemon_r)):
					# Turno del pokemon del entrenador
					turnoPokemon(Pokemon_p, Pokemon_r, int_ataque)

					# ¿Ha derrotado al rival?
					if (Pokemon_r.ps <= 0):
						finCombate = True
						ganador = 1
					else: # Turno del rival, ataque automático
						turnoRival(Pokemon_r, Pokemon_p)

						# ¿Ha derrotado al Pokémon del entrenador?
						if (Pokemon_p.ps <= 0):
							finCombate = True
							ganador = -1

				# EL pokémon del rival es más veloz
				else:
					# Turno del rival, ataque automático
					turnoRival(Pokemon_r, Pokemon_p)

					# ¿Ha derrotado al Pokémon del entrenador?
					if (Pokemon_p.ps <= 0):
						finCombate = True
						ganador = -1
					else: # Turno del pokemon del entrenador
						turnoPokemon(Pokemon_p, Pokemon_r, int_ataque)

						# ¿Ha derrotado al rival?
						if (Pokemon_r.ps <= 0):
							finCombate = True
							ganador = 1

			## VOLVER A ESCENA DE COMBATE


		# 1 - MOCHILA SELECCIONADA
		if (int_queHacer == 1):
			mecanografiar("La mochila aún no está implementada. " + str(blink('⏎')))
			getKey()

			## VOLVER A ESCENA DE COMBATE


		# 2 - EQUIPO SELECCIONADO 
		if (int_queHacer == 2):
			mecanografiar("¡Este es tu último Pokémon! "+ str(blink('⏎')))
			getKey()

			## VOLVER A ESCENA DE COMBATE


		# 3 - HUIR SELECCIONADO
		if (int_queHacer == 3):
			# Si el pokémon es salvaje
			if (Pokemon_r.id == 0):
				# A es la velocidad del Pokémon que quiere huir
				# B es la velocidad del Pokémon oponente. Si B es 0 se cuenta como si fuera 1. 
				# C es la cantidad de veces que el usuario ha intentado huir (contando la actual). 
				# Se reinicia si el usuario realiza un movimiento. 
				A = Pokemon_p.velocidad
				B = Pokemon_r.velocidad
				C = intentosHuida
				if (B == 0):
					B = 1
				F = ((A * 128) / B + 30 * C) % 256 
				# Se calcula un número aleatorio entre 0 y 255, y si es menor que F entonces escapa. 
				exitoHuida = random.randint(0, 256) < F

				# Hubo suerte y podemos huir
				if (exitoHuida):
					os.system("afplay music/flee.wav &")
					mecanografiar("Escapaste sin problemas... "+ str(blink('⏎')))
					getKey()
					finCombate = True
					ganador = 0

				# Mala suerte, no puedes huir
				else: 
					mecanografiar("¡No puedes huir del combate! "+ str(blink('⏎')))
					intentosHuida += 1
					getKey()

					# Es el turno del rival, ataque automático
					turnoRival(Pokemon_r, Pokemon_p)

					# ¿Ha derrotado al pokémon del entrenador?
					if (Pokemon_p.ps <= 0):
						finCombate = True
						ganador = -1

			else:
				mecanografiar("¡No puedes escapar de un combate contra un entrenador! ⏎")
				getKey()


	return ganador



def combateVSPokemonSalvaje (Entrenador_e, Pokemon_r):

	# Imprime escena inicial y entrenador elige primer pokémon no debilitado del equipo
	Pokemon_p = imprimeEscenaInicial(Entrenador_e, Pokemon_r)
	ganador = algoritmoCombate(Pokemon_p, Pokemon_r)
	

	if (ganador == -1):
		mecanografiar(Pokemon_p.nombre + " se debilitó. ⏎")
		getKey()
		if (Entrenador_e.hayPokemonVivo()):
			print("¿Quieres sacar al siguiente pokémon?")
			print("\t 0 - No")
			print("\t 1 - Sí")
			eleccion = getKey()

			if (eleccion == 0):
				print("Escapaste sin problemas")
			else:
				Pokemon_p = Entrenador_e.sacarPokemon()
				pass
		else:
			print("A " + Entrenador_e.nombre)
		
	elif (ganador == 1):
		mecanografiar(r.nombre + " enemigo se debilitó. ⏎")
		getKey()







def combateVSEntrenador (Entrenador_e, Entrenador_r):
	e = Entrenador_e
	r = Entrenador_r

	limpiarPantalla()
	print(strBoxEntrenador(r))
	imprimeEntrenador(r, 10)
	imprimeEntrenadorBack(e)
	print(strBoxEntrenador(e, 1, 10))

	mecanografiar("\n¡Entrenador Guay " + r.nombre + " quiere luchar! ⏎")
	getKey();

	limpiarPantalla()
	print(strBoxEntrenador(r))
	imprimeEntrenador(r, 10)
	imprimeEntrenadorBack(e)
	print(strBoxEntrenador(e, 1, 10))

	# Cada entrenador saca a su primer pokémon no nulo no debilitado
	Pokemon_pe = e.sacarPokemon()
	Pokemon_pr = r.sacarPokemon()

	mecanografiar("\n¡Adelante, " + Pokemon_pe.nombre + '! ⏎')
	getKey();


	# os.system("afplay music/"+str(Pokemon_pe.numero)+"Cry.wav &");
	limpiarPantalla()
	print(strBoxEntrenador(r))
	imprimeEntrenador(r, 10)
	imprimePokemon(Pokemon_pe)


	mecanografiar("\n¡Entrenador rival " + r.nombre + ' envió a ' + Pokemon_pr.nombre + '! ⏎')
	getKey();


	# os.system("afplay music/"+str(Pokemon_pe.numero)+"Cry.wav &");
	limpiarPantalla()
	imprimePokemon(Pokemon_pr)
	imprimePokemon(Pokemon_pe)
	ganador = algoritmoCombate(pe, pr, False)

	if (ganador == -1):
		mecanografiar(pe.nombre + " se debilitó. ⏎")
		getKey()
	elif (ganador == 1):
		mecanografiar(pr.nombre + " enemigo se debilitó. ⏎")
		getKey()



