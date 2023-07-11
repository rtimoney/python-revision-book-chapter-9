# CHAPTER 9
# PAGE 122
# UPDATING CONTENT

# start a new program by assigning a string value to a variable containing text to be written to a file
text = 'The song "Summer Lovin" \n'
text += 'is from the musical film Grease'

# next add statements to write the text string into a file and display the file's current status in the "with" block
with open('update.txt', 'w') as file :
    file.write(text)
    print('\nFile Now Closed?:', file.closed)

# non-indented statement after the 'wih' block to display the  file's new status
print('File Now Closed?:', file.closed)

# reopen the file and display its contents to confirm it now contains the entire text string
with open('update.txt','r+') as file :
    text =file.read()
    print('\nString:',text)

    # DISPLAY THE CURRENT FILE POSITION THEN REPOSITION AND DISPLAY THAT NEW POSITION
    print('\nPosition in File Now:',file.tell())
    position = file.seek(33)
    print('Position in File Now:',file.tell())
    
    # overwrite the text from the current file position
    file.write(' *legendary* ')

    # reposition the file once more and overwrite the text from the new position
    position = file.seek(61)
    file.write(' - do you know it?')


    # return to the start of the file and display the entire updated contents
    position = file.seek(0)
    text =file.read()
    print('\nString:',text)