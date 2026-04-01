# Collections Module
# Built into python and implements specialised data container types

# Counter
# Dictionary sub-class to count hasable objects
# Elements are stored as keys and counts of objects as values
from collections import Counter

my_list = [1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,3,3]
my_list2 = ['a','a','a','a',12,12,12,12,12]

print(Counter(my_list))
print(Counter(my_list2))
print(len(('The quick brown fox jumped over the lazy dog').split()))
print(Counter(('I never never lie').lower().split()))

letters = 'aaaabbbbbccccccddddd'
c = Counter(letters)
c.most_common(3)

# Default dictionary - e.g. assign values to a dictionary if it is not pressent
from collections import defaultdict

d = {'a':10}
print(d['a'])

d = defaultdict(lambda: 0)
d['correct'] = 100
d['WRONG']
print(d)

# Named tuple - named indices for tuple object
from collections import namedtuple

Dog = namedtuple('Dog',['age','breed','name'])
sammy = Dog(age = 5, breed = 'Husky', name = 'Sam')
print(type(sammy))
print(sammy)
print(sammy.age, sammy.breed, sammy.name)
print(sammy[0])