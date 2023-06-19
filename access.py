# CHAPTER 9
# PAGE 119
# ACCESSING FILES 

# start a new program by creating a new File object in which to write content
file = open('example.txt','w')

# next add statements to display the file name and mode
print('File Name:',file.name)
print('File Open Mode:',file.mode)

# now add statements to display the file access permissions
print('Readable:',file.readable())
print('Writable:',file.writable())

# then define a function to determine the file's status
def get_status(f) :
    if not f.closed :
        return 'Open'
    else :
        return 'Closed'
    
# finally add statements to display the current file status then close the file and display the file status once more 

print('File status:',get_status(file))
file.close()
print('\nFile status:',get_status(file))

