from tkinter import *


def startGame(mainApp):
    if ~mainApp.match_inst.gameStarted:
        mainApp.button_gameStart.configure(state=DISABLED, disabledforeground=mainApp.Button_bg_color)
        mainApp.button_gameStart.destroy()
        mainApp.frame9.destroy()

        mainApp.button_addPlayer.configure(state=DISABLED)
        mainApp.button_gameMode.config(state=DISABLED)

        n_players = mainApp.match_inst.getNplayer()

        if n_players != 0 and not mainApp.match_inst.doubleInMode:
            for i in range(n_players):
                mainApp.player_score_labels[i].config(
                    state=DISABLED,
                    disabledforeground=mainApp.currentplayer_color
                )   

    mode = mainApp.match_inst.CommitGameMode[0]

    if mode == 1 or mode == 2:
        if mainApp.match_inst.doubleInMode == True:
            mainApp.player_labels_dict[1]['doubleIn_checkbox'].config(state=NORMAL)

    if mode == 7: # Activate Criquet mode features
        texts = ["Bullseye", "20", "19", "18", "17", "16", "15"]           
        for text in texts:
            mainApp.player_buttons_dict[1]['buttons'][text].config(state=NORMAL)

        def get_team_color(player_id, n_players):
            if n_players != 4:
                return mainApp.currentplayer_color
            if player_id in [0, 1]:
                return mainApp.team_1_color
            else:
                return mainApp.team_2_color
            
        if n_players >= 4 :
            for i in range(n_players):

                # Update UI   
                name_entry = mainApp.player_name_labels[i]
                name_entry.config(state=NORMAL , fg=get_team_color(i, n_players))


    mainApp.match_inst.playerIndex = [1, mainApp.match_inst.getNplayer()]
    mainApp.updateIndexLog() 

    mainApp.match_inst.gameStarted = True
    mainApp.match_inst.currentGameTurn = 1

    mainApp.button_editScore.configure(state='normal')
    mainApp.button_editName.configure(state='normal')
    mainApp.button_endTurn.configure(state='normal')
    mainApp.player_frames_list[0].config(highlightbackground=mainApp.currentplayer_color)
    mainApp.refreshImages()
    mainApp.updateStatusLabel("La Partie est commencée!")

    return
