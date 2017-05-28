from numpy import random
from pokemon_t import *
from movimientos_db import *
import copy
import json
import modulo_dropbox
import modulo_zmq
import time
import os


l_pokemonSinSexo = [
	'baltoy','claydol','beldum','metang','metagross','ditto','voltorb','electrode',
	'lunatone','solrock','magnemite','magneton','porygon','porygon2','starmie','staryu',
	'unown']


l_pokemonLegendarios = [
	'missingno.','moltres','zapdos','articuno','mewtwo','mew','raikou', 
	'entei','suicune','lugia','ho-oh','celebi','regirock','regice', 
	'registeel','latias','latios','kyogre','groudon','rayquaza','jirachi',
	'deoxys','uxie','mesprit','azelf','dialga','palkia','heatran','regigigas',
	'giratina','cresselia','phione','manaphy','darkrai','shaymin','arceus']

l_pokemonSinSexo.extend(l_pokemonLegendarios)

# Quedan excluido Deoxys por tener más de 1 sprite en pokemondb.net
# El último pokémon representable es Deoxys
MAX_POKEMON = 386 # solo pokemon del 0 al 386, 3ª generación

# Si el pokémon está en la base de datos significa que tenemos:
# número, nombre, statsBase, foto delantera, foto trasera, y sonido
# INCOMPLETO
# AQUI DENTRO LOS MOVIMIENTOS ESTÁN PUESTOS COMO SETS, LUEGO HABRA QUE CAMBIARLOS
pokemon_db = {
	"0": {
		'nombre': "MissingNo.", 
		'tipo': NORMAL,
 		'stats': {
 	 		'ps': 120, 'ataque': 120, 'defensa': 120, 
 	 		'ataque_esp': 120, 'defensa_esp': 120, 'velocidad': 120},
 	 	'movimientos': [
 	 		movimientoToSet(movimientos_db['']),
 	 		movimientoToSet(movimientos_db['']),
 	 		movimientoToSet(movimientos_db['']),
 	 		movimientoToSet(movimientos_db[''])]},

 	"1": {
 		'nombre': "Bulbasaur", 
		'tipo': PLANTA,
 		'stats': {
 	 		'ps': 45, 'ataque': 49, 'defensa': 49, 
 	 		'ataque_esp': 65, 'defensa_esp': 65, 'velocidad': 45},
 	 	'movimientos': [
 	 		movimientoToSet(movimientos_db['placaje']),
 	 		movimientoToSet(movimientos_db['latigo cepa']),
 	 		movimientoToSet(movimientos_db['hoja afilada']),
 	 		movimientoToSet(movimientos_db[''])]},
 	
 	"25": {
 		'nombre': "Pikachu",
 		'tipo': ELECTRICO,
			'stats': {
	 			'ps': 35, 'ataque': 55, 'defensa': 40, 
	 			'ataque_esp': 50, 'defensa_esp': 50, 'velocidad': 90},
	 		'movimientos': [
 	 		movimientoToSet(movimientos_db['impactrueno']),
 	 		movimientoToSet(movimientos_db['ataque rapido']),
 	 		movimientoToSet(movimientos_db['rayo']),
 	 		movimientoToSet(movimientos_db['chispa'])]},
 
 	"201": {
 		'nombre': "Unown",
		'tipo': PSIQUICO,
		'stats': {
 			'ps': 48, 'ataque': 72, 'defensa': 48, 
 			'ataque_esp': 72, 'defensa_esp': 48, 'velocidad': 48},
 		'movimientos': [
	 		movimientoToSet(movimientos_db['poder oculto']),
	 		movimientoToSet(movimientos_db['']),
	 		movimientoToSet(movimientos_db['']),
	 		movimientoToSet(movimientos_db[''])]},
 
	"327": {
		'nombre': "Spinda",
		'tipo': NORMAL,
		'stats': {
 			'ps': 60, 'ataque': 60, 'defensa': 60, 
 			'ataque_esp': 60, 'defensa_esp': 60, 'velocidad': 60},
 		'movimientos': [
	 		movimientoToSet(movimientos_db['placaje']),
	 		movimientoToSet(movimientos_db['alboroto']),
	 		movimientoToSet(movimientos_db['psicorrayo']),
	 		movimientoToSet(movimientos_db['finta'])]},

	"351": {
	 	'nombre': "Castform",
		'tipo': NORMAL,
		'stats': {
				'ps': 70, 'ataque': 70, 'defensa': 70, 
				'ataque_esp': 70, 'defensa_esp': 70, 'velocidad': 70},
			'movimientos': [
	 		movimientoToSet(movimientos_db['placaje']),
	 		movimientoToSet(movimientos_db['pistola agua']),
	 		movimientoToSet(movimientos_db['ascuas']),
	 		movimientoToSet(movimientos_db['golpe cabeza'])]},

	"382": {
		'nombre': "Kyogre",
		'tipo': AGUA,
		'stats': {
 			'ps': 100, 'ataque': 100, 'defensa': 90, 
 			'ataque_esp': 150, 'defensa_esp': 140, 'velocidad': 90},
 		'movimientos': [
	 		movimientoToSet(movimientos_db['ventisca']),
	 		movimientoToSet(movimientos_db['surf']),
	 		movimientoToSet(movimientos_db['salpicar']),
	 		movimientoToSet(movimientos_db['hidrobomba'])]},
	 	 				 
 	"383": {
 		'nombre': "Groudon",
		'tipo': TIERRA,
		'stats': {
 			'ps': 100, 'ataque': 150, 'defensa': 140, 
 			'ataque_esp': 100, 'defensa_esp': 90, 'velocidad': 90},
 		'movimientos': [
	 		movimientoToSet(movimientos_db['llamarada']),
	 		movimientoToSet(movimientos_db['rayo solar']),
	 		movimientoToSet(movimientos_db['terremoto']),
	 		movimientoToSet(movimientos_db['estallido'])]},	

	"386": {
 		'nombre': "Deoxys",
		'tipo': PSIQUICO,
		'stats': {
 			'ps': 50, 'ataque': 150, 'defensa': 50, 
 			'ataque_esp': 150, 'defensa_esp': 50, 'velocidad': 150},
 		'movimientos': [
	 		movimientoToSet(movimientos_db['desarme']),
	 		movimientoToSet(movimientos_db['psiquico']),
	 		movimientoToSet(movimientos_db['psicoataque']),
	 		movimientoToSet(movimientos_db['hiperrayo'])]}					
}


def cargarBaseDatosPkm ():
	global pokemon_db
	try:
		with open("pokemon.db") as json_file:
			pokemon_db = json.load(json_file)
			
			# Añadir a missigno, obligatorio
			pokemon_db["0"] = {
				'nombre': "MissingNo.", 
				'tipo': NORMAL,
 				'stats': {
 	 			'ps': 120, 'ataque': 120, 'defensa': 120, 
 	 			'ataque_esp': 120, 'defensa_esp': 120, 'velocidad': 120},
 	 			'movimientos': [
 	 				movimientoToSet(movimientos_db['']),
 	 				movimientoToSet(movimientos_db['']),
 	 				movimientoToSet(movimientos_db['']),
 	 				movimientoToSet(movimientos_db[''])]}

	except Exception as e:
		# No se encuentra el archivo, usar la base de datos estática del programa
		guardarBaseDatosPkm()

	

def guardarBaseDatosPkm ():
	with open("pokemon.db", 'w') as outfile:
		json.dump(pokemon_db, outfile)


# devuelve el set de pokemon dentro del json en img/, 
def jsonDropboxToSet(int_numero):
	str_numero = str(int(int_numero))
	set_p = {}
	with open("img/"+str_numero+".json") as json_file:
		l_json = json.load(json_file)
	
		set_p = l_json[0]

	return set_p

# set de pokemon devuelto por jsonDropboxToSet
def añadirSetPkmBaseDatos (set_p):
	# Formatear entrada
	numero 			= str(int(set_p['numero']))
	nombre 			= str(set_p['nombre'])
	tipo   			= dic_tipo_inv[str(set_p['tipo'])]
	ps 					= int(set_p['ps'])
	ataque			= int(set_p['ataque'])
	defensa 		= int(set_p['defensa'])
	ataque_esp 	= int(set_p['ataque_esp'])
	defensa_esp = int(set_p['defensa_esp'])
	velocidad 	= int(set_p['velocidad'])
	stats  			= {'ps': ps, 'ataque': ataque, 'defensa': defensa, 
								 'ataque_esp': ataque_esp, 'defensa_esp': defensa_esp, 'velocidad': velocidad}

	# Formatear movimientos
	movimientos = set_p['movimientos'] 
	for i in range(0, len(movimientos)):
		movimientos[i]['categoria'] = dic_categoria_inv[movimientos[i]['categoria']]
		movimientos[i]['tipo'] 			= dic_tipo_inv[movimientos[i]['tipo']]
		movimientos[i]['nombre'] 			= movimientos[i]['nombre'].title()

	# Añadir datos a base de datos
	pokemon_db[numero] = {'nombre': nombre, 'tipo': tipo, 'stats': stats, 'movimientos': movimientos}


def pokemonToSet (Pokemon_p):
	p = Pokemon_p

	l_movimientos = []
	for i in range(0, len(p.movimientos)):
		l_movimientos.append(movimientoToSet(p.movimientos[i]))

	set_p = {
		'numero': 			int(p.numero), 
		'nombre': 			str(p.nombre),
		'tipo': 				int(p.tipo),
		'nivel': 				int(p.nivel),
		'id': 					int(p.id),
		'sexo': 				int(p.sexo),
		'ps': 					int(p.ps),
		'ps_max': 			int(p.ps_max),
		'ataque': 			int(p.ataque),
		'defensa': 			int(p.defensa),
		'ataque_esp': 	int(p.ataque_esp),
		'defensa_esp': 	int(p.defensa_esp),
		'velocidad': 		int(p.velocidad),
		'movimientos': l_movimientos}

	return set_p



def setToPokemon (set_p):
	p = set_p

	Pkm = Pokemon(int(p['numero']), int(p['nivel']), int(p['id']))
	Pkm.tipo = int(p['tipo'])
	Pkm.sexo = int(p['sexo'])
	l_stats = {
		'ps': int(p['ps_max']), 'ataque': int(p['ataque']), 'defensa': int(p['defensa']), 
		'ataque_esp': int(p['ataque_esp']), 'defensa_esp': int(p['defensa_esp']), 
		'velocidad': int(p['velocidad'])}

	Pkm.setStatsBase(int(p['numero']), int(p['nivel']), l_stats)
		
	l_movimientos = []
	for movimiento in p['movimientos']:
		l_movimientos.append(setToMovimiento(movimiento))
	Pkm.movimientos = l_movimientos
	Pkm.ps = int(p['ps'])
	
	return Pkm




class Pokemon:

	# Pokémon dado el nombre, nivel y a quien pertenece, si 0 es salvaje
	def __init__ (self, int_numero = 0, int_nivel = 5, int_id_entrenador = 0, 
								t_sexo = NOESPECIFICADO, l4_movimientos = []):
		# Conversiones Explícitas
		int_numero = int(int_numero)
		int_nivel  = int(int_nivel)
		int_id_entrenador = int(int_id_entrenador)

		# Establacer número de pokémon, si está fuera del rango representable será missigno
		if (int_numero < 0):
			self.numero = 0
		elif (int_numero > MAX_POKEMON):
			self.numero = 0
		else:
			self.numero = int_numero

		# Establecer Nivel 
		if (int_nivel < 5):
			self.nivel = 5
		elif (int_nivel > 100):
			self.nivel = 100
		else:
			self.nivel = int_nivel

		# Establecer id entrenador
		if (int_id_entrenador < 0):
			self.id = 0
		else:
			self.id = int_id_entrenador

		# El sexo se establece al final

		# Buscar pokemon por número en la base de datos local, 
		# si está en la base de datos local tenemos las imágenes y todo
		if (str(self.numero) in pokemon_db):

			self.nombre = pokemon_db[str(self.numero)]['nombre']
			self.tipo 	= pokemon_db[str(self.numero)]['tipo']

			# Poner los stats base de la base de datos
			self.setStatsBase(self.numero, self.nivel)

			# Poner movimientos de la base de datos o introducidos
			self.setMovimientos(l4_movimientos)
			# sino se preservarán los movimientos introducidos
					

		else: # Vale, el pokémon no estaba en la base de datos
			# ¿Usamos el dropbox?
			bool_usamosDropbox = True
			try:
				# Probar si se ha llamado a la función modulo_dropbox.initDropbox()
				modulo_dropbox.bool_usaDropbox
			except Exception as e:
				# No está definido bool_usaDropbox, es que no usamos dropbox
				# print(e)
				bool_usamosDropbox = False

			if (bool_usamosDropbox):
				# Trato de buscar el pokémon en dropbox durante 1 minuto (1 segundos * 60)
				bool_pokemonEnDropbox = False
				for i in range (0, 20):
					l_pkm = modulo_dropbox.listarArchivos() 	# Consulto la lista
					if (str(self.numero) + ".png" in l_pkm): 	# si el pokémon está en dropbox, True
						bool_pokemonEnDropbox = True
						break																		# y me salgo del bucle
					else:							
						modulo_zmq.buscarPokemonDbx(self.numero) 	# mando petición de busqueda
						time.sleep(3) 														# espero 5 segundos
					
				# El pokémon está en dropbox
				if (bool_pokemonEnDropbox): 
					# Me descargo los archivos en el directorio, por defecto img/
					modulo_dropbox.descargarArchivos(self.numero)

					# Coger datos de json y añadirlos a base de datos
					set_p = jsonDropboxToSet(self.numero)
					añadirSetPkmBaseDatos(set_p)
					guardarBaseDatosPkm() # guardar los cambios

					# Establecer el nombre y el tipo a partir de la base de datos
					self.nombre = pokemon_db[str(self.numero)]['nombre']
					self.tipo 	= pokemon_db[str(self.numero)]['tipo']

					# Establecer stats base a partir de la base de datos
					self.setStatsBase(self.numero, self.nivel, set_p)

					# Extraer movimientos del set y convertirlos a objetos Movimiento
					l4_movimientos = []
					for i in range(0, len(set_p['movimientos'])):
						l4_movimientos.append(setToMovimiento(set_p['movimientos'][i]))

					# print("Movimietnos. Antes")
					# for i in range(0, len(l4_movimientos)):
					# 	print(l4_movimientos[i])


					# Asignar movimientos al pokemon
					self.setMovimientos(l4_movimientos)

					# print("Movimietnos. Despues")
					# for i in range(0, len(self.movimientos)):
					# 	print(self.movimientos[i])


				# Ha pasado más de 1 minuto y el pokémon no se encuentra en dropbox,
				# por lo tanto, el pokémon es MissingNo. 
				else:
					self.MissingNo()

			# No usamos dropbox y el pokémon no está en la base de datos, 
			# por lo tanto, el pokémon es MissingNo.
			else:
				# Todo ha fallado, el pokemon es MissingNo.
				self.MissingNo()


		# Determinar sexo del pokémon
		if (self.nombre.lower() in l_pokemonSinSexo): # Si pokemon sin sexo, no tiene genero
			self.sexo = NOGENERO
		elif (t_sexo == NOESPECIFICADO): # Si no se especificó y no es legendario se genera al azar
			self.sexo = random.randint(0, 2)
		else: # si no es legendario y se especificó, se pone ese
			self.sexo = t_sexo



	# Establecer movimientos
	def setMovimientos (self, l4_movimientos = []):
		self.movimientos = copy.deepcopy(l4_movimientos)

		# Si la lista es de menos de 4 elementos, rellenar con "movimiento nulo"
		if (len(self.movimientos) < 4):
			for i in range(len(self.movimientos), 4):
				self.movimientos.append(movimientos_db[''])
		elif (len(self.movimientos) > 4): 
			while (len(self.movimientos) > 4): # Si tiene más de 4 elementos vamos quitando
				self.movimientos.pop()	         # los que sobren

		# Si el usuario no introdujo movimientos, 
		# tirar de los movimientos de la base de datos de pokemon
		if (len(l4_movimientos) == 0):
			try:
				for i in range(0, 4):
					self.movimientos[i] = setToMovimiento(pokemon_db[str(self.numero)]['movimientos'][i])
			
			except Exception as e:
				# el movimiento no está en la base de datos, nos quedamos con movimientos nulo,
				# o los que introdujera el usuario
				pass



	# Para usarla debe de haberse definido 
	def MissingNo(self):
		self.numero = 0
		self.nombre = pokemon_db["0"]['nombre']
		self.tipo 	= pokemon_db["0"]['tipo']
		self.sexo 	= NOGENERO

		# Por si no estaba definido self.nivel:
		try:
			self.nivel 
		except Exception as e:
			self.nivel = random.randint(5, 101)

		# Por si no estaba definido self.id:
		try:
			self.id 
		except Exception as e:
			self.id = 0


		# Tendrá los stats de MissignNo.
		self.setStatsBase(0, self.nivel)

		# Movimientos de MissingNo.
		self.movimientos = []
		for i in range(0, 4):
			self.movimientos.append(setToMovimiento(pokemon_db["0"]['movimientos'][i]))
		




	# Desde pokemon_db o a pelo
	def setStatsBase (self, int_numero = 0, int_nivel = random.randint(5, 101), l_stats={}):
		self.numero = int(int_numero)
		str_numero  = str(self.numero)
		int_nivel 	= int(int_nivel)
		
		if (int_nivel > 100):
			self.nivel = 100
		elif (int_nivel < 5):
			self.nivel = 5
		else:
			self.nivel = int(int_nivel)

		# Asignamos stats directamente, sin pasar por la base de datos
		if (len(l_stats) == 6):
			self.ps_max 		 = int(l_stats['ps'])
			self.ps 				 = self.ps_max
			self.ataque			 = int(l_stats['ataque'])
			self.defensa 		 = int(l_stats['defensa'])
			self.ataque_esp  = int(l_stats['ataque_esp'])
			self.defensa_esp = int(l_stats['defensa_esp'])
			self.velocidad 	 = int(l_stats['ps'])
		else: # Asignamos stats desde la base de datos
			if (str_numero in pokemon_db):				
				self.ps_max 		 = pokemon_db[str_numero]['stats']['ps']
				self.ps 				 = self.ps_max
				self.ataque			 = pokemon_db[str_numero]['stats']['ataque']
				self.defensa 		 = pokemon_db[str_numero]['stats']['defensa']
				self.ataque_esp  = pokemon_db[str_numero]['stats']['ataque_esp']
				self.defensa_esp = pokemon_db[str_numero]['stats']['defensa_esp']
				self.velocidad 	 = pokemon_db[str_numero]['stats']['velocidad']
			else: # Si no está en la base de datos, es MissingNo
				self.setStatsBase(0, self.nivel)


		# Actualizamos stats en función del nivel
		for i in range(5, self.nivel):
			self.ps_max 			+= 1
			self.ataque 			+= 1
			self.ataque_esp  	+= 1
			self.defensa 			+= 1
			self.defensa_esp 	+= 1
			self.velocidad 		+= 1

		# Curar al pokemon
		self.ps = self.ps_max 	



	def aprenderMovimiento (self, nuevoMovimiento):
		# Si hay hueco se aprende del tirón
		bool_aprendido = False
		for i in range(0, 4):
			if (self.movimientos[i].nombre == ''):
				self.movimientos[i] = copy.deepcopy(nuevoMovimiento)
				bool_aprendido = True
				break

		# Si no hay sitio hay que preguntar al usuario qué movimiento
		# desea eliminar, INCOMPLETO
		if not bool_aprendido:
			pass

		return bool_aprendido



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


	# Devuelve un diccionario con la siguiente informacion:
	# Nombre del ataque realizado, efectividad sobre el oponente, y si ha acertado o no.
	# {'nombre': "Combate", 'efectividad': int_efectividad, 'acierto': bool_haAcertado}
	def atacar (self, Pokemon_rival, int_sel):
		int_sel = int(int_sel)

		# Si ningún ataque del pokémon tiene PP, este usará combate
		if (int_sel not in [0, 1, 2, 3]): 
			mov = movimientos_db['combate']
		else:
			mov = self.movimientos[int_sel] # movimiento seleccionado


		bool_haAcertado = False
		float_efectividad = -1
		# Si el movimiento tiene PP suficientes y no es un ataque de categoria ESTADO, ataca
		if (mov.pp > 0 and mov.categoria != ESTADO):
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

			E = TablaEfectividad[int(mov.tipo)][int(Pokemon_rival.tipo)]

			# Cálculo de daño
			daño = int(0.01 * B * E * V * ((((0.2 * N + 1) * A * P)/ (25 * D)) + 2))
			

			# DEPURACIÓN
			# print ("N: "+str(N)+"\nA : "+str(A)+"\nP: "+str(P)+"\nD: "+str(D)+
			# 			 "\nB: "+str(B)+"\nE: "+str(E)+"\nV: "+str(V))
			# print(self)
			# print(Pokemon_rival)
			# print(mov.nombre + " causó " + str(daño) + " puntos de daño.")


			# ¿Acierta el ataque
			suerte = random.randint(0, mov.precision)

			if (suerte < mov.precision):
				bool_haAcertado = True

				# Aplicación del cálculo de daño
				if (Pokemon_rival.ps <= daño):
					Pokemon_rival.ps = 0
				else:
					Pokemon_rival.ps -= daño

			float_efectividad = float(E)

			# Si el ataque no es combate, disminuyen los pp del ataque
			if (mov.nombre != 'combate'):
				mov.pp -= 1

		else: # El movimiento seleccionado no tiene PP suficientes o es de categoria ESTADO
			pass

		# Devuelve el ataque utilizado por el pokémon, util para el ataque de IA
		if (int_sel not in [0, 1, 2, 3]):
			return {'ataque': "Combate", 'efectividad': float_efectividad, 'acierto': bool_haAcertado}
		else:
			str_nombre = str(self.movimientos[int_sel].nombre).title()
			return {'ataque': str_nombre, 'efectividad': float_efectividad, 'acierto': bool_haAcertado}

# fin atacar


	# Elige un ataque de forma automática y ataca, devuelve el ataque utilizado
	def atacarIA (self, Pokemon_rival):
		# Comprobar que el pokémon tenga PP en al menos un ataque
		ataques_con_pp = [0, 1, 2, 3]
		for i in range(0, 4):
			if (self.movimientos[i].pp <= 0):
				ataques_con_pp.remove(i)

		# Si no hay pp se usará el ataque especial, "combate"
		if len(ataques_con_pp) == 0:
			return self.atacar(Pokemon_rival, -1)
		else:
			# Elegir uno de los ataques disponibles al azar
			sel = ataques_con_pp[random.randint(0, len(ataques_con_pp))]
			return self.atacar(Pokemon_rival, sel)





	def gritar(self):
		os.system("afplay sounds/"+str(self.numero)+".wav &");


	def restaurarPP (self, int_mov, int_pp = -1):
		int_pp = int(int_pp)

		# Si int_pp es negativo o la suma con los pp es mayor que los pp maximos, curar todos
		if ((int_pp < 0) or 
			 	((self.movimientos[int_mov].pp + int_pp) > self.movimientos[int_mov].pp_max)):
			self.movimientos[int_mov].pp = self.movimientos[int_mov].pp_max
		else:
			self.movimientos[int_mov].pp += int_pp


	def restaurarPS (self, int_ps = -1):
		int_ps = int(int_ps)

		# Si int_ps es negativo o la suma con los ps es mayor que los ps maximos, curar todos
		if ((int_ps < 0) or ((self.ps + int_ps) > self.ps_max)):
			# restaurar todos los ps
			self.ps = self.ps_max
		else:
			self.ps += int_ps


	def restauraTodo (self):
		self.restaurarPS();
		for i in range(0, 4):
			self.restaurarPP(i)


	# Esta es la foma abreviada de imprimir datos de un pokemon, sirve para imprimir
	# los pokémon del equipo principalmente y su estado
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
						"\tPS: " + str(self.ps) + '/' + str(self.ps_max),
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


		# # Imprimir datos del pokémon
		str_pokemon = (
			"Nombre:  " + self.nombre 						+ '\n' 
			"Número:  " + str(self.numero)  			+ '\n'
			"Tipo:    "	+ dic_tipo[self.tipo] 		+ '\n'
			"Salvaje: " + dic_sino[(self.id == 0)] + '\n'
			"ID Entr: " + str(self.id) 		+ '\n'
			"Sexo:    " + str(dic_genero[self.sexo]) 	+ '\n'
			"\n----- Stats -----\n"
			"Nivel:        " + str(self.nivel) 				+ '\n' 
			"PS:           " + str(self.ps)						+ '\n'
			"PS_MAX:       " + str(self.ps_max) 			+ '\n'
			"Ataque:       " + str(self.ataque)				+ '\n'
			"Ataque Esp.:  " + str(self.ataque_esp) 	+ '\n'
			"Defensa:      " + str(self.defensa) 			+ '\n'
			"Defensa Esp.: " + str(self.defensa_esp) 	+ '\n'
			"Velocidad:    " + str(self.velocidad) 		+ '\n'
			"-----------------\n"
		 	"\n-- Movimientos --\n" + str_movimientos + '\n')

		return str_pokemon






