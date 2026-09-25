from dart_game_counter.mainApp_functions import mainApp
from tkinter import *

def initializeWindow(match_inst):

    # Call the tkinter tool
    tk_layer = Tk()
    # Call Constructor
    mainApp_inst = mainApp.mainApp(tk_layer, match_inst)

    return [tk_layer, mainApp_inst]