from tkinter import *

def addPlayer(mainApp):

    # Disable mainApp button
    mainApp.button_addPlayer.config(state=DISABLED)
    mainApp.button_gameMode.config(state=DISABLED)

    # Create another window (sub-window attached to mainApp)
    mainApp.subWin = Tk()
    mainApp.subWin.eval('tk::PlaceWindow . center')

    # Distinguishing if editing the name or adding a new player...
    if mainApp.match_inst.editNameMode == True:
        currentPlayer = mainApp.match_inst.playerIndex[0] # active player index        
    elif mainApp.match_inst.editNameMode == False:
        currentPlayer = mainApp.match_inst.getNplayer() + 1

    # Populate all sub-GUI widgets
    mainApp.subWin.emptylabel_1 = Label(mainApp.subWin, padx=10, pady=10, bg=mainApp.Button_bg_color)
    mainApp.subWin.emptylabel_2 = Label(mainApp.subWin, padx=10, pady=2, bg=mainApp.Button_bg_color)
    mainApp.subWin.emptylabel_3 = Label(mainApp.subWin, text="Entrer le Nom du Joueur #%s" % (currentPlayer),
                                           font=("Helvetica", 12), bg=mainApp.Button_bg_color,
                                           fg=mainApp.Button_ft_color)

    mainApp.subWin.errorStatus = Label(mainApp.subWin, text="", bg=mainApp.Button_bg_color, fg="cyan")
    mainApp.subWin.input_Name = Entry(mainApp.subWin, width=20, bg='black', fg=mainApp.currentplayer_color, borderwidth=3,
                                         font=("Helvetica", 16), justify='center')

    mainApp.subWin.button_commitAddPlayer = Button(mainApp.subWin, text="Enregistrer", padx=10, pady=5,
                                                      font=("Helvetica", 12), bg=mainApp.Button_bg_color,
                                                      fg=mainApp.currentplayer_color, command=mainApp.commitAddPlayer,
                                                      activebackground=mainApp.activeButton_bg_color,
                                                      activeforeground=mainApp.activeButton_ft_color)

    mainApp.subWin.button_cancel = Button(mainApp.subWin, text="Annuler", padx=10, pady=5,
                                             font=("Helvetica", 12), bg=mainApp.Button_bg_color,
                                             fg=mainApp.Button_ft_color,
                                             activebackground=mainApp.activeButton_bg_color,
                                             activeforeground=mainApp.activeButton_ft_color,
                                             command=lambda: mainApp.destroySubWin())

    mainApp.subWin.emptylabel_1.grid(row=0, column=0, columnspan=4)
    mainApp.subWin.emptylabel_2.grid(row=4, column=0, columnspan=4)
    mainApp.subWin.emptylabel_3.grid(row=1, column=0, columnspan=1, padx=50, pady=10)
    mainApp.subWin.errorStatus.grid(row=2, column=1, columnspan=1, padx=1, pady=10, sticky="n")
    mainApp.subWin.input_Name.grid(row=1, column=1, columnspan=1)
    mainApp.subWin.button_commitAddPlayer.grid(row=3, column=1, columnspan=1)
    mainApp.subWin.button_cancel.grid(row=3, column=0, columnspan=1)

    mainApp.subWin.wm_title("Ajouter Joueur #%s" % (currentPlayer))
    mainApp.subWin.configure(background=mainApp.Button_bg_color)
    mainApp.subWin.resizable(False, False)

    mainApp.subWin.bind("<Return>", lambda event: mainApp.commitAddPlayer())
    mainApp.subWin.after(1, lambda: mainApp.subWin.input_Name.focus_force()) 
    

    return
