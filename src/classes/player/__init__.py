class Player:
    """
    Class representing a Player with all its attributes.
    """

    def __init__(self, name, starting_score=301, double_in=False, double_out=False):
        """
        Constructor (runs when creating a new player)

        :param name: Player name (str)
        :param starting_score: Initial score (int)
        :param double_in: Double-in mode enabled (bool)
        """
        self.name = name
        self.current_score = starting_score
        self.doubleInVal = double_in
        self.doubleOutVal = double_out

    # ---------------------------------------------------
    # GETTERS
    # ---------------------------------------------------

    def getPlayerScore(self):
        return self.current_score

    def getDoubleInVal(self):
        return self.doubleInVal
    
    def getDoubleOutVal(self):
        return self.doubleOutVal

    def getName(self):
        return self.name

    # ---------------------------------------------------
    # SETTERS / MODIFIERS
    # ---------------------------------------------------

    def remScorePts(self, points):
        self.current_score -= points

    def editScorePts(self, editedScore):
        self.current_score = editedScore

    def setDoubleInVal(self, newVal):
        self.doubleInVal = newVal
    
    def setDoubleOutVal(self, newVal):
        self.doubleOutVal = newVal

    def setName(self, newName):
        self.name = newName