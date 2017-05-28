import os
import time

def playMP3 (str_song):
	os.system("mpg123 --loop -1 --quiet music/" + str(str_song) + ".mp3 &")
	time.sleep(0.5)

def playWAV (str_sound):
	os.system("afplay music/" + str(str_sound) + ".wav &")


def stop():
	os.system("pkill mpg123")
	os.system("pkill afplay")