# Generators allow us to generate a sequence of values over time rather than create an entire sequence adn hold it in memory
# When a generator function is compiled, they become an object that supports iteration protocol -> when they are called in code, they don't return a value and exit
# Generator functions wil automatically suspend and resume their generation state around their last point of value geenration
# The advantage is that instead of having to compute an entire series of values up front and it in memory, the generator computes one value, and waits until the next value is called for
# E.g. the range() function does not produce a list in memory for all the values. It keeps track of the last number and the step size

# Creating a generator

def create_cubes(n):
    result = []
    for i in range(n):
        result.append(i**3)
    return result

# We may only need one value at a time and not all the values at once
for x in create_cubes(10):
    print(x)

# Output lists is now not in memory:

def create_cubes(n):

    for i in range(n):
        yield i**3

print(create_cubes(10)) # Cannot see list - must be iterated through for the list of numbers
print(list(create_cubes(10))) # can cast as list if necessary

for x in create_cubes(10):
    print(x)

# Fibonacci sequence

# Without generators
def fib(n):
    nums = []
    a = 0
    b = 1
    for _ in range(n):
        nums.append(a)
        a, b = b, a+b
    return nums

# This is less memory efficient as values are being held in memory as a list
for num in fib(10):
    print(num)

print(fib(10))

# With generators
def gen_fib(n):
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a,b = b,a+b

for num in gen_fib(10):
    print(num)



# next function

def simple_gen():
    for x in range(3):
        yield x

# The for loop calls the next() function internally
for x in simple_gen():
    print(x)

g = simple_gen()

print(next(g))
print(next(g))
print(next(g))
print(next(g)) # This will cause a StopIteration error as the loop has ended



# iter function

s = 'Hello'
for l in s:
    print(l)

next(s) # string objects supports iteration (the for loop works) but cannot be directly iterated over

# Turn string into geenrator that you can iterate over

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))