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
    add = sum(l1)
    res = add/len(l1)
    print('%.2f',res)