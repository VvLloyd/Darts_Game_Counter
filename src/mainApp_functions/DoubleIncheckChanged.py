from tkinter import *

def DoubleIncheckChanged(mainApp):
    """
    Triggered when a Double In Checkbutton is clicked.
    Updates the player's doubleIn attribute, disables the checkbox,
    updates the score entry, and logs the turn.
    """
    if not mainApp.match_inst.doubleInMode:
        return  # safety check

    # Determine whose turn it is
    current_index = mainApp.match_inst.playerIndex[0] - 1  # Convert 1-based to 0-based index

    # Update the player's doubleIn attribute from the IntVar
    player = mainApp.match_inst.players[current_index]
    player.doubleInVal = mainApp.player_doubleIn_vars[current_index].get()

    # Disable the Checkbutton and the score Entry for this player
    checkbox_attr = mainApp.player_labels_dict[current_index + 1]['doubleIn_checkbox']  

    score_entry = mainApp.player_score_labels[current_index]

    checkbox_attr.config(state=DISABLED)
    score_entry.config(state=DISABLED, disabledforeground=mainApp.currentplayer_color)

    # Optional: update any logs or turn tracking
    mainApp.updateIndexLog()
