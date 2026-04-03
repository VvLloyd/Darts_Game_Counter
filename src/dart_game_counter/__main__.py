from tkinter import *
from dart_game_counter.classes.Match import Match
import dart_game_counter.initializeWindow as initWin, dart_game_counter.consoleSetup as cS

def main():
    """
    This .py initialize the "tkinter" GUI with all its functionalities.
    This version only has one Class object: the mainApp Class. This Class contains all parameters (variables) and 
    methods required to handle the GUI. A future version of this code will contains subsequent classes such as Member,
    Game and League to manage data in a suitable matter.    
    """

    quitbuttonPressed = False
    gamemode = [7, False, False]

    def on_closing():
        tk_layer.destroy()
        exit()  # Will stop everything

    while quitbuttonPressed == False:
        # Initiates the match object
        match_inst = Match(gamemode=gamemode)
        cS.consoleSetup()  # To display Logs into console (in the proper format)
        [tk_layer, mainApp_inst] = initWin.initializeWindow(match_inst)  # Initialize the window creation
        tk_layer.protocol("WM_DELETE_WINDOW", on_closing)  # if the user closes the Window. Skip the remaining lines if pressed (due to exit())
        tk_layer.mainloop()  # Window is waiting for any action
        gamemode = mainApp_inst.match_inst.CommitGameMode # Retrieve Game mode for re-populate GUI with new mode
        quitbuttonPressed = mainApp_inst.quitbuttonPressed  # may be updated if user presses the Quit Button
        tk_layer.destroy() # Destroy everything, then repeat the loop.