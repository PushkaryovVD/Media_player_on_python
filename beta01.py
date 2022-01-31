import os
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3
from tkinter import *
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3
root=Tk()
root.minsize(300,300)
label_title=('Icon/label.ico')
root.iconbitmap(label_title)
background=PhotoImage(file="Icon/background.gif")
root.configure(bg='skyblue')
root.title("Music Player")
#load photo
add_directory=PhotoImage(file="Icon/add_directory.gif")
minus=PhotoImage(file="Icon/minus.gif")
plus=PhotoImage(file="Icon/plus.gif")
mute=PhotoImage(file="Icon/mute.gif")
play=PhotoImage(file="Icon/play.gif")
pause=PhotoImage(file="Icon/pause.gif")
next_song=PhotoImage(file="Icon/next_song.gif")
previousy_song=PhotoImage(file="Icon/priveously_song.gif")
repeat=PhotoImage(file="Icon/repeat.gif")
stop=PhotoImage(file="Icon/stop.gif")

#list
list_of_songs=[]
realnames=[]
singer_title=[]

v=StringVar()
songlabel=Label(root,textvariable=v,width=35)

index=0
volume=1.0
totalsonglenght=0
count=0
text=''
#test_btn=Button(root)
#test_lab=Label(root)
def Plus_volume(event):
	global volume
	volume+=0.2
	pygame.mixer.music.set_volume(volume)
	if volume>=1:
		volume=1
	#test_lab['text']=volume
def Minus_volume(event):
	global volume
	volume-=0.2
	pygame.mixer.music.set_volume(volume)
	if volume<=0.1:
		volume=0	
	#test_lab['text']=volume
def updatelabel():
	global index
	v.set(f'{realnames[index]}-{singer_title[index]}')
	
def Next_song(event):
	global index
	index+=1
	pygame.mixer.music.load(list_of_songs[index])
	pygame.mixer.music.play()
	updatelabel()
	#pygame.mixer.music.queue(list_of_songs[index+1])
def Repeat_indefinatly(event):
	global index
	pygame.mixer.music.load(list_of_songs[index])
	pygame.mixer.music.play(loops=1)	
#Автоматическое переключение
def Play(event):
	global index 
	pygame.mixer.music.queue(list_of_songs[index+1])
	Song=MP3(list_of_songs[song])
	totalsonglenght=int(Song.info.lenght)
	print(totalsonglenght)
	#pygame.mixer.music.load(list_of_songs[song])
	#pygame.mixer.music.play()
	#updatelabel()
def Previous_song(event):
	global index
	index-=1
	pygame.mixer.music.load(list_of_songs[index])
	pygame.mixer.music.play()
	updatelabel()

def Stop(event):
	pygame.mixer.music.stop()
	v.set("")

def directorychoser():
	directory=askdirectory()
	#directory='C:/Users/Вадим/Desktop/Media_player/music/'
	os.chdir(directory)
	for files in os.listdir(directory):
		if files.endswith('.mp3'):
			realdir=os.path.realpath(files)
			audio=ID3(realdir)
			realnames.append(audio.getall('TIT2')[0])#Вывод названия
			#singer_title.append(audio.getall('TPE2')[0])
			a=audio.getall('TPE2')
			for singer in a:
				singer_title.append(singer)
			list_of_songs.append(files)
			#print(files)

	pygame.mixer.init()
	pygame.mixer.music.load(list_of_songs[0])
	#pygame.mixer.music.play()

directorychoser()
#test_lab.pack()
label_listbox_frame=Frame(root)
label=Label(label_listbox_frame,text="Music Player")
listbox=Listbox(label_listbox_frame)
label_listbox_frame.pack()
label.pack()
listbox.pack()
#Переворачиваю список
realnames.reverse()
for items in realnames:
	listbox.insert(0,items)
#Возвращаю
realnames.reverse()

swithbtn_frame=Frame(root)

nextbtn=Button(swithbtn_frame,image=next_song)
nextbtn.image=next_song
previousbtn=Button(swithbtn_frame,image=previousy_song)
previousbtn.image=previousy_song
stopbtn=Button(swithbtn_frame,image=stop)
stopbtn.image=stopbtn
repeatbtn=Button(swithbtn_frame,image=repeat)
repeatbtn.image=repeatbtn
volume_frame=Frame(root)
plus_volume=Button(volume_frame,image=plus)
plus_volume.image=plus
minus_volume=Button(volume_frame,image=minus)
minus_volume.image=minus
volume_frame.pack(side='right')
plus_volume.pack()
minus_volume.pack()
############################Progressbarmusci
Progressbarmuscicframe=Frame(root)
ProgressbarMusicLabel=Label(Progressbarmuscicframe,text='',bg='red')
ProgressbarStartTimerLabel=Label(Progressbarmuscicframe,text='0:00:0',bg='red')

ProgressbarMusic=Progressbar(ProgressbarMusicLabel,orient=HORIZONTAL,mode='determinate',value=0)


ProgressbarEndTimerLabel=Label(Progressbarmuscicframe,text='0:00:0',bg='red')

####################################
swithbtn_frame.pack(side='bottom')
previousbtn.pack(side='left')
stopbtn.pack(side='left')
nextbtn.pack(side='right')
repeatbtn.pack(side='right')

left_click="<Button-1>"

plus_volume.bind(left_click,Plus_volume)
minus_volume.bind(left_click,Minus_volume)
nextbtn.bind(left_click,Next_song)
previousbtn.bind(left_click,Previous_song)
stopbtn.bind(left_click,Stop)
songlabel.pack()
Progressbarmuscicframe.pack()
ProgressbarMusicLabel.pack(side='top')
ProgressbarStartTimerLabel.pack(side='left')
ProgressbarMusic.pack(side='left')
ProgressbarEndTimerLabel.pack(side='right')
#test_btn.pack()
#test_btn.bind(left_click,Play)
root.mainloop()