from tkinter import TRUE


mystring = "abcdefhjijk"
#Output final character
print(mystring[-1])

#Output a sequence of characters
print(mystring[2:4])
print(mystring[:4])
print(mystring[::])

#Output a sequence of characters specifying the steps
print(mystring[::2])

#Reverse a string
print(mystring[::-1])



#Two methods of print formatting are (1) .format() and (2) f-strings

#(1) .format() method
print('This is a string {}'.format('INSERTED'))
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

#(1) Float formatting "{value:width.precision f}"
result = 100/777
print("The result was {0:1.3f}".format(result))

#(2) f-strigns method
name = "Jose"
print(f'Hello, his name is {name}')
name = "Sam"
age = 3
print(f'{name} is {age} years old.')

#(2) Float formatting with f-strings
result = 10000/777
print(result)
print(f'The result was {result:{1}.{3}}') #precison is total number of digits in f-strings
print(f'The result was {result:1.3f}') #to specify number of digits following the decimal, the .format() syntax can be used



#Lists

my_list = [1,2,3]
my_list = ['STRING', 100, 23.2]
print(len(my_list))

#Indexing and Slicing
my_list = ['one', 'two', 'three']
print(my_list[1:])
another_list = ['four', 'five']
print(new_list := my_list + another_list)
print(new_list)

#Mutable
new_list[0] = 'ONE ALL CAPS'
new_list.append('six')
print(new_list)
popped_item = new_list.pop(0)
print(new_list,
      popped_item)

new_list = ['a', 'e', 'x', 'b']
num_list = [4, 1, 8, 3]
new_list.sort(); num_list.sort()
print(new_list, '\n', num_list)
new_list.reverse()
print(new_list)



#Dictionaries
#Use curly braces and colons to signify the keys and associateed values: {'key1':'value1', 'key2':'value2'}

my_dict = {'apple':2.99, 'oranges':3.99}
print(my_dict['apple'])

d = {'k1':123, 'k2':['a', 'b', 'c'], 'k3':{'insideKey':100}}
print(d['k2'])
print(d['k3']['insideKey']) # call an element from a dictionary within a dictionary
print(d['k2'][2].upper()) # call an element from a list within a dictionary and make it uppercase with a list method

d['k4'] = 300 # can add or overwrite key values with d['k3'] = 300
print(d)

#Dictionary methods

print(d.keys(), d.values(), d.items())



#Tuples
#Similar to lists but are immutable

t = ('one', 2, 2, 33.3)
print(f'{type(t)} {len(t)}')
print(t[-1])
print(f'{t.count(2)} {t.index(2)}') # .index method only returns the first index location of the element



#Sets
#Unordered collections of unique elements (one representative of same object)

my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(2) # Must be a unique element
my_set.update([1, 2, 4, 5]) # Add elements from any iterable into a set

lst = [1, 1, 1, 2, 2, 2, 2, 3, 3]
print(set(lst)) # Turns data type into a set of unique elements
print(set('Mississippi'))



#Booleans
#Operatars that allow you to convey True or False statements

a = True
print(a)
print(1 > 2)
b = None # None can be used as a placeholder for an object that we do not want to reassign yet