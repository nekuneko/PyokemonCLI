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


def listarArchivos ():
	initDropbox()
	# listar los archivos
	files = dbx.files_list_folder("")

	l_pkm = []
	for file in files.entries:
		l_pkm.append(file.name)

	# tener un array con los nombres
	# file_names = [file.name for file in files.entries]

	for i in l_pkm:
		i = i.replace(".jpg", "")
	
	return l_pkm


# INCOMPLETO, NO ESTÁ CONTEMPLADA LA COPIA EN WINDOWS
def descargarArchivos (str_numero, str_directorio="img/"):
	initDropbox()
	str_numero 			= str(str_numero)
	str_directorio 	= str(str_directorio)

	# Descargar imagen delantera
	path = "/" + str_numero + ".jpg" # esto es del dropbox
	name =  str_numero + ".jpg" # nombre que quiera ponerle al descargamelo
	dbx.files_download_to_file(name, path) # para bajarmelo
	os.system("mv " + str_numero + ".jpg " + str_directorio)

	# Descargar imagen trasera
	path = "/" + str_numero + "_t.jpg" # esto es del dropbox
	name =  str_numero + "_t.jpg" # nombre que quiera ponerle al descargamelo
	dbx.files_download_to_file(name, path) # para bajarmelo
	os.system("mv " + str_numero + "_t.jpg " + str_directorio)

	# Descargar stats 
	path = "/" + str_numero + ".json" # esto es del dropbox
	name =  str_numero + ".json" # nombre que quiera ponerle al descargamelo
	dbx.files_download_to_file(name, path) # para bajarmelo
	os.system("mv " + str_numero + ".json " + str_directorio)







