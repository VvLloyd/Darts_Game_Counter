from tkinter import *

def checkChangedDoubleOut(mainApp,buttonPressed):

    selectedMode = mainApp.subWin.mode_var.get()
    prevCommittedMode = mainApp.match_inst.CommitGameMode[:1]
    prevCommittedDoubleOutMode = mainApp.match_inst.CommitGameMode[2:]

    if buttonPressed == "ON":
        mainApp.match_inst.doublOutMode = True
        mainApp.subWin.DoubleOut_ON.configure(fg='black')
        mainApp.subWin.DoubleOut_OFF.configure(fg=mainApp.Button_ft_color)
        mainApp.subWin.DoubleOutModeONVar.set(1)
        mainApp.subWin.DoubleOutModeOFFVar.set(0)

    elif buttonPressed == "OFF":
        mainApp.match_inst.doubleOutMode = False
        mainApp.subWin.DoubleOut_OFF.configure(fg='black')
        mainApp.subWin.DoubleOut_ON.configure(fg=mainApp.Button_ft_color)
        mainApp.subWin.DoubleOutModeONVar.set(0)
        mainApp.subWin.DoubleOutModeOFFVar.set(1)

    if prevCommittedDoubleOutMode[0] != mainApp.match_inst.doubleOutMode and selectedMode != prevCommittedMode[0]:
        mainApp.subWin.button_commitGameMode.config(state='normal')
    elif prevCommittedDoubleOutMode[0] != mainApp.match_inst.doubleOutMode and selectedMode == prevCommittedMode[0]:
        mainApp.subWin.button_commitGameMode.config(state='normal')
    elif prevCommittedDoubleOutMode[0] == mainApp.match_inst.doubleOutMode and selectedMode == prevCommittedMode[0]:
        mainApp.subWin.button_commitGameMode.config(state='disabled')

    return
