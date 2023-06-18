# CHAPTER 9
# PAGE 113
# MANIPULATING STRINGS 

# use + to join strings together
# use * to repeat strings - e.g. - 'Hello' * 2 = 'HelloHello'
# use [] to select a character at a stated position - e.g. - 'HELLO'[3] = 'L'
# use [:] to select a range of characters at a stated range - e.g. - 'HELLO'[2:4] = 'ELL'
# in will return true is a string contains a given character - e.g. - 'H' in 'Hello' = True
# not in will return true is a string does not contain a given character - e.g. - 'J' not in 'Hello' = True
# r/R returns a raw string which supresses the meaning of escape characters - e.g. - print( r'\n')
# "''" = Docstring - describe a function, module, class or a method - e.g. - def sum(a,b) : "''"

def display(s) :
    '"Display an argument value."'
    print(s)

display(display.__doc__)

display(r'C:\Program Files')

display('\nHello' + ' Python')

display('Python in easy steps\n' [7 :])

display('P' in 'Python')
display('p' in 'Python')