from interfaz import *
from entrenador import *


# PRUEBAAASS
e = cargarPartida()
r = cargarPartida("chico.json")

pe = e.sacarPokemon()
pr = r.sacarPokemon()
#pe = Pokemon(0, 100)
pe.movimientos[0].pp = 0
pr = Pokemon(0, 100)

combateVSPokemonSalvaje(e, pr)



#combateVSEntrenador(e, r)
