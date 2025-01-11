from tkinter import *
import tkinter as tk
import numpy as np
import cv2
from mss import mss
import time

from yolo_object_detection import *
from intersection_of_bubbles import intersection

import time


window = Tk()
window.state('zoomed')

platno = Canvas(window, width=1920, height=1080, bg='light gray')
platno.pack()

#prva vrstica gumbov 
platno.create_oval(600, 100, 720, 220, width=3, outline='white', fill='white')
platno.create_oval(790, 100, 910, 220, width=3, outline='white', fill='white')
platno.create_oval(980, 100, 1100, 220, width=3, outline='white', fill='white')

platno.create_text(640, 165, anchor=W, text="1",fill='black',  font=('Purisa 50 bold'))
platno.create_text(830, 165, anchor=W, text="2",fill='black',  font=('Purisa 50 bold'))
platno.create_text(1020, 165, anchor=W, text="3",fill='black',  font=('Purisa 50 bold'))

#druga vrstica gumbov
platno.create_oval(600, 300, 720, 420, width=3, outline='white', fill='white')
platno.create_oval(790, 300, 910, 420, width=3, outline='white', fill='white')
platno.create_oval(980, 300, 1100, 420, width=3, outline='white', fill='white')

platno.create_text(640, 365, anchor=W, text="4",fill='black',  font=('Purisa 50 bold'))
platno.create_text(830, 365, anchor=W, text="5",fill='black',  font=('Purisa 50 bold'))
platno.create_text(1020, 365, anchor=W, text="6",fill='black',  font=('Purisa 50 bold'))

#tretja vrstica gumbov
platno.create_oval(600, 500, 720, 620, width=3, outline='white', fill='white')
platno.create_oval(790, 500, 910, 620, width=3, outline='white', fill='white')
platno.create_oval(980, 500, 1100, 620, width=3, outline='white', fill='white')

platno.create_text(640, 565, anchor=W, text="7",fill='black',  font=('Purisa 50 bold'))
platno.create_text(830, 565, anchor=W, text="8",fill='black',  font=('Purisa 50 bold'))
platno.create_text(1020, 565, anchor=W, text="9",fill='black',  font=('Purisa 50 bold'))

#četrta vrstica gumbov
platno.create_oval(600, 700, 720, 820, width=3, outline='white', fill='white')
platno.create_oval(790, 700, 910, 820, width=3, outline='white', fill='white')
platno.create_oval(980, 700, 1100, 820, width=3, outline='green', fill='green')

platno.create_text(640, 765, anchor=W, text="C",fill='red',  font=('Purisa 50 bold'))
platno.create_text(830, 765, anchor=W, text="0",fill='black',  font=('Purisa 50 bold'))
platno.create_text(1020, 765, anchor=W, text="=",fill='white',  font=('Purisa 50 bold'))

#gumbi operacij
platno.create_oval(1202, 100, 1322, 220, width=3, outline='white', fill='white')
platno.create_oval(1202, 300, 1322, 420, width=3, outline='white', fill='white')
platno.create_oval(1202, 500, 1322, 620, width=3, outline='white', fill='white')
platno.create_oval(1202, 700, 1322, 820, width=3, outline='white', fill='white')

platno.create_text(1243, 160, anchor=W, text="+",fill='green',  font=('Purisa 60 bold'))
platno.create_text(1243, 355, anchor=W, text="-",fill='green',  font=('Purisa 80 bold'))
platno.create_text(1247, 572, anchor=W, text="*",fill='green',  font=('Purisa 70 bold'))
platno.create_text(1250, 765, anchor=W, text="/",fill='green',  font=('Purisa 60 bold'))

#prikaz števil in rezultatov
platno.create_rectangle(100, 300, 500, 600, outline="white", fill="white", width=2)

#gumb za izhod iz kalkulatorja
platno.create_oval(925, 900, 975, 950, width=3, outline='red', fill='red')
platno.create_text(937, 925, anchor=W, text="X",fill='white',  font=('Purisa 30 bold'))


#naložimo Yolo
net = cv2.dnn.readNet("yolov3_training_last.weights", "yolov3_testing.cfg")

#področje iskanja mehurčka bo celoten zaslon
bounding_box = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}

#zajem zaslona
screen = mss()

#spremenljivke, ki jih potrebujemo tekom izvajanja kode
first_number = 0
second_number = 0
chosen_operation = ''
chosen_math_symbol = 0

result = 0

while 1: 

    window.update()
    time.sleep(1.5)


    #koordinate območja zaznanega mehurčka
    x_top = 0
    y_top = 0
    x_bottom = 0
    y_bottom = 0

    #izbrani simbol
    chosen_symbol = ''

    #ujemanje preseka območij mehurčka in simbola
    intersection_match = 0

    #spremenljivke, ki jih potrebujemo pri odločanju za upoštevanje območja 
    pi = 0
    counter = 0
    last_koordinate = ()
    zaporeden_miss = 0 
    zaporeden_match = 0

    
    #pogledamo 5 zaporednih zajemov zaslona 
    while counter < 5:
        window.update()
        
        #zajamemo posnetek zaslona
        screen_img = screen.grab(bounding_box)
        #in ga shranimo v png sliko
        cv2.imwrite('screenshot_current.png', cv2.cvtColor(np.array(screen_img), cv2.COLOR_RGB2BGR))
       
        #poiščemo mehurček (v kolikor obstaja)
        x_top,y_top,x_bottom,y_bottom = findBubbleArea('screenshot_current.png', net)
        
        #izvedemo presek območij in dobimo izbran simbol, ujemanje ombočij in koordinate izbranega simbola
        chosen_symbol, intersection_match, koordinate = intersection(x_top, y_top, x_bottom, y_bottom)
        
        if len(koordinate) != 0: #če koordinate niso prazne
            
            #če se prejšnje in trenutne koordinate ujemajo
            if(last_koordinate == koordinate):
                #izrišemo četrtino obrobe izbranega simbola
                platno.create_arc(koordinate, style=tk.ARC, width=6, outline='goldenrod1', extent=90, start=pi, tag='drawn')
                
                pi = pi + 90
                counter = counter + 1
                
                if zaporeden_match != 4: #če se še niso zapolnile vse četrtine
                    zaporeden_match = zaporeden_match + 1
                
            else:#last_koordinate != koordinate: 
                platno.delete('drawn')
                counter = 1
                pi = 0 
                platno.create_arc(koordinate, style=tk.ARC, width=6, outline='goldenrod1', extent=90, start=pi, tag='drawn')
                zaporeden_match = 1
                pi = pi + 90
                
                
            last_koordinate = koordinate
        else: #če so koordinate prazne
            if zaporeden_miss != 2:
                zaporeden_miss = zaporeden_miss + 1
            if zaporeden_miss == 2: #uporabnik gleda drugam in ne v simbol
                counter = 0
                koordinate = ()
                last_koordinate = ()
                zaporeden_miss = 0
                zaporeden_match = 0
                pi = 0
                platno.delete('drawn')
        

    platno.delete('drawn')   
    
     #preverimo kateri simbol je izbran   
    if chosen_symbol == '1': 
        if chosen_math_symbol == 0:#če še ni izbrana operacija bo to prvo število
            first_number = first_number*10 + 1
            #zapišemo ga na zaslon
            platno.create_text(150, 340, anchor=W, text=str(first_number),fill='green',  font=('Purisa 40 bold'), tag='first_number')
        else: 
            second_number = second_number*10 + 1#če je bila operacija izbrana, bo to drugo število 
            platno.create_text(150, 430, anchor=W, text=str(second_number),fill='green',  font=('Purisa 40 bold'), tag='second_number')
    elif chosen_symbol == '2':  
        if chosen_math_symbol == 0:
            first_number = first_number*10 + 2
            platno.create_text(150, 340, anchor=W, text=str(first_number),fill='green',  font=('Purisa 40 bold'), tag='first_number')
        else: 
            second_number = second_number*10 + 2
            platno.create_text(150, 430, anchor=W, text=str(second_number),fill='green',  font=('Purisa 40 bold'), tag='second_number')
    elif chosen_symbol == '3':  
        if chosen_math_symbol == 0:
            first_number = first_number*10 + 3
            platno.create_text(150, 340, anchor=W, text=str(first_number),fill='green',  font=('Purisa 40 bold'), tag='first_number')
        else: 
            second_number = second_number*10 + 3
            platno.create_text(150, 430, anchor=W, text=str(second_number),fill='green',  font=('Purisa 40 bold'), tag='second_number')
    elif chosen_symbol == '4':  
        if chosen_math_symbol == 0:
            first_number = first_number*10 + 4
            platno.create_text(150, 340, anchor=W, text=str(first_number),fill='green',  font=('Purisa 40 bold'), tag='first_number')
        else: 
            second_number = second_number*10 + 4
            platno.create_text(150, 430, anchor=W, text=str(second_number),fill='green',  font=('Purisa 40 bold'), tag='second_number')
    elif chosen_symbol == '5':  
        if chosen_math_symbol == 0:
            first_number = first_number*10 + 5
            platno.create_text(150, 340, anchor=W, text=str(first_number),fill='green',  font=('Purisa 40 bold'), tag='first_number')
        else: 
            second_number = second_number*10 + 5
            platno.create_text(150, 430, anchor=W, text=str(second_number),fill='green',  font=('Purisa 40 bold'), tag='second_number')
    elif chosen_symbol == '6':  
        if chosen_math_symbol == 0:
            first_number = first_number*10 + 6
            platno.create_text(150, 340, anchor=W, text=str(first_number),fill='green',  font=('Purisa 40 bold'), tag='first_number')
        else: 
            second_number = second_number*10 + 6
            platno.create_text(150, 430, anchor=W, text=str(second_number),fill='green',  font=('Purisa 40 bold'), tag='second_number')
    elif chosen_symbol == '7':  
        if chosen_math_symbol == 0:
            first_number = first_number*10 + 7
            platno.create_text(150, 340, anchor=W, text=str(first_number),fill='green',  font=('Purisa 40 bold'), tag='first_number')
        else: 
            second_number = second_number*10 + 7
            platno.create_text(150, 430, anchor=W, text=str(second_number),fill='green',  font=('Purisa 40 bold'), tag='second_number')
    elif chosen_symbol == '8': 
        if chosen_math_symbol == 0:
            first_number = first_number*10 + 8
            platno.create_text(150, 340, anchor=W, text=str(first_number),fill='green',  font=('Purisa 40 bold'), tag='first_number')
        else: 
            second_number = second_number*10 + 8
            platno.create_text(150, 430, anchor=W, text=str(second_number),fill='green',  font=('Purisa 40 bold'), tag='second_number')
    elif chosen_symbol == '9':  
        if chosen_math_symbol == 0:
            first_number = first_number*10 + 9
            platno.create_text(150, 340, anchor=W, text=str(first_number),fill='green',  font=('Purisa 40 bold'), tag='first_number')
        else: 
            second_number = second_number*10 + 9
            platno.create_text(150, 430, anchor=W, text=str(second_number),fill='green',  font=('Purisa 40 bold'), tag='second_number')
    elif chosen_symbol == '0': 
        if chosen_math_symbol == 0:
            first_number = first_number*10 
            platno.create_text(150, 340, anchor=W, text=str(first_number),fill='green',  font=('Purisa 40 bold'), tag='first_number')
        else: 
            second_number = second_number*10 
            platno.create_text(150, 430, anchor=W, text=str(second_number),fill='green',  font=('Purisa 40 bold'), tag='second_number')
    elif chosen_symbol == 'C': #pobrišemo vse izbrano
        chosen_operation = ''
        first_number = 0
        second_number = 0
        chosen_math_symbol = 0

        platno.delete('first_number')
        platno.delete('second_number')
        platno.delete('operation')
        platno.delete('result')

    elif chosen_symbol == '+': #preverimo katera operacija je izbrana 
        chosen_operation = '+'
        if chosen_math_symbol == 0: #če še ni bila izbrana nobena operacija
            chosen_math_symbol = 1
        else: #če je bila operacija že izbrana, pomeni da imamo nek rezultat zato 
            first_number = str(result) #rezultat postane prvo število
            #vse izračunano pobrišemo 
            result = 0
            second_number = 0
            platno.delete('first_number')
            platno.delete('second_number')
            platno.delete('operation')
            platno.delete('result')

            #zapišemo prvo število (ki je prejšnji rezultat)
            platno.create_text(150, 340, anchor=W, text=str(first_number),fill='green',  font=('Purisa 40 bold'), tag='first_number')

        #zapišemo še operacijo
        platno.create_text(150, 380, anchor=W, text='+',fill='green',  font=('Purisa 20 bold'), tag='operation')
    elif chosen_symbol == '-': 
        chosen_operation = '-'
        if chosen_math_symbol == 0: 
            chosen_math_symbol = 1
        else: 
            first_number = str(result)
            result = 0
            second_number = 0
            platno.delete('first_number')
            platno.delete('second_number')
            platno.delete('operation')
            platno.delete('result')

            platno.create_text(150, 340, anchor=W, text=str(first_number),fill='green',  font=('Purisa 40 bold'), tag='first_number')
        
        platno.create_text(150, 380, anchor=W, text='-',fill='green',  font=('Purisa 20 bold'), tag='operation')
    elif chosen_symbol == '*': 
        chosen_operation = '*'
        if chosen_math_symbol == 0: 
            chosen_math_symbol = 1
        else: 
            first_number = str(result)
            result = 0
            second_number = 0
            platno.delete('first_number')
            platno.delete('second_number')
            platno.delete('operation')
            platno.delete('result')

            platno.create_text(150, 340, anchor=W, text=str(first_number),fill='green',  font=('Purisa 40 bold'), tag='first_number')
        
        platno.create_text(150, 380, anchor=W, text='*',fill='green',  font=('Purisa 20 bold'), tag='operation')
    elif chosen_symbol == '/': 
        chosen_operation = '/'
        if chosen_math_symbol == 0: 
            chosen_math_symbol = 1
        else: 
            first_number = str(result)
            result = 0
            second_number = 0
            platno.delete('first_number')
            platno.delete('second_number')
            platno.delete('operation')
            platno.delete('result')

            platno.create_text(150, 340, anchor=W, text=str(first_number),fill='green',  font=('Purisa 40 bold'), tag='first_number')
    
        platno.create_text(150, 380, anchor=W, text='/',fill='green',  font=('Purisa 20 bold'), tag='operation')
    elif chosen_symbol == '=': #izračunamo vnešeno 
        if chosen_operation == '+':
            result = float(first_number) + float(second_number)
            platno.create_text(150, 500, anchor=W, text='= '+str(result),fill='green',  font=('Purisa 60 bold'), tag='result')
        if chosen_operation == '-':
            result = float(first_number) - float(second_number)
            platno.create_text(150, 500, anchor=W, text='= '+str(result),fill='green',  font=('Purisa 60 bold'), tag='result')
        if chosen_operation == '*':
            result = float(first_number) * float(second_number)
            platno.create_text(150, 500, anchor=W, text='= '+str(result),fill='green',  font=('Purisa 60 bold'), tag='result')
        if chosen_operation == '/':
            result = float(first_number) / float(second_number)
            result = round(result, 2)#zaokrožimo rezultat
            platno.create_text(150, 500, anchor=W, text='= '+str(result),fill='green',  font=('Purisa 60 bold'), tag='result')
    elif chosen_symbol == 'X':#izhod iz programa
        exit(1)

window.mainloop()       
        
        



