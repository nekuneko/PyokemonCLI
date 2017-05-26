import menu
import modulo_dropbox
import pokemon
from pokemon import *
from pokemon_t import *

# Iniciar el módulo dropbox
# modulo_dropbox.initDropbox()
# Consultar la lista del dropbox
# l_pkm = modulo_dropbox.listarArchivos() 	
# print(l_pkm)

# Cargar base de datos de pokémon Local
pokemon.cargarBaseDatosPkm()

#pokemon.guardarBaseDatosPkm()


p = Pokemon(36, -420)
print(p)


pokemon.cargarBaseDatosPkm()
menu.next_move()