# is_old = True
# is_licenced = True
#
# if is_old and is_licenced:
#     print("you're old enough to drive and you have a licence")
# else:
#     print('You\'re not of age!')

#------------Ternary operator-------------------------------

# is_friend = True
# can_message = "message allowed" if is_friend else "not allowed to message"
#
# print(can_message)
#
# while is_friend is True:
#     print("can message")
#     break
# else:
#     print('can\'t message')

#-------- is vs == ---------------------

# print(True == 1)
# print('' == 1)
# print([] == 1)
# print(10 == 10.0)
# print([] == [])

#is actually checks the location in memory if the value is the same
# print(True is True)
# print('' is 1)
# print([] is 1)
# print(10 is 10.0)
# print([] is []) #each new list is added somewhere in memory, this will result to false becase they're 2 completely different lists in memory
#

#------------loops------------------

# for item in (1,2,3,4,5):
#     for x in ['a','b','c']:
#         print(item, x)

#iterable - list, dictionary, tuple, set, string
#iterated - one by one check each item in the collection

# user = {'name': "Golem", 'age': "5006", 'can_swim': False}
#
# for key, value in user.items():
#     print(key, value)
#
# for item in user.values():
#     print(item)
#
# for item in user.keys():
#     print(item)
#
# for item in 50:
#     print(item)

#-----tricky counter --------

# my_list = [1,2,3,4,5,6,7,8,9,10]
#
# total = 0
#
# for number in my_list:
#     total = total + number
#     print(total)
# print(total)

#------range-----------

# print(range(100))
# # _ isn't really a variable but indicates that we don't care what the variable is (maybe we don't need a variable)
# for _ in range(10, 0, -2):
#     print(_)
#
# for _ in range(2):
#     print(list(range(10)))

#------enumerate----------
#
# for i,char in enumerate('Hellloooo'): #prints the index of each item
#     print(i,char)
#
# for i,char in enumerate([1,2,3]):
#     print(i,char)
#
# for i,char in enumerate(list(range(100))):
#     print(i,char)
#     if char == 50:
#         print(f'index of 50 is {i}')

#---------while loop----------

# i = 0
#
# while i < 50:
#     i += 1
# else:
#     print('done with all the work')

#-----more on loops---------------
# my_list = [1,2,3]
#
#
# for item in (my_list):
#     print(item)
#
# i = 0
#
# while i < len(my_list):
#     print(my_list[i])
#     i += 1

# while True:
#     response = input("say something:")
#     if (response == 'bye'):
#         break

#----our fist GUI-------

picture = [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]
]

i = 0

#my way
# for nestedList in picture:
#         for pixel in nestedList:
#             if pixel == 0:
#                 pixel = ' '
#             else:
#                 pixel = '*'
#             print(pixel, end='')
#         print("")

#instructor way

# for row in picture:
#     for pixel in row:
#         if (pixel == 1):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print("")



#print(picture[0])

#------check for duplicates in a list--------

# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# some_list.sort()
#
# duplicates = []
#
# for duplicate in some_list:
#     if some_list.count(duplicate) > 1:
#         if duplicate not in duplicates:
#             duplicates.append(duplicate)
#
# print(duplicates)

#-------functions------------

# def say_hello():
#     print("hello")
# say_hello()
# say_hello()

#-----arguments and parameters------

#parameters - positional
# def say_hello(name, emoji):
#     print(f"hello {name} {emoji}")
#
# #arguments - positional
# say_hello("Nick", ":)") # call, invoking
# say_hello("Andrei", ":)")
# say_hello("Emily", ":)")

#keyword arguments
# say_hello(emoji=":)", name='Nick')

#default parameters
# def say_hello(name = 'Darth Vader', emoji=':0'):
#     print(f"hello {name} {emoji}")
#
# #arguments - positional
# say_hello("Nick", ":)") # call, invoking
# say_hello("Andrei", ":)")
# say_hello("Emily", ":)")
# say_hello()
# say_hello("timmy")

#-------return---------
# def sum(num1, num2):
#     def another_function(num1, num2):
#         return num1 + num2 # must use return so that you can exit the function
#     return another_function(num1, num2)
# # a function should do 1 thing really well, a function should return something
#
# total = sum(10, 20) #you can pass additional arguments and store them in variables
# print(total)

#---------methods vs functions------------

#methods are owned by an object or a datatype

#------docstrings ---------

# def test(a):
#     '''
#     Info: this function test and prints param a
#     '''
#     print(a)
# print(test.__doc__)

#-------clean code-----------

# def is_even(num):
#     return num % 2 == 0
#
# print(is_even(8))


#----*args & *kwargs--------
#
# def super_func(name, *args, i='hi', **kwargs): #adding * allows you to enter any number of positional arguments
#     total = 0
#     print(args) #creates a tuple
#     print(kwargs) #creates a dictionary
#     for items in kwargs.values():
#         total += items
#     return sum(args) + total
#
# print(super_func('Nick', 1,2,3,4,5, num1=5, num2=10))
#
# #Rule: first we have our params, then *args, default parameters, then **kwargs

#----------functions exercise---------

# def highest_even(li):
#     evens = []
#
#     for even in li:
#         if even % 2 == 0:
#             evens.append(even)
#     return max(evens)
#
#
#
# print(highest_even([10,2,3,4,8,11]))

#-----walrus operator--------

#assigns values to variables as a part of a larger expression

# a = 'hellloooooooo'
#
# if ((n := len(a)) > 10): #does not work with the current version of python installed
#     print(f"too long {len(n)} elements")

#--------scope---------
#scope - what variables do I have access to

# def sum_func():
#  total = 100 #global scope
#
# print(total) #total is no longer a part of the scope

# a = 1
# def parent():
#     a = 10 #parent function, we create a new function confusion, we're returning a, it will check the child function and then go up a level to check the parent function for the variable
#     def confusion():
#         return a
#     return confusion()
#
# print(a)
# print(parent())
#
# #1 - start with local
# #2 - Parent local?
# #3 - Global
# #4 - built in python functions.

# a = 10
#
# def confusion(b): #parameters are considered local variables
#     print(b)
#     a = 90
#
# confusion(300)

# total = 0
#
# def count(): #we must declare global if we want to use the outiside total variable, otherwise the function would reset everytime we ran the count function and it would equal 1 (if total is declared inside of the function)
#     global total #we can also create total as the parameter
#     total+= 1
#     return total
#
# count()
# count()
# print(count())
total = 0

# def count(total):  #we can also create total as the parameter
#     total+= 1
#     return total
#
#
# print(count(count(count(total)))) #works without using the global keyword
#

#-----non local keyword------

# def outer():
#     x = "local" #variable is local to the outer function
#     def inner():
#         nonlocal x # modified the scope with the nonlocal keyword
#         x = 'nonlocal'
#         print("inner", x)
#     inner()
#     print("outer", x)
# outer()

#------OOP---------
#everything is built by class keywords
#OOP allows us to go beyond the data types that python gives us
#up until this point we have only written procedural code

# class BigObject: #class
#     pass #code
#
# obj1 = BigObject()
#
# print(type(obj1))

#class is a blueprint that can be instantiated into different instances (objects)

#----creating our own objects------

# class PlayerCharacter:
#     membership = True #class object attribute (static no dynamic)
#     def __init__(self, name='anon', age=0): #this init method is a special method, the two underscores indicate a dunder method (often called a constructor method).
#                       #self refers to the player character, we want self.name to = whatever the parameter is
#        if (age > 18):
#         self.name = name  #self allows us to reference something that hasn't been created yet.
#         self.age = age #name and age are both attributes
#     def run(self):
#         print('run')
#         return 'done'
#
#     def shout(self):
#         print(f'my name is {self.name}')
#
# player1 = PlayerCharacter('Cindy', 44)
# player2 = PlayerCharacter('Tom', 21)
# player2.attack = 50 # create method attack
#
# print(player1) #able to use one blueprint to create two different players in different locations of memory
# print(player2.shout())

#----OOP Exercise------

#Given the below class:

# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# # 1 Instantiate the Cat object with 3 cats
#
# cat_1 = Cat('Bhoori',6)
# cat_2 = Cat(name='Skyee',age=5)
# cat_3 =Cat('Shori',16)
# # 2 Create a function that finds the oldest cat
#
# def age_finder(cats_obj):
#     '''Pass cats as an object a list'''
#     cat_names=[]
#     ages=[]
#
#     for cat in cats_obj:
#         cat_names.append(cat.name)
#         ages.append(int(cat.age))
#     print(f"{cat_names[ages.index(max(ages))]} is the oldest cat with {max(ages)} years")


# 3 Print out: "The oldest cat is x years old.". x will be the oldest \
# cat age by using the function in #2
# age_finder([cat_1,cat_2,cat_3])

#------@classmethod, @staticmethod------

# class PlayerCharacter:
#     membership = True
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def shout(self):
#         print(f'my name is {self.name}')
#
#     @classmethod #we can use cls to instantiate an object inside of the function (cls is the player character)
#     def adding_things(cls, num1, num2):
#         return cls('Teddy', num1 + num2)
#
#     @staticmethod  # we can use cls to instantiate an object inside of the function (cls is the player character)
#     def adding_things(cls, num1, num2):
#         return cls('Teddy', num1 + num2)
#
#
# player1 = PlayerCharacter('Tom', 20)
# player3 = PlayerCharacter.adding_things(2,3) #cls is the 3rd hidden argument in the syntax error, unless we add an additional arg in the function
#
# print(player3.name) #created an instance of a player using @classmethod