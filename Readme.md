# CFG to PDA Converter
A context free grammar to pushdown automaton converter that operates with Greibach Normal Form inputs.

## Use
Run cfgToPda.py to import grammar, after conversion, type in 'y' if you wish to parse strings.

Sample grammars are stored in `./Samples/`, each are a set of two files; sample strings to parse (and their results) and the main grammar file.

Grammar file structure:
- first line: single initial variable (e.g. `S`)
- second line: comma seperated list of terminals
- next lines: each line contains Greibach rules of a grammar in the format `A->aBC|aBB`

There is a debug mode flag in cfgToPda.py that shows stack contents while parsing (global variable).
