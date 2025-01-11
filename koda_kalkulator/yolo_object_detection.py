import cv2
import numpy as np


def findBubbleArea(picturename, net):
    
    lokacija_slike = picturename

    x_top = 1
    y_top = 1
    x_bottom = 1
    y_bottom = 1

    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    
    #slika na kateri zaznavamo
    slika = cv2.imread(lokacija_slike)
    slika = cv2.resize(slika, None, fx=0.2, fy=0.2)
    height, width, _ = slika.shape
    
    blob = cv2.dnn.blobFromImage(slika, 0.00392, (224, 224), (0, 0, 0), False, crop=False)

    net.setInput(blob)
    outs = net.forward(output_layers)
    
    for out in outs:
        for detection in out:

            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            #če smo zaznali mehurček
            if confidence > 0.3:
                
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                #območje zaznanega mehurčka
                x_top = x*5
                y_top = y*5
                x_bottom = (x + w)*5
                y_bottom = (y + h)*5
                    
    return x_top,y_top,x_bottom,y_bottom
    