def commitGameMode(mainApp, master):

    selection = mainApp.match_inst.SelectedGameMode

    mainApp.match_inst.CommitGameMode = eval("["+str(selection)+", mainApp.match_inst.doubleInMode, mainApp.match_inst.doubleOutMode]")

    print('Game Mode is now set:')
    print(mainApp.match_inst.CommitGameMode)
    print(mainApp.match_inst.SelectedGameMode)

    mainApp.destroySubWin()

    master.quit()

    return
