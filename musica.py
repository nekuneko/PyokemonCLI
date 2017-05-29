import os
import time

def initMusica (bool_activar = True):
	global bool_musicaActivada
	bool_musicaActivada = bool_activar


def desactivarMusica ():
	global bool_musicaActivada
	bool_musicaActivada = False


def playMP3 (str_song, str_directory = "music"):
	global bool_musicaActivada
	try:
		if (bool_musicaActivada):
			os.system("mpg123 --loop -1 --quiet "+str(str_directory)+"/"+str(str_song)+".mp3 &")
			time.sleep(0.5)
	except Exception as e:
		pass

		

def playWAV (str_sound, str_directory = "music"):
	global bool_musicaActivada
	try:
		if (bool_musicaActivada):
			os.system("afplay "+str(str_directory)+"/"+str(str_sound)+".wav &")
	except Exception as e:
		pass
	


def stopMP3 ():
	global bool_musicaActivada
	try:
		if (bool_musicaActivada):
			os.system("pkill mpg123")
	except Exception as e:
		pass
	


def stopWAV():
	global bool_musicaActivada
	try:
		if (bool_musicaActivada):
			os.system("pkill afplay")
	except Exception as e:
		pass
	


def stop():
	stopMP3()
	stopWAV()