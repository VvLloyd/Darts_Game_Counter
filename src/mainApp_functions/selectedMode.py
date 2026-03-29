from tkinter import *

def selectedMode(mainApp, sel_mode, double_in, double_out):
    selection = sel_mode
    prevCommittedMode = mainApp.match_inst.CommitGameMode[:1]
    prevCommittedDounleInMode = mainApp.match_inst.CommitGameMode[1:]

    mainApp.subWin.DoubleIn_ON.configure(state='disabled')
    mainApp.subWin.DoubleIn_OFF.configure(state='disabled')
    mainApp.subWin.DoubleOut_ON.configure(state='disabled')
    mainApp.subWin.DoubleOut_OFF.configure(state='disabled')

    if selection == 1:
        mainApp.match_inst.SelectedGameMode = 1
        mainApp.subWin.mode1.configure(fg='black')
        eval("mainApp.subWin.mode"+str(mainApp.match_inst.prevSelGameMode)+".configure(fg=mainApp.Button_ft_color)")
        mainApp.match_inst.prevSelGameMode = 1
        
        mainApp.subWin.DoubleIn_ON.configure(state='normal')
        mainApp.subWin.DoubleIn_OFF.configure(state='normal')
        mainApp.subWin.DoubleOut_ON.configure(state='normal')
        mainApp.subWin.DoubleOut_OFF.configure(state='normal')
        
        if selection != prevCommittedMode[0] or prevCommittedDounleInMode[0] != mainApp.match_inst.doubleInMode:
            mainApp.subWin.button_commitGameMode.config(state='normal')
        else:
            mainApp.subWin.button_commitGameMode.config(state='disabled')


    elif selection == 2:
        mainApp.match_inst.SelectedGameMode = 2
        mainApp.subWin.mode2.configure(fg='black')
        eval("mainApp.subWin.mode"+str(mainApp.match_inst.prevSelGameMode)+".configure(fg=mainApp.Button_ft_color)")
        mainApp.match_inst.prevSelGameMode = 2
        
        mainApp.subWin.DoubleIn_ON.configure(state='normal')
        mainApp.subWin.DoubleIn_OFF.configure(state='normal')
        mainApp.subWin.DoubleOut_ON.configure(state='normal')
        mainApp.subWin.DoubleOut_OFF.configure(state='normal')        
        
        if selection != prevCommittedMode[0] or prevCommittedDounleInMode[0] != mainApp.match_inst.doubleInMode:
            mainApp.subWin.button_commitGameMode.config(state='normal')
        else:
            mainApp.subWin.button_commitGameMode.config(state='disabled')        


    elif selection == 3:
        mainApp.match_inst.SelectedGameMode = 3
        mainApp.subWin.mode3.configure(fg='black')
        eval("mainApp.subWin.mode"+str(mainApp.match_inst.prevSelGameMode)+".configure(fg=mainApp.Button_ft_color)")
        mainApp.match_inst.prevSelGameMode = 3
        
        mainApp.subWin.DoubleIn_ON.configure(state='disabled')
        mainApp.subWin.DoubleIn_OFF.configure(state='disabled')
        mainApp.subWin.DoubleOut_ON.configure(state='disabled')
        mainApp.subWin.DoubleOut_OFF.configure(state='disabled')
        
        if selection != prevCommittedMode[0] or prevCommittedDounleInMode[0] != mainApp.match_inst.doubleInMode:
            mainApp.subWin.button_commitGameMode.config(state='normal')
        else:
            mainApp.subWin.button_commitGameMode.config(state='disabled')

    elif selection == 4:
        mainApp.match_inst.SelectedGameMode = 4
        mainApp.subWin.mode4.configure(fg='black')
        eval("mainApp.subWin.mode"+str(mainApp.match_inst.prevSelGameMode)+".configure(fg=mainApp.Button_ft_color)")
        mainApp.match_inst.prevSelGameMode = 4
        
        mainApp.subWin.DoubleIn_ON.configure(state='disabled')
        mainApp.subWin.DoubleIn_OFF.configure(state='disabled')
        mainApp.subWin.DoubleOut_ON.configure(state='disabled')
        mainApp.subWin.DoubleOut_OFF.configure(state='disabled')    
                
        if selection != prevCommittedMode[0] or prevCommittedDounleInMode[0] != mainApp.match_inst.doubleInMode:
            mainApp.subWin.button_commitGameMode.config(state='normal')
        else:
            mainApp.subWin.button_commitGameMode.config(state='disabled')

    elif selection == 5:
        mainApp.match_inst.SelectedGameMode = 5
        mainApp.subWin.mode5.configure(fg='black')
        eval("mainApp.subWin.mode"+str(mainApp.match_inst.prevSelGameMode)+".configure(fg=mainApp.Button_ft_color)")
        mainApp.match_inst.prevSelGameMode = 5
        
        mainApp.subWin.DoubleIn_ON.configure(state='disabled')
        mainApp.subWin.DoubleIn_OFF.configure(state='disabled')
        mainApp.subWin.DoubleOut_ON.configure(state='disabled')
        mainApp.subWin.DoubleOut_OFF.configure(state='disabled')
        
        if selection != prevCommittedMode[0] or prevCommittedDounleInMode[0] != mainApp.match_inst.doubleInMode:
            mainApp.subWin.button_commitGameMode.config(state='normal')
        else:
            mainApp.subWin.button_commitGameMode.config(state='disabled')

    elif selection == 6:
        mainApp.match_inst.SelectedGameMode = 6
        mainApp.subWin.mode6.configure(fg='black')
        eval("mainApp.subWin.mode"+str(mainApp.match_inst.prevSelGameMode)+".configure(fg=mainApp.Button_ft_color)")
        mainApp.match_inst.prevSelGameMode = 6

        mainApp.subWin.DoubleIn_ON.configure(state='disabled')
        mainApp.subWin.DoubleIn_OFF.configure(state='disabled')
        mainApp.subWin.DoubleOut_ON.configure(state='disabled')
        mainApp.subWin.DoubleOut_OFF.configure(state='disabled')

        if selection != prevCommittedMode[0] or prevCommittedDounleInMode[0] != mainApp.match_inst.doubleInMode:
            mainApp.subWin.button_commitGameMode.config(state='normal')
        else:
            mainApp.subWin.button_commitGameMode.config(state='disabled')

    elif selection == 7:
        mainApp.match_inst.SelectedGameMode = 7
        mainApp.subWin.mode7.configure(fg='black')
        eval("mainApp.subWin.mode"+str(mainApp.match_inst.prevSelGameMode)+".configure(fg=mainApp.Button_ft_color)")
        mainApp.match_inst.prevSelGameMode = 7

        mainApp.subWin.DoubleIn_ON.configure(state='disabled')
        mainApp.subWin.DoubleIn_OFF.configure(state='disabled')
        mainApp.subWin.DoubleOut_ON.configure(state='disabled')
        mainApp.subWin.DoubleOut_OFF.configure(state='disabled')

        if selection != prevCommittedMode[0] or prevCommittedDounleInMode[0] != mainApp.match_inst.doubleInMode:
            mainApp.subWin.button_commitGameMode.config(state='normal')
        else:
            mainApp.subWin.button_commitGameMode.config(state='disabled')

        mainApp.match_inst.doubleInMode = False

    if (selection == 1 or selection == 2) and double_in == True:
        mainApp.subWin.DoubleIn_ON.select()
        mainApp.subWin.DoubleIn_OFF.deselect()
        mainApp.subWin.DoubleIn_ON.configure(fg='black')
        mainApp.subWin.DoubleIn_OFF.configure(fg=mainApp.Button_ft_color)
    else:
        mainApp.subWin.DoubleIn_OFF.select()
        mainApp.subWin.DoubleIn_ON.deselect()
        mainApp.subWin.DoubleIn_OFF.configure(fg='black') 
        mainApp.subWin.DoubleIn_ON.configure(fg=mainApp.Button_ft_color)

    if (selection == 1 or selection == 2) and double_out == True:
        mainApp.subWin.DoubleOut_ON.select()
        mainApp.subWin.DoubleOut_OFF.deselect()
        mainApp.subWin.DoubleOut_ON.configure(fg='black')
        mainApp.subWin.DoubleOut_OFF.configure(fg=mainApp.Button_ft_color)
    else:
        mainApp.subWin.DoubleOut_OFF.select()
        mainApp.subWin.DoubleOut_ON.deselect()
        mainApp.subWin.DoubleOut_OFF.configure(fg='black') 
        mainApp.subWin.DoubleOut_ON.configure(fg=mainApp.Button_ft_color)
        
    concoleMsg = "You selected the option " + str(mainApp.match_inst.SelectedGameMode)
    print(concoleMsg)

    return
