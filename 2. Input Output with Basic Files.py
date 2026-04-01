my_file = open('text.txt')
print(my_file.read())
my_file.seek(0) # The seek function moves the file cursor to a specific location inside a file
print(my_file.read()) # Seek function must be used to read entire file again as the file cursor is at the -1 index position
my_file.seek(0)

'''
.seek() function
Syntax: file.seek(offset, from_what)
    offset: Number of bytes to move the cursor.
    from_what: (optional) Reference point to start from:
        0: sets the reference point at the beginning of the file
        1: sets the reference point at the current file position
        2: sets the reference point at the end of the file
'''

print(my_file.readlines()) # the readlines() method returns a list containing each line in the file as a list item


#File locations
# Pass entire file path to open file from any location
''' 
For Windows you need to use double \ so python doesn't treat the second \ as an escape character, a file path is in the form:
myfile = open("C:\\Users\\YourUserName\\Home\\Folder\\myfile.txt")

For MacOS and Linux you use slashes in the opposite direction:
myfile = open("/Users/YouUserName/Folder/myfile.txt") 
'''


#Opening and closing files

my_file.close() # it is good practice to close a file after using it to access it elsewhere

# Open / Run file without having to close it
with open('text.txt') as my_new_file:
    contents = my_new_file.read()
    print(contents)


# Reading, Writing and Appending Modes
'''
• mode='r' is read only .
• mode='w' is write only (will overwrite files or create new!)
• mode='a' is append only (will add on to files)
• mode='r+' is reading and writing
• mode= 'w+' is writing and reading (Overwrites existing files or creates a
new file!)
'''

#Writing to files

with open('new_file.txt', mode='a') as f:
    f.write('\nFOUR ON FOURTH')

with open('new_file.txt', mode='r') as f:
    print(f.read())

with open('open.txt',mode='w') as f:
    f.write('I created this file')

with open('open.txt', mode='r') as f:
    print(f.read())