def make_bricks():
    # We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops
    small, large, goal = list(map(int, input('Enter the numbers of small bricks, large bricks and the goal: ').split()))
    max_large = goal // 5
    if large > max_large:
        return small >= (goal - 5*max_large)
    elif large <= max_large:
        return (5*large + small) >= goal
    return False

def make_bricks_improved(small, large, goal):
    # How many big bricks *should* we use?
    use_big = min(large, goal // 5)
    # How much length is left after using those big bricks?
    remaining = goal - use_big * 5
    # Can small bricks cover the rest?
    return remaining <= small

def lone_sum():
    # Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.
    a, b, c = list(map(int, input('Enter three integers to sum: ').split()))
    lst = [a,b,c]
    s = 0
    for i in lst:
        if len(set(lst)) == 3:
            return sum(lst)
        elif lst.count(i) == 1:
            s += i
    return s

def lucky_sum():
    # Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.
    a, b, c = list(map(int, input('Enter three integers to sum: ').split()))
    lst = [a,b,c]
    skip = False
    s = 0
    for i in lst:
        if i == 13:
            skip = True
        if not skip:
            s += i
    return s

def fibonacci():
    args = list(map(str, input('Select any number of fibonacci numbers to know its index position: ').split()))
    sequence = []
    indexes = []
    n1, n2 = 0, 1
    for _ in range(2,1001):
        sequence.append(str(n1))
        n1, n2 = n2, n1 + n2
    for i in args:
        if i in sequence:
            indexes.append(f'{i} has an index position {sequence.index(i)+1}')
    return '\n'.join(indexes)

def even_fibonacci():
    terms = int(input('Select the number of terms: '))
    s = 0
    sequence = []
    n1, n2 = 1, 2
    for _ in range(1, terms+1):
        sequence.append(n1)
        n1, n2 = n2, n1 + n2
    for i in sequence:
        if i%2 == 0:
            s += i
    return f'The sum of the even terms is {s}'

def prime_factor():
    num = int(input('Enter a number: '))
    prime = []
    x = 2
    while num > 1:
        if num % x == 0:
            prime.append(x)
            num /= x
        else:
            x += 1
    return prime

funcdict = {'1': make_bricks,
            '2': lone_sum,
            '3': lucky_sum,
            '4': fibonacci,
            '5': even_fibonacci,
            '6': prime_factor}

functions = ('''
'1': make_bricks
'2': lone_sum
'3': lucky_sum
'4': fibonacci
'5': even_fibonacci
'6': prime_factor
''')

while True:
    func_choice = input(f"\nPlease choose a function: {functions}")
    while func_choice not in [str(i) for i in range(1,7)]:
        func_choice = input(f"Sorry please select a valid function: {functions}")
    print(funcdict[func_choice]())