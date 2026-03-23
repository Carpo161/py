import math
import random
import collections

print("CO\N{subscript eight}")

# Prime or Not
def amIPrime():
  n = int(int(input('Select a number to check if it is prime: ')))
  if n == 1:
    print("1 ISN'T A PRIME NUMBER GET SOME HELP")
    return
  if n == 2:
    print("Yes, 2 is a prime number.")
    return
  for i in range(2,math.ceil(math.sqrt(n)) + 1):
    if n % i == 0:
      print(n, "is not a prime number.")
      break
    else:
      if i == math.ceil(math.sqrt(n)):
        print(n, 'is a prime number.')

isPrime = True
def primeOrNot(n, isPrime):
  if isPrime:
    print(n, "is a prime number")

# Fibonacci Sequence:
def fibonacci():
  fib = []
  num1 = int(input("Select a starting number: "))
  num2 = int(input("Select the second number: "))
  num3 = int(input("Select the number of terms: "))
  print("The first", num3, "terms of the Fibonacci sequence starting with", num1, "and", num2, "are:")
  for i in range(num3 + 1):
    fib.append(str(num1)) ##print(num1)
    sum = num1 + num2
    num1 = num2
    num2 = sum
  print(", ".join(fib))

# Fibonacci Sequence that makes a nicer pattern than the other when you request a large number of terms:
def fibonacciPretty():
  fib = []
  num1 = int(input("Select a starting number: "))
  num2 = int(input("Select the second number: "))
  num3 = int(input("Select the number of terms: "))
  print("The first", num3, "terms of the Fibonacci sequence starting with", num1, "and", num2, "are:")
  for i in range(num3 + 1):
    fib.append(str(num1)) ##print(num1)
    sum = num1 + num2
    num1 = num2
    num2 = sum
  print(fib)

# Print the sum of numbers from 1 to a given number
def sumOfNumbers():
  sum = 0
  number = int(input("Enter a number: "))
  for n in range(1, number + 1):
    sum = sum + n
  print("The sum of numbers from 1 to", number, "is", sum)

# Multiplication table of any given number
def multiplicationTable():
  number = int(input("Mupltiplication table of: "))
  for n in range(1, 11):
    print(number, "*", n, "=", n*number)

# Count the total number of digits in a number
def numOfDigits():
  number = int(input("Enter a number: "))
  counter = 0
  while number != 0:
    number = number // 10
    counter = counter + 1
  print("The number of digits in the number is:", counter)

# Display all prime numbers within a range
def prime1():
  start = int(input("Enter a start number: "))
  end = int(input("Enter an end number: "))
  for n in range(start, end + 1):
    isPrime = True
    for i in range(2,n):
      if n % i == 0:
        isPrime = False
        break
    primeOrNot(n, isPrime)

# Display all prime numbers within a range, better version

def prime2():
  prime = []
  count = 0
  start = int(input("Enter a start number: "))
  end = int(input("Enter an end number: "))
  for n in range(start, end + 1):
    if n == 2:
      prime.append(str(n))
      count += 1
    for i in range(2,math.ceil(math.sqrt(n)) + 1):
      if n % i == 0:
        break
      else:
        if i == math.ceil(math.sqrt(n)):
          prime.append(str(n))
          count += 1
  print('The', count, 'prime numbers between', start, "and", end, "are:")
  print(", ".join(prime))

# https://stackoverflow.com/questions/12495218/using-user-input-to-call-functions

def factors():
  factors = []
  number = int(input("Enter a number: "))
  for i in range(1, number + 1):
    if number % i == 0:
      factors.append(str(i))
  if factors[0] == "1" and factors[1] == str(number) and len(factors) == 2:
    print(number , "is a prime number.")
  else:
    print("The" , len(factors) , "factors of", number, "are: ")
    print(", ".join(factors))
  
def primeFactors():
  n = int(input("Enter a number: "))
  i = 2
  factors = []
  while i * i <= n:
      if n % i:
          i += 1
      else:
          n //= i
          factors.append(str(i))
  if n > 1:
      factors.append(str(n))
  print(", ".join(factors))



def factorial():
  f = 1
  n = int(input('Enter a number: '))
  if n == 0:
    print("The factorial of 0 is 1")
  for i in range(1, n+1):
    f = f * i
  print(str(n) + '! =', f)


# Simple Recursive function - factorials

def factorialRec():
  def factorialRec(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n * factorialRec(n-1)

#def factorialRec():
#  n = int(input('Enter a number: '))
#  def factorialRecHelper(n):
#    if n == 0:
#        return 1
#    if n == 1:
#        return 1
#    else:
#        return n * factorialRec(n-1)
#    print(str(n) + '! =', factorialRecHelper(n))


# Recursion: Print all possible strings of length k that can be formed from a set of n characters

# def printAllKLength():

def hangman():
  words = ["abruptly", "absurd", "abyss" , "affix", "askew", "avenue", "awkward", "axiom", "azure",  "crypt" , "cycle", "dizzying", "duplex", "dwarves", "embezzle", "galaxy", "larynx"]
  word = random.choice(words)
  display = ""
  while display != word:
    print("The word is", len(word), " letters long")
    while len(display) < len(word):
      display = display + "_"
    print(display)
    guess = input("Guess a letter: ")
    if guess in word:
      for i in range(len(word)):
        if word[i] == guess:
          display.replace(i, guess)

# my_list = [10, 12, 14, 10, 16, 14, 18]

# set to store duplicate elements
# duplicate = set()

#for num in my_list:
    # count number of times element appears in the list
 #   if my_list.count(num) > 1:
  #      duplicate.add(num)

#print(duplicate)

functions = """
- 1: amIPrime
- 2: fibonacci
- 3: fibonacciPretty - Gives a nicer-looking pattern if you make the number of terms large
- 4: sumOfNumbers
- 5: multiplicationTable
- 6: numOfDigits
- 7: prime1
- 8: prime2 - Prints in a nicer way
- 9: factors
- 10: primeFactors
- 11: factorial
- 12: factorialRec
- 13: hangman
"""

funcDict = {"1":amIPrime,
            "2":fibonacci,
            "3":fibonacciPretty,
            "4":sumOfNumbers,
            "5":multiplicationTable,
            "6":numOfDigits,
            "7":prime1,
            "8":prime2,
            "9":factors,
            "10":primeFactors,
            "11":factorial,
            "12":factorialRec,
            "13":hangman
           }

while True:
  uInput = input("\n" + "Choose a function between 1 and 10: " + functions + "\n")
  funcDict[uInput]()

# uInput = input("Enter a function name: ")
# funcDict[uInput]()