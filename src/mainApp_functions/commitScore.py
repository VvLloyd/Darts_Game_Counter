def commitScore(mainApp):
    if mainApp.match_inst.editScoreMode == True:
        mainApp.editScore()
        mainApp.updateIndexLog()
        mainApp.updateIndexLog(log_setting_change="edit_score")

    elif mainApp.match_inst.editScoreMode == False:
        scoreToInput = mainApp.input_Score.get()
        if scoreToInput != '':
            mainApp.writeCommitScore()            
    return

