#geeks for geeks problems 

def palindrome(a):
      
    # finding the mid, start
    # and last index of the string
    mid = (len(a)-1)//2     
    start = 0                
    last = len(a)-1
    flag = 0
 
    # A loop till the mid of the
    # string
    while(start <= mid):
  
        # comparing letters from right
        # from the letters from left
        if (a[start]== a[last]):
             
            start += 1
            last -= 1
             
        else:
            flag = 1
            break;
             

    if flag == 0:
        print("The entered string is palindrome")
    else:
        print("The entered string is not palindrome")
         
#swap
def swapPositions(lis, pos1, pos2):
    temp=lis[pos1]
    lis[pos1]=lis[pos2]
    lis[pos2]=temp
    return lis
# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3
 
print(swapPositions(List, pos1-1, pos2-1))

#sum of sq no
def squaresum(n):
     
    sm = 0
    for i in range(1, n+1):
        sm = sm + (i * i)
 
    return s
n = 4
print(squaresum(n))

#print ascii
c = 'g'
print("The ASCII value of '" + c + "' is", ord(c))


def PrintNumber(N, Original, K, flag):
    #print the number
    print(N, end = " ")
     
     
    if (N <= 0):
        if(flag==0):
            flag = 1
        else:
            flag = 0

    if (N == Original and (not(flag))):
        return
    
     
    if (flag == True):
        PrintNumber(N - K, Original, K, flag)
        return
     
    # second case (Addition )
    if (not(flag)):
        PrintNumber(N + K, Original, K, flag);
        return
     
N = 80
K = 9
PrintNumber(N, N, K, True)
 