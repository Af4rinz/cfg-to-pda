import Utils.constants as constant
from .state import State

class Transition:
    inputSymbol = ''
    currState = ''
    nextState = ''
    popSymbol = ''
    pushSymbols = []
    
    def __init__(self, inputSymbol, currState, nextState, popSymbol, pushSymbols):
        self.inputSymbol = inputSymbol
        self.currState = currState
        self.nextState = nextState
        self.popSymbol = popSymbol
        self.pushSymbols = pushSymbols
    
    def addPushSymbol(self, sym):
        self.pushSymbols.add(sym)
    
    def __str__(self):
        pushString = ''.join(self.pushSymbols)
        string = self.inputSymbol + ", " + self.popSymbol + ", " + pushString 
        return string
        
