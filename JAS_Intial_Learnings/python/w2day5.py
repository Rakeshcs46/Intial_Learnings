
test_list = [[3, 4, 6, 2], [3, 4, 9, 1], [8, 5, 4, 7], [9, 1, 2, 3]]

print("The original list is : " + str(test_list))
 

cur = min(test_list[5])
 
res = True
for sub in test_list[1:]:
    res = False
 
    # checking row for greater than previous minimum
    for idx in sub:
        if idx >= cur:
            res = True
 
            # storing new minimum
            cur = idx
            break
             
    # Not there
    if not res:
        break
 
# printing result
print("Is ascending list possible ? : " + str(res))


#itertools
  
from itertools import combinations
  
  
def subsetSum(b, arr, c):
    
    for i in range(b+1):
        for subs in combinations(arr, i):
            if sum(subs) == c:
                print(list(subs))
b = 20
arr = [18, 30, 45, 70, 4, 20]
c = 20
subsetSum(b, arr, c)


def new(arr):
      
    list = []
      
    for i in arr:
        list.append(i**2)
          
    return list
    
list1 = [1, 2, 3, 4]
l2 = new(list1)
  
print("Old list:", list1)
print("Updated list:", l2)