import Grammar.grammarImport as Grammar
import Utils.constants as constant

def toPda(Grammar):
    grammar = Grammar.fullGrammar
    transitions = ''
    t = ''
    
    for state in grammar:
        t = constant.DELTA + "(q, " + constant.LAMBDA + ", " + str(state) + ") = {"
        nt = len(grammar[state]) #number of transitions in state
        idxState = 0

        #single transition
        if nt == 1 :
            t = t + "(q, " + str(grammar[state][idxState]) + ")}"

        else:
            while idxState < len(grammar[state]) - 1:
                t = t + "(q, " + str(grammar[state][idxState]) + "), "
                idxState += 1
            t = t + "(q, " + str(grammar[state][idxState]) + ")}"  
        
        #extend transitions
        transitions = transitions + '\n' + t
    
    for terminal in Grammar.terminals:
        if terminal != constant.LAMBDA:
            transitions = transitions + '\n' + str(constant.DELTA + "(q, " + terminal + ', ' + 
            terminal + "), ") + " = " + "{(q, " + constant.LAMBDA + ")}"
    
    return transitions


if __name__ == "__main__":
    grammar = Grammar.importGrammar('D:/Afarin/Edu/Theory of Languages and Automata/CFG_to_PDA/SampleGrammar2.txt')
    print(toPda(grammar))
