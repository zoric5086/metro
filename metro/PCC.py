import tkinter as tk
from tkinter import *
import time
#from gtts import gTTS
#import pygame
#import os
from Ligne1 import ClasseLigne1
from Ligne4 import ClasseLigne4
from Ligne14 import ClasseLigne14
from LigneTest import ClasseLigne0
from Ligne2 import ClasseLigne2
from Ligne6 import ClasseLigne6
import sys
from PIL import Image, ImageTk


liste_refresh_old=[]
liste_refresh=[]
liste_refresh_depot_old=[]
liste_refresh_depot=[]

shape_ids=None
text_id=None

def Raise_Text(text):
    # test bulle

    global shape_ids
    global text_id

    x1, y1, x2, y2 = 1850, 250, 2150, 350
    radius = 50
    #if shape_ids != None:
    #    for shape in shape_ids:
    #        canvas.delete(shape)

    #if text_id != None:
    #    canvas.delete(text_id)

    shape_ids = create_rounded_rectangle(canvas, x1, y1, x2, y2, radius)
    text_id = write_text_rounded_rectangle(canvas, text, 2000, 300)
    dx, dy = -15, 0  # Décalage vers la gauche
    stop_x = 1000
    move_rounded_rectangle_left(canvas, shape_ids + (text_id,), dx, dy, stop_x)

    #move_rounded_rectangle_left(canvas, shape_ids + (text_id,), dx, dy, stop_x)
def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius):
    return canvas.create_arc(x1, y1, x1+2*radius, y1+2*radius, start=90, extent=90, style=tk.ARC, outline="white"), \
           canvas.create_arc(x2-2*radius, y1, x2, y1+2*radius, start=0, extent=90, style=tk.ARC, outline="white"), \
           canvas.create_arc(x1, y2-2*radius, x1+2*radius, y2, start=180, extent=90, style=tk.ARC, outline="white"), \
           canvas.create_arc(x2-2*radius, y2-2*radius, x2, y2, start=270, extent=90, style=tk.ARC, outline="white"), \
           canvas.create_line(x1+radius, y1, x2-radius, y1, fill="white"), \
           canvas.create_line(x1+radius, y2, x2-radius, y2, fill="white"), \
           canvas.create_line(x1, y1+radius, x1, y2-radius, fill="white"), \
           canvas.create_line(x2, y1+radius, x2, y2-radius, fill="white")

def write_text_rounded_rectangle(canvas, text ,x, y):
    return canvas.create_text(x, y, text=f"Attention, le {text} est en arret colision", font=("Helvetica", 10), fill="white")

def move_rounded_rectangle_left(canvas, shape, dx, dy, stop_x):

    global shape_ids
    current_x = canvas.coords(shape[0])[0] # Obtenir la position actuelle en x du premier arc (le coin supérieur gauche)
    if current_x <= stop_x:
        #shape_ids = None
        return  # Arrêter la récursion une fois que la forme atteint la position stop_x

    for shape_id in shape:
        canvas.move(shape_id, dx, dy)
        canvas.pack()

    canvas.after(100, move_rounded_rectangle_left, canvas, shape, dx, dy, stop_x)

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
        #== "#EB0004":
        if x1 <= x <= x2 and y1 - 2 <= y <= y1 + 2 and train.color != "#000000":
            train.color = "#000000"
            train.on_off= 0
            train.speed = 0
        #si fleche gauche
        if train.button_dir_droit != None and x1 - 5  <= x <= x1 and y1 - 2.5 <= y <= y1 + 2.5 and (train.color == "#000000" or train.arret_collision ==1) :
            train.color = "#EB0004"
            train.arret_collision = 0
            train.on_off = 1
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
        if train.button_dir_droit != None and x2 <= x <= x2 + 5 and y2 - 2.5 <= y <= y2 + 2.5 and (train.color == "#000000" or train.arret_collision ==1):
            train.color = "#EB0004"
            train.arret_collision = 0
            train.on_off = 1
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
            identity = canvas.create_line(element[0], element[1], element[2], element[3], fill="#EBEBEB", width=2)
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

def refresh_eguillages_depot():
    global liste_refresh_depot_old
    global liste_refresh_depot

    if len(liste_refresh_depot) > 0:
        liste_refresh_depot_old = liste_refresh_depot

    liste_refresh_depot = []
    for element in liste_depot_eguillage:

        if element[4] == 0:
            identity = canvas.create_line(element[0], element[1], element[2], element[3], fill=element[6], width=2)
            liste_refresh_depot.append(identity)

        if element[4] == 1:
            identity = canvas.create_line(element[0], element[1], element[2], element[3], fill="#00FF00", width=2)
            liste_refresh_depot.append(identity)

            identity = canvas.create_polygon([(element[0]+element[2])/2,(element[1]+element[3])/2+5,(element[0]+element[2])/2,(element[1]+element[3])/2-5,(element[0]+element[2])/2+10,(element[1]+element[3])/2], outline="", fill="#000000", width=0)
            liste_refresh_depot.append(identity)

        if element[4] == 2:
            identity = canvas.create_line(element[0], element[1], element[2], element[3], fill="#00FF00", width=2)
            liste_refresh_depot.append(identity)

            identity = canvas.create_polygon([(element[0] + element[2]) / 2, (element[1] + element[3]) / 2 + 5, (element[0] + element[2]) / 2,(element[1] + element[3]) / 2 - 5, (element[0] + element[2]) / 2 - 10, (element[1] + element[3]) / 2],outline="", fill="#000000", width=2)
            liste_refresh_depot.append(identity)

        for element in liste_refresh_depot_old:
            canvas.delete(element)

def clic_sur_canevas(event):
    # Cette fonction sera appelée lorsque le canevas est cliqué
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)

    #controle des stations : fermeture de station
    for station in metro_control.stations:
        if station.x1 <= x <= station.x2:
            if station.open == 0:
                station.Start()
            else:
                station.Stop()
            #station.canvas.delete(station.rec_id)
            #station.canvas.delete(station.text_id)
            #station.text_id = canvas.create_text(station.x1 + 32, 20, text=station.name, fill=station.color, font=("Arial", 8), anchor="center")
            #station.rec_id = canvas.create_rectangle(station.x1, station.y1, station.x2, station.y2, fill=station.color, outline="")


    #controle des trains : arret et direction de demarrage
    for train in metro_control.trains:
        #== "#EB0004":
        if train.x1 <= x <= train.x2 and train.y1 - 2 <= y <= train.y1 + 2 and train.color != "#000000":
            train.color = "#000000"
            train.speed = 0
            train.on_off = 0
        #si fleche gauche
        if train.button_dir_droit != None and train.x1 - 5  <= x <= train.x1 and train.y1 - 2.5 <= y <= train.y1 + 2.5 and (train.color == "#000000" or train.arret_collision == 1):
            train.color = "#EB0004"
            train.arret_collision = 0
            train.on_off = 1
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
        if train.button_dir_droit != None and train.x2 <= x <= train.x2 + 5 and train.y2 - 2.5 <= y <= train.y2 + 2.5 and (train.color == "#000000" or  train.arret_collision == 1):
            train.color = "#EB0004"
            train.arret_collision = 0
            train.on_off = 1
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

    for element in liste_depot_eguillage:
        if (element[0]+element[2])/2 - 10 <= x <= (element[0]+element[2])/2 + 10:
            if (element[1]+element[3])/2 - 10 <= y <= (element[1]+element[3])/2 +10:
                if element[4] == 0:
                    liste_depot_eguillage.append((element[0], element[1], element[2], element[3], 1, element[5], element[6]))
                if element[4] == 1:
                    liste_depot_eguillage.append((element[0], element[1], element[2], element[3], 2, element[5], element[6]))
                if element[4] == 2:
                    liste_depot_eguillage.append((element[0], element[1], element[2], element[3], 0, element[5], element[6]))
                liste_depot_eguillage.remove(element)
                refresh_eguillages_depot()

class Train:
    def __init__(self, canvas, canvas_metro, name, position, speed, y_offset, on_off, color, order):
        self.bouton_parametre =None
        self.canvas = canvas
        self.last_station = None
        self.canvas_metro = canvas_metro
        self.color = color
        self.order = order
        self.on_off = on_off
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
        self.arret_station = 0
        self.arret_collision = 0
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

        if self.on_off == 0:
            self.color = "#000000"
            self.speed = 0
            self.arret = self.arret + 1

        # gestion de l'arrivé du train en station
        for station in metro_control.stations:
            #Arrivée en station d'un train circulant de la gauche vers la droite
            if (station.lineUp == self.y1 or station.lineBottom == self.y1) and self.arret_station == 0 and self.speed > 0 and (station.x1 + station.x2)/2 - self.speed/2 <= (self.x1 + self.x2)/2 <= (station.x1 + station.x2)/2 + self.speed/2  and station.open == 1 and self.last_station != station.name+str(station.lineUp):
                self.last_station = station.name+str(station.lineUp)
                print(self.name + " " + station.name)
                self.canvas_metro.delete(self.text_metro)
                self.text_metro = self.canvas_metro.create_text(580, self.order * 20 + 50, text=station.name, anchor="w", fill="#000000", font=("Arial", 8))
                self.speed = 0
                self.arret_station = 1
                station.FQ_ON()

            # Arrivée en station d'un train circulant de la droite vers la gauche

            elif (station.lineUp == self.y1 or station.lineBottom == self.y1) and  self.arret_station == 0 and self.speed < 0 and (station.x1 + station.x2)/2 - self.speed/2 >= (self.x1 + self.x2)/2 >= (station.x1 + station.x2)/2 + self.speed/2 and station.open == 1 and self.last_station != station.name+str(station.lineUp):
                self.last_station = station.name+str(station.lineUp)
                print(self.name + " " + station.name)
                self.canvas_metro.delete(self.text_metro)
                self.text_metro = self.canvas_metro.create_text(580, self.order * 20 + 50, text=station.name, anchor="w", fill="#000000", font=("Arial", 8))
                station.FQ_ON()
                self.speed = 0
                self.arret_station = 1

            #compteur de temps d'arrêt
            elif  (station.lineUp == self.y1 or station.lineBottom == self.y1) and self.arret_station == 1 and self.last_station == station.name+str(station.lineUp):
                self.arret = self.arret + 1
                if self.arret > station.duree_stop and self.color != "#000000":
                    self.arret = 0
                    self.arret_station = 0
                    self.speed = self.orig_speed
                    station.FQ_OFF()

            #elif (station.x1 - abs(self.orig_speed / 2) <= self.x1 < station.x1 + abs(self.orig_speed / 2) and station.open == 0 and self.color != "#000000"):
            #    self.arret = 0
            #    station.FQ_OFF()
            #    self.speed = self.orig_speed
            #    self.canvas.delete(self.button_dir_droit)
            #    self.canvas_metro.delete(self.can_metro_button_dir_droit)
            #    self.canvas.delete(self.button_dir_gauche)
            #    self.canvas_metro.delete(self.can_metro_button_dir_gauche)
            #    self.can_metro_button_dir_droit = None
            #    self.button_dir_droit = None
            #    self.button_dir_gauche = None
            #    self.can_metro_button_dir_gauche = None

        #gestion des feux
        for feu in metro_control.feux:
            if self.speed < 0 and self.y1 == feu.Y and self.x1 < feu.X < self.x2 :
                feu.Stop(self.nom_metro)
            elif self.speed > 0 and self.y1 == feu.Y and self.x1 < feu.X < self.x2:
                feu.Stop(self.nom_metro)
            elif self.nom_metro == feu.TrainID and self.y1 == feu.Y and self.speed > 0 and self.x1 > feu.X + 120:
                #not (( self.x1 < feu.X < self.x2) or ( self.x1 > feu.X > self.x2) ):
                feu.Start()
            elif self.nom_metro == feu.TrainID and self.y1 == feu.Y and self.speed < 0 and self.x2 < feu.X - 120:
                feu.Start()
            elif self.nom_metro == feu.TrainID and self.y1 != feu.Y:
                feu.Start()
            #print(abs(self.x1 - feu.X))

        #Gestion des arrets avant collision
        for metro in metro_control.trains:
            if self.speed > 0 and metro.x1 - self.x2 <= 30 and self.x1 < metro.x1 and metro.y1 == self.y1 and self.order != metro.order and self.color != "#000000" and self.arret==0:
                if self.arret_collision == 0:
                    self.speed = 0
                    self.arret_collision = 1
                    #Raise_Text(self.name)
                    self.color = "#985717"
                break
            elif self.speed < 0 and self.x1 - metro.x2 <= 30 and self.x1 > metro.x1 and metro.y1 == self.y1 and self.order != metro.order and self.color != "#000000" and self.arret==0 :
                if self.arret_collision == 0:
                    self.speed = 0
                    self.arret_collision = 1
                    #Raise_Text(self.name)
                    self.color = "#985717"
                break
            elif self.speed == 0 and self.x1 - metro.x2 <= 30 and self.x1 > metro.x1 and metro.y1 == self.y1 and self.order != metro.order and self.color != "#000000" and self.arret==0 :
                if self.arret_collision == 0:
                    self.speed = 0
                    self.arret_collision = 1
                    #Raise_Text(self.name)
                    #self.color = "#985717"
                break
            elif self.arret_collision == 1 and self.color != "#000000":
                self.arret_collision = 0
                self.speed = self.orig_speed
                self.canvas.delete(self.button_dir_droit)
                self.canvas.delete(self.button_dir_gauche)
                self.canvas_metro.delete(self.can_metro_button_dir_droit)
                self.canvas_metro.delete(self.can_metro_button_dir_gauche)
                self.can_metro_button_dir_droit = None
                self.button_dir_droit = None
                self.button_dir_gauche = None
                self.can_metro_button_dir_gauche = None
                self.color = "#EB0004"

        #Gestion des équillages de dépots
        for element in liste_depot_eguillage:
            if (element[0] - abs(self.speed / 2) <= self.x1 < element[0] + abs(self.speed / 2) and element[1] == self.y1 ) and element[4]==1 and self.speed > 0 and element[0] < element[2]:
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

            if (element[0] - abs(self.speed / 2) <= self.x1 < element[0] + abs(self.speed / 2) and element[1] == self.y1 ) and element[4]==1 and self.speed < 0 and element[0] > element[2]:
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

            if (element[0] - abs(self.speed / 2) <= self.x1 < element[0] + abs(self.speed / 2) and element[1] == self.y1) and element[4] == 2 and self.speed > 0 and element[2] < element[0]:
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

            if (element[2] - abs(self.speed / 2) <= self.x1 < element[2] + abs(self.speed / 2) and element[3] == self.y1) and element[4] == 2 and self.speed < 0 and element[2] > element[0]:
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
                    if self.arret > 120 and self.color != "#000000":
                        self.arret = 0
                        self.speed = self.orig_speed*(-1)
                        self.orig_speed = self.speed
                        self.move()

        if self.line_id:
            self.canvas.coords(self.line_id, self.x1, self.y1, self.x2, self.y2)
            self.canvas.itemconfig(self.line_id, fill=self.color)

            self.canvas_metro.delete(self.draw_metro)
            self.draw_metro = self.canvas_metro.create_line(500, (self.order +1) * 20 + 50, 550, (self.order +1) * 20 + 50, fill=self.color,
                                          width=5)
            if self.speed > 0:
                self.canvas_metro.delete(self.text_metro)
                self.canvas_metro.delete(self.dir_metro)
                self.dir_metro = self.canvas_metro.create_polygon(
                    [550, (self.order +1) * 20 + 50 + 5, 550,
                     (self.order +1) * 20 + 50 - 5, 550 + 5,
                     (self.order +1) * 20 + 50], outline="", fill="#000000", width=0)
            if self.speed < 0:
                self.canvas_metro.delete(self.text_metro)
                self.canvas_metro.delete(self.dir_metro)
                self.dir_metro = self.canvas_metro.create_polygon(
                    [500, (self.order +1) * 20 + 50 + 5, 500,
                     (self.order +1) * 20 + 50 - 5, 500 - 5,
                     (self.order +1) * 20 + 50], outline="", fill="#000000", width=0)
            if (self.color == "#000000" and self.button_dir_droit == None) or (self.arret_collision==1 and self.button_dir_droit == None):
                self.button_dir_droit = self.canvas.create_polygon([self.x2, self.y2  + 5, self.x2, self.y2 - 5, self.x2 + 5, self.y2], outline="", fill="#00FF00", width=0)
                self.button_dir_gauche = self.canvas.create_polygon([self.x1, self.y1 + 5, self.x1, self.y1 - 5, self.x1 - 5, self.y1], outline="", fill="#00FF00",width=0)
                self.can_metro_button_dir_droit = self.canvas_metro.create_polygon([canvas_metro.coords(self.draw_metro)[2], canvas_metro.coords(self.draw_metro)[3] + 5, canvas_metro.coords(self.draw_metro)[2], canvas_metro.coords(self.draw_metro)[3] - 5, canvas_metro.coords(self.draw_metro)[2] + 5, canvas_metro.coords(self.draw_metro)[3]], outline="", fill="#00FF00",width=0)
                self.can_metro_button_dir_gauche = self.canvas_metro.create_polygon([canvas_metro.coords(self.draw_metro)[0], canvas_metro.coords(self.draw_metro)[1] + 5, canvas_metro.coords(self.draw_metro)[0], canvas_metro.coords(self.draw_metro)[1] - 5, canvas_metro.coords(self.draw_metro)[0] - 5, canvas_metro.coords(self.draw_metro)[1]], outline="", fill="#00FF00", width=0)
                image = Image.open("parametre.png")
                image = image.resize((20, 00))
                photo_parametre = ImageTk.PhotoImage(image)



                # Créer un Frame pour contenir le bouton
                frame_bouton = tk.Frame(canvas)
                frame_bouton.pack()

                # Créer le bouton dans le frame avec l'image et associer la fonction ouvrir_fenetre
                self.button_parametre = tk.Button(frame_bouton, image=photo_parametre, command=ouvrir_fenetre)
                self.button_parametre.image = photo_parametre  # Garder une référence à l'image
                self.button_parametre.pack()

                canvas.create_window(20, (self.order +1) * 20 + 50, anchor=tk.CENTER, window=frame_bouton)
        else:
            self.line_id = self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.color, width=5)
            self.canvas_metro.delete(self.nom_metro)

            self.nom_metro = self.canvas_metro.create_text(450, (self.order +1) * 20 + 50, text=self.name, fill="#000000",
                                                                       font=("Arial", 8))



class Station:
    def __init__(self, canvas, X, Name, Offset, DureeStop, Open):
        self.canvas = canvas
        self.x1 = X
        self.name = Name
        self.Offset = Offset
        self.lineUp = (Offset)*(30) + 10
        self.lineBottom = (Offset)*(30) + 40
        self.open = 1
        self.quai_on = 1
        self.duree_stop = DureeStop
        self.y1 = Offset * 30 + 15
        self.x2 = X + 65
        self.y2 = Offset * 30 + 35
        self.color = "#8BB1D5"
        self.text_id = canvas.create_text(self.x1 + 32, 30, text=self.name, fill="#000000", font = ("Arial", 6), anchor = "center")
        self.rec_id = canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill= self.color, outline = "")
        self.image = canvas.create_image((self.x1+self.x2)/2,(self.y1 + self.y2)/2 , anchor=tk.CENTER, image=photo_fq_off)

        # station.canvas.delete(station.rec_id)
        # station.canvas.delete(station.text_id)
        # station.text_id =
        # station.rec_id =

    def Start(self):
        self.open = 1
        self.color = "#8BB1D5"
        canvas.delete(self.text_id)
        self.text_id = canvas.create_text(self.x1 + 32, 20, text=self.name, fill="#000000", font=("Arial", 8), anchor="center")
        canvas.delete(self.rec_id)
        self.rec_id = canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=self.color, outline="")
        canvas.delete(self.image)
        if self.quai_on == 0:
            self.image = canvas.create_image((self.x1 + self.x2) / 2, (self.y1 + self.y2)/2 , anchor=tk.CENTER, image=photo_fq_off)
        else:
            self.image = canvas.create_image((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2, anchor=tk.CENTER,image=photo_fq_on)

    def Stop(self):
        self.open = 0
        self.color = "#FF0000"
        canvas.delete(self.text_id)
        self.text_id = canvas.create_text(self.x1 + 32, 20, text=self.name, fill=self.color, font=("Arial", 8), anchor="center")
        canvas.delete(self.rec_id)
        self.rec_id = canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=self.color, outline="")
        canvas.delete(self.image)
        if self.quai_on == 0:
            self.image = canvas.create_image((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2, anchor=tk.CENTER, image=photo_fq_off)
        else:
            self.image = canvas.create_image((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2, anchor=tk.CENTER, image=photo_fq_on)
    def FQ_ON(self):
        self.quai_on = 1
        canvas.delete(self.image)
        self.image = canvas.create_image((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2, anchor=tk.CENTER, image=photo_fq_on)

    def FQ_OFF(self):
        self.quai_on = 0
        canvas.delete(self.image)
        self.image = canvas.create_image((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2, anchor=tk.CENTER, image=photo_fq_off)
class Feu:
    def __init__(self, canvas, X, Y, Etat):
        self.canvas = canvas
        self.X = X
        self.Y = Y
        self.Etat = Etat
        self.TrainID = None
        # image_feu_vert
        if Etat == 2:
            self.image = canvas.create_image(self.X, self.Y - 12 , anchor=tk.CENTER, image=photo_feu_rouge)
        else:
            self.image = canvas.create_image(self.X, self.Y - 12 , anchor=tk.CENTER, image=photo_feu_vert)

    def Start(self):
        self.Etat = 1
        canvas.delete(self.image)
        self.image = canvas.create_image(self.X, self.Y - 12 , anchor=tk.CENTER, image=photo_feu_vert)

    def Stop(self, TrainID):
        self.Etat = 2
        self.TrainID = TrainID
        canvas.delete(self.image)
        self.image = canvas.create_image(self.X, self.Y - 12 , anchor=tk.CENTER, image=photo_feu_rouge)

class MetroControl:
    def __init__(self, canvas, canvas_metro):
        self.canvas = canvas
        self.canvas_metro = canvas_metro
        self.trains = []
        self.stations = []
        self.feux = []

    def add_train(self, train):
        self.trains.append(train)

    def add_station(self, station):
        self.stations.append(station)

    def add_feu(self, feu):
        self.feux.append(feu)


    def update_trains(self):
        for train in self.trains:
            train.move()


# Fonction appelée lors du clic sur le bouton
def action_bouton_stop():
    print("Bouton cliqué !")
    for train in metro_control.trains:
            train.color = "#000000"
            train.speed = 0


def action_bouton_reprise():
    print("Bouton cliqué !")
    for train in metro_control.trains:
        train.color = "#EB0004"
        train.arret_collision = 0
        train.speed = train.orig_speed
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
def ouvrir_fenetre():
    root_metro.deiconify()



root = tk.Tk()

root.title("Metro Control")

root_metro = tk.Toplevel(root)
root_metro.title("Metro List")

# Créer un canvas pour représenter la ligne de métro
canvas = tk.Canvas(root, width=root.winfo_screenwidth()-50-root_metro.winfo_screenwidth()/5, height=root.winfo_screenheight()/3, bg="#ABABAB", scrollregion=(0, 0, 10000, root.winfo_screenheight()/3))


# Ajouter un ascenseur horizontal
horizontal_scrollbar = tk.Scrollbar(root, orient="horizontal", command=on_horizontal_scroll)
horizontal_scrollbar.pack(side="bottom", fill="x")

# Connecter l'ascenseur au Canvas
canvas.configure(xscrollcommand=horizontal_scrollbar.set)

# Créer un canvas pour représenter la ligne de métro
canvas_metro = tk.Canvas(root_metro, width=root_metro.winfo_screenwidth()/1.5, height=root_metro.winfo_screenheight()/1.5, bg="#E0E0E0",  scrollregion=(0, 0, root_metro.winfo_screenwidth()/1.5, 6000))
vertical_scrollbar = tk.Scrollbar(root_metro, orient="vertical", command=on_vertical_scroll)
vertical_scrollbar.pack(side="left", fill="x")


#Affichage du boutton stop


# Bouton "reprise" (image)
#bouton_reprise = tk.Button(canevas, command=action_bouton)
#bouton_reprise.pack()

Ligne = sys.argv[1]
#Ligne = "14"

if Ligne == "1":
    #Ligne 1
    liste_stations = ClasseLigne1.liste_stations
    liste_eguillages = ClasseLigne1.liste_eguillages
    liste_terminus = ClasseLigne1.liste_terminus
    liste_metro = ClasseLigne1.liste_metro
    liste_lignes = ClasseLigne1.liste_lignes
    liste_depot_eguillage = ClasseLigne1.liste_depot_eguillage
    liste_depot_ligne= ClasseLigne1.liste_depot_ligne
    liste_feu_traffic = ClasseLigne1.liste_feu_traffic


if Ligne == "2":
    #Ligne 1
    liste_stations = ClasseLigne2.liste_stations
    liste_eguillages = ClasseLigne2.liste_eguillages
    liste_terminus = ClasseLigne2.liste_terminus
    liste_metro = ClasseLigne2.liste_metro
    liste_lignes = ClasseLigne2.liste_lignes
    liste_depot_eguillage = ClasseLigne2.liste_depot_eguillage
    liste_depot_ligne= ClasseLigne2.liste_depot_ligne
    liste_feu_traffic = ClasseLigne2.liste_feu_traffic

if Ligne == "4":
    #Ligne 4
    liste_stations = ClasseLigne4.liste_stations
    liste_eguillages = ClasseLigne4.liste_eguillages
    liste_terminus = ClasseLigne4.liste_terminus
    liste_metro = ClasseLigne4.liste_metro
    liste_lignes = ClasseLigne4.liste_lignes
    liste_depot_eguillage = ClasseLigne4.liste_depot_eguillage
    liste_depot_ligne = ClasseLigne4.liste_depot_ligne
    liste_feu_traffic = ClasseLigne4.liste_feu_traffic

if Ligne == "6":
    #Ligne 6
    liste_stations = ClasseLigne6.liste_stations
    liste_eguillages = ClasseLigne6.liste_eguillages
    liste_terminus = ClasseLigne6.liste_terminus
    liste_metro = ClasseLigne6.liste_metro
    liste_lignes = ClasseLigne6.liste_lignes
    liste_depot_eguillage = ClasseLigne6.liste_depot_eguillage
    liste_depot_ligne = ClasseLigne6.liste_depot_ligne
    liste_feu_traffic = ClasseLigne6.liste_feu_traffic


if Ligne == "14":
    #Ligne 14
    liste_stations = ClasseLigne14.liste_stations
    liste_eguillages = ClasseLigne14.liste_eguillages
    liste_terminus = ClasseLigne14.liste_terminus
    liste_metro = ClasseLigne14.liste_metro
    liste_lignes = ClasseLigne14.liste_lignes
    liste_depot_eguillage = ClasseLigne14.liste_depot_eguillage
    liste_depot_ligne = ClasseLigne14.liste_depot_ligne
    liste_feu_traffic = ClasseLigne14.liste_feu_traffic

if Ligne == "0":
    #Ligne 14
    liste_stations = ClasseLigne0.liste_stations
    liste_eguillages = ClasseLigne0.liste_eguillages
    liste_terminus = ClasseLigne0.liste_terminus
    liste_metro = ClasseLigne0.liste_metro
    liste_lignes = ClasseLigne0.liste_lignes
    liste_depot_eguillage = ClasseLigne0.liste_depot_eguillage
    liste_depot_ligne = ClasseLigne0.liste_depot_eguillage
    liste_feu_traffic = ClasseLigne0.liste_feu_traffic

#Materialisation des terminus
for element in liste_terminus:
    canvas.create_rectangle(element[0]-3, element[1]-3, element[0]+3, element[1]+3, fill="#000000", outline="")

#Materialisation des terminus


#Materialisation des lignes
for element in liste_lignes:
    canvas.create_line(element[0],element[1],element[2],element[3], fill=element[4],width=element[5])

for element in liste_depot_ligne:
    canvas.create_line(element[0],element[1],element[2],element[3], fill=element[4],width=element[5])



canvas.pack(expand=True, fill="both")

canvas_metro.pack(expand=True, fill="both")

# Créer un poste de commande centralisé
metro_control = MetroControl(canvas, canvas_metro)



#Materialisation des terminus
for element in liste_terminus:
    canvas.create_rectangle(element[0]-3, element[1]-3, element[0]+3, element[1]+3, fill="#EBEBEB", outline="")


#Materialisation des EGUILLAGES
refresh_eguillages()
refresh_eguillages_depot()
# Ajouter des trains avec un léger décalage vertical entre les lignes



for element in liste_metro:
    train = Train(canvas, canvas_metro, element[0], element[1], element[2], element[3], element[4], element[5], liste_metro.index(element))
    metro_control.add_train(train)

global photo_fq_on
global photo_fq_off
image = Image.open("fq_on.PNG")
# Redimensionner l'image à une taille de 50x50 pixels
image = image.resize((22, 20))
# Convertir l'image en format compatible avec Tkinter
photo_fq_on = ImageTk.PhotoImage(image)

image = Image.open("fq_off.PNG")
# Redimensionner l'image à une taille de 50x50 pixels
image = image.resize((22, 20))
# Convertir l'image en format compatible avec Tkinter
photo_fq_off = ImageTk.PhotoImage(image)



for element in liste_stations:
    station = Station(canvas, element[0], element[1], element[2], element[3], 1)
    metro_control.add_station(station)

#for station in metro_control.stations:
#    station.text_id = canvas.create_text(station.x1+ 32, 20, text=station.name, fill=station.color, font=("Arial", 8), anchor="center")
#    station.rec_id = canvas.create_rectangle(station.x1, station.y1, station.x2, station.y2 , fill=station.color, outline="")

# Mettre à jour les trains à intervalle régulier
def update_trains():
    metro_control.update_trains()
    root.after(50, update_trains)



update_trains()
# Appeler la fonction update_time pour mettre à jour l'heure
update_time()
canvas_metro.create_text(200, 30, text="Gestion des stations", anchor=tk.CENTER, fill="#000000", font=("Arial",12))
canvas_metro.create_text(600, 30, text="Gestion des trains", anchor=tk.CENTER, fill="#000000", font=("Arial",12))
canvas_metro.create_text(980, 30, text="Gestion du traffic", anchor=tk.CENTER, fill="#000000", font=("Arial", 12))
canvas_metro.create_line(10, 20, 10, 1000, fill="#000000",width=2)
canvas_metro.create_line(400, 20, 400, 1000, fill="#000000",width=2)
canvas_metro.create_line(800, 20, 800, 1000, fill="#000000",width=2)


#bouton stop
bouton_stop = tk.Button(canvas_metro, command=action_bouton_stop)
global photo_stop
# Charger l'image
image = Image.open("stop.png")
# Redimensionner l'image à une taille de 50x50 pixels
image = image.resize((30, 30))
# Convertir l'image en format compatible avec Tkinter
photo_stop = ImageTk.PhotoImage(image)
# Mettre à jour le bouton avec l'image "stop"
bouton_stop.config(image=photo_stop, command=action_bouton_stop)
bouton_stop.image = photo_stop
button_stop_window = canvas_metro.create_window(920, 150, anchor=tk.CENTER, window=bouton_stop)

#bouton reprise
bouton_reprise = tk.Button(canvas_metro, command=action_bouton_reprise)
global photo_reprise
# Charger l'image
image = Image.open("reprise.png")
# Redimensionner l'image à une taille de 50x50 pixels
image = image.resize((30, 30))
# Convertir l'image en format compatible avec Tkinter
photo_reprise = ImageTk.PhotoImage(image)
# Mettre à jour le bouton avec l'image "stop"
bouton_reprise.config(image=photo_reprise, command=action_bouton_reprise)
bouton_reprise.image = photo_reprise
button_reprise_window = canvas_metro.create_window(920, 100, anchor=tk.CENTER, window=bouton_reprise)

#bouton parametre
#bouton_parametre = tk.Button(metro_control, command=ouvrir_fenetre())
#global photo_parametre
# Charger l'image
#image = Image.open("parametre.webp")
# Redimensionner l'image à une taille de 50x50 pixels
#image = image.resize((30, 30))
# Convertir l'image en format compatible avec Tkinter
#photo_parametre = ImageTk.PhotoImage(image)
# Mettre à jour le bouton avec l'image "stop"
#bouton_parametre.config(image=photo_parametre, command=ouvrir_fenetre())
#bouton_parametre.image = photo_parametre
#button_parametre_window = metro_control.create_window(620, 350, anchor=tk.CENTER, window=bouton_parametre)
# Charger et redimensionner l'image
image = Image.open("parametre.png")
image = image.resize((30, 30))
photo_parametre = ImageTk.PhotoImage(image)

# Créer un Frame pour contenir le bouton
frame_bouton = tk.Frame(canvas)
frame_bouton.pack()

# Créer le bouton dans le frame avec l'image et associer la fonction ouvrir_fenetre
bouton_parametre = tk.Button(frame_bouton, image=photo_parametre, command=ouvrir_fenetre)
bouton_parametre.image = photo_parametre  # Garder une référence à l'image
bouton_parametre.pack()

# Ajouter le frame contenant le bouton dans le Canvas
canvas.create_window(50, 50, anchor=tk.CENTER, window=frame_bouton)

canvas_metro.bind("<Button-1>", clic_sur_canevas_metro)
canvas.bind("<Button-1>", clic_sur_canevas)


global photo_feu_vert
global photo_feu_rouge

# Charger l'image
image = Image.open("feu_vert.jpg")
#Redimensionner l'image à une taille de 50x50 pixels
image = image.resize((20, 20))
# Convertir l'image en format compatible avec Tkinter
photo_feu_vert = ImageTk.PhotoImage(image)
image = Image.open("feu_rouge.jpg")
# Redimensionner l'image à une taille de 50x50 pixels
image = image.resize((20, 20))
# Convertir l'image en format compatible avec Tkinter
photo_feu_rouge = ImageTk.PhotoImage(image)





for element in liste_feu_traffic:
    feu = Feu(canvas,element[0], element[1],element[2])
    metro_control.add_feu(feu)


# Lancer la boucle principale Tkinter
root_metro.withdraw()
root.mainloop()

