from tkinter import *
from classes.Player import Player


def commitAddPlayer(mainApp):
    playerName = mainApp.subWin.input_Name.get().strip()

    if not playerName:
        mainApp.subWin.errorStatus.configure(text="Vous devez entrer un nom...")
        return

    # --------------------------------------------------
    # BEFORE GAME START
    # --------------------------------------------------
    if not mainApp.match_inst.gameStarted:

        mainApp.button_gameStart.configure(state="normal", fg="#60ff30")

        status_messages = [
            "Ajouter un deuxième joueur OU Cliquer Démarrer Partie!",
            "Ajouter un troisième joueur OU Cliquer Démarrer Partie!",
            "Ajouter un quatrième joueur OU Cliquer Démarrer Partie!",
            "Cliquer Démarrer Partie!"
        ]

        player_index = mainApp.match_inst.getNplayer()  # 0-based

        # Get widgets safely from lists
        label = mainApp.player_name_labels[player_index]
        frame = mainApp.player_frames_list[player_index]

        # Update UI
        label.config(state=NORMAL)
        label.delete(0, END)
        label.insert(0, playerName)
        label.config(state=DISABLED, disabledforeground=mainApp.currentplayer_color)

        frame.config(relief="raised")

        # Update match model
        mainApp.match_inst.addNplayer()

        new_count = mainApp.match_inst.getNplayer()
        mainApp.updateStatusLabel(status_messages[new_count - 1])

        # Create player correctly
        new_player = Player(playerName)
        mainApp.match_inst.addPlayer(new_player)

        mainApp.refreshImages()

    # --------------------------------------------------
    # EDIT NAME MODE (GAME ALREADY STARTED)
    # --------------------------------------------------
    else:
        currentPlayer = mainApp.match_inst.playerIndex[0] - 1

        mainApp.match_inst.players[currentPlayer].name = playerName

        label = mainApp.player_name_labels[currentPlayer]

        label.config(state=NORMAL)
        label.delete(0, END)
        label.insert(0, playerName)
        label.config(state=DISABLED)

        mainApp.button_commitScore.configure(state="disabled")
        mainApp.button_editName.configure(state="normal")

        def get_team_color(player_id, n_players):
            if n_players != 4:
                return mainApp.currentplayer_color
            if player_id in [0, 1]:
                return mainApp.team_1_color
            else:
                return mainApp.team_2_color
        
        n_players = mainApp.match_inst.getNplayer()           
        if n_players >= 4 :
            for i in range(n_players):

                # Update UI   
                name_entry = mainApp.player_name_labels[i]
                name_entry.config(state=NORMAL , fg=get_team_color(i, n_players))

        if mainApp.match_inst.editNameMode == True:
            mainApp.updateIndexLog(log_setting_change="edit_name") 

    mainApp.destroySubWin()