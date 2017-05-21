from numpy import random
from pokemon_t import *
from movimientos_db import *
import json


pokemon_legendarios = {'moltres', 'zapdos', 'articuno', 'mewtwo', 'mew', 'raikou', 'entei',
											 'suicune', 'lugia', 'ho-oh', 'celebi', 'regirock', 'regice', 'registeel',
											 'latias', 'latios', 'kyogre', 'groudon', 'rayquaza', 'jirachi', 'deoxys',
											 'uxie', 'mesprit', 'azelf', 'dialga', 'palkia', 'heatran', 'regigigas',
											 'giratina', 'cresselia', 'phione', 'manaphy', 'darkrai', 'shaymin', 'arceus'}

pokemon_db = { 0: 'MissingNo.', 1: 'Bulbasur', 382: 'Kyogre', 383: 'Groudon'}
pokemon_db_t = {0: NORMAL, 1: PLANTA, 382: AGUA, 383: TIERRA}


def formatearPokemon (pkm):
	pkm['numero'] 			= int(pkm['numero'])
	pkm['nombre'] 			= str(pkm['nombre']).title()
	pkm['tipo']					= int(dic_tipo_inv[pkm['tipo'].lower()])
	pkm['ps']						= int(pkm['ps'])
	pkm['ataque']				= int(pkm['ataque'])
	pkm['defensa']			= int(pkm['defensa'])
	pkm['ataque_esp']		= int(pkm['ataque_esp'])
	pkm['defensa_esp']	= int(pkm['defensa_esp'])
	pkm['velocidad']		= int(pkm['velocidad'])


def pokemonToSet (Pokemon_p):
	p = Pokemon_p

	l_movimientos = []
	for i in range(0, len(p.movimientos)):
		l_movimientos.append(movimientoToSet(p.movimientos[i]))

	set_p = {
		'numero': p.numero, 
		'nombre': p.nombre,
		'tipo': p.tipo,
		'nivel': p.nivel,
		'id_entrenador': p.id_entrenador,
		'sexo': p.sexo,
		'ps': p.ps_max,
		'ataque': p.ataque,
		'defensa': p.defensa,
		'ataque_esp': p.ataque_esp,
		'defensa_esp': p.defensa_esp,
		'velocidad': p.velocidad,
		'movimientos': l_movimientos}

	return set_p


def setToPokemon (set_p):
	p = set_p
	Pkm = Pokemon(p['numero'], p['nivel'], p['id_entrenador'])
	Pkm.tipo = p['tipo']
	Pkm.sexo = p['sexo']
	Pkm.setStatsBase(p['ps'], p['ataque'], p['defensa'], p['ataque_esp'], p['defensa_esp'], p['velocidad'])
		
	movimientos = []
	for movimiento in p['movimientos']:
		movimientos.append(setToMovimiento(movimiento))
	Pkm.movimientos = movimientos
	
	return Pkm;



class Pokemon:

	# Pokémon dado el nombre, nivel y estado salvaje 
	def __init__ (self, int_numero = 0, int_nivel = 5, int_id_entrenador = 0):
		
		# Buscar pokemon por número INCOMPLETO
		if (int_numero in pokemon_db):
			self.nombre = pokemon_db[int_numero]
			self.tipo = pokemon_db_t[int_numero]
		else: # Buscar el tipo del pokemon en database IMCOMPLETO
			self.nombre = "INCOMPLETO"
			self.tipo = NOTIPO

		# Establacer número de pokémon
		self.numero  = int_numero

		# Establecer Nivel 
		if (int_nivel < 5):
			int_nivel = 5
		self.nivel = int_nivel

		# Establecer ID de entrenador
		self.id_entrenador = int_id_entrenador
		
		# Lista de 4 movimientos, 0: atq0, 1: atq1, 2: atq2, 3: atq3
		self.movimientos = []
		# Inicializar movimientos a null
		for i in range(0, 4):
			self.movimientos.append(movimientos_db[''])

		# Determinar sexo del pokémon
		if (self.nombre.lower() in pokemon_legendarios):
			self.sexo = NOGENERO
		else:
			self.sexo = random.randint(0, 2)

		# Stats base por defecto, genérico
		self.ps_max 		 = 45
		self.ps 				 = self.ps_max
		self.ataque			 = 49
		self.defensa 		 = 65
		self.ataque_esp  = 49
		self.defensa_esp = 65
		self.velocidad 	 = 45

		# actualizar stats base según nivel
		for i in range(5, int_nivel):
			self.levelUp()




	def setStatsBase (self, ps, ataque, defensa, ataque_esp, defensa_esp, velocidad):
		self.ps_max 		 = ps
		self.ps 				 = self.ps_max
		self.ataque			 = ataque
		self.defensa 		 = defensa
		self.ataque_esp  = ataque_esp
		self.defensa_esp = defensa_esp
		self.velocidad 	 = velocidad

		# actualizar stats base según nivel
		for i in range(5, self.nivel):
			self.levelUp()


	def setMovimientos (self, l4_movimientos):
		if (len(l4_movimientos) <= 4):
			self.movimientos = l4_movimientos
		#for i in range(0, len(self.movimientos)):
		#	print(self.movimientos[i])



	def aprenderMovimiento (self, nuevoMovimiento):
		# Si hay hueco se aprende del tirón
		bool_aprendido = False
		for i in range(0, 4):
			if (self.movimientos[i].nombre == '-'):
				self.movimientos[i] = nuevoMovimiento
				bool_aprendido = True
				break

		# Si no hay sitio hay que preguntar al usuario qué movimiento
		# desea eliminar, INCOMPLETO
		if not bool_aprendido:
			pass




	def levelUp (self):
		if (self.nivel < 100):
			self.nivel += 1
			# actualizar stats, todo sube un 1
			self.ps_max 			+= 1
			self.ataque 			+= 1
			self.ataque_esp  	+= 1
			self.defensa 			+= 1
			self.defensa_esp 	+= 1
			self.velocidad 		+= 1


	def atacar (self, Pokemon_rival, int_sel):
		if (int_sel == -1): # El pokémon usará combate
			mov = movimientos_db['combate']
		else:
			mov = self.movimientos[int_sel] # movimiento seleccionado

		# b ni idea
		# e efectividad
		# v ni idea

		if (mov.tipo == self.tipo):
			b = 1.5
		else:
			b = 1
		e = TablaEfectividad[mov.tipo][Pokemon_rival.tipo]
		v = random.randint(85, 101) # Tiene que ser un valor discreto entre 85 y 100

		daño = 0
		if (mov.categoria == FISICO):
			daño = int(0.01 * b * e * v * (((0.2 * self.nivel + 1) * self.ataque  * mov.potencia) / (25 * Pokemon_rival.defensa) + 2))
		elif (mov.categoria == ESPECIAL):
			daño = int(0.01 * b * e * v * (((0.2 * self.nivel + 1) * self.ataque_esp * mov.potencia) / (25 * Pokemon_rival.defensa_esp) + 2))

		#	print(mov.nombre + " causó " + daño + " puntos de daño.")


		# Aplicación del cálculo de daño
		if (Pokemon_rival.ps <= daño):
			Pokemon_rival.ps = 0
		else:
			Pokemon_rival.ps -= daño

		# Si el ataque no es combate, disminuyen los pp del ataque
		if (mov.nombre != 'combate'):
			mov.pp -= 1
# fed atacar


# El ataque se elige de forma automática
	def atacarIA (self, Pokemon_rival):
		ataques_con_pp = [0, 1, 2, 3]
		
		# Comprobar ataques sin pp
		for i in range(0, 4):
			if (self.movimientos[i].pp == 0):
				ataques_con_pp.remove(i)

		# Si no hay pp se usará el ataque especial, "combate"
		if len(ataques_con_pp) == 0:
			self.atacar(Pokemon_rival, -1)
			return "combate"
		else:
			# Elegir uno de los ataques disponibles al azar
			sel = ataques_con_pp[random.randint(0, len(ataques_con_pp))]
			self.atacar(Pokemon_rival, sel)
			return str(self.movimientos[sel].nombre).lower()


	def restaurarPS (self, int_ps = 2000):
		if ((self.ps + int_ps) > self.ps_max):
			self.ps = self.ps_max
		else:
			self.ps += int_ps


	def restaurarPP (self, int_mov, int_pp = 100):
		if ((self.movimientos[int_mov].pp + int_pp) > self.movimientos[int_mov].pp_max):
			self.movimientos[int_mov].pp = self.movimientos[int_mov].pp_max
		else:
			self.movimientos[int_mov].pp += int_pp

	def restauraTodo (self):
		self.restaurarPS();
		for i in range(0, 4):
			self.restaurarPP(i)


	def list (self, l):
		b_max = l-2
		b = int(self.ps * b_max / self.ps_max)
		str_vida = ('#' * b) + ('_' * (b_max-b))

		if (self.sexo == NOGENERO):
			str_sexo = ""
		else:
			str_sexo = str(dic_genero[self.sexo])

		return 	[self.nombre + " " + str_sexo,
						"-"*l,
						"Nivel: " + str(self.nivel),
						"Tipo: " + dic_tipo[self.tipo],
					  "("+str_vida+")",
						"\tPs: " + str(self.ps) + '/' + str(self.ps_max),
						"-"*l]


	def __str__ (self):
		str_pokemon 		= ""
		str_movimientos = ""

		if (len(self.movimientos) != 0):
			str_movimientos = list_toString(self.movimientos, 8, len(self.movimientos), 24)

		# # Imprimir los movimientos en columnas de a dos
		# for i in range(0, 8):
		# 	for j in range(0, 2):
				
		# 		str_movimientos += (self.movimientos[j].list()[i]) + '\t'
		# 	str_movimientos += '\n'

		# str_movimientos += '\n'

		# for i in range(0, 8):
		# 	for j in range(2, 4):
		# 		str_movimientos += (self.movimientos[j].list()[i]) + '\t'
		# 	str_movimientos += '\n'


		# Imprimir datos del pokémon
		str_pokemon = (
			"Nombre:  " + self.nombre 						+ '\n' 
			"Número:  " + str(self.numero)  			+ '\n'
			"Tipo:    "	+ dic_tipo[self.tipo] 		+ '\n'
			"Salvaje: " + dic_sino[(self.id_entrenador == 0)] + '\n'
			"ID Entr: " + str(self.id_entrenador) 		+ '\n'
			"Sexo:    " + str(dic_genero[self.sexo]) 	+ '\n'
			"----- Stats -----\n"
			"Nivel:        " + str(self.nivel) 				+ '\n' 
			"PS:           " + str(self.ps)						+ '\n'
			"PS_MAX:       " + str(self.ps_max) 			+ '\n'
			"Ataque:       " + str(self.ataque)				+ '\n'
			"Ataque Esp.:  " + str(self.ataque_esp) 	+ '\n'
			"Defensa:      " + str(self.defensa) 			+ '\n'
			"Defensa Esp.: " + str(self.defensa_esp) 	+ '\n'
			"Velocidad:    " + str(self.velocidad) 		+ '\n'
			"-----------------\n"
			"-- Movimientos --\n" + str_movimientos + '\n')

		return str_pokemon






