from tkinter import *

def writeCommitScore(mainApp, number='', player_id=None, event=None):

    mode = mainApp.match_inst.CommitGameMode[0]   
    
    if mode == 1 or mode == 2: 

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

    elif mode == 7: # Criquet mode 

        ctrl_pressed = False
        if event is not None:
            ctrl_pressed = (event.state & 0x4) != 0

        if player_id is None:
            currentPlayer = mainApp.match_inst.playerIndex[0] - 1
            player_id = currentPlayer + 1

        # Because of the binding of buttons with an event, must cancel the 
        # command of the button of another player has been pressed.
        if mainApp.match_inst.playerIndex[0] != player_id:  # active player index
            return

        # Convert bull
        if number == 'Bullseye':
            number_value = 25
        else:
            number_value = int(number)

        n_players = mainApp.match_inst.getNplayer()
        #player_id = currentPlayer + 1

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
        

        def update_checkbox_colors(n_players, number):
            for p in range(1, n_players + 1):
                closed = count_checks(p) >= 3

                for k in range(3):
                    cb = mainApp.player_buttons_dict[p]['checkboxes'][number][str(k)]

                    if number in mainApp.dead_button_texts:
                        cb.config(state=DISABLED, fg="gray")
                    else:
                        cb.config(state=NORMAL)
                        if closed:
                            cb.config(fg=mainApp.checkbox_fg_color2)
                        else:
                            cb.config(fg=mainApp.checkbox_fg_color1)
        

        def dead_check(n_players, mode):  # DEAD CHECK
            if mode == "team":
                if team_checks(1) >= 3 and team_checks(2) >= 3:
                    if number not in mainApp.dead_button_texts:
                        mainApp.dead_button_texts.append(number)
            else:
                all_closed = all(count_checks(p) >= 3 for p in range(1, n_players + 1))
                if all_closed:
                    if number not in mainApp.dead_button_texts:
                        mainApp.dead_button_texts.append(number)

            # Disable buttons + checkboxes if dead
            if number in mainApp.dead_button_texts:
                for p in range(1, n_players + 1):
                    mainApp.player_buttons_dict[p]['buttons'][number].config(state=DISABLED)

                    for k in range(3):
                        cb = mainApp.player_buttons_dict[p]['checkboxes'][number][str(k)]
                        cb.config(state=DISABLED, fg="gray")

            # Always refresh colors
            update_checkbox_colors(n_players, number)

        # 1Dead check
        if number in mainApp.dead_button_texts:
            return
        
        # CTRL = REMOVE last check
        if ctrl_pressed:
            for k in reversed(range(3)):  # remove last checked
                box = mainApp.player_buttons_dict[player_id]['checkboxes'][number][str(k)]
                if box.cget("text") == "✓":
                    box.config(text=" ")

                    update_checkbox_colors(n_players, number)
                    dead_check(n_players, mode)

                    mainApp.updateIndexLog(criquet_in="-✓ " + number)
                    return

        # Add mark if possible
        for k in range(3):
            box = mainApp.player_buttons_dict[player_id]['checkboxes'][number][str(k)]
            if box.cget("text") == ' ':
                box.config(state=NORMAL, text="✓")

                # NEW: update colors immediately
                update_checkbox_colors(n_players, number)

                dead_check(n_players, mode)

                mainApp.updateIndexLog(criquet_in="+✓ " + number)
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

                    # Special criquet_input to log score for both player of the same team
                    mainApp.updateIndexLog(criquet_in=f"team-{teammate}-{str(current_score + number_value)}")

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

                # Special criquet_input to log score for both opponents
                mainApp.updateIndexLog(criquet_in=f"cutthroat-{opponent}-{str(current_score + number_value)}")

        else:  # standard (2 players)

            opponent = 2 if player_id == 1 else 1

            if count_checks(player_id) >= 3 and count_checks(opponent) < 3:
                score_entry = mainApp.player_labels_dict[player_id]['score']
                current_score = int(score_entry.get())

                score_entry.config(state=NORMAL)
                score_entry.delete(0, END)
                score_entry.insert(0, str(current_score + number_value))
                score_entry.config(state=DISABLED)

                mainApp.updateIndexLog()

        # Dead Check
        dead_check(n_players, mode)      


    return
