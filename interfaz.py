import os
import time
import sys
from pokemon import *
from pokemon_t import *
from imagenToString import imgToStr
from getch_py import getKey
from fabulous.color import blink, fg256


def mecanografiar(texto, velocidad=0.10):
	lista = texto.split()
	for palabra in lista:
		sys.stdout.write(palabra + " ")
		sys.stdout.flush()
		time.sleep(velocidad)
	print()


def imprimeCuantoEfectivo (Pokemon_p, Pokemon_r, sel):
	if (Pokemon_p.movimientos[sel].nombre != '-'): # No es ataque nulo
		efectividad = TablaEfectividad[Pokemon_p.movimientos[sel].tipo][Pokemon_r.tipo]

		if (efectividad == 2):
			# system("afplay music/superdamage.wav &");
			mecanografiar("¡Es muy eficaz!")
		elif (efectividad == 0.5):
			# system("afplay music/notverydamage.wav &");
			mecanografiar("No es muy eficaz...")
		elif (efectividad == 1):
			# system("afplay music/normaldamage.wav &");
			pass
		elif (efectividad == 0):
			mecanografiar("No afecta a " + Pokemon_r.nombre + " enemigo...")


def imprimeRival (Pokemon_r, tab_len=10):
	# Calcular barra de vida
	b_max = 30-4-8
	b = int(Pokemon_r.ps * b_max / Pokemon_r.ps_max)
	str_vida = ('#' * b) + ('_' * (b_max-b))

	# Obtener imagen delantera del pokemon, se supone que está en el directorio local
	str_imagen = "\n" + imgToStr((str(Pokemon_r.numero) + ".jpg").lower(), 35)

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
	str_imagen = imgToStr((str(Pokemon_p.numero) + "_t.jpg").lower(), 35)

	# El nombre y el nivel ocupan como maximo 30 caracteres
	str_box = (
		'\n     '+ ('#'* 32) +
		'\n    ## ' + (Pokemon_p.nombre+' '+dic_genero[Pokemon_p.sexo]).ljust(20) + ("Nv: "+str(Pokemon_p.nivel)).ljust(8) + ' #' +
		'\n  ####     PS: (' + str_vida + ') #' +
		'\n' + '#'* 37)
	print(str_imagen)
	print(str_box.replace("\n", ("\n" + '\t'*tab_len)))


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
def imprimeMenuAtaque (Pokemon_p, ancho=70):
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
	os.system('clear')
	imprimeRival(r)
	imprimePokemon(p)



def imprimeMenuSeleccionAtaque (Pokemon_p, Pokemon_r):
	p = Pokemon_p
	r = Pokemon_r

	sel_atk = -1
	str_atk = '-'
	while (str_atk == '-'): # mientras ataque nulo
		imprimeCombate(p, r)
		try: 
			sel_atk = imprimeMenuAtaque(p) # devuelve el ataque sleccionado
		except Exception as e: # si se introduce un caracter raro
			sel_atk = -1

		if (sel_atk in [0, 1, 2, 3]): # ataque válido
			str_atk = p.atacar(r, sel_atk)

	mecanografiar(p.nombre + " usó " + str_atk + " contra pokémon " + r.nombre + " enemigo.")
	time.sleep(0.25)

	imprimeCuantoEfectivo(pe, pr, sel_atk)
	getKey()










def imprimeEntrenador (Entrenador_e, tab_len=0):
	str_imagen = imgToStr((dic_genero[Entrenador_e.genero] + ".jpg").lower())
	str_imagen = str_imagen.replace("\n", "\n" + '\t'*tab_len)
	print(str_imagen)


def imprimeEntrenadorBack (Entrenador_e, tab_len=0):
	str_imagen = imgToStr((dic_genero[Entrenador_e.genero] + "_t.jpg").lower())
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




# devuelve -1 si gana rival, 0 si empate, 1 si gana entrenador
def algoritmoCombate (Pokemon_p, Pokemon_r, pkm_salvaje=True):
	p = Pokemon_p
	r = Pokemon_r
	selec_menu = 0
	max = 0 	# selección de movimiento del pokemon p
	min = 0		# selección de movimiento del pokemon rival r
	finCombate = False
	intentosHuida = 0

	while (not finCombate):
		# Menú combate
		while (True):
			imprimeCombate(p, r)
			print("¿Qué debería hacer " + p.nombre + "?")
			selec_menu = imprimeMenuCombate()

			if (selec_menu in [0, 1, 2, 3]):
				break


		########### NOTAAAA: HACER UN DIAGRAMA DE FLUJO A MI MANERA PARA ENTENDERLO MEJOR

		# Menú ataque
		if (selec_menu == 0):
			while (True):
				while(True):
					imprimeCombate(p, r)
					print("¿Qué debería hacer " + p.nombre + "?")
					max = imprimeMenuAtaque(p)
					# Si se pulsa 'B'
					if (max not in [0, 1, 2, 3]):
						break

					# Comprobar que el pokémon tenga PP en al menos un ataque
					ataques_con_pp = [0, 1, 2, 3]
					for i in range(0, 4):
						if (p.movimientos[i].pp == 0):
							ataques_con_pp.remove(i)


					# Si ningún ataque del pokémon tiene PP, entonces este usará combate
					if (len(ataques_con_pp) == 0): 
						max = -1
					else:
						# Comprobar que el movimiento elegido tenga suficientes PP
						# Los movimientos nulos no tienen PP, así que entran también por aquí
						if (p.movimientos[max].pp <= 0):
							mecanografiar("¡No quedan PP para este movimiento! ⏎")
							getKey()
						else:
							break
				
				# Determinar el orden de ataque en función de la velocidad:
				if (p.velocidad > r.velocidad):
					primero = p
					segundo = r
				elif (p.velocidad < r.velocidad):
					primero = r
					segundo = p
				else: # (p.velocidad == r.velocidad)
					suerte = random.randint(0,1)
					if (suerte == 0):
						primero = p
						segundo = r
					else:
						primero = r
						segundo = p

				# Atacar
				if (primero == p):
					str_atk = p.atacar(r, max)
					# Si el pokemon del entrenador realiza un movimiento, se resetea el contador de huidas
					intentosHuida = 0
					imprimeCombate(p, r)
					mecanografiar (p.nombre + " usó " + str_atk + ". ⏎")
					getKey()
					imprimeCuantoEfectivo(p, r, max)

					imprimeCombate(p, r)


					if (r.ps <= 0):
						return 1

					str_atk = r.atacarIA(p)
					mecanografiar ("Pokémon " + r.nombre + " enemigo usó " + str_atk + ". ⏎")
					getKey()
					imprimeCuantoEfectivo(p, r, max)

					imprimeCombate(p, r)

					if (p.ps <= 0):
						return -1

				else:
					str_atk = r.atacarIA(p)

					if (r.ps <= 0):
						return 1

					if (p.ps <= 0):
						return -1

					


				break 
				#


		# Menú mochila
		if (selec_menu == 1):
			mecanografiar("La mochila aún no está implementada. ⏎")
			getKey()

		# Menú Equipo
		if (selec_menu == 2):
			mecanografiar("¡Este es tu último Pokémon! ⏎")
			getKey()

		# Menú Escapar
		if (selec_menu == 3):
			if (pkm_salvaje):
				# A es la velocidad del Pokémon que quiere huir
				# B es la velocidad del Pokémon oponente. Si B es 0 se cuenta como si fuera 1. 
				# C es la cantidad de veces que el usuario ha intentado huir (contando la actual). 
				# Se reinicia si el usuario realiza un movimiento. 
				A = p.velocidad
				B = r.velocidad
				C = intentosHuida
				if (B == 0):
					B = 1
				F = ((A * 128) / B + 30 * C) % 256 
				# Se calcula un número aleatorio entre 0 y 255, y si es menor que F entonces escapa. 
				exitoHuida = random.randint(0, 256) < F

				if (exitoHuida):
					mecanografiar("Escapaste sin problemas... ⏎")
					getKey()
					finCombate = True
					return 0
				else:
					mecanografiar("¡No puedes huir del combate! ⏎")
					intentosHuida += 1
					getKey()

					# Turno del rival
					str_atk = r.atacarIA(p)
					mecanografiar ("Pokémon " + r.nombre + " enemigo usó " + str_atk + ". ⏎")
					getKey()
					imprimeCuantoEfectivo(p, r, max)

					imprimeCombate(p, r)

					if (p.ps <= 0):
						return -1

			else:
				mecanografiar("¡No puedes escapar de un combate contra un entrenador! ⏎")
				getKey()





def combateVSPokemonSalvaje (Entrenador_e, Pokemon_r):
	e = Entrenador_e
	r = Pokemon_r
	os.system('clear')
	# os.system("afplay music/"+str(Pokemon_r.numero)+"Cry.wav &");
	imprimeRival(r)
	imprimeEntrenadorBack(e)

	mecanografiar("\n¡Pokémon " + r.nombre + " salvaje apareció! ⏎")
	getKey();


	os.system('clear')
	imprimeRival(r)
	imprimeEntrenadorBack(e)
	
	# Entrenador saca a su primer pokémon no nulo no debilitado
	Pokemon_p = e.sacarPokemon()
	mecanografiar("\n¡Adelante, " + Pokemon_p.nombre + '! ⏎')
	getKey();

	# os.system("afplay music/"+str(Pokemon_p.numero)+"Cry.wav &");
	ganador = algoritmoCombate(Pokemon_p, r)
	

	if (ganador == -1):
		mecanografiar(Pokemon_p.nombre + " se debilitó. ⏎")
		getKey()
	elif (ganador == 1):
		mecanografiar(r.nombre + " enemigo se debilitó. ⏎")
		getKey()







def combateVSEntrenador (Entrenador_e, Entrenador_r):
	e = Entrenador_e
	r = Entrenador_r

	os.system('clear')
	print(strBoxEntrenador(r))
	imprimeEntrenador(r, 10)
	imprimeEntrenadorBack(e)
	print(strBoxEntrenador(e, 1, 10))

	mecanografiar("\n¡Entrenador Guay " + r.nombre + " quiere luchar! ⏎")
	getKey();

	os.system('clear')
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
	os.system('clear')
	print(strBoxEntrenador(r))
	imprimeEntrenador(r, 10)
	imprimePokemon(Pokemon_pe)


	mecanografiar("\n¡Entrenador rival " + r.nombre + ' envió a ' + Pokemon_pr.nombre + '! ⏎')
	getKey();


	# os.system("afplay music/"+str(Pokemon_pe.numero)+"Cry.wav &");
	os.system('clear')
	imprimePokemon(Pokemon_pr)
	imprimePokemon(Pokemon_pe)
	ganador = algoritmoCombate(pe, pr, False)

	if (ganador == -1):
		mecanografiar(pe.nombre + " se debilitó. ⏎")
		getKey()
	elif (ganador == 1):
		mecanografiar(pr.nombre + " enemigo se debilitó. ⏎")
		getKey()



