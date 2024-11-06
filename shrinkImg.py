import cv2
import matplotlib.pyplot as plt
import glob
import shutil
import numpy as np

jpgs=glob.glob("./images/*.jpg")

black_background = np.zeros((768, 1024, 3), dtype = np.uint8)
for jpg in jpgs:
    jpg=jpg.replace("\\","/")
    bg_img=black_background.copy()
    #bg_img=cv2.imread(bg_img)
    #cv2.imshow('black image',bg_img)
    #cv2.waitKey(0) 
    
    image = cv2.imread(jpg)
    # Create a new np array

    
    image = cv2.resize(image,(1024,576)) #from 1366x768 to 1024x576 (same ratio)

    #cv2.imshow('image',image)
    #cv2.imshow('black image',black_background)
    
    
    bg_img[96:672,0:1024]=image
    #cv2.imshow('merged',bg_img)
    
    cv2.waitKey(0) 



    short_file_name=jpg.split("/")[-1].split(".")[0]+"_shrink.jpg"
    cv2.imwrite('processed/'+short_file_name,bg_img)
    #cv2.imwrite(), image)
    

#image = cv2.imread("C:\Users\bryan_ni\Desktop\第二螢幕_票_檔期1016", 1)