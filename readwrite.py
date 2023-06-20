# CHAPTER 9
# PAGE 120
# MANIPULATING CONTENT

# start a new program by initializing a variable with a concantenated string containing newline characters

poem='I never saw a man who looked\n'
poem += 'With such a wistful eye\n'
poem += 'Upon that little tent of blue\n'
poem += 'Which prisoners call the sky\n'

# create a File object for a new text file to write content into
file = open('poem.txt','w')

# write the string contained in 'poem' to the text file
file.write(poem)

# close the file
file.close()

# open the file again to read from it
file = open('poem.txt','r')

# display the contents of the text file 
for line in file :
    print(line, end= '')

# close the file 
file.close()


# apend text to the end of our txt file
# open the file 
file = open('poem.txt','a')
file.write('(Oscar Wilde)')
# close the file 
file.close()

# open the file again to read from it
file = open('poem.txt','r')

# display the contents of the text file 
for line in file :
    print(line, end= '')

# close the file 
file.close()