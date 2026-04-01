# If Elif and Else Statements

location = 'Bank'
if location == 'Bank':
    print('Money is cool!')
elif location == 'Auto Shop':
    print('Cars are cool!')
if location == 'Store':
    print('Welcome to the store.')
else:
    print('What is your location?')



# For loops
# Many python objects are iterable, i.e. we can iterate over every element in the object and for loops can be used to execute a block of code for every iteration
# For exmaple you can iterate over ebery character in a string, iterate over every items in a list and every key in a dictionary
''' Syntax:
my_iterable = [1,2,3]
for item_name in my_iterable:
    print(item_name) '''

my_list = [1,2,3,4,5,6,7,8,9,10]
for i in my_list:
    print(i)
for i in my_list:
    print('hello')

# Check for even numbers
for i in my_list:
    if i % 2 == 0:
        print(i)
    else:
        print(f'Odd number: {i}')

# List sum
list_sum = 0
for i in my_list:
    list_sum = list_sum + i
print(list_sum)

# For loops with strings
for i in 'Hello World':
    print(i)

# To print something a certain number of times use an udenrscore as the variable name as a placeholder and for readability if it is not being used
for _ in '12345678':
    print('Cool!')

# Tuple unpacking
my_list = [(1,2,3), (4,5,6), (7,8,9), (10,11,12)]
for a,b,c in my_list:
    print(a)
    print(b)
    print(c)
for a,b,c in my_list:
    print(b)

#Iterating through a dictonary
d = {'k1':1, 'k2':2, 'k3':3}
for i in d:
    print(i) # Iterating through a dictionary interates through the keys

for i in d.items():
    print(i) # Use the .items() method to grab key-value pair

for i in d.values():
    print(i) # Use the .values() method to grab values

for k,v in d.items():
    print(v) # Tuple unpacking to grab keys and values



# While loops
# Will continue to execute a block of code while some conditon reamins True
''' Syntax:
while some_bolean_condition:
    #do something
else:
    #do something different '''

x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x += 1 # the same as x = x + 1
else:
    print('x is not less than 5')



# Keywords: break, continue, pass

# break: Breaks out of the current closest enclosing loop.
x = 0
while x < 5:
    if x ==2:
        break
    print(x)
    x += 1

# continue: Goes to the top of the closest enclosing loop.
my_string = 'Sammy'
for l in my_string:
    if l == 'a':
        continue
    print(l)

# pass: Does nothing at all.
x = [1,2,3]
for i in x:
    pass # Avoids a syntax error and is utilised as a placeholder for when you wish to come back to this line of code



# Useful Operators

# Range operator
my_list = [1,2,3]
for n in range(1,11,2):
    print(n)

print(list(range(1,11,2))) # Generator to create a list

# Enumerate function
index_count = 0
for i in 'abcde':
    print(f'At index {index_count} the letter is {i}')
    index_count += 1

index_count = 0
word = 'abcde'
for l in word:
    print(word[index_count]) # Indexing useful when dealing with an iterable like a list
    index_count += 1

# This was built into the enumerate function to do an index count automatically in the form of tuples
word = 'abcde'
for index,letter in enumerate(word): # Tuple unpacking to get elements
    print(index)
    print(letter)
    print('\n')

# Zip function: Pair up items in a list to match them together
my_list1 = [1,2,3,4,5,6]
my_list2 = ['a', 'b', 'c']
my_list3 = [100, 200, 300]

for i in zip(my_list1, my_list2, my_list3): # Can only zip until the shortest list
    print(i)

for a,b,c in zip(my_list1, my_list2, my_list3): # Can only zip until the shortest list
    print(b)

print(list(zip(my_list1, my_list2, my_list3)))

# In operator
print('x' in [1,2,3])
print('a' in 'a World')
d = {'my_key':345}
print('my_key' in d) # check for key in dictionary
print(345 in d.values()) # check for values in dictionary
print(345 in d.keys())

# Mathematical functions min, max and random library
my_list = [10,20,30,40,40,100]
print(f'The minimum value is {min(my_list)}')
print(f'the maximum value is {max(my_list)}')

# random library
from random import shuffle # shuffle a list
my_list = [1,2,3,4,5,6,7,8,9,10]
shuffle(my_list)
print(my_list)

from random import randint # grab a random integer
print(randint(0,100))

#input function
result = float(input('Favourite number:'))
print(result)



# List Comprehensions
# Unique way of quickly creating a list

# For loop method of creating a list
my_string = 'hello'
my_list = []
for i in my_string:
    my_list.append(i)
print(my_list)

# More efficient list comprehension method
my_string = 'hello'
my_list = [i for i in my_string]
print(my_list)

my_list = [i for i in 'word']
print(my_list)

my_list = [i for i in range(0,11)]
print(my_list)

my_list = [i**2 for i in range(0,11)]
print(my_list)

# Implementing if statements into list comprehension
my_list = [i**2 for i in range(0,11) if i%2 == 0] # printing square of even numbers in range
print(my_list)

# Mathematical operation as a list comprehension
celcius = [0,10,20,34.5]
fahrenheit = [((9/5)*t + 32) for t in celcius]
print(fahrenheit)

# Mathematical operation as a for loop
celcius = [0,10,20,34.5]
fahrenheit = []
for t in celcius:
    fahrenheit.append((9/5)*t + 32)
print(fahrenheit)

# if and else statments in list comprehensions
results = [x if x%2 == 0 else 'ODD' for x in range(0,11)]
print(results)

# nested loops
my_list = []
for i in [2,4,6]:
    for j in [1,10,1000]:
        my_list.append(i*j)
print(my_list)

# nested loops in list comprehension
my_list = [i*j for i in [2,4,6] for j in [1,10,1000]]
print(my_list)