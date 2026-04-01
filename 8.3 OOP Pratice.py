class Animal:
    pass

class Dog(Animal):
    pass

class Puppy(Dog):
    pass

class Cat:
    pass

def subclass():
    clas = input('Class: ')
    sub_class = input('Subclass: ')
    return issubclass(sub_class, clas)

subclass()