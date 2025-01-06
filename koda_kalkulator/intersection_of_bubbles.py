from shapely.geometry import Polygon
from tkinter import *
import time
import numpy as np
import random
from turtle import *
import turtle
import tkinter as tk


def countdown(t):
     while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        #print(timer, end="\r")
        time.sleep(1)
        t -= 1

def percentage(box_shape_1, box_shape_2): 
    # Draw polygon 1 from shape 1 
    # dimensions
    polygon_1 = Polygon(box_shape_1)

    # Draw polygon 2 from shape 2 
    # dimensions
    polygon_2 = Polygon(box_shape_2)

    # Calculate the intersection of
    # bounding boxes
    intersect = polygon_1.intersection(
        polygon_2).area / polygon_1.union(polygon_2).area

    # Print the intersection percentage
    #print(round(intersect*100, 2), '%')
    percent_match = round(intersect*100, 2)
    
    return percent_match



def intersection(x_top, y_top, x_bottom, y_bottom, platno, tags):
    # Give dimensions of shape 1
    box_shape_1 = [[x_top, y_top], [x_bottom, y_top], 
                [x_bottom, y_bottom], [x_top,y_bottom]]

    box_shape_2 = [[1, 1], [1, 1], 
                [1,1], [1, 1]]
    chosen = 'none'
    percent = 0
    
    #zelva = RawTurtle(platno)
    #zelva.pensize= 10
    #zelva.color = 'green'
    #zelva.circle(100,180)

    #screen = turtle.TurtleScreen(platno)
    
    #my_lovely_turtle = turtle.RawTurtle(platno, shape="turtle")

    
    # List of items
    color_list = ['goldenrod1', 'goldenrod2','goldenrod3','goldenrod4']#'cornflower blue', 'light slate blue', 'blue', 'deep sky blue', 'cyan', 'lawn green', 'yellow', 'red', 'violet red', 'purple', 'DodgerBlue4', 'chocolate2']

    
    color = random.choice(color_list)#'goldenrod2'#

    if x_top >= 565 and x_top <= 720 and y_bottom <= 260:
        #print('one')
        chosen = '1'
        
        # Give dimensions of shape 2
        box_shape_2 = [[600, 100], [720, 100], 
                [720,220], [600, 220]]
        
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            #if tags != '':
            platno.delete(tags)
            
            platno.create_arc(600,100, 720,220, style=tk.ARC, width=6, outline='goldenrod1', extent=90, start=360, tag='one')
           
            platno.create_arc(600,100, 720,220, style=tk.ARC, width=6, outline='goldenrod2', extent=90, start=90, tag='one')
            
            #platno.create_oval(600, 100, 720, 220, width=6, outline=color, tag='one')
            tags = 'one'

    elif x_top >= 755 and x_top <= 910 and y_bottom <= 260:
        #print('two')
        chosen = '2'
        # Give dimensions of shape 2
        box_shape_2 = [[790, 100], [910, 100], 
                [910,220], [790, 220]]
        percent = percentage(box_shape_1, box_shape_2)
        if percent >= 50:
            platno.delete(tags)
            platno.create_oval(790, 100, 910, 220, width=6, outline=color, tag='two')
            tags = 'two'
            
    elif x_top >= 945 and x_top <= 1100 and y_bottom <= 260:
        #print('three')
        chosen = '3'
        # Give dimensions of shape 2
        box_shape_2 = [[980, 100], [1100, 100], 
                [1100,220], [980, 220]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            platno.delete(tags)
            platno.create_oval(980, 100, 1100, 220, width=6, outline=color, tag='three')
            tags = 'three'

    elif x_top >= 1150 and x_top <= 1322 and y_bottom <= 260:
        #print('plus')
        chosen = '+'
        # Give dimensions of shape 2
        box_shape_2 = [[1200, 100], [1322, 100], 
                [1322,220], [1200, 220]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            platno.delete(tags)
            platno.create_oval(1202, 100, 1322, 220, width=6, outline=color, tag='+')
            tags = '+'

    elif x_top >= 565 and x_top <= 720 and y_top >=260 and y_bottom <= 460:
        #print('four')
        chosen = '4'
        # Give dimensions of shape 2
        box_shape_2 = [[600, 300], [720, 300], 
                [720,420], [600, 420]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            platno.delete(tags)
            platno.create_oval(600, 300, 720, 420, width=6, outline=color, tag='four')
            tags = 'four'

    elif x_top >= 755 and x_top <= 910 and y_top >=260 and y_bottom <= 460:
        #print('five')
        chosen = '5'
        # Give dimensions of shape 2
        box_shape_2 = [[790, 300], [910, 300], 
                [910,420], [790, 420]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            platno.delete(tags)
            platno.create_oval(790, 300, 910, 420, width=6, outline=color, tag='five')
            tags = 'five'

    elif x_top >= 945 and x_top <= 1100 and y_top >=260 and y_bottom <= 460:
        #print('six')
        chosen = '6'
        # Give dimensions of shape 2
        box_shape_2 = [[980, 300], [1100, 300], 
                [1100,420], [980, 420]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            platno.delete(tags)
            platno.create_oval(980, 300, 1100, 420, width=6, outline=color, tag='six')
            tags = 'six'

    elif x_top >= 1150 and x_top <= 1322 and y_top >=260 and y_bottom <= 460:
        #print('minus')
        chosen = '-'
        # Give dimensions of shape 2
        box_shape_2 = [[1200, 300], [1322, 300], 
                [1322,420], [1200, 420]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            platno.delete(tags)
            platno.create_oval(1202, 300, 1322, 420, width=6, outline=color, tag='-')
            tags = '-'

    elif x_top >= 565 and x_top <= 720 and y_top >=460 and y_bottom <= 660:
        #print('seven')
        chosen = '7'
        # Give dimensions of shape 2
        box_shape_2 = [[600, 500], [720, 500], 
                [720,620], [600, 620]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            platno.delete(tags)
            platno.create_oval(600, 500, 720, 620, width=6, outline=color, tag='seven')
            tags = 'seven'

    elif x_top >= 755 and x_top <= 910 and y_top >=460 and y_bottom <= 660:
        #print('eight')
        chosen = '8'
        # Give dimensions of shape 2
        box_shape_2 = [[790, 500], [910, 500], 
                [910,620], [790, 620]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            platno.delete(tags)
            platno.create_oval(790, 500, 910, 620, width=6, outline=color, tag='eight')
            tags = 'eight'

    elif x_top >= 945 and x_top <= 1100 and y_top >=460 and y_bottom <= 660:
        #print('nine')
        chosen = '9'
        # Give dimensions of shape 2
        box_shape_2 = [[980, 500], [1100, 500], 
                [1100,620], [980, 620]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            platno.delete(tags)
            platno.create_oval(980, 500, 1100, 620, width=6, outline=color, tag='nine')
            tags = 'nine'

    elif x_top >= 1150 and x_top <= 1322 and y_top >=460 and y_bottom <= 660:
        #print('multiply')
        chosen = '*'
        # Give dimensions of shape 2
        box_shape_2 = [[1200, 500], [1322, 500], 
                [1322,620], [1200, 620]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            platno.delete(tags)
            platno.create_oval(1202, 500, 1322, 620, width=6, outline=color, tag='*')
            tags = '*'

    elif x_top >= 565 and x_top <= 720 and y_top >=660 and y_bottom <= 860:
        #print('delete')
        chosen = 'C'
        # Give dimensions of shape 2
        box_shape_2 = [[600, 700], [720, 700], 
                [720,820], [600, 820]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            platno.delete(tags)
            platno.create_oval(600, 700, 720, 820, width=6, outline=color, tag='C')
            tags = 'C'

    elif x_top >= 755 and x_top <= 910 and y_top >=660 and y_bottom <= 860:
        #print('zero')
        chosen = '0'
        # Give dimensions of shape 2
        box_shape_2 = [[790, 700], [910, 700], 
                [910,820], [790, 820]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            platno.delete(tags)
            platno.create_oval(790, 700, 910, 820, width=6, outline=color, tag='zero')
            tags = 'zero'

    elif x_top >= 945 and x_top <= 1100 and y_top >=660 and y_bottom <= 860:
        #print('equals')
        chosen = '='
        # Give dimensions of shape 2
        box_shape_2 = [[980, 700], [1100, 700], 
                [1100,820], [980, 820]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            platno.delete(tags)
            platno.create_oval(980, 700, 1100, 820, width=6, outline=color, tag='=')
            tags = '='

    elif x_top >= 1150 and x_top <= 1322 and y_top >=660 and y_bottom <= 860:
        #print('divide')
        chosen = '/'
        # Give dimensions of shape 2
        box_shape_2 = [[1200, 700], [1322, 700], 
                [1322,820], [1200, 820]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            platno.delete(tags)
            platno.create_oval(1202, 700, 1322, 820, width=6, outline=color, tag='/')
            tags = '/'

    elif x_top >= 850 and x_top <= 975 and y_top >= 860 and y_bottom <= 1000:
        chosen = 'X'
        #print('X was chosen')
        box_shape_2 = [[900, 880], [1000, 880], 
                [1000,980], [900, 980]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            platno.delete(tags)
            platno.create_oval(925, 900, 975, 950, width=6, outline=color, tag='x')
            tags = 'x'


    #time.sleep(1)
    #platno.delete('test')
    return chosen, percent, tags