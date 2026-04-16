from tkinter import *


def updateStatusLabel(mainApp, text):
    mainApp.StatusLabel.destroy()
    mainApp.StatusLabel = Label(mainApp.emptylabel0, padx=1, pady=20, text=text, font=(mainApp.font, 12),
                                   bg=mainApp.Button_bg_color, fg=mainApp.Button_status_ft_color)
    mainApp.StatusLabel.grid(row=0, column=0, columnspan=1)
    return
