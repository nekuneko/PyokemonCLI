import os
from pokemon_db import *
from pokemon_t import *
from imagenToString import imgToStr

import time
import sys

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
	str_imagen = imgToStr((Pokemon_r.nombre + ".png").lower(), 35)

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
	str_imagen = imgToStr((Pokemon_p.nombre + "_t.png").lower(), 35)

	# El nombre y el nivel ocupan como maximo 30 caracteres
	str_box = (
		'\n     '+ ('#'* 32) +
		'\n    ## ' + (Pokemon_p.nombre+' '+dic_genero[Pokemon_p.sexo]).ljust(20) + ("Nv: "+str(Pokemon_p.nivel)).ljust(8) + ' #' +
		'\n  ####     PS: (' + str_vida + ') #' +
		'\n' + '#'* 37)
	print(str_imagen)
	print(str_box.replace("\n", ("\n" + '\t'*tab_len)))


def menuCombate (ancho=70):
	print("#"*ancho)
	print('#' + (' '*int(ancho/2-2)) + '#' + (' '*int(ancho/2-1)) + '#')
	print('#' + " 0) LUCHAR".center(int(ancho/2-2)) + '#' + " 1) MOCHILA".center(int(ancho/2-1)) + '#') 
	print('#' + (' '*int(ancho/2-2)) + '#' + (' '*int(ancho/2-1)) + '#')
	print("#"*ancho)
	print('#' + (' '*int(ancho/2-2)) + '#' + (' '*int(ancho/2-1)) + '#')
	print('#' + " 2) CAMBIAR POKEMON".center(int(ancho/2-2))  + '#' + " 3) ESCAPAR".center(int(ancho/2-1)) + '#') 
	print('#' + (' '*int(ancho/2-2)) + '#' + (' '*int(ancho/2-1)) + '#')
	print("#"*ancho)

	print("Su elección: ", end="")
	eleccion = input()
	return int(eleccion)




def menuAtaque (Pokemon_p, ancho=70):
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

	print("Su elección: ", end="")
	eleccion = input()
	return int(eleccion)












def imprimeCombate (Pokemon_p, Pokemon_r):
	os.system('clear')
	imprimeRival(r)
	imprimePokemon(p)



def finCombate (Pokemon_p):
	return Pokemon_p.ps <= 0


def algoritmoCombate (Pokemon_p, Pokemon_r):
	p = Pokemon_p
	r = Pokemon_r



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
	from fabulous.color import fg256
	str_box = str_box.replace('@', str(fg256('red', '@')))
	str_box = str_box.replace('O', str(fg256('white', '@')))
	str_box = str_box.replace('X', str(fg256('black', '#')))
	return str_box



def combateVSPokemonSalvaje (Entrenador_e, Pokemon_r):
	os.system('clear')
	# os.system("afplay music/"+str(Pokemon_r.numero)+"Cry.wav &");
	imprimeRival(Pokemon_r)
	imprimeEntrenadorBack(Entrenador_e)

	mecanografiar("\n¡Pokémon " + r.nombre + " salvaje apareció! ⏎")
	input();


	os.system('clear')
	imprimeRival(Pokemon_r)
	imprimeEntrenadorBack(Entrenador_e)
	# Entrenador saca a su primer pokémon no nulo no debilitado
	pkm_elegido = -1
	for i in range(0, len(Entrenador_e.equipo)):
		if (Entrenador_e.equipo[i].nombre != '-' and Entrenador_e.equipo[i].ps > 0):
			pkm_elegido = i
			break

	if (pkm_elegido ==  -1):
		print("ERROR, EL ENTRENADOR NO TIENE POKÉMONS SANOS")
		# SE LANZARIA UNA EXCEPCION

	Pokemon_p = Entrenador_e.equipo[pkm_elegido]
	mecanografiar("\n¡Adelante, " + Pokemon_p.nombre + '! ⏎')
	input();

	# os.system("afplay music/"+str(Pokemon_p.numero)+"Cry.wav &");
	# algoritmoCombate()



def combateVSEntrenador (Entrenador_e, Entrenador_r):
	e = Entrenador_e
	r = Entrenador_r

	os.system('clear')
	print(strBoxEntrenador(r))
	imprimeEntrenador(r, 10)
	imprimeEntrenadorBack(e)
	print(strBoxEntrenador(e, 1, 10))

	mecanografiar("\n¡Entrenador Guay " + r.nombre + " quiere luchar! ⏎")
	input();

	os.system('clear')
	print(strBoxEntrenador(r))
	imprimeEntrenador(r, 10)
	imprimeEntrenadorBack(e)
	print(strBoxEntrenador(e, 1, 10))

	# Cada entrenador saca a su primer pokémon no nulo no debilitado
	pkm_elegido = -1
	for i in range(0, len(e.equipo)):
		if (e.equipo[i].nombre != '-' and e.equipo[i].ps > 0):
			pkm_elegido = i
			break

	if (pkm_elegido ==  -1):
		print("ERROR, EL ENTRENADOR NO TIENE POKÉMONS SANOS")
		# SE LANZARIA UNA EXCEPCION

	Pokemon_pe = e.equipo[pkm_elegido]

	pkm_elegido = -1
	for i in range(0, len(r.equipo)):
		if (r.equipo[i].nombre != '-' and r.equipo[i].ps > 0):
			pkm_elegido = i
			break

	if (pkm_elegido ==  -1):
		print("ERROR, EL ENTRENADOR NO TIENE POKÉMONS SANOS")
		# SE LANZARIA UNA EXCEPCION

	Pokemon_pr = r.equipo[pkm_elegido]


	mecanografiar("\n¡Adelante, " + Pokemon_pe.nombre + '! ⏎')
	input();


	# os.system("afplay music/"+str(Pokemon_pe.numero)+"Cry.wav &");
	os.system('clear')
	print(strBoxEntrenador(r))
	imprimeEntrenador(r, 10)
	imprimePokemon(Pokemon_pe)


	mecanografiar("\n¡Entrenador rival " + r.nombre + ' envió a ' + Pokemon_pr.nombre + '! ⏎')
	input();


	# os.system("afplay music/"+str(Pokemon_pe.numero)+"Cry.wav &");
	os.system('clear')
	imprimePokemon(Pokemon_pr)
	imprimePokemon(Pokemon_pe)


	# algoritmoCombate()




# PRUEBAAASS
from entrenador import *
e = cargarPartida()
r = Pokemon(1, 100)
# el entrenador saca al primero del equipo
p = e.equipo[0]  
#p = Pokemon(383, 100)

#combateVSPokemonSalvaje(e, r)
combateVSEntrenador(e, e)


str_a = '-'
while (str_a == '-'): # mientras ataque nulo
	imprimeCombate(p, r)
	a = menuAtaque(p)
	str_a = p.atacar(r, a)

mecanografiar(p.nombre + " usó " + str_a + " contra pokémon " + r.nombre + " enemigo.")
time.sleep(0.25)
imprimeCuantoEfectivo(p, r, a)
input()
imprimeCombate(p, r)


