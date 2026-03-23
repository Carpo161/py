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

# Class Keyword and Attributes

# class is a blueprint that defines the nature of a future object --> an instance of the object can then be constructed from classes --> an instance is a specfic object created from a specific class
# classes have attributes --> an attribute is a characteristic of an object --> methods are operations you can perform on objects
class Dog():
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

# creating an instance of the dog class
my_dog = Dog(breed='Lab', name='Sammy', spots=False)
print(type(my_dog))
print(f'Name: {my_dog.name}, Breed: {my_dog.breed}, Spots: {my_dog.spots}')



# Class Object Attributes and Methods

class Dog2():
    
    def __init__(self,breed,name,spots): # creating an attribute that we want the user to define
        # the variable 'breed' is passed in and is set equal to the attribute .breed itself or in other words self.breed as self represents an instance of the object

        # Attributes
        # We take in the argument and assign it using self.attribute_name
        self.breed = breed
        self.name = name

        # Expect boolean for .spots attribute
        self.spots = spots

# creating an instance of the dog class
my_dog = Dog(breed='Lab', name='Sammy', spots=False)
print(type(my_dog))
print(f'Name: {my_dog.name}, Breed: {my_dog.breed}, Spots: {my_dog.spots}')