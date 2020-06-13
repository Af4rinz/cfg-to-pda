import Utils.constants as constant

class Transition:
    inputSymbol = ''
    popSymbol = ''
    pushSymbols = []
    def __init__(self, inputSymbol, popSymbol, pushSymbols):
        self.inputSymbol = inputSymbol
        self.popSymbol = popSymbol
        self.pushSymbols = pushSymbols
    
    def addPushSymbol(self, sym):
        self.pushSymbols.add(sym)
    
    def __str__(self):
        pushString = ''.join(self.pushSymbols)
        string = self.inputSymbol + ", " + self.popSymbol + ", " + pushString 
        return string
        
