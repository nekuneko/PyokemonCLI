from pokemon_t import *


def formatearMovimiento (mov):  
	mov['nombre'] 		= str(mov['nombre']).title()									# cadena en formato titulo
	mov['tipo'] 			= int(dic_tipo_inv[mov['tipo'].lower()])			# buscamos el tipo en minusculas, tipo: ACERO, DRAGON, NORMAL....
	mov['categoria'] 	= int(dic_categoria_inv[mov['categoria'].lower()])	# buscamos la categoria en minusculas, tipo: FISICO, ESPECIAL ó NOCATEG
	mov['potencia']		= int(mov['potencia'])		# tiene que ser entero
	if mov['precision'] == '-':
		mov['precision'] = int(100)
	else:
		mov['precision'] = int(mov['precision'])		# tiene que ser entero
	mov['pp']					= int(mov['pp'])					# tiene que ser entero


def movimientoToSet (Movimiento_m):
	m = Movimiento_m
	return {'nombre': m.nombre,
					'tipo': 	m.tipo,
					'categoria': m.categoria,
					'potencia':  m.potencia,
					'precision': m.precision,
					'pp': m.pp,
					'pp_max': m.pp_max}

def setToMovimiento (set_m):
	m = set_m
	mov = Movimiento(m['nombre'], m['tipo'], m['categoria'],m['potencia'], m['precision'], m['pp_max'])
	mov.pp = m['pp']

	return mov

class Movimiento:
	# Constructor de Movimiento
	def __init__ (self, str_nombre = '', t_tipo = NOTIPO, t_categoria = NOCATEGORIA, 
								int_potencia = 0, int_precision = 0, int_pp = 0):
		self.nombre 		= str_nombre
		self.tipo 			= t_tipo
		self.categoria 	= t_categoria
		self.potencia 	= int_potencia
		self.precision 	= int_precision
		self.pp_max 		= int_pp 
		self.pp 				= self.pp_max



	# devuelve las propiedades del movimiento en formato lista
	def list (self, l=8):
		return 	[self.nombre,
						"-"*l,
						"Tipo:      " + dic_tipo[self.tipo], 
						"Categoría: " + dic_categoria[self.categoria],
						"Potencia:  " + str(self.potencia),
						"Precisión: " + str(self.precision),
						"PP:        " + str(self.pp) + "/" + str(self.pp_max),
						"-"*l]

	# devuelve las propiedades del movimiento en formato cadena de caracteres
	def __str__ (self):
		return "\n".join(self.list()) + '\n'

movimientos_db = {
	'': 							Movimiento("-", 						NOTIPO, NOCATEGORIA, 	0, 0, 0),
	'combate': 				Movimiento("Combate", 			NORMAL, FISICO,       50, 100, 10),
	'ataque rapido': 	Movimiento("Ataque rápido", NORMAL, FISICO, 			40, 100, 30),
	'placaje': 				Movimiento("Placaje", 			NORMAL, FISICO, 			50, 100, 35),
	'golpe cabeza':		Movimiento("Gole cabeza", 	NORMAL, FISICO, 			70, 100, 15),
	'poder oculto':		Movimiento("Poder oculto", 	NORMAL, ESPECIAL,			60, 100, 15),
	'alboroto': 			Movimiento("Alboroto", 			NORMAL, ESPECIAL, 		90, 100, 10),
	'hiperrayo':			Movimiento("Hiperrayo", 		NORMAL, ESPECIAL, 		150, 90, 5),
	'chispa':					Movimiento("Chispa", 				ELECTRICO, FISICO, 		65, 100, 20),
	'impactrueno':		Movimiento("Impactrueno", 	ELECTRICO, ESPECIAL, 	40, 100, 30),
	'rayo':						Movimiento("Rayo", 					ELECTRICO, ESPECIAL, 	90, 100, 15),
	'trueno': 				Movimiento("Trueno", 				ELECTRICO, ESPECIAL, 	110, 70, 10),
	'psicorrayo': 		Movimiento("Psicorrayo", 		PSIQUICO, ESPECIAL, 	65, 100, 20),
	'psiquico':				Movimiento("Psíquico",			PSIQUICO, ESPECIAL, 	90, 100, 10),
	'psicoataque':		Movimiento("Psicoataque", 	PSIQUICO, ESPECIAL, 	140, 90, 5),
	'latigo cepa': 		Movimiento("Látigo cepa", 	PLANTA, FISICO, 			45, 100, 15),
	'hoja afilada':		Movimiento("Hoja afilada", 	PLANTA, FISICO, 			55, 95, 25),
	'rayo solar': 		Movimiento("Rayo Solar", 		PLANTA, ESPECIAL, 		120, 100, 10),
	'finta': 					Movimiento("Finta", 				SINIESTRO, FISICO, 		60, 100, 20),
	'desarme':				Movimiento("Desarme", 			SINIESTRO, FISICO, 		65, 100, 20),
	'llamarada': 			Movimiento("Llamarada", 		FUEGO, FISICO, 				110, 85, 5),
	'ascuas':					Movimiento("Ascuas", 				FUEGO, ESPECIAL, 			40, 100, 25),
	'estallido':  		Movimiento("Estallido", 		FUEGO, ESPECIAL, 			150, 100, 5),
	'terremoto': 			Movimiento("Terremoto", 		TIERRA, FISICO, 			100, 100, 10),
	'ventisca': 			Movimiento("Ventisca", 			HIELO, ESPECIAL, 			110, 70, 5),
	'pistola agua':		Movimiento("Pistola agua", 	AGUA, ESPECIAL, 			40, 100, 25),
	'surf':						Movimiento("Surf", 					AGUA, ESPECIAL, 			90, 100, 15),
	'salpicar': 			Movimiento("Salpicar", 			AGUA, ESPECIAL, 			150, 100, 5),
	'hidrobomba': 		Movimiento("Hidrobomba", 		AGUA, ESPECIAL, 			110, 80, 5)}

