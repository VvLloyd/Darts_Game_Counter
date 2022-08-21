"""Temporary method to store data; The variables are stored in "self" (i.e. Mainwindow).
Since all methods use the MainWindow Object as an input/output, it is a lazy effective way to implement functionalities"""

def initializeGUIvar(MainWindow):
    MainWindow.softVersion = "ver 1.1"
    # Visual Stuff. These are used in the Populate GUI methods:
    MainWindow.Button_bg_color = "#245042"
    MainWindow.Button_ft_color = "#D3DBE5"
    MainWindow.activeButton_bg_color = "#9aa794"
    MainWindow.activeButton_ft_color = "#D3DBE5"

    # Variabled
    MainWindow.nbPlayer = 0
    MainWindow.gameMode = []  #
    MainWindow.gameStarted = False  # some methods (such as the log) act differently if the game is started.
    MainWindow.playerIndex = [0, 0]  # Variable tracking player turn and total number of players.
                                # A quick variable to know who is playing
    MainWindow.turnIndexLog = []  #
    MainWindow.editScoreMode = False
    MainWindow.editNameMode = False
    MainWindow.currentGameTurn = 0
    MainWindow.logIndex = 0
    MainWindow.doubleInMode = True

    return