from tkinter import *

def checkChangedDoubleIn(mainApp,buttonPressed):

    selectedMode = mainApp.subWin.mode_var.get()
    prevCommittedMode = mainApp.match_inst.CommitGameMode[:1]
    prevCommittedDoubleInMode = mainApp.match_inst.CommitGameMode[1:]

    if buttonPressed == "ON":
        mainApp.match_inst.doubleInMode = True
        mainApp.subWin.DoubleIn_ON.configure(fg='black')
        mainApp.subWin.DoubleIn_OFF.configure(fg=mainApp.Button_ft_color)
        mainApp.subWin.DoubleInModeONVar.set(1)
        mainApp.subWin.DoubleInModeOFFVar.set(0)

    elif buttonPressed == "OFF":
        mainApp.match_inst.doubleInMode = False
        mainApp.subWin.DoubleIn_OFF.configure(fg='black')
        mainApp.subWin.DoubleIn_ON.configure(fg=mainApp.Button_ft_color)
        mainApp.subWin.DoubleInModeONVar.set(0)
        mainApp.subWin.DoubleInModeOFFVar.set(1)

    if prevCommittedDoubleInMode[0] != mainApp.match_inst.doubleInMode and selectedMode != prevCommittedMode[0]:
        mainApp.subWin.button_commitGameMode.config(state='normal')
    elif prevCommittedDoubleInMode[0] != mainApp.match_inst.doubleInMode and selectedMode == prevCommittedMode[0]:
        mainApp.subWin.button_commitGameMode.config(state='normal')
    elif prevCommittedDoubleInMode[0] == mainApp.match_inst.doubleInMode and selectedMode == prevCommittedMode[0]:
        mainApp.subWin.button_commitGameMode.config(state='disabled')

    return
