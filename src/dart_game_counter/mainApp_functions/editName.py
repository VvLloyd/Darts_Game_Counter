from tkinter import *

def editName(mainApp):
    if mainApp.match_inst.gameStarted:
        mainApp.button_editName.config(state='disabled')
        mainApp.match_inst.editNameMode = True
        mainApp.addPlayer()        
    return
