from Utils.Exceptions import IllegalVariableException
import Utils.constants as constant
class Grammar(object):
    nTerminal = 0
    nState = 0
    linearity = 0 #-1 = ll, 1 =rl, 2 = regular

    def __init__(self):
        self.terminals = []
        self.states = []
        self.startVar = ''
        self.fullGrammar = {}
    
    def setNTerminal(self):
        Grammar.nTerminal = len(self.terminals)
    
    def setNState (self):
        Grammar.nState = len(self.states)
    
    def display(self):
        st = "Full grammar is: "
        for state in self.fullGrammar[state]:
            rules = ''
            for r in self.fullGrammar[state]:
                rules = rules + ' | ' + r #extend rules by |

            rules = rules.lstrip('|') #remove first extra |
            st = st + state + ' -> ' + rules + '\n'
        return st


def importGrammar (File):
    file = open(File,'r')
    data = file.readlines()
    grammar = Grammar()

    initState = data[0].rstrip()
    states = data[1].rstrip()
    terminals = data[2].rstrip()
    
    grammar.startVar = initState
    grammar.states = states.split(',')
    grammar.terminals = terminals.split(',')
    
    grammar.setNState()
    grammar.setNTerminal()
    
    for idx in range(3, 3 + grammar.nState):
        rule = data[idx].rstrip()
        for character in rule:
            if character == '-' or character == '>' or character == '|':
                pass
            elif character not in grammar.terminals and character not in grammar.states and character != constant.LAMBDA:
                raise IllegalVariableException(character, rule)
        #left hand side: state        
        lhs = rule[:rule.find('-')]
        #right hand side: productions
        rhs = rule[rule.find('>') + 1:]
        #split productions
        rhs = rhs.split('|')
        #assign productions to each state
        grammar.fullGrammar[lhs]=rhs

    return grammar
