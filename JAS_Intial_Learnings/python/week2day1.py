#loops , Functions , modifiers 
import math 
# #factorial using for loops 
# n = int(input("Enter the no"))
# fact = 1 
# if n < 0:
#     print("Error")
# elif  n == 0:
#     print("The factorial is ",fact)
# else:
#     for i in range(n):
#         fact *= i+1
# print(fact)

# #using for while loop 

# num  = int(input("enter the no "))
# a  = 1 
# fact = 1 
# while a <= num:
#     fact *= a 
#     a += 1 
# print(fact)


# #using functiion 
# def factorial():
#     n = int(input("enter a interger "))
#     fact0 = 1 
#     if n < 0: 
#       print("error")
#     elif n == 0:
#         return fact0
#     else:
#         for i in range(1 , n+1):
#             fact0 *= i
#     print(fact0)
# result  = factorial()
# print(result)

# # # using funcn and recuricosn  
# # def rec(n):
# #     if n == 0:
# #         return 1 
# #     else:
# #         return n  * rec(n-1)
# # print(rec(5))


# #funcns recap 
# m = 123
# con = str(m)
# rev = (con[::-1])
# print(rev)
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    l1 = list(student_marks[query_name])
    
    
    #modifiers
    
    # # # # # <!-- #python modifier 

# # # # # Public access modifier in python
# # # # # In the case of the Public access modifier in python, all the members in python class are public by default. Any member declared as public can be accessed from outside the class through an object. -->

# # # # # class Teacher:
# # # # # def __init__(self,name,salary):
# # # # # self.name=name
# # # # # self.salary=salary
# # # # # t1=Teacher("Simon", 12500)
# # # # # t1.name="Sam"
# # # # # print(t1.name)

# # # # After writing the above code (public access modifier in python), Ones you will print “t1.name” then the output will appear as a “ Sam”. 
# # Here, we get the modified values, so in this way, we can modify any values.

# # # # You can refer to the below screenshot.

# # # Private access modifier in Python
# # class Teacher:
# #     def __init__(self,name,salary):
# # self.__name=name
# # self.__salary=salary
# # t1=Teacher("Simon", 12500)
# # print(t1.__name)
# 4

# So, to access the private members of a class we have name mangling of private variables. 
# Every member with a double underscore will be changed to ” object._class__variable “ and then it can be accessed from outside the class.


# class Teacher:
#     def __init__(self,name,salary):
# self.__name=name
# self.__salary=salary
# t1=Teacher("Simon", 12500)
# print(t1._Teacher__name)

# #Acess modifier in python example
# Example:

# class Teacher:
# val1 = None
# _val2 = None
# __val3 = None
# def __init__(self, val1, val2, val3):
# self.val1 = val1
# self._val2 = val2
# self.__val3 = val3
# def dispPublicMembers(self):
# print("This is public member: ", self.val1)
# def _dispProtectedMembers(self):
# print("This is protected member: ", self._val2)
# def __dispPrivateMembers(self):
# print("This is private member: ", self.__val3)
# def accessPrivateMembers(self):
# self.__dispPrivateMembers()
# class Child(Teacher):
# def __init__(self, val1, val2, val3):
# Teacher.__init__(self, val1, val2, val3)
# def accessProtectedMembers(self):
# self._dispProtectedMembers()
# obj1 = Child("Hello", "Simon", 100000)
# obj1.dispPublicMembers()
# obj1.accessProtectedMembers()
# obj1.accessPrivateMembers()
    add = sum(l1)
    res = add/len(l1)
    print('%.2f',res)
