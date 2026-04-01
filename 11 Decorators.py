def hello():
    return "Hello!"

greet = hello # assign greet to hello function object
print(greet())

del hello
print(greet()) # greet can still be called even after deleting hello
hello()

# Functions are objects that can be passed into other objects


# Calling functions within another function or passing functions into other functions

def hello(name='Jose'):
    print('The hello() function has been executed!')

    # Greet and welcome are defined inside the hello function which means their scope is limited to the hello function
    # therefore, they can only be executed within hello
    def greet(): # greet() is defined within hello, it has not been called here
        return '\t This is the greet() function inside hello!'
    
    def welcome():
        return '\t This is welcome() function inside hello!'
    
    print('I am going to return a function')

    # Returning a function within another function
    if name == 'Jose':
        return greet
    else:
        return welcome

my_new_func = hello()

# Greet function has been returned from hello()
print(my_new_func())



# Return function and then execute it
def cool():

    def super_cool():
        return 'I am very cool!'
    
    return super_cool

some_func = cool()
print(some_func())



# Passing in a function as an argument into another function

def hello():
    return 'Hi Jose'

def other(some_defined_func):
    print('Other code runs here!')
    print(some_defined_func())

other(hello) # hello has been passed in as a raw function and not been executed as we want the other() function to execute it



# Creating a decorator

def new_decorator(original_func):
    def wrap_func(): # wrap_func represents extra functionality that we want to 'decorate' the original function with

        print('Some extra code, before the original function')

        original_func() # call / execute original function that was passed in

        print('Some extra code, after the original function')
    
    return wrap_func

def func_needs_decorator():
    print("I want to be decorated!")

decorated_func = new_decorator(func_needs_decorator)
print(decorated_func())

# Line 84 can be written more succintly
@new_decorator # commenting this out will preserve func_needs_decorator
def func_needs_decorator(): # this function is passed into new_decorator() as the original_func parameter and return wrap_func version
    print("I want to be decorated!")

func_needs_decorator()