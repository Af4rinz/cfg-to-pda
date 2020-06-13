import cfgToPda as c2p
import Grammar.grammarImport as Grammar

def main():
    grammarPath = input()
    grammar = Grammar.importGrammar(grammarPath)
    c2p.toPda(grammar)
