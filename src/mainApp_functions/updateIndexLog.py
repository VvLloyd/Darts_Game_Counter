import numpy as np
import pandas as pd
import os

from datetime import datetime

# The LOG function initializes a log and records all actions that occurred during the game.
# Actions such as : EndTurn, Commit Score.

# Notes; 
# The recorded information could be use for downstream logics such as calculating the player Average, High score, and more.
# This log records could also serve as the dataset for the undo/redo functions.

def updateIndexLog(mainApp, criquet_in=None, log_setting_change=None):

    #-------------------------------------------------------------------------------------------------------------------
    #                                               INITIALIZING THE LOG
    #-------------------------------------------------------------------------------------------------------------------
    # If the game is not started, create the IndexLog with all added players
        # get Current Player turn over the total nb of player.


    if mainApp.match_inst.gameStarted == False:  # if the game is not started
        
        # Store game start time
        mainApp.match_inst.game_start_time = datetime.now()   
        mainApp.match_inst.log_setting_changes = []
        
        totalPlayer = mainApp.match_inst.playerIndex[1:] #get number of players
        mainApp.turnIndexLog = pd.DataFrame([[0, 0, 1]], columns=['index', 'gameTurn', 'playerTurn']) # create first default columns

        for i in range(totalPlayer[0]): # add all columns needed for the match

            CommittedScoreToLog = mainApp.player_labels_dict[i+1]['score'].get()
            
            eval("mainApp.turnIndexLog.insert(len(mainApp.turnIndexLog.columns), 'P_"+str(i+1)+"_Entry', 0)")
            eval("mainApp.turnIndexLog.insert(len(mainApp.turnIndexLog.columns), 'P_"+str(i+1)+"_Score', CommittedScoreToLog)")
            if mainApp.match_inst.doubleInMode == True: # if this mode is on, add column for each player
                eval("mainApp.turnIndexLog.insert(len(mainApp.turnIndexLog.columns), 'P_"+str(i+1)+"_DoubleIn', 0)")

    #-------------------------------------------------------------------------------------------------------------------
    #                                                  UPDATE THE LOG
    #-------------------------------------------------------------------------------------------------------------------
    # If the game is started, add the committed score, record the endturn for the current player
    if mainApp.match_inst.gameStarted: #if the game is started

        # DO A BUNCH OF CHECKS AND CHANGES ON VARIABLES DEPENDING OF THE SITUATION

        # Extract information that is needed before logging
        mainApp.match_inst.logIndex += 1 # The log index event increase. (refer to initializeGUIvar for parameters)
        currentIndex = mainApp.match_inst.logIndex # Any event is logged

        # Store who is playing out of the total
        totalPlayer = mainApp.match_inst.playerIndex[1:]
        currentPlayer = mainApp.match_inst.playerIndex[:1]

        # Get the current and previous game turn. If there are the same, the player entry will be affected.
        currentGameTurn = mainApp.match_inst.currentGameTurn # What is the game turn
        lastGameTurn = mainApp.turnIndexLog['gameTurn'].iloc[-1] # Get previous game turn

        #----------------------------------------------------------------------------------------------------------
        # This loop looks for the last logged score. It looks back until it finds a score. If it finds a PIPE, it continues.
        PIPE = True  #Generate the PIPE variable bolean
        PIPE_count = 1 #Count to go to the next (previous) row in the column.

        while PIPE == True: # Start the search
            # Get the previous score
            lastPlayerScoreTurn = eval("mainApp.turnIndexLog['P_"+str(currentPlayer[0])+"_Score'].iloc[-"+str(PIPE_count)+"]")# Get previous game turn
            if lastPlayerScoreTurn == "|":
                PIPE_count += 1 # add one and restart
            elif lastPlayerScoreTurn != "|": # if not
                PIPE = False # Set to false, loop is over...

        # Extract the score that just got commited (after commit score button was pressed)
        CommittedScoreToLog = mainApp.player_labels_dict[currentPlayer[0]]['score'].get()

        # if setting changed, add the log into the static log header
        if log_setting_change is not None:
            if log_setting_change in "edit_name":
                mainApp.match_inst.log_setting_changes.append(f"Event: {log_setting_change} , Player {currentPlayer[0]}, at index: {currentIndex-1}, new name is: {mainApp.match_inst.players[currentPlayer[0]-1].name}")
            elif log_setting_change in "edit_score":
                mainApp.match_inst.log_setting_changes.append(f"Event: {log_setting_change}, Player {currentPlayer[0]}, at index: {currentIndex-1}, new score is: {CommittedScoreToLog}")

        # If the score is the same as the previous, overwrite the variable with "|". This is to ease the statistical functions.
        # The idea is to only keep score changes. Note that the EndTurn symbol is "|".
        # Which won't be counted during statistical calculations
        if CommittedScoreToLog == lastPlayerScoreTurn:
            CommittedScoreToLog = "|" # Will log this symbol if the score remained as-is.
        #----------------------------------------------------------------------------------------------------------

        # Inputs when playing criquet mode, 1 VS 1, CutThroat, or 2V2
        if criquet_in is not None:
            if "cutthroat" not in criquet_in:
                CommittedScoreToLog = criquet_in  

        # The below code deals with the player entries. This allows the player to add its score for each darts.
        # If this is still is turn, the player_entry gets incremented.
        lastPlayerTurn = mainApp.turnIndexLog['playerTurn'].iloc[-1]
        if currentPlayer == lastPlayerTurn: # On this player turn, something happened (score or DoubleIn)
            # This allows multiple entries for each turn. The log will display all entries for a specific game turn
            if lastGameTurn == currentGameTurn: # During this turn
                if mainApp.turnIndexLog["P_" + str(currentPlayer[0]) + "_Entry"].iloc[-1] != "|":
                    player_entry = mainApp.turnIndexLog["P_" + str(currentPlayer[0]) + "_Entry"].iloc[-1] + 1
                    # increment the player entry number
                else:
                    print('hit')
                    player_entry = 1
            elif lastGameTurn != currentGameTurn: # Not the same game turn. This is the first entry
                player_entry = 1

        # THe below code records tht the End-Turn button was pressed.
        elif currentPlayer != lastPlayerTurn:  # Below will log the EndTurn event by adding a PIPE .
            player_entry = "|"
            CommittedScoreToLog = "|"
            if mainApp.match_inst.doubleInMode == True:
                DoubleInStatus = "|"
                print(type(DoubleInStatus))

        #---------------------------------------------------------------------------------------------------------------
        #                                 LOG THE DATA AND PRINT IN THE CONSOLE
        #---------------------------------------------------------------------------------------------------------------
        # Log and Deal with the DoubleIn mode
        if mainApp.match_inst.doubleInMode == True:
            if currentPlayer == lastPlayerTurn:
                DoubleInStatus = mainApp.player_labels_dict[currentPlayer[0]]['doubleIn_var'].get()
            # Will log the line with the double-in status
            toAppend = eval("pd.DataFrame([[currentIndex, currentGameTurn, currentPlayer[0], player_entry, CommittedScoreToLog, DoubleInStatus]], "
                            "columns=['index', 'gameTurn', 'playerTurn', 'P_"+str(currentPlayer[0])+"_Entry', 'P_"+str(currentPlayer[0])+"_Score','P_"+str(currentPlayer[0])+"_DoubleIn'])")
        else: # If double-in is off
            toAppend = eval("pd.DataFrame([[currentIndex, currentGameTurn, currentPlayer[0], player_entry, CommittedScoreToLog]], "
                            "columns=['index', 'gameTurn', 'playerTurn', 'P_"+str(currentPlayer[0])+"_Entry', 'P_"+str(currentPlayer[0])+"_Score'])")
            
            if criquet_in is not None:
                if any(s in criquet_in for s in ["cutthroat", "team"]):
                    parts = criquet_in.split("-")
                    player_ID = parts[1]
                    new_score = parts[2]
                    toAppend = pd.DataFrame(
                        [[currentIndex, currentGameTurn, currentPlayer[0], player_entry, new_score]],
                        columns=['index', 'gameTurn', 'playerTurn',
                                 f'P_{player_ID}_Entry', f'P_{player_ID}_Score'])

                    if "team" in criquet_in:
                        currentplayerscore = new_score
                    else:
                        currentplayerscore = lastPlayerScoreTurn
                    
                    toAppend_0 = pd.DataFrame(
                        [[currentIndex, currentGameTurn, currentPlayer[0], player_entry, currentplayerscore]],
                        columns=['index', 'gameTurn', 'playerTurn',
                                 f'P_{currentPlayer[0]}_Entry', f'P_{currentPlayer[0]}_Score'])
  
                    
                    mainApp.turnIndexLog = pd.concat([mainApp.turnIndexLog, toAppend_0])
                    mainApp.turnIndexLog = mainApp.turnIndexLog.replace(np.nan, "|")               

        mainApp.turnIndexLog = pd.concat([mainApp.turnIndexLog, toAppend])
        mainApp.turnIndexLog = mainApp.turnIndexLog.replace(np.nan, "|")

        mainApp.turnIndexLog = (            
            mainApp.turnIndexLog
            .groupby(['index', 'gameTurn', 'playerTurn'], as_index=False)
            .agg(lambda x: next((v for v in x if v != "|" and pd.notna(v)), "|"))
        )
  
        n_players = mainApp.match_inst.getNplayer()
        columns = mainApp.turnIndexLog.columns
        row = [""] * len(columns)

        # Compute column widths
        table_str = mainApp.turnIndexLog.to_string(index=False)
        header_line = table_str.split("\n")[0]
        col_widths = [len(col) for col in header_line.split()]

        # Fill player names
        for i in range(1, n_players + 1):
            entry_col = f"P_{i}_Entry"
            
            if entry_col in columns:
                col_index = columns.get_loc(entry_col)
                name = mainApp.match_inst.players[i-1].name
                
                width = col_widths[col_index]
                row[col_index] = name.rjust(width) 

        player_names_df = pd.DataFrame([row], columns=columns)

        combined_df = pd.concat([player_names_df, mainApp.turnIndexLog], ignore_index=True)
               
        header = mainApp.match_inst.game_start_time.strftime("Game played on %Y-%m-%d at %H:%M:%S")

        os.system('cls' if os.name == 'nt' else 'clear')

        print(header)
        for row in mainApp.match_inst.log_setting_changes:
            print(row)
        print("=" * len(header))  # nice underline
        print(combined_df.to_string(index=False))

        return
