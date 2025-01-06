from tkinter import *
from yolo_object_detection import *
import numpy as np
import cv2
from mss import mss
import pyautogui
import time
from intersection_of_bubbles import *


import time


def countdown(t):
     while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        #print(timer, end="\r")
        time.sleep(1)
        t -= 1

    #print("Time's up!")

window = Tk()
#window.geometry("500x600")
window.state('zoomed')

platno = Canvas(window, width=1920, height=1080, bg='light gray')
platno.pack()

#first row of buttons:
platno.create_oval(600, 100, 720, 220, width=3, outline='white', fill='white')
platno.create_oval(790, 100, 910, 220, width=3, outline='white', fill='white')
platno.create_oval(980, 100, 1100, 220, width=3, outline='white', fill='white')

platno.create_text(640, 165, anchor=W, text="1",fill='black',  font=('Purisa 50 bold'))
platno.create_text(830, 165, anchor=W, text="2",fill='black',  font=('Purisa 50 bold'))
platno.create_text(1020, 165, anchor=W, text="3",fill='black',  font=('Purisa 50 bold'))

#second row of buttons
platno.create_oval(600, 300, 720, 420, width=3, outline='white', fill='white')
platno.create_oval(790, 300, 910, 420, width=3, outline='white', fill='white')
platno.create_oval(980, 300, 1100, 420, width=3, outline='white', fill='white')

platno.create_text(640, 365, anchor=W, text="4",fill='black',  font=('Purisa 50 bold'))
platno.create_text(830, 365, anchor=W, text="5",fill='black',  font=('Purisa 50 bold'))
platno.create_text(1020, 365, anchor=W, text="6",fill='black',  font=('Purisa 50 bold'))

#third row of buttons
platno.create_oval(600, 500, 720, 620, width=3, outline='white', fill='white')
platno.create_oval(790, 500, 910, 620, width=3, outline='white', fill='white')
platno.create_oval(980, 500, 1100, 620, width=3, outline='white', fill='white')

platno.create_text(640, 565, anchor=W, text="7",fill='black',  font=('Purisa 50 bold'))
platno.create_text(830, 565, anchor=W, text="8",fill='black',  font=('Purisa 50 bold'))
platno.create_text(1020, 565, anchor=W, text="9",fill='black',  font=('Purisa 50 bold'))

#fourth row of buttons
platno.create_oval(600, 700, 720, 820, width=3, outline='white', fill='white')
platno.create_oval(790, 700, 910, 820, width=3, outline='white', fill='white')
platno.create_oval(980, 700, 1100, 820, width=3, outline='green', fill='green')

platno.create_text(640, 765, anchor=W, text="C",fill='red',  font=('Purisa 50 bold'))
platno.create_text(830, 765, anchor=W, text="0",fill='black',  font=('Purisa 50 bold'))
platno.create_text(1020, 765, anchor=W, text="=",fill='white',  font=('Purisa 50 bold'))

#operation buttons
platno.create_oval(1202, 100, 1322, 220, width=3, outline='white', fill='white')
platno.create_oval(1202, 300, 1322, 420, width=3, outline='white', fill='white')
platno.create_oval(1202, 500, 1322, 620, width=3, outline='white', fill='white')
platno.create_oval(1202, 700, 1322, 820, width=3, outline='white', fill='white')

platno.create_text(1243, 160, anchor=W, text="+",fill='green',  font=('Purisa 60 bold'))
platno.create_text(1243, 355, anchor=W, text="-",fill='green',  font=('Purisa 80 bold'))
platno.create_text(1247, 572, anchor=W, text="*",fill='green',  font=('Purisa 70 bold'))
platno.create_text(1250, 765, anchor=W, text="/",fill='green',  font=('Purisa 60 bold'))

platno.create_rectangle(100, 300, 500, 600, outline="white", fill="white", width=2)

platno.create_oval(925, 900, 975, 950, width=3, outline='red', fill='red')
platno.create_text(937, 925, anchor=W, text="X",fill='white',  font=('Purisa 30 bold'))

#področje iskanja mehurčka bo celoten zaslon
bounding_box = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}

#zajem zaslona
screen = mss()

first_number = 0
second_number = 0
chosen_operation = ''
chosen_math_symbol = 0

result = 0


tag = ''
active_tag = ''



#koda za sledenje
while 1: 

    x_top = 0
    y_top = 0
    x_bottom = 0
    y_bottom = 0
    chosen_symbol = ''
    intersection_match = 0
    window.update()

    for x in range(3):
         
        time.sleep(1.5)
    
        #countdown(2)
        
        screen_img = screen.grab(bounding_box)

        #ponoven zajem zaslona
        current = pyautogui.screenshot()
        cv2.imwrite('screenshot_current.png', cv2.cvtColor(np.array(current), cv2.COLOR_RGB2BGR))
        x_top,y_top,x_bottom,y_bottom = findBubbleArea('screenshot_current.png')

        chosen_symbol, intersection_match, active_tag = intersection(x_top, y_top, x_bottom, y_bottom, platno, active_tag)
        #print('active tag ', active_tag)
        
        color_list = ['goldenrod1', 'goldenrod2','goldenrod3','goldenrod4']#'cornflower blue', 'light slate blue', 'blue', 'deep sky blue', 'cyan', 'lawn green', 'yellow', 'red', 'violet red', 'purple', 'DodgerBlue4', 'chocolate2']
        print(chosen_symbol)
        
        
    if intersection_match >= 50: #če je ujemanje vsaj 50% 
        
        if chosen_symbol == '1': #preverimo kateri simbol je izbran 
            if chosen_math_symbol == 0:
                
                first_number = first_number*10 + 1
                
                platno.create_arc(600,100, 720,220, style=tk.ARC, width=6, outline='goldenrod3', extent=90, start=180, tag='one')
                color = random.choice(color_list)#'goldenrod2'#
                platno.create_arc(600,100, 720,220, style=tk.ARC, width=6, outline='goldenrod4', extent=90, start=270, tag='one')
                platno.create_text(150, 340, anchor=W, text=str(first_number),fill='green',  font=('Purisa 40 bold'), tag='first_number')
                
            else: 
                second_number = second_number*10 + 1
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

        elif chosen_symbol == '+': #preverimo kateri simbol je izbran 
            chosen_operation = '+'
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

            
            platno.create_text(150, 380, anchor=W, text='+',fill='green',  font=('Purisa 20 bold'), tag='operation')
        elif chosen_symbol == '-': #preverimo kateri simbol je izbran 
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
        elif chosen_symbol == '*': #preverimo kateri simbol je izbran 
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
        elif chosen_symbol == '/': #preverimo kateri simbol je izbran 
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
                result = round(result, 2)
                
                platno.create_text(150, 500, anchor=W, text='= '+str(result),fill='green',  font=('Purisa 60 bold'), tag='result')
        elif chosen_symbol == 'X': #preverimo kateri simbol je izbran 
            
            exit(1)

window.mainloop()       
        
        



