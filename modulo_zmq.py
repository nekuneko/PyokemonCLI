import zmq
import json

contextTwitter = zmq.Context()
contextDropbox = zmq.Context()

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



print("Conectando Fernando Server...")
socketDropbox = contextDropbox.socket(zmq.PUSH)
socketDropbox.connect("tcp://10.182.108.214:6969")
print("Conectado a Fernando Server 2007 X Pro.")

for i in range(38, 50):
	socketDropbox.send_string(str(i))







