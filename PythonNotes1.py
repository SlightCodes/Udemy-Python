# #-----formatted strings----------
#
# name = "Nick"
# age = 29
#
# print(f'Hi {name}. You are {age} years old.')
#
# print('hi {}. You are {} years old...'.format(name, age))
#
# print('hi {new_name}. You are {age} years old.....'.format(new_name="sally", age=60))
#
# #--------string indexes------------
#
# selfish = "01234567"
#
# print(selfish[:5]) # 0-4
# print(selfish[-1]) # 7, negative index will start at the back of the string
# print(selfish[::2]) #skip by 2
#
# #-----immutability--------
# # In memory python saves the fist instance of assignment, you can't reassign part of a string
# #the only way we can change it is to create something new
# selfish = selfish + '8' # correct syntax to create a new string
# print(selfish)
#
# #----built-in functions and methods--------
#
# greet = "hellllooooo"
# print(greet[0:len(greet)])
#
#       #.format() - This is a string method
#
# quote = "to be or not to be"
#
# print(quote.upper())
# print(quote.capitalize())
# print(quote.find('be'))
# print(quote.replace('be','me'))
#
# #challange #1 ----
#
# print("Enter your birth year\n")
#
# birth_year = int(input())
#
# current_year = 2022
#
# age = current_year - birth_year
#
# print("Your age is {}".format(age))

#-----lists-------

# li = [1, 2, 3, 4, 5]
# li2 = ['a', 'b', 'c']
# li3 = [1, 2, 'a', True]
#
# print(li[2:4])
#-----Matrix-------

# matrix = [[1,5,1],[0,1,0],[0,1,0]] #two dimensional array

# print(matrix[0][1])

#----list methods------
# basket = [1,2,3,4,5]
#
# print(len(basket))
#
# #method is owned by something and is specific to a data type
# basket.append(100)
# #new_list = basket#=basket.append(100) #This doesn't work because append changes the list in place (it doesn't produce a value it just appends 100 to the basket)
#  # new list points to basket so we can now see the 100 in new_list
# print(basket)
# #print(new_list)
#
# basket.insert(4, 500) #inset modifies the list in place, at the index of 4 we insert 500
#
# #print(new_list)
#
# #new_list = basket.extend([100, 101])
#
# print(basket)
#
# #removing
# basket.pop()
# print(basket)
# basket.pop()
# print(basket)
# basket.pop(0) #can remove using indexes
# print(basket)
# basket.remove(4)
# print(basket)

#-----list unpacking-----
# a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
#
# print(a)
# print(b)
# print(c)
# print(other)
# print(d)

#---None----
# weapons = None
# print(weapons)

#---dictionary----
# dictionary = {'a':1, 'b':2}
#
# print(dictionary['b']) #finds where b is stored in the memory and grabs 2

# my_list = [{'a':[1,2,3], 'b':'hello', 'x':True},{'a':[4,5,6], 'b':'hello', 'x':True}]
#
# print(my_list[0]['a'][2])
#

#dictionarys aren't sorted, lists are

# dictionary = {'a': [1, 2, 3], 'b': 'hello', 'x': True}
# print(dictionary['a'])
#
# #a key needs to be immutible (cannot change)
# print(dictionary.get('age')) #.get method won't throw and error if a key is invalid and returns type none if the key doesn't exist
#
# user = dict(name='NickNick') #this built in function allows you to create a dictionary
# print(user)

# user = {'basket':[1,2,3], 'greet': 'hello', 'age':20}
#
# print(user.items())
#
# #print(user.popitem()) # removes the last item on the dictionary
# print(user.update({'age':55})) #update the key in a dictionary
# print(user)

#-----Tuples-----
#like immutible lists

# my_tuple = (1,2,3,4,5) #brackets denote tuple
# print(5 in my_tuple)
# # they're more performant than lists, if you don't need a list you should use tuple
#
# new_tuple = my_tuple[1:4]
# print(new_tuple)

#-----sets-----

#unordered collections of unique objects

# my_set = {1,2,3,4,5,5} # only returns the unique items, no duplicates
# my_set.add(100)
# my_set.add(2) #2 won't be added because the set already contains this data
# print(my_set)
#
# my_list = [1,2,3,4,5,5]
# print(set(my_list)) #removed duplicate values from the list


