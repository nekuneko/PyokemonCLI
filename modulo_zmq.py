import zmq
import json

# Las funciones init se auto inician, así que no es necesario llamarlas de forma explicita
# pero en cambio SI ES NECESARIO CAMBIAR LA IP Y EL PUERTO AQUI SI FUERA NECESARIO
GLOBAL_STR_IP 		= "10.182.106.194"
GLOBAL_STR_PUERTO = "6969"

def initTwitter (str_ip=GLOBAL_STR_IP, str_puerto=GLOBAL_STR_PUERTO):
	global contextTwitter
	global socketTwitter

	contextTwitter 	= zmq.Context()
	socketTwitter 	= contextTwitter.socket(zmq.PUSH)
	socketTwitter.connect("tcp://"+str(str_ip)+':'+str(str_puerto))

def initBusqueda (str_ip=GLOBAL_STR_IP, str_puerto=GLOBAL_STR_PUERTO):
	global contextBusqueda
	global socketBusqueda
	contextBusqueda = zmq.Context()
	socketBusqueda = contextBusqueda.socket(zmq.PUSH)	
	socketBusqueda.connect("tcp://"+str(str_ip)+':'+str(str_puerto))



# Publicar algo en twitter relacionado con un pokémon, primero debe de haberse ejecutado
# al menos una vez initTwitter()
def publicarTwitter (Pokemon_p, str_msg = "¡Pokémon salvaje apareció!", password = "pepe"):
	initTwitter()
	p_name 		= Pokemon_p.nombre
	p_numero 	= Pokemon_p.numero
	p_nivel 	= Pokemon_p.nivel
	if (Pokemon_p.id == 0):
		salvaje = True
	else:
		salvaje = False

	# Si el pokémon es salvaje, mensaje que apareció,
	# sino mensaje y punto

	str_msg += '\n' + p_name + "   Nv: " + str(p_nivel)
	str_json = {'password': password, 'mensaje': str_msg, 'salvaje': salvaje, 'numero': p_numero, 'nivel': p_nivel}
	l_json = json.dumps(str_json)

	socketTwitter.send_json(l_json)



# Buscar Pokemon con scrapy en máquina remota, primero debe haberse ejecutado al menos
# una vez initBusqueda()
def buscarPokemonDbx (int_numero):
	initBusqueda()
	socketBusqueda.send_string(str(int_numero))




# print("Conectando a twitter...")
# socketTwitter = contextTwitter.socket(zmq.PUSH)
# socketTwitter.connect("tcp://10.182.106.194:6969")
# print("Conectado a twitter.")


# for i in range(0, 6):
# 	p_name = str(i) #"Bulbasaur"
# 	p_numero = i
# 	p_nivel = 25
# 	print(i)

# 	str_msg = "¡Pokémon salvaje apareció!"
# 	str_msg += '\n' + p_name + "   Nv: " + str(p_nivel)
# 	str_json = {'password': "pepe", 'mensaje': str_msg, 'salvaje': True, 'numero': p_numero, 'nivel': p_nivel}
# 	l_json = json.dumps(str_json)

# 	socketTwitter.send_json(l_json)



# print("Conectando Fernando Server...")
# contextBusqueda = contextBusqueda.socket(zmq.PUSH)
# contextBusqueda.connect("tcp://10.182.108.214:6969")
# print("Conectado a Fernando Server 2007 X Pro.")

# for i in range(38, 50):
# 	contextBusqueda.send_string(str(i))







