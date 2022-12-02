# def increment(n):
#     n = n + 1
#     return n
#
# print(increment(0))

#------------------------------

#
# def dis(price, discount):
#
#     i = price * (discount/100)
#     FinalPrice = price - i
#     return print("{:.2f}".format(FinalPrice))
#
# dis(50, 50)

#-------------------------------

# def stutter(word):
#
#     firstTwo = word[:2]
#
#     return print("{}... {}... {}?".format(firstTwo, firstTwo, word))
#
# stutter("incredible")

# class Circle():
#     def __init__(self, r):
#         self.r = r
#
#         self.PI = 3.141592653589793
#
#     def getArea(self):
#         return print('{0:.16f}'.format(self.PI*self.r**2))
#
#     def getPerimeter(self):
#         return (print('{0:.16f}'.format(2*self.PI*self.r)))
#
# circy = Circle(11)
# circy.getArea()
#
# circy1 = Circle(4.44)
# circy1.getPerimeter()

# class Player:
#     def __init__(self, name, age, height, weight):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight
#
#     def get_age(self):
#         return print("{} is age {}".format(self.name, self.age))
#
#     def get_height(self):
#         return print("{} is {}cm".format(self.name, self.height))
#
#     def get_weight(self):
#         return print("{} weighs {}kg".format(self.name, self.weight))
#
# p1 = Player("David Jones", 25, 175, 75)
#
# p1.get_age()
# p1.get_height()
# p1.get_weight()
#----------------------------------------------------

# class Employee():
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#
#     def fullname(self):
#         return print("{} {}".format(self.fname, self.lname))
#
#     def email(self):
#         return print("{}.{}@company.com".format(self.fname, self.lname))
#
#     def firstname(self):
#         return print(self.fname)
#
# emp_1 = Employee("John", "Smith")
# emp_2 = Employee("Mary",  "Sue")
# emp_3 = Employee("Antony", "Walker")
#
# emp_1.fullname()
# emp_1.email()
# emp_1.firstname()
#
# emp_2.fullname()
# emp_2.email()
# emp_2.firstname()
#
# emp_3.fullname()
# emp_3.email()
# emp_3.firstname()

#----------------------------------------------------