from tkinter import *
from PIL import ImageTk, Image

def refreshImages(mainApp):
    global logoImage

    mainApp.BackgroundFrame.grid(row=0, column=0, sticky=NSEW)
    logoImage = ImageTk.PhotoImage(Image.open("./data/images/dart_Logo2.sgi"))
    mainApp.logoImage = Label(mainApp.emptylabel_3, image=logoImage, bg=mainApp.Button_bg_color, fg="grey")
    mainApp.logoImage.grid(row=1, column=1, columnspan=2)

    return
