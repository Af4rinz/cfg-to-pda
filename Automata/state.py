import Util.constants as constant
class State:
    name = ""
    transitions = []
    isFinal = False

    def __init__(self, name, isFinal, transitions):
        self.name = name
        self.transitions = transitions
        self.isFinal = isFinal
    
    def __init__(self):
        self.isFinal = False
    
    def addTransition(self, transition):
        self.transitions.add(transition)
    
    def setFinal (self, isFinal):
        self.isFinal = isFinal
    
    def __str__(self):
        string = self.name 
        return string



