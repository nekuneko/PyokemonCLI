import menu
import modulo_dropbox
import pokemon
from pokemon import *
from pokemon_t import *
import interfaz

# Iniciar el módulo dropbox
modulo_dropbox.initDropbox()

# Consultar la lista del dropbox
# l_pkm = modulo_dropbox.listarArchivos() 	
# print(l_pkm)

# Cargar base de datos de pokémon Local
pokemon.cargarBaseDatosPkm()
menu.next_move()

# Guardar base de datos y salir
pokemon.guardarBaseDatosPkm()
print("Fin de la Partida")
print("Gracias por jugar :D")





