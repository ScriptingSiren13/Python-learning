
# #1. First way of using classes(not so useful)
# class Employee:
#     pass

# emp1=Employee()
# emp2=Employee()
# # print(emp1)  #<__main__.Employee object at 0x00000229FA79E590>
# # print(emp2)  #<__main__.Employee object at 0x00000229FA79E5D0>

# emp1.first='Corey'
# emp1.last='Kardashian'
# emp1.email="CoreyK@gmail.com"
# emp1.pay=80000

# emp2.first='Kris'
# emp2.last='Jenner'
# emp2.email="KrisJ@gmail.com"
# emp2.pay=1000000
# print(emp1.email)  #CoreyK@gmail.com

#2. Second way of using classes:
# class Employee:
#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last=last
#         self.pay=pay
#         self.mail=first + "." + last + "@company.com"
# emp1=Employee('Corey','Gamble',80000)
# emp2=Employee('Test','User',60000)
# print(emp1.last)  #Gamble
# print(emp2.mail)  #Test.User@company.com

#3. Adding a method to our class:
# class Employee:
#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last=last
#         self.pay=pay
#         self.mail=first + "." + last + "@company.com"
#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)

# emp1=Employee('Corey','Gamble',80000)
# emp2=Employee('Kim','Kardashian',60000)
# print(emp1.last)  #Gamble
# print(emp2.mail)

# print(emp1.fullname())  #Corey Gamble
# print(emp2.fullname())   #Kim 

#4. If we do not use 'self as an argument in our method:
# class Employee:
#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last=last
#         self.pay=pay
#         self.mail=first + "." + last + "@company.com"
#     def fullname():
#         return '{} {}'.format(self.first,self.last)

# emp1=Employee('Corey','Gamble',80000)
# emp2=Employee('Kim','Kardashian',60000)

# print(emp1.fullname())   #TypeError: Employee.fullname() takes 0 positional arguments but 1 was given 
  
#5. Running methods using class name:
# class Employee:
#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last=last
#         self.pay=pay
#         self.mail=first + "." + last + "@company.com"
#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)

# emp1=Employee('Corey','Gamble',80000)
# emp2=Employee('Kim','Kardashian',60000)

# print(Employee.fullname(emp1))  #Corey Gamble
# print(Employee.fullname(emp2))  #Kim Kardashian


#FROM SECOND YOUTUBE CHANNEL:
class Person:
    name="Isa"
    occupation='SD'
    def info(self):
        print(f"{self.name} is a {self.occupation}")
    
a=Person()
b=Person()
c=Person()

a.name="David"
a.occupation="Engineer"

b.name='Sofia'
b.occupation='Designer'

a.info()  #David is a Engineer
b.info()  #Sofia is a Designer