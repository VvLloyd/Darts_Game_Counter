# import all Class methods as aliases, from the mainApps_functions directory;

class Match: 

    def __init__(self, gamemode=[1, True, False]):
        """
        Class representing the main window attributes.

        Attributes:
            nbPlayer (int): Number of players.
            p1_DoubleInVar (bool): Player 1 Double In variable.
            p2_DoubleInVar (bool): Player 2 Double In variable.
            p3_DoubleInVar (bool): Player 3 Double In variable.
            p4_DoubleInVar (bool): Player 4 Double In variable.
            p1_DoubleOutVar (bool): Player 1 Double Out variable.
            p2_DoubleOutVar (bool): Player 2 Double Out variable.
            p3_DoubleOutVar (bool): Player 3 Double Out variable.
            p4_DoubleOutVar (bool): Player 4 Double Out variable.
            SelectedGameMode (list): Selected Game Mode.
            prevSelMode (int): Previous Selected Mode.
            doubleInMode (bool): Double In Mode.
            doubleOutMode (bool): Double Out Mode.
            CommitGameMode (list): Game Mode to commit.
            gameStarted (bool): Indicates if the game has started.
            playerIndex (list): Player turn index and total number of players.
            turnIndexLog (list): Turn index log.
            editScoreMode (bool): Edit Score Mode.
            editNameMode (bool): Edit Name Mode.
            currentGameTurn (int): Current game turn.
            logIndex (int): Log index.
            quitbuttonPressed (bool): Indicates if the quit button has been pressed.
        """

        # Declare variables & types
        self.nbPlayer = int(0)
        self.players = []

        #Used to be stored in the GUI, must be located in the player object
        self.p1_DoubleInVar = bool(False)
        self.p2_DoubleInVar = bool(False)
        self.p3_DoubleInVar = bool(False)
        self.p4_DoubleInVar = bool(False)

        #Used to be stored in the GUI, must be located in the player object
        self.p1_DoubleOutVar = bool(False)
        self.p2_DoubleOutVar = bool(False)
        self.p3_DoubleOutVar = bool(False)
        self.p4_DoubleOutVar = bool(False)

        self.SelectedGameMode = []
        self.prevSelGameMode = gamemode[0] # to initiate the GUI with the current mode
        self.prevSelDoubleInMode = bool(True) # to initiate the GUI with the current mode
        self.prevSelDoubleOutMode = bool(True) # to initiate the GUI with the current mode
        self.doubleInMode = gamemode[1]
        self.doubleOutMode = gamemode[2]
        self.CommitGameMode = gamemode

        self.gameStarted = bool(False)
        self.playerIndex = [0, 0]
        self.turnIndexLog = []
        self.editScoreMode = bool(False)
        self.editNameMode = bool(False)
        self.currentGameTurn = int(0)
        self.logIndex = int(0)
        
        self.quitbuttonPressed = bool(False)    
    
    # -------------------------------------------------------------------------------------------------------------------
    # DEFINING FUNCTIONS (CLASS METHODS)
    # -------------------------------------------------------------------------------------------------------------------
    # All below methods are stored in the mainApps_functions directory in separate .py files.
    # The name of the .py file and function must be the same in order to work properly

    def getNplayer(self):
        """
        A regular method that can access instance attributes.
        """
        return self.nbPlayer
    
    def addNplayer(self):
        """
        A regular method that can access instance attributes.
        """
        self.nbPlayer += 1
        return
    
    def addPlayer(self, player):
        """
        A regular method that can access instance attributes.
        """
        self.players.append(player)
        return self
    
    def getPlayer(self, index):
        """
        A regular method that can access instance attributes.
        """
        player = self.players(index)
        return player