import matplotlib.pyplot as plt
import cv2 #used to display image in window
import easygui #easy to use interface for user having no knowledge of programming
import imageio # read and write a range of images
import numpy as np #used to store image in the form of number 
import sys
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

top=tk.Tk()
top.geometry('500x500')
top.title("Let's Have Fun, Cartoonify your image")
top.configure(background='white')
label=Label(top,background='#CDCDCD', font=('calibri',20,'italic'))

def upload():
    ImagePath=easygui.fileopenbox()
    cartoonify(ImagePath)


def cartoonify(ImagePath):
    # read the image
    originalmage = cv2.imread(ImagePath)
    originalmage = cv2.cvtColor(originalmage, cv2.COLOR_BGR2RGB)


    ReSized1 = cv2.resize(originalmage, (500, 500))
    plt.imshow(ReSized1, cmap='gray')


    #converting an image to grayscale
    grayScaleImage= cv2.cvtColor(originalmage, cv2.COLOR_BGR2GRAY)
    ReSized2 = cv2.resize(grayScaleImage, (500, 500))
    plt.imshow(ReSized2, cmap='gray')


    #applying median blur to smoothen an image
    smoothGrayScale = cv2.medianBlur(grayScaleImage, 5)
    ReSized3 = cv2.resize(smoothGrayScale, (500, 540))
    plt.imshow(ReSized3, cmap='gray')

    
    getEdge = cv2.adaptiveThreshold(smoothGrayScale, 400, 
        cv2.ADAPTIVE_THRESH_MEAN_C, 
        cv2.THRESH_BINARY, 9, 9)

    ReSized4 = cv2.resize(getEdge, (500, 500))
    
    
    colorImage = cv2.bilateralFilter(originalmage, 9, 400, 400)
    ReSized5 = cv2.resize(colorImage, (500, 500))
    plt.imshow(ReSized5, cmap='gray')


    #masking edged image with our "BEAUTIFY" image
    cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=getEdge)

    ReSized6 = cv2.resize(cartoonImage, (500, 500))
    #plt.imshow(ReSized6, cmap='gray')

    # Plotting the whole transition
    images=[ReSized1, ReSized2, ReSized3, ReSized4, ReSized5, ReSized6]

    fig, axes = plt.subplots(3,2, figsize=(8,8), subplot_kw={'xticks':[], 'yticks':[]}, gridspec_kw=dict(hspace=0.1, wspace=0.1))
    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap='gray')

    save1=Button(top,text="Download Cartoonified image",command=lambda: save(ReSized4, ImagePath),padx=30,pady=5)
    save1.configure(background='#364156', foreground='white',font=('calibri',12,'italic'))
    save1.pack(side=TOP,pady=50)
    
    plt.show()
    
    
def save(ReSized4, ImagePath):
    #saving an image using imwrite()
    newName="Cartoonified"
    path1 = os.path.dirname(ImagePath)
    extension=os.path.splitext(ImagePath)[1]
    path = os.path.join(path1, newName+extension)
    cv2.imwrite(path, cv2.cvtColor(ReSized4, cv2.COLOR_RGB2BGR))
    I= "Image saved by name " + newName +" at "+ path
    tk.messagebox.showinfo(title="Congratulations!", message="Image is Downloaded successfully")

upload=Button(top,text="Cartoonify an Image",command=upload,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('calibri',12,'italic'))
upload.pack(side=TOP,pady=50)

top.mainloop()



