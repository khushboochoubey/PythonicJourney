# phrase = ['printed', 'with', 'a', 'dash', 'in', 'between']
# for word in phrase:
#      print(word, end='-')

# print('cats', 'dogs', 'mice', sep=',')

# print('What is your name?')   # ask for their name
# my_name = input()
# print('Hi, {}'.format(my_name))

# my_name = input('What is your name? ')  # default message
# print('Hi, {}'.format(my_name))

# print('Hi', my_name)

# a = [1, 2, 3]
# if len(a) > 0: 
#     print("the list is not empty!")

# today_responses = [200, 300, 404, 500]
# match today_responses:
#      case [a]:
#              print(f"One response today: {a}")
#      case [a, b]:
#              print(f"Two responses today: {a} and {b}")
#      case [a, b, *rest]:
#              print(f"All responses: {a}, {b}, {rest}")

# spam = 0
# while spam < 5:
#      print('Hello, world.')
#      spam = spam + 1

# pets = ['Bella', 'Milo', 'Loki']
# for pet in pets:
#     print(pet)

# for i in range(5):
#      print(f'Will stop at 5! or 4? ({i})') 
# for i in range(0, 10, 2):
#          print(i)


# global_variable = 'I am available everywhere'

# def some_function():
#      print(global_variable)  # because is global
#      local_variable = "only available within this function"
#      print(local_variable)

# def spam():
#      global eggs
#      eggs = 'spam'

# eggs = 'global'
# spam()
# print(eggs)

# This function:

# >>> def add(x, y):
# ...     return x + y
# ...
# >>> add(5, 3)
# # 8
# Is equivalent to the lambda function:

# >>> add = lambda x, y: x + y
# >>> add(5, 3)
# # 8

# furniture = ['table', 'chair', 'rack', 'shelf']

# for index, item in enumerate(furniture):
#    print(f'index: {index} - item: {item}')

# Loop in Multiple Lists with zip()
# >>> furniture = ['table', 'chair', 'rack', 'shelf']
# >>> price = [100, 50, 80, 40]

# >>> for item, amount in zip(furniture, price):
# ...     print(f'The {item} costs ${amount}')
# The table costs $100
# The chair costs $50
# The rack costs $80
# The shelf costs $40