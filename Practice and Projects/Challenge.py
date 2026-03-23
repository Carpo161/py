# While true loop

from random import randint
num = randint(1,100)
print('The goal of this game is to guess the number in the range of 1 - 100.')
guess_list = []

while True:
    guess = int(input('Guess the number: '))
    guess_list.append(guess)

    if (guess < 1 or guess > 100):
        print('OUT OF BOUNDS. Please try again: ')
        continue

    valid_guess = [guess for guess in guess_list if 1 <= guess <= 100]

    if len(valid_guess) == 1:
        if abs(num - guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')
    
    else:
        if abs(num - valid_guess[-1]) < abs(num - valid_guess[-2]):
            print('WARMER!')
        else:
            print('COLDER')
    
    if guess == num:
        print(f'Well done! The number was {num} and it took you {len(guess_list)} guesses.')
        break




from random import randint
print('Rules: Guess the number in the range 1 - 100')
num = randint(1,100)
guess_list = []
guess = int(input('Guess the number: '))
guess_list.append(guess)
count = 1

while guess < 1 or guess > 100:
    count += 1
    print('OUT OF BOUNDS')
    guess = int(input('Guess the number: '))
    guess_list.append(guess)

if abs(num - guess_list[-1]) <= 10:
    print('WARM!')
elif abs(num - guess_list[-1]) > 10:
    print('COLD!')

while guess != num:
    count += 1
    guess = int(input('Guess the number: '))
    guess_list.append(guess)
    if abs(num - guess_list[-1]) < abs(num - guess_list[-2]):
        print('WARMER!')
    elif abs(num - guess_list[-1]) > abs(num - guess_list[-2]):
        print('COLDER!')

print(f'Well done! The number was {num} and it took you {count} guesses.')