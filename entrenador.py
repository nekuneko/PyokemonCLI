from numpy import random
from pokemon_t import *
from movimientos_db import *
from pokemon import *
import json


def cargarPartida (fichero = "PyokemonCLIsave.json"):
	with open(fichero) as json_file:  
		save = json.load(json_file)
		equipo = []
		
		entrenador = Entrenador(save['nombre'], save['genero'], save['id'])

		# Equipar pokémon
		for pokemon in save['equipo']:
		 	entrenador.equipar(setToPokemon(pokemon))

		#print(entrenador)
		entrenador.mapa = save['mapa']
		entrenador.x = save['coord_x']
		entrenador.y = save['coord_y']
	return entrenador



def guardarPartida (entrenador_e, fichero = "PyokemonCLIsave.json"):
	e = entrenador_e
	
	list_equipo =[]
	for i in range(0, len(e.equipo)):
		list_equipo.append(pokemonToSet(e.equipo[i])) 

	str_fichero = {
		'nombre': e.nombre, 
		'genero': e.genero,
		'id': e.id,
		'equipo': list_equipo,
		'mapa': e.mapa,
		'coord_x': e.x,
		'coord_y': e.y}
	
	with open(fichero, 'w') as outfile:  
		json.dump(str_fichero, outfile)




class Entrenador:

	def __init__  (self, str_nombre, t_genero = CHICO, id = random.randint(1, 2^32), equipo_Pokemon = []):
		self.nombre = str_nombre
		self.genero = t_genero
		self.id 		= id
		self.equipo = equipo_Pokemon 
		self.mapa = "route1"
		self.x = 22
		self.y = 6

		# Quitar Pokemon que sobren
		while(len(self.equipo_Pokemon) > 6):
			self.equipo_Pokemon.pop()




	def equipar (self, Pokemon_p):
		bool_exito = False

		# Captura al pokémon si es salvaje, asignandole el id del entrenador
		if (Pokemon_p.id_entrenador == 0):
			Pokemon_p.id_entrenador = self.id
		# Sino no hace nada porque podría ser un pokémon de intercambio de otro jugador
		
		# Trata de meter el pokémon en el equipo, si hay espacio, sino devuelve False
		if (len(self.equipo) <= 5):
			self.equipo.append(Pokemon_p)
			bool_exito = True

		return bool_exito


	def curarEquipo (self):
		for i in range(0, len(self.equipo)):
			self.equipo[i].restauraTodo()


	def hayPokemonVivo (self):
		bool_hayPokemonVivo = False

		for i in range(0, len(self.equipo)): # Si hay un pokemon vivo que no sea nulo
			if (self.equipo[i].ps > 0):
				bool_hayPokemonVivo = True
				break
				
		return bool_hayPokemonVivo


	# Entrenador saca a su primer pokémon no nulo no debilitado,
	# Verificar primero que haya un pokemon vivo con el metdoo hayPokemonVivo
	# si no hay pokemon vivo lanzara una excepcion
	def sacarPokemon (self):
		pkm_elegido = -1

		for i in range(0, len(self.equipo)):
			if (self.equipo[i].ps > 0):
				pkm_elegido = i
				break

		if (pkm_elegido ==  -1):
			print("ERROR, EL ENTRENADOR NO TIENE POKÉMONS SANOS")

		return self.equipo[pkm_elegido]




	def __str__ (self):
		str_id = str(self.id)
		str_genero = str(dic_genero[self.genero])

		str_equipo = ""

		if (len(self.equipo) == 0):
			str_equipo = "No hay ningún Pokémon en el equipo.\n"
		else: 
			str_equipo = list_toString(self.equipo, 7, len(self.equipo), 24)
			# for i in range(0, len(self.equipo)):
			# 	str_equipo += str("\n".join(self.equipo[i].list()))


		return ("Nombre: "  + self.nombre 		+ '\n' 
					  "Género: "  + str_genero 			+ '\n' 
					 	"ID:     "  + str_id 					+ '\n' 
					 	"Mapa:    " + str(self.mapa) 	+ '\n'
					 	"Coord_x: " + str(self.x) 	 	+ '\n'
					 	"Coord_y: " + str(self.y) 		+ '\n'
					 	"--- Equipo ---\n" + str_equipo)



# # Como crear  un entrenador
# e = Entrenador("Bruno", CHICO)
# print(e)



# # Pokémon Kyogre de tipo Agua al nivel 100 salvaje
# #  ps, ataque, defensa, ataque_esp, defensa_esp, velocidad
# # vector de 4 ataques
# kyogre = Pokemon(382, 100)
# kyogre.setStatsBase(310, 205, 185, 305, 285, 185)
# movimientos = {0: movimientos_db['ventisca'], 1: movimientos_db['surf'], 
# 							 2: movimientos_db['salpicar'], 3: movimientos_db['hidrobomba']}
# #kyogre.setMovimientos(movimientos)


# # Como meter un movimiento en la base de datos, doy un numero, me devuelven un diccionario:
# mov = {'nombre': "RAYO carGa", 'tipo': "ElEcTrIcO", 'categoria': "ESPECial", 'potencia': 50, 'precision': 90, 'pp': 10} # <-
# formatearMovimiento(mov); # Formatear entrada
# # Introducir en base de datos
# movimientos_db[mov['nombre'].lower()] = Movimiento(mov['nombre'], mov['tipo'], mov['categoria'],
# 																									 mov['potencia'], mov['precision'], mov['pp']) 


# # Como meter un pokemon en la base de datos
# numero = 383 # -> Solicitar Pkm por numero
# nivel = 100
# pkm = {'numero': 383, 'nombre': "GroUDON", 'tipo': "TIERRA", 'ps': 310, 'ataque': 205, 'defensa': 305, 
# 			 'ataque_esp': 285, 'defensa_esp': 205, 'velocidad': 185}	# <- 

# formatearPokemon(pkm)
# groudon = Pokemon(numero, nivel)
# groudon.setStatsBase(pkm['ps'], pkm['ataque'], pkm['defensa'], pkm['ataque_esp'], pkm['defensa_esp'], pkm['velocidad'])
# movimientos = {0: movimientos_db[''], 1: movimientos_db['rayo solar'],
# 							 2: movimientos_db['trueno'], 3: movimientos_db['estallido']}
# #groudon.setMovimientos(movimientos)

# # Como hacer que el pokémon aprenda un movimiento
# print(groudon)
# groudon.aprenderMovimiento(movimientos_db['terremoto'])
# groudon.aprenderMovimiento(movimientos_db['estallido'])
# groudon.aprenderMovimiento(movimientos_db['rayo carga'])
# print(groudon)

# # Curar al pokémon y restaurar PP
# groudon.ps = 3
# groudon.movimientos[2].pp = 3
# print(groudon)
# groudon.restaurarPS()
# groudon.restaurarPP(2, 3)
# print(groudon)

# # Ejemplo de combate
# print(kyogre)
# groudon.atacar(kyogre, 0)
# print(kyogre)


# atq = kyogre.atacarIA(groudon)
# print(kyogre.nombre + " usó " + atq)
# print(groudon)



# # Ejemplo de entrenador con equipo pokemon
# groudon.restauraTodo()
# kyogre.restauraTodo()
# groudon.ps = 155
# e.equipar(groudon)
# e.equipar(kyogre)
# e.equipar(kyogre)
# e.equipar(Pokemon(1))
# kyogre.ps = 30
# e.equipar(kyogre)
# e.equipar(kyogre)
# e.equipar(groudon) # este groudon no se mete
# print(e)

# #guardarPartida(e)
# e = cargarPartida()
# print(e)

# mov = e.equipo[0].atacarIA(e.equipo[1])
# print(e.equipo[0].nombre + " usó " + mov + " contra " + e.equipo[1].nombre)
# print(e)
