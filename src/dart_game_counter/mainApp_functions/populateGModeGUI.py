from tkinter import *


def populateGModeGUI(mainApp, master):
    mainApp.button_addPlayer.config(state=DISABLED)
    mainApp.button_gameMode.config(state=DISABLED)

    mainApp.subWin = Tk()
    mainApp.subWin.eval('tk::PlaceWindow . center')
    mainApp.subWin.geometry("355x500")

    mode = mainApp.match_inst.CommitGameMode[0]  # Value between 1 and 7
    double_in = mainApp.match_inst.CommitGameMode[1]  # True or False
    double_out = mainApp.match_inst.CommitGameMode[2]  # True or False

    mainApp.subWin.emptylabel_0 = Label(mainApp.subWin, padx=20, pady=2, bg=mainApp.modeButton_bg_color)
    mainApp.subWin.emptylabel_1 = LabelFrame(mainApp.subWin, padx=20, pady=10, bg=mainApp.modeButton_bg_color,
                                           borderwidth=2)
    mainApp.subWin.emptylabel_2 = LabelFrame(mainApp.subWin, padx=20, pady=10, bg=mainApp.modeButton_bg_color,
                                           borderwidth=2)
    mainApp.subWin.emptylabel_3 = LabelFrame(mainApp.subWin, padx=20, pady=2, bg=mainApp.modeButton_bg_color)

    #----------------------------------------------------------------------------------------------------------------
    # Radiobuttons
    #----------------------------------------------------------------------------------------------------------------
    mainApp.subWin.mode_var = IntVar(mainApp.subWin)
    mainApp.subWin.mode1 = Radiobutton(mainApp.subWin.emptylabel_1, indicatoron=0, text="Standard: 301", font=(mainApp.font, 14), anchor='center',
                                          width=27, pady=5, bg=mainApp.Button_bg_color, activebackground=mainApp.activeButton_bg_color, selectcolor = mainApp.activeButton_bg_color,
                                          fg=mainApp.modeButton_ft_color, variable=mode, value=1, command=lambda: mainApp.selectedMode(1, double_in, double_out))

    mainApp.subWin.mode2 = Radiobutton(mainApp.subWin.emptylabel_1, indicatoron=0, text="Standard: 501", font=(mainApp.font, 14), anchor='center',
                                          width=27, pady=5, bg=mainApp.Button_bg_color, activebackground=mainApp.activeButton_bg_color, selectcolor = mainApp.activeButton_bg_color,
                                          fg=mainApp.modeButton_ft_color, variable=mode, value=2, command=lambda: mainApp.selectedMode(2, double_in, double_out))


    mainApp.subWin.DoubleInModeONVar = IntVar(mainApp.subWin)
    mainApp.subWin.DoubleInModeOFFVar = IntVar(mainApp.subWin)
    mainApp.subWin.DoubleIn_ON = Checkbutton(mainApp.subWin.emptylabel_1, indicatoron=0, onvalue=1, offvalue=0,
                                                variable=mainApp.subWin.DoubleInModeONVar,
                                                command=lambda: mainApp.checkChangedDoubleIn('ON'),
                                                width = 7, selectcolor = mainApp.activeButton_bg_color,
                                                bg=mainApp.modeButton_bg_color,
                                                text = "ON",
                                                fg=mainApp.modeButton_ft_color,
                                                activebackground=mainApp.activeButton_bg_color)
    mainApp.subWin.DoubleIn_OFF = Checkbutton(mainApp.subWin.emptylabel_1, indicatoron=0, onvalue=1, offvalue=0,
                                                 variable=mainApp.subWin.DoubleInModeOFFVar,
                                                 command=lambda: mainApp.checkChangedDoubleIn('OFF'),
                                                 width = 7, selectcolor = mainApp.activeButton_bg_color,
                                                 bg=mainApp.modeButton_bg_color,
                                                 text = "OFF",
                                                 fg=mainApp.modeButton_ft_color,
                                                 activebackground=mainApp.activeButton_bg_color)
    
    mainApp.subWin.DoubleOutModeONVar = IntVar(mainApp.subWin)
    mainApp.subWin.DoubleOutModeOFFVar = IntVar(mainApp.subWin)
    mainApp.subWin.DoubleOut_ON = Checkbutton(mainApp.subWin.emptylabel_1, indicatoron=0, onvalue=1, offvalue=0,
                                                variable=mainApp.subWin.DoubleOutModeONVar,
                                                command=lambda: mainApp.checkChangedDoubleOut('ON'),
                                                width = 7, selectcolor = mainApp.activeButton_bg_color,
                                                bg=mainApp.modeButton_bg_color,
                                                text = "ON",
                                                fg=mainApp.modeButton_ft_color,
                                                activebackground=mainApp.activeButton_bg_color)
    mainApp.subWin.DoubleOut_OFF = Checkbutton(mainApp.subWin.emptylabel_1, indicatoron=0, onvalue=1, offvalue=0,
                                                 variable=mainApp.subWin.DoubleOutModeOFFVar,
                                                 command=lambda: mainApp.checkChangedDoubleOut('OFF'),
                                                 width = 7, selectcolor = mainApp.activeButton_bg_color,
                                                 bg=mainApp.modeButton_bg_color,
                                                 text = "OFF",
                                                 fg=mainApp.modeButton_ft_color,
                                                 activebackground=mainApp.activeButton_bg_color)
    
    if (mode == 1 or mode == 2) and double_in == True:
        mainApp.subWin.DoubleIn_ON.select()
        mainApp.subWin.DoubleIn_OFF.deselect()
        mainApp.subWin.DoubleIn_ON.configure(fg='black')
        
    elif (mode == 1 or mode == 2) and double_in == False:
        mainApp.subWin.DoubleIn_OFF.select()
        mainApp.subWin.DoubleIn_ON.deselect()
        mainApp.subWin.DoubleIn_OFF.configure(fg='black')

    if (mode == 1 or mode == 2) and double_out == True:
        mainApp.subWin.DoubleOut_ON.select()
        mainApp.subWin.DoubleOut_OFF.deselect()
        mainApp.subWin.DoubleOut_ON.configure(fg='black')

    elif (mode == 1 or mode == 2) and double_out == False:
        mainApp.subWin.DoubleOut_OFF.select()
        mainApp.subWin.DoubleOut_ON.deselect()
        mainApp.subWin.DoubleOut_OFF.configure(fg='black')

    mainApp.subWin.DoubleInLabel = Entry(mainApp.subWin.emptylabel_1, bg=mainApp.modeButton_bg_color, fg="grey", width=15,
                                            font=(mainApp.font, 12), justify='right', disabledbackground=mainApp.modeButton_bg_color,
                                            disabledforeground= mainApp.disabledButton_ft_color, border=0)
    mainApp.subWin.DoubleInLabel.insert(0, "Double-In Mode: ")
    mainApp.subWin.DoubleInLabel.config(state=DISABLED)

    mainApp.subWin.DoubleOutLabel = Entry(mainApp.subWin.emptylabel_1, bg=mainApp.modeButton_bg_color, fg="grey", width=15,
                                            font=(mainApp.font, 12), justify='right', disabledbackground=mainApp.modeButton_bg_color,
                                            disabledforeground= mainApp.disabledButton_ft_color, border=0)
    mainApp.subWin.DoubleOutLabel.insert(0, "Double-Out Mode: ")
    mainApp.subWin.DoubleOutLabel.config(state=DISABLED)

    mainApp.subWin.mode3 = Radiobutton(mainApp.subWin.emptylabel_2, indicatoron=0, text="Around the Clock", font=(mainApp.font, 14),
                                          width=27, pady=5, bg=mainApp.modeButton_bg_color, activebackground=mainApp.activeButton_bg_color, selectcolor = mainApp.activeButton_bg_color,
                                          fg=mainApp.modeButton_ft_color, anchor="center", variable=mode, value=3, command=lambda: mainApp.selectedMode(3), state=DISABLED)

    mainApp.subWin.mode4 = Radiobutton(mainApp.subWin.emptylabel_2, indicatoron=0, text="180 Around the Clock", font=(mainApp.font, 14),
                                          width=27, pady=5, bg=mainApp.modeButton_bg_color, activebackground=mainApp.activeButton_bg_color, selectcolor = mainApp.activeButton_bg_color,
                                          fg=mainApp.modeButton_ft_color, anchor="center", variable=mode, value=4, command=lambda: mainApp.selectedMode(4), state=DISABLED)

    mainApp.subWin.mode5 = Radiobutton(mainApp.subWin.emptylabel_2, indicatoron=0, text="Baseball", font=(mainApp.font, 14),
                                          width=27, pady=5, bg=mainApp.modeButton_bg_color, activebackground=mainApp.activeButton_bg_color, selectcolor = mainApp.activeButton_bg_color,
                                          fg=mainApp.modeButton_ft_color, anchor="center", variable=mode, value=5, command=lambda: mainApp.selectedMode(5), state=DISABLED)

    mainApp.subWin.mode6 = Radiobutton(mainApp.subWin.emptylabel_2, indicatoron=0, text="Chase The Dragon", font=(mainApp.font, 14),
                                          width=27, pady=5, bg=mainApp.modeButton_bg_color, activebackground=mainApp.activeButton_bg_color, selectcolor = mainApp.activeButton_bg_color,
                                          fg=mainApp.modeButton_ft_color, anchor="center", variable=mode, value=6, command=lambda: mainApp.selectedMode(6), state=DISABLED)

    mainApp.subWin.mode7 = Radiobutton(mainApp.subWin.emptylabel_2, indicatoron=0, text="Cricket", font=(mainApp.font, 14),
                                          padx=5, pady=5, bg=mainApp.modeButton_bg_color, activebackground=mainApp.activeButton_bg_color, selectcolor = mainApp.activeButton_bg_color,
                                          fg=mainApp.modeButton_ft_color, anchor="center", variable=mode, value=7, command=lambda: mainApp.selectedMode(7))



    #----------------------------------------------------------------------------------------------------------------
    # Buttons
    #----------------------------------------------------------------------------------------------------------------
    mainApp.subWin.button_commitGameMode = Button(mainApp.subWin.emptylabel_3, text="Appliquer", padx=12, pady=5, anchor='center',
                                                     font=(mainApp.font, 14), bg=mainApp.modeButton_bg_color,
                                                     fg=mainApp.currentplayer_color, command=lambda: mainApp.commitGameMode(master), width=11,
                                                     activebackground=mainApp.activeButton_bg_color, state='disabled',
                                                     activeforeground=mainApp.activeButton_ft_color)

    mainApp.subWin.button_cancel = Button(mainApp.subWin.emptylabel_3, text="Annuler", padx=12, pady=5, anchor='center',
                                             font=(mainApp.font, 14), bg=mainApp.modeButton_bg_color,
                                             fg=mainApp.modeButton_ft_color, width=11,
                                             activebackground=mainApp.activeButton_bg_color,
                                             activeforeground=mainApp.activeButton_ft_color,
                                             command=lambda: mainApp.destroySubWin())

    mainApp.subWin.emptylabel_0.grid(row=1, column=1, sticky=NSEW)
    mainApp.subWin.emptylabel_1.grid(row=0, column=1, sticky=NSEW)
    mainApp.subWin.emptylabel_2.grid(row=1, column=1, sticky=NSEW)
    mainApp.subWin.emptylabel_3.grid(row=4, column=1, sticky=NSEW)

    mainApp.subWin.mode1.grid(row=0, column=0, sticky='ew', columnspan=3)
    mainApp.subWin.mode2.grid(row=1, column=0, sticky='ew',columnspan=3)
    mainApp.subWin.DoubleInLabel.grid(row=3, column=0, ipady=15)
    mainApp.subWin.DoubleIn_ON.grid(row=3, column=1, sticky=E)
    mainApp.subWin.DoubleIn_OFF.grid(row=3, column=2, sticky=W)
    mainApp.subWin.DoubleOutLabel.grid(row=4, column=0, ipady=15)
    mainApp.subWin.DoubleOut_ON.grid(row=4, column=1, sticky=E)
    mainApp.subWin.DoubleOut_OFF.grid(row=4, column=2, sticky=W)
    mainApp.subWin.mode3.grid(row=2, column=0, sticky='ew')
    mainApp.subWin.mode4.grid(row=3, column=0, sticky='ew')
    mainApp.subWin.mode5.grid(row=4, column=0, sticky='ew')
    mainApp.subWin.mode6.grid(row=5, column=0, sticky='ew')
    mainApp.subWin.mode7.grid(row=6, column=0, sticky='ew')

    mainApp.subWin.button_commitGameMode.grid(row=3, column=3, sticky=E)
    mainApp.subWin.button_cancel.grid(row=3, column=2, sticky=E)

    mainApp.subWin.wm_title("Sélectionner le Mode de Jeu")
    mainApp.subWin.configure(background=mainApp.Button_bg_color)
    mainApp.subWin.resizable(False, False)

    mainApp.subWin.bind("<Return>", lambda event: mainApp.commitGameMode())
    mainApp.selectedMode(mode, double_in=double_in, double_out=double_out)
    eval("mainApp.subWin.mode"+str(mode)+".select()")
    eval("mainApp.subWin.mode"+str(mode)+".configure(fg='black')")

    return


