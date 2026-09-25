from dart_game_counter.mainApp_functions import endTurn as eT
from dart_game_counter.mainApp_functions import clickPad as cP, commitScore as cS

def keyBindSetup(self, master):
    master.bind("1", lambda event: cP.clickPad(self, 1))
    master.bind("2", lambda event: cP.clickPad(self, 2))
    master.bind("3", lambda event: cP.clickPad(self, 3))
    master.bind("4", lambda event: cP.clickPad(self, 4))
    master.bind("5", lambda event: cP.clickPad(self, 5))
    master.bind("6", lambda event: cP.clickPad(self, 6))
    master.bind("7", lambda event: cP.clickPad(self, 7))
    master.bind("8", lambda event: cP.clickPad(self, 8))
    master.bind("9", lambda event: cP.clickPad(self, 9))
    master.bind("0", lambda event: cP.clickPad(self, 0))
    master.bind("<Return>", lambda event: cS.commitScore(self))
    master.bind("<space>", lambda event: eT.endTurn(self))
    master.bind("<BackSpace>", lambda event: cP.clickPad(self, -1))
    return
