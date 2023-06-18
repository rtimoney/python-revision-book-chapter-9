# CHAPTER 9
# PAGE 115
# FORMATTING STRINGS 

# initialize  a variable with a formatted string
snack = '{} and {}'.format('Burger','Fries')

# display the value to see the text replaced in their listed order
print( '\nReplaced:',snack)

# assign a differently formatted (using specified index elements) string to the same variable
snack='{1} and {0}'.format('Burger','Fries')

# display the variable to see the text not replaced by their specified index element value
print('Replaced:',snack)

#assign another formatted string to the variable 
snack = '%s and %s' % ('Milk','Cookies')

# display the variable to see the text substituted in their listed order 
print('\nSubstituted:',snack)

