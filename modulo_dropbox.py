import dropbox

token = "6UFVrW8YL3EAAAAAAAAHsilYoLPNXvzLA5q1v8xCZymMFUdgi-dKxalZRGU2m8Cn"
dbx = dropbox.Dropbox(token)
user = dbx.users_get_current_account()


# listar los archivos
files = dbx.files_list_folder("")

for file in files.entries:
	print(file.name)


# tener un array con los nombres
file_names = [file.name for file in files.entries]


path = "/" + str(383) + ".jpg" # esto es del dropbox
name =  str(383) + ".jpg" # nombre que quiera ponerle al descargamelo
dbx.files_download_to_file(name, path) # para bajarmelo






