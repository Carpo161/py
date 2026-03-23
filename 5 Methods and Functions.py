# Methods in build in objects

my_list = [1,2,3]
my_list.append(4) # Methods
my_list.pop()
help(my_list.insert) # help function for information on object
from platform import python_version
print(python_version())



# Functions
# Allow us to create blocks of code that can be easily executed many times without needing to rewrite the block of code

# def keyword
# by convention, function names use Snake Casing - all lowercase letters with udnerscores between words
# arguments / parameters can be passed into the function between parantheses
# this is the syntax used to create a function
''' Syntax:
def name_of_function(name):

    # Docstring explains function

    print('Hello' + name)

>> name_of_function('Jose')
>> Hello Jose

'''

# return keyword is used to send back the result of the function, instead of just printing it out
# return allows us to assign the output of the function to a new variable
# return allows us to save the result to a variable
'''
def add_function(num1,num2):
    return num1+num2

>> result = add_function(1,2)
>>
>> print(result)
>> 3
'''



# Basic Functions

def say_hello():
    print("hello")
    print('how')
    print('are you')

say_hello()
say_hello # not adding parantheses does not call function

def say_hello(name='Default'): # can use a default value in case a prameter is not provided when the function is called
    print(f'Hello {name}')

say_hello('Jose')
say_hello()

# Using the return keyword
def add_num(num1,num2):
    return num1 + num2

result = add_num(10,20) # can assign function to variable with the return keyword, which is not possible with print()
print(result)


def print_result(a,b):
    print(a+b)

def return_result(a,b):
    return(a+b)

result = print_result(10,20)
print(result) # nothing is being returned to be saved. A output is printed and then the function is closed

result = return_result(10,20)
print(result)

# To print the result and return it (save it as a variable for example):
def myfunc(a,b):
    print(a+b)
    return a+b

result = myfunc(10,20)
result

# Python is dynamically typed and the data type does not need to be specified beforehand
def sum_numbers(num1,num2): # num1 and num2 do not need to be specified as integers
    return num1 + num2

print(sum_numbers('10','20')) # this concatenates as they are strings. may need to be addressed if dealing with user inputs



# Logic with Python Functions

# Check if a number is even
def even_check(number):
    return number%2 == 0

print(even_check(20))
print(even_check(21))

# Check if any number is even inside a list
def check_even_list(num_list):
    for i in  num_list:
        if i%2 == 0:
            return True
        else:
            pass # Cannot place `return False` here as this would termiante the loop and would only check one number
    return False
print(check_even_list([2,1,3,5]))
print(check_even_list([1,3,5,2]))
print(check_even_list([1,3,5,7]))

# Return all the even numbers in a list
def return_even_list(num_list):
    even_numbers = [] # placeholder variables common at the top of function
    for i in  num_list:
        if i%2 == 0:
            even_numbers.append(i)
    if len(even_numbers) != 0:
        return even_numbers
    else:
        return 'No even numbers'

def return_even_list_concise(num_list):
    even_numbers = [n for n in num_list if n%2 == 0]
    return even_numbers or 'No even numbers'

print(return_even_list([2,1,3,5,4,6,8]))
print(return_even_list([1,3,5,2,8]))
print(return_even_list([1,3,5,7,9,11]))



# Tuple Unpacking with Functions
stock_prices = [('APPL', 200), ('GOOG', 400), ('MSFT', 100)]
for ticker,price in stock_prices:
    print(price+(0.1*price)) # 10 percent icnrease in prices

work_hours = [('Abby', 100), ('Billy', 4000), ('Cassie', 800)]
def employee_check(work_hours):
    current_max = 0
    employee_of_month = '' # placehodler values

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    return (employee_of_month, current_max)

name,hours = employee_check(work_hours)
print(f'{name} worked the most hours at {hours} hours')



# Interactions between functions
# Typically a python script contains several functions interacting with each other
# Demonstrated through a python script mimicing the 'Three Cup Monte' carnival game

from random import shuffle
example = [1,2,3,4,5,6,7]
result = shuffle(example)
print(result) # this happens in place in the list, therefore it cannot be called

# Adding some functionality to the shuffle method in order to store it as a variable
def shuffle_list(my_list):
    shuffle(my_list)
    return my_list
result = shuffle_list(example)
print(result)

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input('Pick a number: 0, 1 or 2')
    
    return int(guess)

def check_guess(my_list, guess):
    if my_list[guess] == 'O':
        print('Correct!')
        print(my_list)
    else:
        print('Wrong guess!')
        print(my_list)

# Adding some logic to ensure the order of the functions is correct
# 1) Intial list 
my_list = ['', 'O', '']

# 2) Shuffle list 
shuffled_list = shuffle_list(my_list)

# 3) User guess 
guess = player_guess() 

# 4) Check guess
check_guess(shuffled_list, guess)



# *args and **kwargs

def myfunc(a,b,c=0,d=0,e=0):
    # Returns 5% of the sum of a and b
    return sum((a,b,c,d,e)) * 0.05
print(myfunc(40,60,30))

# *args: allows us to take an arbitrary number of arguments
# can take as many arguments as the user wants and will create a tuple of arguments
# the use of 'args' is an arbitary choice but should always be used to adhere with PEP-8 guidelines
def myfunc(*args):
    return sum(args) * 0.05
print(myfunc(30,50,60,70.90,100))

def func(*args):
    for i in args:
        print(i)
print(func(10,20,30,100,400,1000))

# **kwargs
def func(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        return f'My fruit of choice is {kwargs['fruit']}'
    else:
        return 'I did not find any frit here'
print(func(fruit = 'apple', veggie = 'lettuce'))

#*args and **kwargs in combiantion
def myfunc(*args, ** kwargs): 
    print(args)
    print(kwargs)
    return f'I would like {args[0]} {kwargs['food']}'
# arguments and keyword arguments must be in the order specified in the function
print(myfunc(10,20,30,fruit='orange',food='eggs',animal='dog'))

# Functions 10: Skyline
# Original:
def myfunc(string):
    string_list = [i for i in string]
    for i,v in enumerate(string_list):
        if i%2 != 0:
            string_list[i] = string_list[i].upper()
        else:
           string_list[i] = string_list[i].lower()
    return ''.join([i for i in string_list])
            
print(myfunc('Anthropomorphism'))

# Revised from solution:
def myfunc(x):
    out = []
    for i, ch in enumerate(x):
        if i % 2 == 0:
            out.append(ch.lower())
        else:
            out.append(ch.upper())
    return ''.join(out)



# Labmda Expressions, Map and Filter

# Map function
# Applies the function to every single item or element in the list
# Function is inputted as an argument and only passed into map as map itself will execute the function, therefore, parantheses do not need to applied in the map function

def square(num):
    return num**2
my_nums = [1,2,3,4,5]

for i in map(square, my_nums):
    print(i)

# To get a list back:
print(list(map(square, my_nums)))

# Function with strings
def splicer(my_string):
    if len(my_string)%2 == 0:
        return 'EVEN'
    else:
        return my_string[0]

names = ['Andy', 'Eve', 'Sally']
print(list(map(splicer, names)))

# Filter function
# Returns an iterator yielding those items of an iterable for which when you pass in those items of the iterable, its true
# Therefore, you need to filter by a function that yields a boolean, i.e. True or False

def check_even(n):
    return  n%2 == 0

mynums = [1,2,3,4,5,6]

for n in filter(check_even, mynums):
    print(n)

print(list(filter(check_even, mynums)))

# Lambda Expression
# Useful when you intend to use a function one time and can be used in conjunction with map and filter

square = lambda n: n**2

print(square(5))
print((lambda n: n**2)(5))

my_nums = [1,2,3,4,5,6]

# Using lambda expressions with the map function
for n in map(lambda n: n**2, my_nums):
    print(n)

print(list(map(lambda n: n**2, my_nums)))

# Using lambda expressions with the filter function
for n in filter(lambda n: n%2 == 0, my_nums):
    print(n)

print(list(filter(lambda n: n%2 == 0, my_nums)))

# Grabbing the first charcter of a string with lambda 
names = ['Andy', 'Eve', 'Sally']
print(list(map(lambda i: i[::-1], names)))



# Nested Statements and Scope
# A variable name is stored in a namespace
# Scope determines the visibility of a variable to other parts of the code
'''
LEGB rule format:
L: Local — Names assigned in any way within a function (def or lambda), and not declared global in that function.
E: Enclosing function locals — Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.
G: Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.
B: Built-in (Python) — Names preassigned in the built-in names module : open, range, SyntaxError,...
'''

name = 'THIS IS A GLOBAL STRING' # name defined in global namespace
def greet ():
    name = 'Sammy' # Enclosing Function Local
    def hello():
        return f'Hello {name}' # name is not defined Locally
    return hello()

print(greet())

def greet ():
    # name = 'Sammy' # Enclosing Function Local
    def hello():
        return f'Hello {name}' # name is not defined Locally
    return hello()

print(greet())

# Local variables and global keyword

x = 50

def func(x):
    print(f'X is {x}')
    
    # Local reassignment
    x = 200 # scope of local reassignment cannot extend to global level
    print(f'I JUST LOCALLY CHANGED X TO {x}')

print(func(x))
print(x)

# To grab global x and reassign it locally:
x = 50

def func():
    global x # Grab global x
    print(f'X is {x}')
    
    # Local reassignment on a Global variable
    x = 'NEW VALUE'
    print(f'I JUST LOCALLY CHANGED GLOBAL X TO {x}')

print(x)
print(func())
print(x)

# better to reassign result of funcitn to another variable than use global keyword as makes debugging easier