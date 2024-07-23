"""
Création des séquences pour ImageJ à partir des vidéos .MOV obtenues
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
import os
import glob


Path =""
files = glob.glob(Path+"DSC_7089.MOV")


def getFrame(vidcap0,sec, path, count):
    vidcap0.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap0.read()
    if hasFrames:
        cv2.imwrite(os.path.join(path , "image"+str(count)+".png"), image)
    return hasFrames




for file in files: 
    vidcap0 = cv2.VideoCapture(file)
    savePath = file[:-4]+"/"
    print(savePath)
    try : 
        os.mkdir(savePath)
    except:
        print(savePath + " already exists")
    sec = 0
    frameRate = 0.5  #prends une image toutes les 0.5 secondes
    count=0
    success = getFrame(vidcap0,sec, savePath, count)

    while success:
            sec = sec + frameRate
            success = getFrame(vidcap0,sec, savePath, count)
            count = count + 1
        
    
    
