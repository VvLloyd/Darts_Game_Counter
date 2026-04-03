from tkinter import *


def updateStatusLabel(mainApp, text):
    mainApp.StatusLabel.destroy()
    mainApp.StatusLabel = Label(mainApp.emptylabel0, padx=1, pady=20, text=text, font=("Helvetica", 12),
                                   bg=mainApp.Button_bg_color, fg="cyan")
    mainApp.StatusLabel.grid(row=0, column=0, columnspan=1)
    return
