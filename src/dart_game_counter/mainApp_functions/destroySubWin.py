from tkinter import *

def destroySubWin(mainApp):
    if mainApp.match_inst.gameStarted == False:
        if mainApp.match_inst.getNplayer() < 4:
            mainApp.button_addPlayer.configure(state='normal')

        mainApp.button_gameMode.config(state=NORMAL)
    elif mainApp.match_inst.gameStarted == True:
        mainApp.match_inst.editNameMode = False
        mainApp.button_editName.config(state='normal')

    mainApp.subWin.destroy()
    return
