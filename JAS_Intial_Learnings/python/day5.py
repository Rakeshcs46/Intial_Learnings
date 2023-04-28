# #geeks for geeks problems 

# def palindrome(a):
      
#     # finding the mid, start
#     # and last index of the string
#     mid = (len(a)-1)//2     #you can remove the -1 or you add <= sign in line 21 
#     start = 0                #so that you can compare the middle elements also.
#     last = len(a)-1
#     flag = 0
 
#     # A loop till the mid of the
#     # string
#     while(start <= mid):
  
#         # comparing letters from right
#         # from the letters from left
#         if (a[start]== a[last]):
             
#             start += 1
#             last -= 1
             
#         else:
#             flag = 1
#             break;
             
#     # Checking the flag variable to
#     # check if the string is palindrome
#     # or not
#     if flag == 0:
#         print("The entered string is palindrome")
#     else:
#         print("The entered string is not palindrome")
         
# #swap
# ef swapPositions(lis, pos1, pos2):
#     temp=lis[pos1]
#     lis[pos1]=lis[pos2]
#     lis[pos2]=temp
#     return lis
# # Driver function
# List = [23, 65, 19, 90]
# pos1, pos2 = 1, 3
 
# print(swapPositions(List, pos1-1, pos2-1))

# #sum of sq no
# def squaresum(n):
     
#     sm = 0
#     for i in range(1, n+1):
#         sm = sm + (i * i)
 
#     return s
# n = 4
# print(squaresum(n))

# #print ascii
# c = 'g'
# print("The ASCII value of '" + c + "' is", ord(c))


# ef PrintNumber(N, Original, K, flag):
#     #print the number
#     print(N, end = " ")
     
#     # change flag if number
#     # become negative
     
#     if (N <= 0):
#         if(flag==0):
#             flag = 1
#         else:
#             flag = 0
         
#     # base condition for
#     # second_case (Adding K)
     
#     if (N == Original and (not(flag))):
#         return
     
#     # if flag is true
#     # we subtract value until
#     # number is greater than zero
     
#     if (flag == True):
#         PrintNumber(N - K, Original, K, flag)
#         return
     
#     # second case (Addition )
#     if (not(flag)):
#         PrintNumber(N + K, Original, K, flag);
#         return
     
# N = 20
# K = 6
# PrintNumber(N, N, K, True)
 