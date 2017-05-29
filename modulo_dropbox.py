import dropbox
import os

# No es necesario llamar a esta función de forma explícita
def initDropbox (str_token="6UFVrW8YL3EAAAAAAAAHsilYoLPNXvzLA5q1v8xCZymMFUdgi-dKxalZRGU2m8Cn"):
	global bool_usaDropbox
	global token
	global dbx
	global user
	bool_usaDropbox = True
	token = str_token
	dbx 	= dropbox.Dropbox(token)
	user 	= dbx.users_get_current_account()



# devuelve True si el módulo está activado, False en caso contrario
def estaActivado ():
	global bool_usaDropbox
	try:
		# Probar si se ha llamado a la función modulo_dropbox.initDropbox()
		bool_dropboxActivado = bool_usaDropbox
	except Exception as e:
		# No está definido bool_usaDropbox, es que no usamos dropbox
		# print(e)
		bool_dropboxActivado = False

	return bool_dropboxActivado



def desactivar ():
	global bool_usaDropbox
	try:
		bool_usaDropbox = False
	except Exception as e:
		pass


def listarArchivos ():
	initDropbox()
	# listar los archivos
	files = dbx.files_list_folder("")

	# l_pkm = []
	# for file in files.entries:
	# 	l_pkm.append(file.name)

	# tener un array con los nombres
	l_pkm = [file.name for file in files.entries]

	# for i in l_pkm:
	# 	i = i.replace(".png", "")
	
	return l_pkm



# INCOMPLETO, NO ESTÁ CONTEMPLADA LA COPIA EN WINDOWS
def descargarArchivos (str_numero, str_directorio="img/"):
	initDropbox()
	str_numero 			= str(str_numero)
	str_directorio 	= str(str_directorio)

	# Descargar imagen delantera
	path = "/" + str_numero + ".png" # esto es del dropbox
	name =  str_numero + ".png" # nombre que quiera ponerle al descargamelo
	dbx.files_download_to_file(name, path) # para bajarmelo
	os.system("mv " + str_numero + ".png " + str_directorio)

	# Descargar imagen trasera
	path = "/" + str_numero + "_t.png" # esto es del dropbox
	name =  str_numero + "_t.png" # nombre que quiera ponerle al descargamelo
	dbx.files_download_to_file(name, path) # para bajarmelo
	os.system("mv " + str_numero + "_t.png " + str_directorio)

	# Descargar stats 
	path = "/" + str_numero + ".json" # esto es del dropbox
	name =  str_numero + ".json" # nombre que quiera ponerle al descargamelo
	dbx.files_download_to_file(name, path) # para bajarmelo
	os.system("mv " + str_numero + ".json " + str_directorio)







