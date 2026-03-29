from tkinter import *


def clickPad(mainApp, number):

    if not mainApp.match_inst.gameStarted:
        return

    currentPlayer = mainApp.match_inst.playerIndex[0] - 1  # active player index

    mode = mainApp.match_inst.CommitGameMode[0]
    if mode == 1 or mode == 2: 
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

    elif mode == 7: # Criquet mode 

        # Convert bull
        if number == 'Bullseye':
            number_value = 25
        else:
            number_value = int(number)

        n_players = mainApp.match_inst.getNplayer()
        player_id = currentPlayer + 1

        # Mode detection
        if n_players == 3:
            mode = "cutthroat"
        elif n_players == 4:
            mode = "team"
        else:
            mode = "standard"

        # Define teams (only used in team mode)
        teams = {
            1: [1, 2],
            2: [3, 4]
        }

        def get_team(player):
            for team_id, members in teams.items():
                if player in members:
                    return team_id

        # Helper: count checks for ONE player
        def count_checks(player):
            return sum(
                1 for k in range(3)
                if mainApp.player_buttons_dict[player]['checkboxes'][number][str(k)].cget("text") == "✓"
            )

        # Helper: count checks for TEAM (sum of both players)
        def team_checks(team_id):
            return sum(count_checks(p) for p in teams[team_id])

        # 1Dead check
        if number in mainApp.dead_button_texts:
            return

        # Add mark if possible
        for k in range(3):
            box = mainApp.player_buttons_dict[player_id]['checkboxes'][number][str(k)]
            if box.cget("text") == ' ':
                box.config(state=NORMAL, text="✓")
                return

        # SCORING LOGIC

        if mode == "team":

            player_team = get_team(player_id)
            opponent_team = 1 if player_team == 2 else 2

            if team_checks(player_team) >= 3 and team_checks(opponent_team) < 3:

                # Add points to BOTH teammates (or shared score if you have one)
                for teammate in teams[player_team]:
                    score_entry = mainApp.player_labels_dict[teammate]['score']
                    current_score = int(score_entry.get())

                    score_entry.config(state=NORMAL)
                    score_entry.delete(0, END)
                    score_entry.insert(0, str(current_score + number_value))
                    score_entry.config(state=DISABLED)

        elif mode == "cutthroat":

            opponents_not_closed = [
                p for p in range(1, n_players + 1)
                if p != player_id and count_checks(p) < 3
            ]

            for opponent in opponents_not_closed:
                score_entry = mainApp.player_labels_dict[opponent]['score']
                current_score = int(score_entry.get())

                score_entry.config(state=NORMAL)
                score_entry.delete(0, END)
                score_entry.insert(0, str(current_score + number_value))
                score_entry.config(state=DISABLED)

        else:  # standard (2 players)

            opponent = 2 if player_id == 1 else 1

            if count_checks(player_id) >= 3 and count_checks(opponent) < 3:
                score_entry = mainApp.player_labels_dict[player_id]['score']
                current_score = int(score_entry.get())

                score_entry.config(state=NORMAL)
                score_entry.delete(0, END)
                score_entry.insert(0, str(current_score + number_value))
                score_entry.config(state=DISABLED)

        # 4️⃣ DEAD CHECK

        if mode == "team":
            if team_checks(1) >= 3 and team_checks(2) >= 3:
                mainApp.dead_button_texts.append(number)

        else:
            all_closed = all(count_checks(p) >= 3 for p in range(1, n_players + 1))
            if all_closed:
                mainApp.dead_button_texts.append(number)

        # Disable buttons if dead
        if number in mainApp.dead_button_texts:
            for p in range(1, n_players + 1):
                mainApp.player_buttons_dict[p]['buttons'][number].config(state=DISABLED)

       



