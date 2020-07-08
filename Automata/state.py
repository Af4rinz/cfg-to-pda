import Utils.constants as constant

class State:
    name = ""
    transitions = []
    isInitial = False
    isFinal = False

    def __init__(self, name, isInitial, isFinal, transitions):
        self.name = name
        self.isInitial = isInitial
        self.isFinal = isFinal
        self.transitions = transitions
    
    def addTransition(self, transition):
        self.transitions.add(transition)
    
    def setFinal (self, isFinal):
        self.isFinal = isFinal
    
    def setInitial (self, isInitial):
        self.isInitial = isInitial
    
    def __str__(self):
        string = self.name 
        return string



