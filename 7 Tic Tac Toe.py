def display(**kwargs):
    board = {k: kwargs.get(k, ' ') for k in "123456789"}
    print(f"{board['7']} | {board['8']} | {board['9']}")
    print("----------")
    print(f"{board['4']} | {board['5']} | {board['6']}")
    print("----------")
    print(f"{board['1']} | {board['2']} | {board['3']}")

def players():
    while True:
        ch1 = input('Player 1: Please choose between X and O: ').upper()
        if ch1 not in ['X', 'O']:
            print('Please pick between X and O.')
            continue
        if ch1 == 'X':
            ch2 = 'O'
        else:
            ch2 = 'X'
        return ch1, ch2

def position():
    while True:
        position = input('Select a position (1-9): ')
        if position.isdigit() == False:
            print('Please select a digit.')
            continue

        position = int(position)
        if 1 <= position <= 9:
            return str(position)
        print('Please select a position in the range 1-9.')

def game_on_func():
    while True:
        choice = input('Would you like to continue playing (Y / N)?').upper()
        
        if choice in ['Y', 'N']:
            return choice == 'Y'
        
        print('Please select between Y and N.')

def wins(i):
    combs = [('7','4','1'),
             ('8','5','2'),
             ('9','6','3'),
             ('7','8','9'),
             ('4','5','6'),
             ('1','2','3'),
             ('7','5','3'),
             ('9','5','1')]
    for a,b,c in combs:
        if i[a] == i[b] == i[c] in ('X', 'O'):
            return True
    return False




print('Welcome to TIC TAC TOE')

game_on = True
while game_on:

    board = {k: ' ' for k in "123456789"}
    x, o = players()

    while True:
        display(**board)
        
        print('Player 1:')
        pos = position()
        while board[pos] != ' ':
            print('That position is already taken. Please select another.')
            pos = position()
        board[pos] = x

        if wins(board) == True:
            print('Player 1 wins!')
            display(**board)
            break

        if all(val != ' ' for val in board.values()):
            print("It's a draw!")
            display(**board)
            break

        display(**board)
        
        print('Player 2')
        pos = position()
        while board[pos] != ' ':
            print('That position is already taken. Please select another.')
            pos = position()
        board[pos] = o
        
        if wins(board) == True:
            print('Player 2 wins!')
            display(**board)
            break

        if all(val != ' ' for val in board.values()):
            print("It's a draw!")
            display(**board)
            break

    game_on = game_on_func()


print('Thank you for playing.')