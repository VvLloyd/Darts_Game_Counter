# import all Class methods as aliases, from the mainApps_functions directory;

class __init__:
    """
    Class representing the main window attributes.

    Attributes:
        DoubleInVar (bool): Player Double In variable.

    """

    doubleInVar = bool(False)
    doubleOutVar = bool(False)
    currentScore = []
    matchPrevScores = []
    matchHighScore = []
    matchAvgScore = []
    
    # -------------------------------------------------------------------------------------------------------------------
    # DEFINING FUNCTIONS (CLASS METHODS)
    # -------------------------------------------------------------------------------------------------------------------
    # All below methods are stored in the "player" class directory in separate .py files.

    @staticmethod
    def static_method():
        """
        A static method that does not require access to instance attributes.
        """
        print("This is a static method")

    def regular_method(self):
        """
        A regular method that can access instance attributes.
        """
        print("This is a regular method")
        print("Number of players:", self.nbPlayer)

    def getDoubleInVar(self):
        return self.nbPlayer
    
    def setDoubleInVar(self,value):
        self.DoubleInVar = bool(value)
        return
    
    def getDoubleOutVar(self):
        return self.nbPlayer
    
    def setDoubleOutVar(self,value):
        self.DoubleOutVar = bool(value)
        return