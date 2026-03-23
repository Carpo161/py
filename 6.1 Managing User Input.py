# Displaying information

print([1,2,3])
print([4,5,6])
print([7,8,9])

def display_rows(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)

def display_args(*args):
    print(args)

example_row = [1,2,3]
print(display_rows(example_row, example_row, example_row))

row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']

display_rows(row1,row2,row3)

row2[1] = 'X'



# Accepting user input

result = int(input('Please enter a value: '))



# Validating user input

def user_choice():
    while True:
        choice = ''
        choice = input('Please enter a number 0-10: ')
        if choice.isdigit() == False:
            print('Sorry that is not a digit ')
            continue

        choice = int(choice)
        if 0 <= choice <= 10:
            return choice
        print('Sorry that number is out of range ')
print(user_choice())



# Simple user interaction
# The goal is to create a small game where a user can choose a "position" in an existing list and replace it with a value of their choice.

lst = [1, 2, 3]

def display(row):
    print(f'Here is the current list:\n{row}')

def user_choice_index():
    choice = ''
    while choice not in ['0','1','2']:
        choice = input('Pick an index position to change the list (0, 1, 2): ')
        if choice.isdigit() == False:
            print('Sorry that is not a digit. Please try again.')
            continue

        choice = int(choice)
        if 0 <= choice <= 2:
            return choice
        print('Sorry that number is out of range. Please try again.')

def user_choice_value(i):
    replacement = input('Choose a replacement for that position: ')
    lst[i] = replacement
    return f'The new list is: {lst}'

def game_on():
    while True:
        choice = input('Would you like to continue playing? (Y / N): ').upper()

        if choice in ['Y', 'N']:
            return choice == 'Y'
        
        print('Please pick between Y or N.')

gameon = True
while gameon:
    display(lst)

    index_choice = user_choice_index()

    print(user_choice_value(index_choice))
    gameon = game_on()