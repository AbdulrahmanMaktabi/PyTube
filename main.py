from pytube import YouTube
from pytube import Playlist
from os import system , name
import math

def clear():
	if name == 'nt':
		_ = system('cls')
	else :
		_ = system('clear')
def finish():
	print("Download Done!")

def Draw():
	print ("														   ")
	print ("	    ██████╗ ██╗   ██╗████████╗██╗   ██╗██████╗ ███████╗")
	print (" 	    ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝")
	print ("	    ██████╔╝ ╚████╔╝    ██║   ██║   ██║██████╔╝█████╗  ")
	print ("	    ██╔═══╝   ╚██╔╝     ██║   ██║   ██║██╔══██╗██╔══╝  ")
	print ("	    ██║        ██║      ██║   ╚██████╔╝██████╔╝███████╗")
	print ("	    ╚═╝        ╚═╝      ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝")
	print ("		           V 1.0						 		   ")
	print ("		           								 		   ")

def Download_Video():
	clear()
	Draw()

	link = input("Enter The Url: ")
	path = input("Enter The Path: ")
	clear()
	Draw()
	video = YouTube(link)
	print(f"\nVideo Titel is ===> \"{video.title}\"")
	print(f"\nVideo Duration is ===> \"{math.ceil(video.length/60)} minute\"")
	video.streams.get_highest_resolution().download(output_path=path)
	clear()
	Draw()

	video.register_on_complete_callback(finish())

def Download_PlayList():
	clear()
	Draw()

	playlist_link = input("Enter The Url: ")
	playlist_path = input("Enter The Path: ")
	playlist = Playlist(playlist_link)
	clear()
	Draw()
	for v in playlist.videos:
		v.streams.get_highest_resolution().download(output_path=playlist_path)
	playlist.register_on_complete_callback(finish())
	finish()


clear()
Draw()

print("-1- Download Video")
print("-2- Download Play List")
print("-3- Exit")
c = int(input("Enter [1-2-3]: "))

if c == 1:
	Download_Video()
elif c == 2:
	Download_PlayList()
elif c ==3:
	quit()
else :
	print("Invalid Character !")