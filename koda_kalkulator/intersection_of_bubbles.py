from shapely.geometry import Polygon
from tkinter import *

def percentage(box_shape_1, box_shape_2): 
    obmocje_mehurcka = Polygon(box_shape_1)

    obmocje_simbola = Polygon(box_shape_2)

    intersect = obmocje_mehurcka.intersection(obmocje_simbola).area / obmocje_mehurcka.union(obmocje_simbola).area

    percent_match = round(intersect*100, 2)
    
    return percent_match

def intersection(x_top, y_top, x_bottom, y_bottom):
    
    box_shape_1 = [[x_top, y_top], [x_bottom, y_top], 
                [x_bottom, y_bottom], [x_top,y_bottom]]

    box_shape_2 = [[1, 1], [1, 1], 
                [1,1], [1, 1]]
    chosen = 'none'
    percent = 0
    koordinate = ()
    
    if x_top >= 565 and x_top <= 720 and y_bottom <= 260:
        chosen = '1'
        box_shape_2 = [[600, 100], [720, 100], 
                [720,220], [600, 220]]
        
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            koordinate = (600,100, 720,220)
            
    elif x_top >= 755 and x_top <= 910 and y_bottom <= 260:
        chosen = '2'
        box_shape_2 = [[790, 100], [910, 100], 
                [910,220], [790, 220]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            koordinate = (790, 100, 910, 220)
            
    elif x_top >= 945 and x_top <= 1100 and y_bottom <= 260:
        chosen = '3'
        box_shape_2 = [[980, 100], [1100, 100], 
                [1100,220], [980, 220]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            koordinate = (980, 100, 1100, 220)

    elif x_top >= 1150 and x_top <= 1322 and y_bottom <= 260:
        chosen = '+'
        box_shape_2 = [[1200, 100], [1322, 100], 
                [1322,220], [1200, 220]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            koordinate = (1202, 100, 1322, 220)    
            
    elif x_top >= 565 and x_top <= 720 and y_top >=260 and y_bottom <= 460:
        chosen = '4'
        box_shape_2 = [[600, 300], [720, 300], 
                [720,420], [600, 420]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            koordinate = (600, 300, 720, 420)  

    elif x_top >= 755 and x_top <= 910 and y_top >=260 and y_bottom <= 460:
        chosen = '5'
        box_shape_2 = [[790, 300], [910, 300], 
                [910,420], [790, 420]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            koordinate = (790, 300, 910, 420)

    elif x_top >= 945 and x_top <= 1100 and y_top >=260 and y_bottom <= 460:
        chosen = '6'
        box_shape_2 = [[980, 300], [1100, 300], 
                [1100,420], [980, 420]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            koordinate = (980, 300, 1100, 420)

    elif x_top >= 1150 and x_top <= 1322 and y_top >=260 and y_bottom <= 460:
        chosen = '-'
        box_shape_2 = [[1200, 300], [1322, 300], 
                [1322,420], [1200, 420]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            koordinate = (1202, 300, 1322, 420)

    elif x_top >= 565 and x_top <= 720 and y_top >=460 and y_bottom <= 660:
        chosen = '7'
        box_shape_2 = [[600, 500], [720, 500], 
                [720,620], [600, 620]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            koordinate = (600, 500, 720, 620)

    elif x_top >= 755 and x_top <= 910 and y_top >=460 and y_bottom <= 660:
        chosen = '8'
        box_shape_2 = [[790, 500], [910, 500], 
                [910,620], [790, 620]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            koordinate = (790, 500, 910, 620)

    elif x_top >= 945 and x_top <= 1100 and y_top >=460 and y_bottom <= 660:
        chosen = '9'
        box_shape_2 = [[980, 500], [1100, 500], 
                [1100,620], [980, 620]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            koordinate = (980, 500, 1100, 620)

    elif x_top >= 1150 and x_top <= 1322 and y_top >=460 and y_bottom <= 660:
        chosen = '*'
        box_shape_2 = [[1200, 500], [1322, 500], 
                [1322,620], [1200, 620]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            koordinate = (1202, 500, 1322, 620)

    elif x_top >= 565 and x_top <= 720 and y_top >=660 and y_bottom <= 860:
        chosen = 'C'
        box_shape_2 = [[600, 700], [720, 700], 
                [720,820], [600, 820]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            koordinate = (600, 700, 720, 820)

    elif x_top >= 755 and x_top <= 910 and y_top >=660 and y_bottom <= 860:
        chosen = '0'
        box_shape_2 = [[790, 700], [910, 700], 
                [910,820], [790, 820]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            koordinate = (790, 700, 910, 820)

    elif x_top >= 945 and x_top <= 1100 and y_top >=660 and y_bottom <= 860:
        chosen = '='
        box_shape_2 = [[980, 700], [1100, 700], 
                [1100,820], [980, 820]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            koordinate = (980, 700, 1100, 820)

    elif x_top >= 1150 and x_top <= 1322 and y_top >=660 and y_bottom <= 860:
        chosen = '/'
        box_shape_2 = [[1200, 700], [1322, 700], 
                [1322,820], [1200, 820]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            koordinate = (1202, 700, 1322, 820)

    elif x_top >= 850 and x_top <= 975 and y_top >= 860 and y_bottom <= 1000:
        chosen = 'X'
        box_shape_2 = [[900, 880], [1000, 880], 
                [1000,980], [900, 980]]
        percent = percentage(box_shape_1, box_shape_2)

        if percent >= 50:
            koordinate = (925, 900, 975, 950)

    return chosen, percent, koordinate