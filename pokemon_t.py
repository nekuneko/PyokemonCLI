# Tipos de Movimientos, Pokémon, etc. TipoMovimiento, TipoRival
ACERO 			= 0
AGUA 				= 1
BICHO 			= 2
DRAGON 			= 3
ELECTRICO 	= 4
FANTASMA 		= 5
FUEGO				= 6
HADA				= 7
HIELO				= 8
LUCHA				= 9
NORMAL			= 10
PLANTA			= 11
PSIQUICO		= 12
ROCA				= 13
SINIESTRO		= 14
TIERRA			= 15
VENENO			= 16
VOLADOR			= 17
NOTIPO     	= 18 

dic_tipo = {
	ACERO: 'Acero', AGUA: 'Agua', BICHO: 'Bicho', DRAGON: 'Dragón', ELECTRICO: 'Eléctrico',
	FANTASMA: 'Fantasma', FUEGO: 'Fuego', HADA: 'Hada', HIELO: 'Hielo', LUCHA: 'Lucha',
	NORMAL: 'Normal', PLANTA: 'Planta', PSIQUICO: 'Psíquico', ROCA: 'Roca', 
	SINIESTRO: 'Siniestro', TIERRA: 'Tierra', VENENO: 'Veneno', VOLADOR: 'Volador', NOTIPO: ' '}

dic_tipo_inv = {
	'acero': ACERO, 'agua': AGUA, 'bicho': BICHO,  'dragon': DRAGON, 'electrico': ELECTRICO,
	'fantasma': FANTASMA, 'fuego': FUEGO, 'hada': HADA, 'hielo': HIELO, 'lucha': LUCHA,
	'normal': NORMAL, 'planta': PLANTA, 'psiquico': PSIQUICO, 'roca': ROCA, 'siniestro': SINIESTRO,
	'tierra': TIERRA, 'veneno': VENENO, 'volador': VOLADOR, ' ': NOTIPO}

# Categorias de Movimientos
FISICO 			= 0
ESPECIAL 		= 1
NOCATEGORIA	= 2

dic_categoria = {
	FISICO: 		 'Físico',
	ESPECIAL: 	 'Especial',
	NOCATEGORIA: ' '}

dic_categoria_inv = {
	'fisico': 	FISICO,
	'especial': ESPECIAL,
	' ': 				NOCATEGORIA}

# Género
HEMBRA		= 0
MACHO 		= 1
CHICA 		= 2
CHICO    	= 3
NOGENERO 	= 4

dic_genero = {
	HEMBRA: 	'♀',
	MACHO: 		'♂',
	CHICA:		'Chica',
	CHICO: 		'Chico',
	NOGENERO: ' '}

dic_genero_inv = {
	'♀':			HEMBRA,
	'♂':			MACHO,
	'hembra': HEMBRA,
	'macho': 	MACHO,
	'chica':	CHICA,
	'chico':  CHICO,
	' ': 			NOGENERO}


dic_sino =  {True: 'Sí', False: 'No'}

# Efectividad:
#  0 		- Sin efecto
#  0.5 	- Poco efectivo
#  1 		- Efectivo
#  2 		- Super efectivo
TablaEfectividad = { 
# Acero, Agua, Bicho, Dragón, Eléctrico, Fantasma, Fuego, Hada, Hielo, Lucha, Normal, PLanta, Psíquico, Roca, Siniestro, Tierra, Veneno, Volador 
	0 : [0.5, 0.5,  1 ,  1 , 0.5,  1 , 0.5,  2 ,  2 ,  1 ,  1 ,  1 ,  1 ,  2 ,  1 ,  1 ,  1 ,  1 ], # Acero
	1 : [ 1 , 0.5,  1 , 0.5,  1 ,  1 ,  2 ,  1 ,  1 ,  1 ,  1 , 0.5,  1 ,  2 ,  1 ,  2 ,  1 ,  1 ], # Agua
	2 : [0.5,  1 ,  1 ,  1 ,  1 , 0.5, 0.5, 0.5,  1 , 0.5,  1 ,  2 ,  2 ,  1 ,  2 ,  1 , 0.5, 0.5], # Bicho
	3 : [0.5,  1 ,  1 ,  2 ,  1 ,  1 ,  1 ,  0 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ], # Dragón
	4 : [ 1 ,  2 ,  1 , 0.5, 0.5,  1 ,  1 ,  1 ,  1 ,  1 ,  1 , 0.5,  1 ,  1 ,  1 ,  0 ,  1 ,  2 ], # Eléctrico	
	5 : [ 1 ,  1 ,  1 ,  1 ,  1 ,  2 ,  1 ,  1 ,  1 ,  1 ,  0 ,  1 ,  2 ,  1 , 0.5,  1 ,  1 ,  1 ], # Fantasma
	6 : [ 2 , 0.5,  2 , 0.5,  1 ,  1 , 0.5,  1 ,  2 ,  1 ,  1 ,  2 ,  1 , 0.5,  1 ,  1 ,  1 ,  1 ], # Fuego
	7 : [0.5,  1 ,  1 ,  2 ,  1 ,  1 , 0.5,  1 ,  1 ,  2 ,  1 ,  1 ,  1 ,  1 ,  2 ,  1 , 0.5,  1 ], # Hada
	8 : [0.5, 0.5,  1 ,  2 ,  1 ,  1 , 0.5,  1 , 0.5,  1 ,  1 ,  2 ,  1 ,  1 ,  1 ,  2 ,  1 ,  2 ], # Hielo
	9 : [ 2 ,  1 , 0.5,  1 ,  1 ,  0 ,  1 , 0.5,  2 ,  1 ,  2 ,  1 , 0.5,  2 ,  2 ,  1 , 0.5, 0.5], # Lucha
	10: [0.5,  1 ,  1 ,  1 ,  1 ,  0 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 , 0.5,  1 ,  1 ,  1 ,  1 ], # Normal
	11: [0.5,  2 , 0.5, 0.5,  1 ,  1 , 0.5,  1 ,  1 ,  1 ,  1 , 0.5,  1 ,  2 ,  1 ,  2 , 0.5, 0.5], # Planta
	12: [0.5,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  2 ,  1 ,  1 , 0.5,  1 ,  0 ,  1 ,  2 ,  1 ], # Psíquico
	13: [0.5,  1 ,  2 ,  1 ,  1 ,  1 ,  2 ,  1 ,  2 , 0.5,  1 ,  1 ,  1 ,  1 ,  1 , 0.5,  1 ,  2 ], # Roca
	14: [ 1 ,  1 ,  1 ,  1 ,  1 ,  2 ,  1 , 0.5,  1 , 0.5,  1 ,  1 ,  2 ,  1 , 0.5,  1 ,  1 ,  1 ], # Siniestro
	15: [ 2 ,  1 , 0.5,  1 ,  2 ,  1 ,  2 ,  1 ,  1 ,  1 ,  1 , 0.5,  1 ,  2 ,  1 ,  1 ,  2 ,  0 ], # Tierra 
	16: [ 0 ,  1 ,  1 ,  1 ,  1 , 0.5,  1 ,  2 ,  1 ,  1 ,  1 ,  2 ,  1 , 0.5,  1 , 0.5, 0.5,  1 ], # Veneno
	17: [0.5,  1 ,  2 ,  1 , 0.5,  1 ,  1 ,  1 ,  1 ,  2 ,  1 ,  2 ,  1 , 0.5,  1 ,  1 ,  1 ,  1 ]  # Volador
}


def list_toString (lista, int_filas, int_columnas, int_ancho):
	fil = int_filas
	col = int_columnas
	l 	= int_ancho
	str_lista = ""

	# Imprimir los movimientos en columnas de a dos o de a tres
	for i in range(0, fil):
		for j in range(0, int(col/2)):
			if (i == 0):
				str_lista += (str(j) + ') ' + lista[j].list(l)[i]).ljust(l) + '\t'
			else:
				str_lista += (lista[j].list(l)[i]).ljust(l) + '\t'
		str_lista += '\n'
	str_lista += '\n'

	for i in range(0, fil):
		for j in range(int(col/2), col):
			if (i == 0):
				str_lista += (str(j) + ') ' + lista[j].list(l)[i]).ljust(l) + '\t'
			else:
				str_lista += (lista[j].list(l)[i]).ljust(l) + '\t'
		str_lista += '\n'

	return str_lista





	
