import tkinter as tk

import time
from gtts import gTTS
import pygame
import os
from Ligne1 import ClasseLigne1
from Ligne4 import ClasseLigne4
from Ligne14 import ClasseLigne14
from LigneTest import ClasseLigne0
from Ligne2 import ClasseLigne2
import sys


liste_refresh_old=[]
liste_refresh=[]

def on_horizontal_scroll(*args):
    canvas.xview(*args)

def on_vertical_scroll(*args):
    canvas_metro.yview(*args)
def clic_sur_canevas_metro(event):
    # Cette fonction sera appelée lorsque le canevas est cliqué
    x = canvas_metro.canvasx(event.x)
    y = canvas_metro.canvasy(event.y)


    for train in metro_control.trains:
        x1 = train.canvas_metro.coords(train.draw_metro)[0]
        y1 = train.canvas_metro.coords(train.draw_metro)[1]
        x2 = train.canvas_metro.coords(train.draw_metro)[2]
        y2 = train.canvas_metro.coords(train.draw_metro)[3]
        #== "#FFCC45":
        if x1 <= x <= x2 and y1 - 2 <= y <= y1 + 2 and train.color != "#000000":
            train.color = "#000000"
            train.speed = 0
        #si fleche gauche
        if train.button_dir_droit != None and x1 - 5  <= x <= x1 and y1 - 2.5 <= y <= y1 + 2.5 and (train.color == "#000000" or train.arret_collision ==0) :
            train.color = "#FFCC45"
            train.arret_collision = -1
            train.speed = abs(train.orig_speed) * (-1)
            train.orig_speed = train.speed
            train.canvas.delete(train.button_dir_droit)
            train.canvas_metro.delete(train.can_metro_button_dir_droit)
            train.can_metro_button_dir_droit = None
            train.button_dir_droit = None
            train.canvas.delete(train.button_dir_gauche)
            train.canvas_metro.delete(train.can_metro_button_dir_gauche)
            train.button_dir_gauche = None
            train.can_metro_button_dir_gauche = None
            train.move()
        # si fleche droite
        if train.button_dir_droit != None and x2 <= x <= x2 + 5 and y2 - 2.5 <= y <= y2 + 2.5 and (train.color == "#000000" or train.arret_collision ==0):
            train.color = "#FFCC45"
            train.arret_collision = -1
            train.speed = train.orig_speed
            train.speed = abs(train.orig_speed)
            train.orig_speed = train.speed
            train.canvas.delete(train.button_dir_droit)
            train.canvas_metro.delete(train.can_metro_button_dir_droit)
            train.can_metro_button_dir_droit = None
            train.button_dir_droit = None
            train.canvas.delete(train.button_dir_gauche)
            train.canvas_metro.delete(train.can_metro_button_dir_gauche)
            train.button_dir_gauche = None
            train.can_metro_button_dir_gauche = None
            train.move()


def update_time():


    # Obtenir la date et l'heure actuelles
    temps_actuel = time.localtime()
    format_temps = time.strftime("%d/%m/%Y %H:%M:%S", temps_actuel)

    # Mettre à jour le texte du Canvas avec la date et l'heure formatées
    canvas.delete("heure_texte")  # Supprimer le texte précédent s'il existe
    canvas.create_text(10, 200, text=format_temps, anchor="w", tags="heure_texte", font=("Arial", 8), fill="#FFFFFF")

    # Actualiser toutes les 1000 millisecondes (1 seconde)
    root.after(1000, update_time)

def refresh_eguillages():
    global liste_refresh_old
    global liste_refresh

    if len(liste_refresh) > 0:
        liste_refresh_old = liste_refresh

    liste_refresh = []
    for element in liste_eguillages:

        if element[4] == 0:
            identity = canvas.create_line(element[0], element[1], element[2], element[3], fill="#FCFF42", width=2)
            liste_refresh.append(identity)


        if element[4] == 1:
            identity = canvas.create_line(element[0], element[1], element[2], element[3], fill="#00FF00", width=2)
            liste_refresh.append(identity)

            identity = canvas.create_polygon([(element[0]+element[2])/2,(element[1]+element[3])/2+5,(element[0]+element[2])/2,(element[1]+element[3])/2-5,(element[0]+element[2])/2+10,(element[1]+element[3])/2], outline="", fill="#000000", width=0)
            liste_refresh.append(identity)

        if element[4] == 2:
            identity = canvas.create_line(element[0], element[1], element[2], element[3], fill="#00FF00", width=2)
            liste_refresh.append(identity)

            identity = canvas.create_polygon([(element[0] + element[2]) / 2, (element[1] + element[3]) / 2 + 5, (element[0] + element[2]) / 2,(element[1] + element[3]) / 2 - 5, (element[0] + element[2]) / 2 - 10, (element[1] + element[3]) / 2],outline="", fill="#000000", width=2)
            liste_refresh.append(identity)

        for element in liste_refresh_old:
            canvas.delete(element)
def clic_sur_canevas(event):
    # Cette fonction sera appelée lorsque le canevas est cliqué
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)

    #controle des stations : fermeture de station
    for station in metro_control.stations:
        if station.x1 <= x <= station.x2:
            if station.color == "#FF0000":
                station.color = "#8BB1D5"
                station.open = 1
            else:
                station.color = "#FF0000"
                station.open = 0
            station.canvas.delete(station.rec_id)
            station.canvas.delete(station.text_id)
            station.text_id = canvas.create_text(station.x1 + 32, 20, text=station.name, fill=station.color,
                                                 font=("Arial", 8), anchor="center")
            station.rec_id = canvas.create_rectangle(station.x1, station.y1, station.x2, station.y2, fill=station.color,
                                                     outline="")


    #controle des trains : arret et direction de demarrage
    for train in metro_control.trains:
        #== "#FFCC45":
        if train.x1 <= x <= train.x2 and train.y1 - 2 <= y <= train.y1 + 2 and train.color != "#000000":
            train.color = "#000000"
            train.speed = 0
        #si fleche gauche
        if train.button_dir_droit != None and train.x1 - 5  <= x <= train.x1 and train.y1 - 2.5 <= y <= train.y1 + 2.5 and (train.color == "#000000" or train.arret_collision == 0):
            train.color = "#FFCC45"
            train.arret_collision = -1
            train.speed = abs(train.orig_speed) * (-1)
            train.orig_speed = train.speed
            train.canvas.delete(train.button_dir_droit)
            train.canvas_metro.delete(train.can_metro_button_dir_droit)
            train.can_metro_button_dir_droit = None
            train.button_dir_droit = None
            train.canvas.delete(train.button_dir_gauche)
            train.canvas_metro.delete(train.can_metro_button_dir_gauche)
            train.button_dir_gauche = None
            train.can_metro_button_dir_gauche = None
            train.move()
        # si fleche droite
        if train.button_dir_droit != None and train.x2 <= x <= train.x2 + 5 and train.y2 - 2.5 <= y <= train.y2 + 2.5 and (train.color == "#000000" or  train.arret_collision == 0):
            train.color = "#FFCC45"
            train.arret_collision = -1
            train.speed = train.orig_speed
            train.speed = abs(train.orig_speed)
            train.orig_speed = train.speed
            train.canvas.delete(train.button_dir_droit)
            train.canvas_metro.delete(train.can_metro_button_dir_droit)
            train.can_metro_button_dir_droit = None
            train.button_dir_droit = None
            train.canvas.delete(train.button_dir_gauche)
            train.canvas_metro.delete(train.can_metro_button_dir_gauche)
            train.button_dir_gauche = None
            train.can_metro_button_dir_gauche = None
            train.move()

    for element in liste_eguillages:
        if (element[0]+element[2])/2 - 10 <= x <= (element[0]+element[2])/2 + 10:
            if (element[1]+element[3])/2 - 10 <= y <= (element[1]+element[3])/2 +10:
                if element[4] == 0:
                    liste_eguillages.append((element[0], element[1], element[2], element[3], 1, element[5]))
                if element[4] == 1:
                    liste_eguillages.append((element[0], element[1], element[2], element[3], 2, element[5]))
                if element[4] == 2:
                    liste_eguillages.append((element[0], element[1], element[2], element[3], 0, element[5]))
                liste_eguillages.remove(element)
                refresh_eguillages()


class Train:
    def __init__(self, canvas, canvas_metro, name, position, speed, y_offset, color, order):
        self.canvas = canvas
        self.canvas_metro = canvas_metro
        self.color = color
        self.order = order
        self.text_metro = None
        self.dir_metro = None
        self.draw_metro = None
        self.nom_metro = None
        self.line_id = None
        self.speed = speed
        self.y_offset = y_offset
        self.x1 = position
        self.x2 = position + 50
        self.y1 = 50 + y_offset
        self.y2 = 50 + y_offset
        self.arret = 0
        self.arret_collision = -1
        self.orig_speed = speed
        self.name = name
        self.button_dir_droit = None
        self.button_dir_gauche = None
        self.can_metro_button_dir_droit = None
        self.can_metro_button_dir_gauche = None
        self.sound=0
        self.button = None
    def move(self):
        self.x1 += self.speed
        self.x2 += self.speed

        # gestion de l'arrivé du train en station
        for station in metro_control.stations:
            if station.x1 -abs(self.orig_speed/2) <= self.x1 < station.x1 + abs(self.orig_speed/2) and station.open == 1:
                if self.speed != 0:
                    print(self.name + " " + station.name)
                    self.canvas_metro.delete(self.text_metro)
                    self.text_metro = self.canvas_metro.create_text(180, self.order * 20 + 50, text=station.name, anchor="w", fill="#FFFFFF", font=("Arial", 8))
                    if self.sound == 1:
                        nom_fichier = station.name+".mp3"
                        if not os.path.exists(nom_fichier):
                            texte_a_lire = station.name
                            # Création de l'objet gTTS
                            tts = gTTS(text=texte_a_lire, lang='fr')
                            # Sauvegarde de la parole dans un fichier audio
                            tts.save(station.name+".mp3")
                        pygame.mixer.music.load(nom_fichier)
                        # Lecture du fichier audio
                        pygame.mixer.music.play()
                        #while pygame.mixer.music.get_busy():
                        #    pygame.time.Clock().tick(10)
                        # Nettoyage après la lecture
                        #pygame.mixer.quit()


                self.speed = 0
                self.arret = self.arret + 1
                #print(self.arret)
                if self.arret > 280 and self.color != "#000000":
                    self.arret = 0
                    self.speed = self.orig_speed
            elif station.x1 - abs(self.orig_speed / 2) <= self.x1 < station.x1 + abs(self.orig_speed / 2) and station.open == 0 and self.color != "#000000":
                self.arret = 0
                self.speed = self.orig_speed
                self.canvas.delete(self.button_dir_droit)
                self.canvas_metro.delete(self.can_metro_button_dir_droit)
                self.canvas.delete(self.button_dir_gauche)
                self.canvas_metro.delete(self.can_metro_button_dir_gauche)
                self.can_metro_button_dir_droit = None
                self.button_dir_droit = None
                self.button_dir_gauche = None
                self.can_metro_button_dir_gauche = None


        #gestion des collisions

        for metro in metro_control.trains:
            if self.speed > 0 and metro.x1 - self.x2 <= 10 and self.x1 < metro.x1 and metro.y1 == self.y1 and self.order != metro.order and self.color != "#000000" and self.arret==0:
                if self.arret_collision == -1:
                    self.speed = 0
                    self.arret_collision = 0
                    self.color = "#985717"
                break
            elif self.speed < 0 and self.x1 - metro.x2 <= 10 and self.x1 > metro.x1 and metro.y1 == self.y1 and self.order != metro.order and self.color != "#000000" and self.arret==0 :
                if self.arret_collision == -1:
                    self.speed = 0
                    self.arret_collision = 0
                    self.color = "#985717"
                break
            elif self.speed == 0 and self.x1 - metro.x2 <= 10 and self.x1 > metro.x1 and metro.y1 == self.y1 and self.order != metro.order and self.color != "#000000" and self.arret==0 :
                if self.arret_collision == -1:
                    self.speed = 0
                    self.arret_collision = 0
                    #self.color = "#985717"
                break
            elif self.arret_collision == 0 and self.color != "#000000":
                self.arret_collision = -1
                self.speed = self.orig_speed
                self.canvas.delete(self.button_dir_droit)
                self.canvas.delete(self.button_dir_gauche)
                self.canvas_metro.delete(self.can_metro_button_dir_droit)
                self.canvas_metro.delete(self.can_metro_button_dir_gauche)
                self.can_metro_button_dir_droit = None
                self.button_dir_droit = None
                self.button_dir_gauche = None
                self.can_metro_button_dir_gauche = None
                self.color = "#FFCC45"


        #if self.arret_collision ==-1:
        for element in liste_eguillages:

            if (element[0] - abs(self.orig_speed / 2) <= self.x1 < element[0] + abs(self.orig_speed / 2) and element[1] == self.y1 ) and element[4]==1 and self.speed > 0 and element[0] < element[2]:
                print(self.name + " arrive a " + element[5])
                while element[3] != self.y1 :
                    if element[1] > element[3]:
                        self.y1 -= 1
                        self.y2 -= 1
                        self.x1 += 1
                        self.x2 += 1
                    else:
                        self.y1 += 1
                        self.y2 += 1
                        self.x1 += 1
                        self.x2 += 1

            if (element[0] - abs(self.orig_speed / 2) <= self.x1 < element[0] + abs(self.orig_speed / 2) and element[1] == self.y1 ) and element[4]==1 and self.speed < 0 and element[0] > element[2]:
                print(self.name + " arrive a " + element[5])
                while element[3] != self.y1 :
                    if element[1] > element[3]:
                        self.y1 -= 1
                        self.y2 -= 1
                        self.x1 -= 1
                        self.x2 -= 1
                    else:
                        self.y1 += 1
                        self.y2 += 1
                        self.x1 -= 1
                        self.x2 -= 1

            if (element[0] - abs(self.orig_speed / 2) <= self.x1 < element[0] + abs(self.orig_speed / 2) and element[1] == self.y1) and element[4] == 2 and self.speed > 0 and element[2] < element[0]:
                print(self.name + " arrive a " + element[5])
                while element[3] != self.y1:
                    if element[1] > element[3]:
                        self.y1 -= 1
                        self.y2 -= 1
                        self.x1 += 1
                        self.x2 += 1
                    else:
                        self.y1 += 1
                        self.y2 += 1
                        self.x1 += 1
                        self.x2 += 1

            if (element[2] - abs(self.orig_speed / 2) <= self.x1 < element[2] + abs(self.orig_speed / 2) and element[3] == self.y1) and element[4] == 2 and self.speed < 0 and element[2] > element[0]:
                print(self.name + " arrive en mode 2 a " + element[5])
                while element[1] != self.y1:
                    if element[1] > element[3]:
                        self.y1 += 1
                        self.y2 += 1
                        self.x1 -= 1
                        self.x2 -= 1
                    else:
                        self.y1 -= 1
                        self.y2 -= 1
                        self.x1 -= 1
                        self.x2 -= 1


        for element in liste_terminus:
            if element[0] - abs(self.orig_speed / 2) <= self.x1 < element[0] + abs(self.orig_speed / 2) :
                if self.y1 == element[1]:
                    if self.speed != 0:
                        print(self.name + " " + element[2])
                    self.speed = 0
                    self.arret = self.arret + 1
                    # print(self.arret)
                    if self.arret > 70 and self.color != "#000000":
                        self.arret = 0
                        self.speed = self.orig_speed*(-1)
                        self.orig_speed = self.speed
                        self.move()

        if self.line_id:
            self.canvas.coords(self.line_id, self.x1, self.y1, self.x2, self.y2)
            self.canvas.itemconfig(self.line_id, fill=self.color)

            self.canvas_metro.delete(self.draw_metro)
            self.draw_metro = self.canvas_metro.create_line(100, self.order * 20 + 50, 150, self.order * 20 + 50, fill=self.color,
                                          width=5)
            if self.speed > 0:
                self.canvas_metro.delete(self.text_metro)
                self.canvas_metro.delete(self.dir_metro)
                self.dir_metro = self.canvas_metro.create_polygon(
                    [150, self.order * 20 + 50 + 5, 150,
                     self.order * 20 + 50 - 5, 150 + 5,
                     self.order * 20 + 50], outline="", fill="#000000", width=0)
            if self.speed < 0:
                self.canvas_metro.delete(self.text_metro)
                self.canvas_metro.delete(self.dir_metro)
                self.dir_metro = self.canvas_metro.create_polygon(
                    [100, self.order * 20 + 50 + 5, 100,
                     self.order * 20 + 50 - 5, 100 - 5,
                     self.order * 20 + 50], outline="", fill="#000000", width=0)
            if (self.color == "#000000" and self.button_dir_droit == None) or (self.arret_collision==0 and self.button_dir_droit == None):
                self.button_dir_droit = self.canvas.create_polygon([self.x2, self.y2  + 5, self.x2, self.y2 - 5, self.x2 + 5, self.y2], outline="", fill="#00FF00", width=0)
                self.button_dir_gauche = self.canvas.create_polygon([self.x1, self.y1 + 5, self.x1, self.y1 - 5, self.x1 - 5, self.y1], outline="", fill="#00FF00",width=0)
                self.can_metro_button_dir_droit = self.canvas_metro.create_polygon([canvas_metro.coords(self.draw_metro)[2], canvas_metro.coords(self.draw_metro)[3] + 5, canvas_metro.coords(self.draw_metro)[2], canvas_metro.coords(self.draw_metro)[3] - 5, canvas_metro.coords(self.draw_metro)[2] + 5, canvas_metro.coords(self.draw_metro)[3]], outline="", fill="#00FF00",width=0)
                self.can_metro_button_dir_gauche = self.canvas_metro.create_polygon([canvas_metro.coords(self.draw_metro)[0], canvas_metro.coords(self.draw_metro)[1] + 5, canvas_metro.coords(self.draw_metro)[0], canvas_metro.coords(self.draw_metro)[1] - 5, canvas_metro.coords(self.draw_metro)[0] - 5, canvas_metro.coords(self.draw_metro)[1]], outline="", fill="#00FF00", width=0)
        else:
            self.line_id = self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.color, width=5)
            self.canvas_metro.delete(self.nom_metro)

            self.nom_metro = self.canvas_metro.create_text(50, self.order * 20 + 50, text=self.name, fill="#FFFFFF",
                                                                       font=("Arial", 8))



class Station:
    def __init__(self, canvas, X, Name, Line, Open):
        self.canvas = canvas
        self.x1 = X
        self.name = Name
        self.line = Line
        self.open = 1
        self.y1 = Line * 30 + 15
        self.x2 = X + 65
        self.y2 = Line * 30 + 35
        self.color = "#8BB1D5"
        self.text_id = None
        self.rec_id = None


class MetroControl:
    def __init__(self, canvas, canvas_metro):
        self.canvas = canvas
        self.canvas_metro = canvas_metro
        self.trains = []
        self.stations = []

    def add_train(self, train):
        self.trains.append(train)

    def add_station(self, station):
        self.stations.append(station)

    def update_trains(self):
        for train in self.trains:
            train.move()

# Créer une fenêtre Tkinter
pygame.init()


root = tk.Tk()

root.title("Metro Control")

root_metro = tk.Toplevel(root)
root_metro.title("Metro List")

# Créer un canvas pour représenter la ligne de métro
canvas = tk.Canvas(root, width=root.winfo_screenwidth()-50-root_metro.winfo_screenwidth()/5, height=root.winfo_screenheight()/3, bg="#1E42B2", scrollregion=(0, 0, 10000, root.winfo_screenheight()/3))

# Ajouter un ascenseur horizontal
horizontal_scrollbar = tk.Scrollbar(root, orient="horizontal", command=on_horizontal_scroll)
horizontal_scrollbar.pack(side="bottom", fill="x")

# Connecter l'ascenseur au Canvas
canvas.configure(xscrollcommand=horizontal_scrollbar.set)

# Créer un canvas pour représenter la ligne de métro
canvas_metro = tk.Canvas(root_metro, width=root_metro.winfo_screenwidth()/5, height=root_metro.winfo_screenheight(), bg="#1E42B2",  scrollregion=(0, 0, root_metro.winfo_screenwidth()/5, 9000))
vertical_scrollbar = tk.Scrollbar(root_metro, orient="vertical", command=on_vertical_scroll)
vertical_scrollbar.pack(side="left", fill="x")



# Créer un poste de commande centralisé
metro_control = MetroControl(canvas, canvas_metro)

Ligne = sys.argv[1]

if Ligne == "1":
    #Ligne 1
    liste_stations = ClasseLigne1.liste_stations
    liste_eguillages = ClasseLigne1.liste_eguillages
    liste_terminus = ClasseLigne1.liste_terminus
    liste_metro = ClasseLigne1.liste_metro
    liste_lignes = ClasseLigne1.liste_lignes

if Ligne == "2":
    #Ligne 1
    liste_stations = ClasseLigne2.liste_stations
    liste_eguillages = ClasseLigne2.liste_eguillages
    liste_terminus = ClasseLigne2.liste_terminus
    liste_metro = ClasseLigne2.liste_metro
    liste_lignes = ClasseLigne2.liste_lignes
if Ligne == "4":
    #Ligne 4
    liste_stations = ClasseLigne4.liste_stations
    liste_eguillages = ClasseLigne4.liste_eguillages
    liste_terminus = ClasseLigne4.liste_terminus
    liste_metro = ClasseLigne4.liste_metro
    liste_lignes = ClasseLigne4.liste_lignes


if Ligne == "14":
    #Ligne 14
    liste_stations = ClasseLigne14.liste_stations
    liste_eguillages = ClasseLigne14.liste_eguillages
    liste_terminus = ClasseLigne14.liste_terminus
    liste_metro = ClasseLigne14.liste_metro
    liste_lignes = ClasseLigne14.liste_lignes

if Ligne == "0":
    #Ligne 14
    liste_stations = ClasseLigne0.liste_stations
    liste_eguillages = ClasseLigne0.liste_eguillages
    liste_terminus = ClasseLigne0.liste_terminus
    liste_metro = ClasseLigne0.liste_metro
    liste_lignes = ClasseLigne0.liste_lignes
#Materialisation des terminus
for element in liste_terminus:
    canvas.create_rectangle(element[0]-3, element[1]-3, element[0]+3, element[1]+3, fill="#000000", outline="")

#Materialisation des terminus


#Materialisation des lignes
for element in liste_lignes:
    canvas.create_line(element[0],element[1],element[2],element[3], fill=element[4],width=element[5])

canvas.pack(expand=True, fill="both")
canvas_metro.pack(expand=True, fill="both")

#Materialisation des terminus
for element in liste_terminus:
    canvas.create_rectangle(element[0]-3, element[1]-3, element[0]+3, element[1]+3, fill="#FCFF42", outline="")


#Materialisation des EGUILLAGES
refresh_eguillages()
# Ajouter des trains avec un léger décalage vertical entre les lignes



for element in liste_metro:
    train = Train(canvas, canvas_metro, element[0], element[1], element[2], element[3], element[4], liste_metro.index(element))
    metro_control.add_train(train)

for element in liste_stations:
    station = Station(canvas, element[0], element[1], element[2], 1)
    metro_control.add_station(station)

for station in metro_control.stations:
    station.text_id = canvas.create_text(station.x1+ 32, 20, text=station.name, fill=station.color, font=("Arial", 8), anchor="center")
    station.rec_id = canvas.create_rectangle(station.x1, station.y1, station.x2, station.y2 , fill=station.color, outline="")

# Mettre à jour les trains à intervalle régulier
def update_trains():
    metro_control.update_trains()
    root.after(50, update_trains)

update_trains()
# Appeler la fonction update_time pour mettre à jour l'heure
update_time()

canvas_metro.bind("<Button-1>", clic_sur_canevas_metro)
canvas.bind("<Button-1>", clic_sur_canevas)

# Lancer la boucle principale Tkinter
root.mainloop()

