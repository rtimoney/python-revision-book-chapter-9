# CHAPTER 9
# PAGE 117
# MODIFYING STRINGS 

# start a new prograsm by initializing  a variable with a string of lowercase characters and spaces
string = 'coding for beginners in easy steps'

# display the string capitalized, titled and centered
print( '\nCapitalized:\t',string.capitalize())
print( '\nTitled:\t\t',string.title())
print( '\nCentered:\t',string.center(30,'*'))

# now display the string in all uppercase and merged with a sequence of two asterisks 
print( '\nUppercase:\t',string.upper())
print( '\nJoined:\t\t',string.join('**'))

# then display the string padded with asterisks on the left
print( '\nJustified:\t\t',string.rjust(30,'*'))

# finally, display the string with all occurrances of the 's' character replaced by asterisks 
print( '\nReplaced:\t\t',string.replace('s','*'))
