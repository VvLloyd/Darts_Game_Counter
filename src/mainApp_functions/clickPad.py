from tkinter import *


def clickPad(mainApp, number):

    if not mainApp.match_inst.gameStarted:
        return

    currentPlayer = mainApp.match_inst.playerIndex[0] - 1  # active player index

    # -----------------------------------------
    # Double In Check
    # -----------------------------------------
    if mainApp.match_inst.doubleInMode:
        DoubleInStatus = mainApp.player_doubleIn_vars[currentPlayer].get()
    else:
        DoubleInStatus = False

    if not DoubleInStatus and mainApp.match_inst.doubleInMode:
        return

    # -----------------------------------------
    # DELETE LAST DIGIT
    # -----------------------------------------
    if number == -1:
        current = mainApp.input_Score.get()
        if len(current) > 0:
            mainApp.input_Score.config(state="normal")
            mainApp.input_Score.delete(len(current) - 1, END)
            mainApp.input_Score.config(state=DISABLED)
        return

    # -----------------------------------------
    # NORMAL SCORE ENTRY MODE
    # -----------------------------------------
    if not mainApp.match_inst.editScoreMode:

        current = mainApp.input_Score.get()

        if len(current) < 3:
            mainApp.input_Score.config(state="normal")
            mainApp.input_Score.delete(0, END)
            mainApp.input_Score.insert(0, current + str(number))
            mainApp.input_Score.config(state=DISABLED)

        newCurrent = mainApp.input_Score.get()

        if len(newCurrent) > 0:
            mainApp.button_commitScore.configure(state="normal")
        else:
            mainApp.button_commitScore.configure(state=DISABLED)

    # -----------------------------------------
    # EDIT SCORE MODE
    # -----------------------------------------
    else:
        score_label = mainApp.player_score_labels[currentPlayer]

        currentScore = score_label.get()

        if len(currentScore) < 3:
            score_label.config(state="normal")
            score_label.delete(0, END)
            score_label.insert(0, currentScore + str(number))
            score_label.config(state=DISABLED)

        newCurrentScore = score_label.get()

        if len(newCurrentScore) > 0:
            mainApp.button_commitScore.configure(state=NORMAL)
        else:
            mainApp.button_commitScore.configure(state=DISABLED)   
                