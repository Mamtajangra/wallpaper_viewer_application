## import libraries

from tkinter import *
from PIL import ImageTk,Image 
import os

## to rotate the image from last to first
def rotate_img():
    global counter
    img_label.config(image = img_arr[counter%len(img_arr)])
    counter += 1

counter = 1

root= Tk()  

## title of thee ui
root.title("Wallpaper viewer")
root.geometry('500x500')
root.configure(bg = "black")
  
  ## images is in list
files = os.listdir("wallpaper")


## create an empty array to store all images with perfect size in this array
img_arr = []
for file in files:
    img = Image.open(os.path.join("wallpaper",file))
    resized_img = img.resize((400,400))
    img_arr.append(ImageTk.PhotoImage(resized_img))


img_label = Label(root,image = img_arr[0])
img_label.pack(pady =(15,10))

## apply next button to move move photos with background colour,height and call the rotate img function to move phots
next_btn = Button(root,text= "Next",fg = "black",bg = "white",width = 25,height = 3,command = rotate_img)
next_btn.pack()


root.mainloop()