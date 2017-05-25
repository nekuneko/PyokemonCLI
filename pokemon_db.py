from numpy import random
from pokemon_t import *
from movimientos_db import *
import json

# Antes de usar la clase Pokémon se tiene que llamar a esta función
def usaDropbox (param = False):
	global bool_usaDropbox
	bool_usaDropbox = param



pokemon_legendarios = {'moltres', 'zapdos', 'articuno', 'mewtwo', 'mew', 'raikou', 'entei',
											 'suicune', 'lugia', 'ho-oh', 'celebi', 'regirock', 'regice', 'registeel',
											 'latias', 'latios', 'kyogre', 'groudon', 'rayquaza', 'jirachi', 'deoxys',
											 'uxie', 'mesprit', 'azelf', 'dialga', 'palkia', 'heatran', 'regigigas',
											 'giratina', 'cresselia', 'phione', 'manaphy', 'darkrai', 'shaymin', 'arceus'}

# Si el pokémon está en la base de datos significa que tenemos:
# número, nombre, statsBase, foto delantera, foto trasera, y sonido
pokemon_db = {
	0: {'nombre': "MissingNo.", 
			'tipo': NORMAL,
	 		'stats': {
	 	 		'ps': 120, 'ataque': 120, 'defensa': 120, 
	 	 		'ataque_esp': 120, 'defensa_esp': 120, 'velocidad': 120}},
 	1: {'nombre': "Bulbasaur", 
			'tipo': PLANTA,
	 		'stats': {
	 	 		'ps': 45, 'ataque': 49, 'defensa': 49, 
	 	 		'ataque_esp': 65, 'defensa_esp': 65, 'velocidad': 45}},
 	382: {'nombre': "Kyogre",
 				'tipo': AGUA,
 				'stats': {
	 	 			'ps': 100, 'ataque': 100, 'defensa': 90, 
	 	 			'ataque_esp': 150, 'defensa_esp': 140, 'velocidad': 90}},						 
 	383: {'nombre': "Groudon",
 				'tipo': TIERRA,
 				'stats': {
	 	 			'ps': 100, 'ataque': 150, 'defensa': 140, 
	 	 			'ataque_esp': 100, 'defensa_esp': 90, 'velocidad': 90}}}


def cargarBaseDatosPkm ():
	with open("pokemon.db") as json_file:
		pokemon_db = json_file

def guardarBaseDatosPkm ():
	with open("pokemon.db", 'w') as outfile:
		json.dump(pokemon_db, outfile)


def formatearPokemon (set_pkm):
	pkm = set_pkm
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

	# Pokémon dado el nombre, nivel y a quien pertenece, si 0 es salvaje
	def __init__ (self, int_numero = 0, int_nivel = 5, int_id_entrenador = 0):

		# Establacer número de pokémon
		self.numero = int_numero

		# Establecer Nivel 
		if (int_nivel < 5):
			int_nivel = 5
		self.nivel = int_nivel

		# Buscar pokemon por número en la base de datos local, si está en la base de datos
		# local tenemos las imágenes y todo
		if (int_numero in pokemon_db):
			self.nombre = pokemon_db[int_numero]['nombre']
			self.tipo = pokemon_db[int_numero]['tipo']
		else:
			try:
				if (bool_usaDropbox == True):
					pass # INCOMPLETO
				else: # Pokémon MissingNo.
					self.nombre = pokemon_db[0]['nombre']
					self.tipo = pokemon_db[0]['tipo']
					self.numero = 0

			# Esta escepción salta cuando no se ha establecido que se use el dropbox ó
			# ha fallado la búsqueda
			except Exception as e:
				self.nombre = pokemon_db[0]['nombre']
				self.tipo = pokemon_db[0]['tipo']
				self.numero = 0

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
		self.ps_max 		 = pokemon_db[self.numero]['stats']['ps']
		self.ataque			 = pokemon_db[self.numero]['stats']['ataque']
		self.defensa 		 = pokemon_db[self.numero]['stats']['defensa']
		self.ataque_esp  = pokemon_db[self.numero]['stats']['ataque_esp']
		self.defensa_esp = pokemon_db[self.numero]['stats']['defensa_esp']
		self.velocidad 	 = pokemon_db[self.numero]['stats']['velocidad']

		# actualizar stats base según nivel
		for i in range(5, int_nivel):
		 	self.levelUp()

		self.ps 				 = self.ps_max


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
		if (self.nivel >= 100):
			self.nivel = 100
		else:
			self.nivel += 1

		# actualizar stats, todo sube un 1
		self.ps_max 			+= 1
		self.ataque 			+= 1
		self.ataque_esp  	+= 1
		self.defensa 			+= 1
		self.defensa_esp 	+= 1
		self.velocidad 		+= 1


	def atacar (self, Pokemon_rival, int_sel):
		# Si ningún ataque del pokémon tiene PP, este usará combate
		if (int_sel not in [0, 1, 2, 3]): 
			mov = movimientos_db['combate']
		else:
			mov = self.movimientos[int_sel] # movimiento seleccionado

		
		# Si el movimiento tiene PP suficientes, ataca
		if (mov.pp > 0):
			# CÁLCULO DE DAÑO
			#
			# DAÑO = 0.01 * B * E * V * ((((0.2 * N + 1) * A * P)/ (25 * D)) + 2) 
			#
			# N = Nivel del Pokémon que ataca. 
			# A = Cantidad de ataque o ataque especial del Pokémon. Si el ataque que utiliza 
			# 		el Pokémon es físico se toma la cantidad de ataque y si es especial se toma 
			#  		la cantidad de ataque especial. 
			# P = Poder del ataque, el potencial del ataque. 
			# D = Cantidad de defensa del Pokémon rival. Si el ataque que hemos utilizado es físico
			#  		cogeremos la cantidad de defensa del Pokémon rival, si el ataque que hemos
			# 		utilizado es especial, se coge la cantidad de defensa especial del Pokémon rival. 
			# B = Bonificación. Si el ataque es del mismo tipo que el Pokémon que lo lanza toma un 
			#  		valor de 1.5, si el ataque es de un tipo diferente al del Pokémon que lo lanza 
			# 		toma un valor de 1. 
			# E = Efectividad. Puede tomar los valores de 0, 0.25, 0.5, 1, 2 y 4. 
			# V = Variación. Es una variable que comprende todos los valores discretos entre 85 y 100 (ambos incluidos). 
				
			N = self.nivel
			A = 0
			P = mov.potencia
			D = 0
			B = 0
			E = 0
			V = random.randint(85, 101)

			if (mov.categoria == FISICO):
				A = self.ataque
				D = Pokemon_rival.defensa
			elif (mov.categoria == ESPECIAL):
				A = self.ataque_esp
				D = Pokemon_rival.defensa_esp

			if (mov.tipo == self.tipo):
				B = 1.5
			else:
				B = 1
			D = 300
			if (mov.categoria != ESTADO):
				E = TablaEfectividad[mov.tipo][Pokemon_rival.tipo]

			# Cálculo de daño
			daño = int(0.01 * B * E * V * ((((0.2 * N + 1) * A * P)/ (25 * D)) + 2))
			print ("N: "+str(N)+"\nA : "+str(A)+"\nP: "+str(P)+"\nD: "+str(D)+
						 "\nB: "+str(B)+"\nE: "+str(E)+"\nV: "+str(V))

			# DEPURACIÓN
			print(self)
			print(Pokemon_rival)
			print(mov.nombre + " causó " + str(daño) + " puntos de daño.")



			# Aplicación del cálculo de daño
			if (Pokemon_rival.ps <= daño):
				Pokemon_rival.ps = 0
			else:
				Pokemon_rival.ps -= daño

			# Si el ataque no es combate, disminuyen los pp del ataque
			if (mov.nombre != 'combate'):
				mov.pp -= 1

		else: # El movimiento seleccionado no tiene PP suficientes
			pass

		# Devuelve el ataque utilizado por el pokémon
		if (int_sel not in [0, 1, 2, 3]):
			return "combate"
		else:
			return str(self.movimientos[int_sel].nombre).lower()

# fed atacar


	# Elige un ataque de forma automática y ataca, devuelve el ataque utilizado
	def atacarIA (self, Pokemon_rival):
		# Comprobar que el pokémon tenga PP en al menos un ataque
		ataques_con_pp = [0, 1, 2, 3]
		for i in range(0, 4):
			if (self.movimientos[i].pp == 0):
				ataques_con_pp.remove(i)

		# Si no hay pp se usará el ataque especial, "combate"
		if len(ataques_con_pp) == 0:
			return self.atacar(Pokemon_rival, -1)
		else:
			# Elegir uno de los ataques disponibles al azar
			sel = ataques_con_pp[random.randint(0, len(ataques_con_pp))]
			return self.atacar(Pokemon_rival, sel)


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






