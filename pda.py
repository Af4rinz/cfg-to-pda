import gnf
class PDA:
    rules = []

    def __init__ (self, file_path):
        self.file_path = file_path;
        self.readFile()
    
    def readFile(self):
        count = 0
        self.srcFile = open (file_path, 'r') 
        
        temp = srcFile.readline() # a single line formatted as "S, A, B" denoting variables
        self.variables = temp.split(',') 
        
        temp = srcFile.readline() #starting variable such as "S"
        self.startVar = temp 
        
        temp = srcFile.readline() # a single line formatted as "a, b, c" denoting terminals
        self.terminals = temp.split(',') 
        
        while True: 
            count += 1
            temp = srcFile.readline
            if not temp: break
            rules.append(temp)
        self.ruleCount = count
    
    def cfgToPda(Grammar):

