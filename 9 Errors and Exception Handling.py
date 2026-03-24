'''Three keywords:
- try: this is the block of code to be attempted (may lead to an error)
- except: Block of code that will execute in case there is an error in try block
- finally: a final block of code to be executed, ragardless of an error'''

def add(n1,n2):
    return n1+n2
print(add(10,20))

number1 = 10
number2 = input('Please provide a number: ')
print(add(number1,number2))
print("Something happened!") # this code will not run as the script stops running after the error




try:
    # want to attempt this code
    # may have an error
    result = 10 + '10'
except:
    print("Hey, it looks like you arent adding correctly!")
else:
    print('Add went well!')
    print(result)

print(result) # can still execute this code and the program was not shut down due to an error



try:
    f = open('testfile','r')
    f.write("Write a test file")
except TypeError:
    print("There was a type error!")
except OSError:
    print("Hey, you have an OS Error")
except:
    print("All other exceptions!")
finally:
    print("I always run")



# Using try, except, finally in a function with user input

def ask_for_int():

    while True:
        try:
            result = int(input('Please provide a number: '))
        except:
            print("Sorry, that is not a number")
        else:
            print("Yes, thank you")
            break
        finally:
            print("I am going to ask you again. \n")
            print("I will always run at the end")

ask_for_int()