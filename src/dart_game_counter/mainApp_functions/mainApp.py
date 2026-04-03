from tkinter import *
# import all Class methods as aliases, from the mainApps_functions directory;
from dart_game_counter.mainApp_functions import writeCommitScore as wCS
from dart_game_counter.mainApp_functions import DoubleIncheckChanged as DIcC, addPlayer as aP, checkChangedDoubleIn as cCDI, checkChangedDoubleOut as cCDO, clearClickPad as cCP, clickPad as cP, commitAddPlayer as cAP, commitGameMode as cGM, commitScore as cS, destroySubWin as dSW, editName as eN, editScore as eS, endTurn as eT, initializeGUIvar, keyBindSetup as kBs, populateGModeGUI as popGMGUI, populateGUI as pGUI, quitGame as qG, refreshImages as rI, selectedMode as sM, startGame as sG, updateIndexLog as uIL, updateStatusLabel as uSL


class mainApp:

    def __init__(self, tk_layer, match_inst):

        """The init initializes variables and populate the GUI. The variables will be remove from
        this object in the next version.
        """
        self.match_inst = match_inst
        self.initializeGUIvar() # Create variables (temporary method)
        self.populateGUI(tk_layer)  # Create all tkinter GUI widgets
        self.keyBindSetup(tk_layer)  # keybinds the keyboard caLculator to the GUI

    # -------------------------------------------------------------------------------------------------------------------
    # DEFINING FUNCTIONS (CLASS METHODS)
    # -------------------------------------------------------------------------------------------------------------------
    # All below methods are stored in the mainApps_functions directory in separate .py files.
    # The name of the .py file and function must be the same in order to work properly

    def initializeGUIvar(self): # Method that initialize all variables stored in the mainApp Object (Temporary)
        initializeGUIvar.initializeGUIvar(self)
        return

    def populateGUI(self, tk_layer): # Creates and locates all tkinter widgets
        pGUI.populateGUI(self, tk_layer)
        return

    def keyBindSetup(self, tk_layer): # Keybinding methods
        kBs.keyBindSetup(self, tk_layer)
        return

    def clickPad(self, number):
        cP.clickPad(self, number)
        return

    def commitScore(self):
        cS.commitScore(self)
        return

    def writeCommitScore(self, number='', player_id=None, event=None):
        wCS.writeCommitScore(self, number, player_id, event)
        return

    def endTurn(self):
        eT.endTurn(self)
        return

    def updateStatusLabel(self, text):
        uSL.updateStatusLabel(self, text)
        return

    def commitAddPlayer(self):
        cAP.commitAddPlayer(self)
        return

    def startGame(self):
        sG.startGame(self)
        return

    def refreshImages(self):
        rI.refreshImages(self)
        return

    def clearClickPad(self):
        cCP.clearClickPad(self)
        return

    def updateIndexLog(self, criquet_in=None, log_setting_change=None):
        uIL.updateIndexLog(self, criquet_in=criquet_in, log_setting_change=log_setting_change)
        return

    def editScore(self):
        eS.editScore(self)
        return

    def editName(self):
        eN.editName(self)
        return

    def addPlayer(self):
        aP.addPlayer(self)
        return

    def destroySubWin(self):
        dSW.destroySubWin(self)
        return

    def quitGame(self, tk_layer):
        qG.quitGame(self, tk_layer)
        return

    def populateGModeGUI(self, tk_layer):
        popGMGUI.populateGModeGUI(self, tk_layer)
        return

    def commitGameMode(self, tk_layer):
        cGM.commitGameMode(self, tk_layer)
        return

    def selectedMode(self, sel_mode, double_in=False, double_out=False):
        sM.selectedMode(self, sel_mode, double_in, double_out)
        return

    def DoubleIncheckChanged(self):
        DIcC.DoubleIncheckChanged(self)
        return   

    def checkChangedDoubleIn(self, buttonPressed):
        cCDI.checkChangedDoubleIn(self,buttonPressed)

    def checkChangedDoubleOut(self, buttonPressed):
        cCDO.checkChangedDoubleOut(self,buttonPressed)

