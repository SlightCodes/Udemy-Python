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
