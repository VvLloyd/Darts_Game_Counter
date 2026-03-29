from tkinter import *

def endTurn(mainApp):
    if mainApp.match_inst.gameStarted == True:

        print(mainApp.match_inst.playerIndex)
        mainApp.button_endTurn.configure(state=DISABLED)

        n_players = mainApp.match_inst.getNplayer()

        # Current player (1-based index)
        current = mainApp.match_inst.playerIndex[0]

        # Compute next player (wrap automatically)
        next_player = current % n_players + 1

        # Update stored index
        mainApp.match_inst.playerIndex[0] = next_player

        # Update UI highlights
        mainApp.player_frames_list[current - 1].config(
            highlightbackground=mainApp.Button_bg_color
        )
        mainApp.player_frames_list[next_player - 1].config(
            highlightbackground=mainApp.currentplayer_color
        )

        mode = mainApp.match_inst.CommitGameMode[0]
        if mode == 1 or mode == 2:  # 301/501 mode

            # Handle double-in mode
            if mainApp.match_inst.doubleInMode:
                # Disable current player's checkbox
                mainApp.player_labels_dict[current]['doubleIn_checkbox'].config(state=DISABLED)

                # Enable next player's checkbox only if needed
                if not mainApp.player_labels_dict[next_player]['doubleIn_var'].get():
                    mainApp.player_labels_dict[next_player]['doubleIn_checkbox'].config(state=NORMAL)

        elif mode == 7: # Criquet mode

            for text in mainApp.open_button_texts:
                mainApp.player_buttons_dict[current]['buttons'][text].config(state=DISABLED)
                if text not in mainApp.dead_button_texts:
                    mainApp.player_buttons_dict[next_player]['buttons'][text].config(state=NORMAL)

        # If we wrapped around, increment turn
        if next_player == 1:
            mainApp.match_inst.currentGameTurn += 1

        # Cleanup score field for next player
        mainApp.input_Score.config(state='normal')
        mainApp.input_Score.delete(0, END)
        mainApp.input_Score.config(state=DISABLED)

        mainApp.button_endTurn.configure(state='normal')
        mainApp.updateIndexLog()
        mainApp.refreshImages()

    return