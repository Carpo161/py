# OOP allows programmers to create their own objects that have methods and attributes
# These methods act as functions taht use information about the object, as well as the object itself to return results, or change the current object
# allows you to create code that is repeatable and organised
# commonly repeated tasks and objects can be defined with OOP as functions will not suffice organisation and repeatability of larger scripts
# name of classes follows camel casing
''' Syntax:
class NameOfClass():
    def __init__(self,param1,param2):
        self.param1 = param1
        self.param2 = param2
    
    def some_method(self):
        #perform some action
        print(self.param1)'''

# 1. Class Keyword and Attributes
# 2. Class Object Attributes and Methods

# class is a blueprint that defines the nature of a future object --> an instance of the object can then be constructed from classes --> an instance is a specfic object created from a specific class
# classes have attributes --> an attribute is a characteristic of an object --> methods are operations you can perform on objects
class Dog():
    # Define Class Object Attribute at class object level and not at a particular instance
    # These are the same for any instance of the class
    species = 'mammal'


    # init is the constructor for a class and will be called automatically when you create an instance of the class
    # the self keyword represents the instance of the object itself
    # the self keyword is passed by most OOP languages to the methods defined on an object but has to be declared explicitly on python
    def __init__(self,breed,name,spots): # creating an attribute that we want the user to define
        # the variable 'breed' is passed in and is set equal to the attribute .breed itself or in other words self.breed as self represents an instance of the object

        # Attributes
        # We take in the argument and assign it using self.attribute_name
        self.breed = breed
        self.name = name

        # Expect boolean for .spots attribute
        self.spots = spots

    # 3. Methods
    # Methods are functions defined inside the body of the class and are used to perform operations that can utilize attributes of the object we created
    # They can be thought of as functions acting on an object that take the object itself into account through the use of self keyword
    # They belong to the objects they act on
    # Operations / Actions -> Methods

    def bark(self, number):
        print(f'Woof! My name is {self.name} and the number is {number}') # Need to pass in particular instance of name as it an attribute of the class

# creating an instance of the dog class
my_dog = Dog('Lab', 'Sammy', False)
print(type(my_dog))
print(f'Name: {my_dog.name}, Breed: {my_dog.breed}, Spots: {my_dog.spots}, Species = {my_dog.species}')
my_dog.bark(10) # Attributes do not need to be executed but methods do

# Putting it all together

class Circle():
    # Class Object Attribute - true for any instance of the class
    pi = 3.14

    def __init__(self,radius=1): # The radius has a default value of 1
        self.radius = radius
        self.area = self.pi*(radius**2) # An attribute does not necessarily have to defined from a particular parameter call in OOP
        # self.area = Class.pi*(radius**2) --> Can use NameOfClass.classobjectattribute for clarity
    
    # Method
    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle()
print(f'The circle with radius {my_circle.radius} has a circumference of approx. {my_circle.get_circumference()} and an area of approx. {my_circle.area}')



# Inheritance
# Inheritance is a way to form new classes using classes that have already been defined -> can reuse code that you have worked on and reduce the complexity

# Base Class
class Animal():
    def __init__(self):
        print('ANIMAL CREATED')
    
    def who_am_i(self):
        print('I am an animal')
        return ''
    
    def eat(self):
        print('I am eating')
        return ''

# Derived Class
class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog Created')

    # Overwrite one of older methods
    def who_am_i(self):
        print('I am a dog')
        return ''
    
    def eat(self):
        print('I am a dog and eating')
        return ''

    # Add on methods
    def bark(self):
        print('Woof!!')
        return ''

my_animal = Animal()
my_dog = Dog()
print(my_dog.eat())
print(my_dog.who_am_i())
print(my_dog.bark())



# Polymorphism
# Refers to how Different object classes can share the same method name and methods can be called from the same place even though a variatey of objects might be passed in

class Dog():
    
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"

class Cat():
    
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"
    
niko = Dog('Niko')
felix = Cat('Felix')

print(niko.speak())
print(felix.speak())

# Demonstration of Polymorphism - can use method for both classes in the same function as method name is the same
# Can obtain object specific results from the same method call

for pet_class in [niko,felix]:
    print(type(pet_class))
    print(pet_class.speak())

def pet_speak(pet):
    print(pet.speak())

pet_speak(felix)
pet_speak(niko)

# Abtracted Classes and Inheritance is more common practice
# An abstract class is one that never expects to be instantiated / not expected to create an instance of the class
# Designed to serve as a base class

# Abtract Method

# Create a Base class to inherit the Animal class and overwrite the speak method
class Animal():

    def __init__(self,name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method')

class Dog(Animal):

    # DO not need constructor for class

    def speak(self):
        return self.name + " says Woof!"
    
class Dog(Animal):

    # DO not need constructor for class

    def speak(self):
        return self.name + " says Meow!"

fido = Dog('Fido')
isis = Dog('Isis')
print(f'{fido.speak()} and {isis.speak()}')

my_animal = Animal('Fred')
my_animal.speak()



# Special (Magic/Dunder) Methods

# How to use build in python functions (e.g. len(), print()) on user defined object

class Sample():
    pass

my_sample = Sample()
print(len(my_sample)) # Type error arises

class Book():

    def __init__(self,title,author,pages): # the __init__ special method is called automaticlaly when you create the object
        
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self): # special method for strings --> returns back a string representation to print user defined objects --> if a function asks for a string representation of the book class, it will return what this method returns
        return f'{self.title} by {self.author}'
    
    def __len__(self): # special method for len function
        return self.pages
    
    def __del__(self): # Function runs when you an delete instance of the class
        print('A book object has been deleted')

b = Book('Python rocks','Jose',200)
print(b) # print function calls for the string representation of b
print(len(b))

# Delete a variable from memory:
del b
print(b)