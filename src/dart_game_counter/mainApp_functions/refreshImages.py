from tkinter import *
from PIL import ImageTk, Image

def refreshImages(mainApp):
    global logoImage

    '''
    mainApp.BackgroundFrame.grid(row=0, column=0, sticky=NSEW)
    logoImage = ImageTk.PhotoImage(Image.open("./data/images/dart_Logo2.sgi"))
    mainApp.logoImage = Label(mainApp.emptylabel_3, image=logoImage, bg=mainApp.Button_bg_color, fg="grey")
    mainApp.logoImage.grid(row=1, column=1, columnspan=2)
    '''
    
    # Load image
    img = Image.open("./data/images/dart_Logo4.sgi")

    # Resize it (width, height)
    img = img.resize((250, 250), Image.LANCZOS)  # high-quality downsampling

    # Convert to Tkinter image
    logoImage = ImageTk.PhotoImage(img)

    # Keep a reference!
    mainApp.logoImage = logoImage

    # Create label
    label = Label(mainApp.emptylabel_3, image=logoImage, bg=mainApp.Button_bg_color)
    label.grid(row=1, column=2, columnspan=3)

    return
