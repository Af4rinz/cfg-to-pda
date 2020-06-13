class IllegalVariableException(Exception):
    def __init__(self, character, rule):
        self.st1 = "Illegal character not in states or terminals"
        self.st2 = character + " in " + rule
    def __str__(self):
        string =  self.st1 + '\n' + self.st2
        return string  
