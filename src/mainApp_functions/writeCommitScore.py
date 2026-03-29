from tkinter import *

def writeCommitScore(mainApp):
    # get Current Player turn over the total nb of player
    scoreToInput = mainApp.input_Score.get()
    if scoreToInput != '':
        scoreToInput = int(mainApp.input_Score.get())
        currentPlayer = mainApp.match_inst.playerIndex[:1]
        mainApp.input_Score.config(state=NORMAL)
        mainApp.input_Score.delete(0, END)
        mainApp.input_Score.config(state=DISABLED)

        currentPlayerScore = mainApp.player_labels_dict[currentPlayer[0]]['score'].get()

        if int(currentPlayerScore) >= int(scoreToInput):
            mainApp.player_labels_dict[currentPlayer[0]]['score'].config(state=NORMAL)
            mainApp.player_labels_dict[currentPlayer[0]]['score'].delete(0, END)
            mainApp.player_labels_dict[currentPlayer[0]]['score'].insert(0, str(int(currentPlayerScore) - scoreToInput))
            mainApp.player_labels_dict[currentPlayer[0]]['score'].config(state=DISABLED)

        mainApp.button_commitScore.configure(state=DISABLED)
    return
