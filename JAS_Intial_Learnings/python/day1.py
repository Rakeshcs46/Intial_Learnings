""" Installing python Since I have linux distribution python was installed using the terminal  and  python was already
build in using the command sudo apt update then by a command sudo apt install python3 after the package was installed
I went back to terminal to check the python version by using the command python3 --version AND  it was 3.8.10

# Basics of python
# Topic 1 Numbers , String , Variables
print(5*6)
print(12+10)
 print(8-9)
print(9/3)
print((8*3)/2)
print(2**2)


# String -  Sequence of characters in called strings
print("rakesh")

# reverse the list using slice operator
''' # original list
my_name = "Rakesh"
# reversing original list
my_name_reversed = my_numbers[::-1]
print(my_name_reversed)'''


# reverse using function
def reverse(s):
    result = " " 
    for i in s:
        result = i+result 
        print(result)
    return result 
s = ("Rakesh")
print(reverse(s)

# created a simple program for variables
i = int(input())
if i%3 == 0:
     i += 1
     print(i)
else:
 print(i)

#operators in python
a=int(input("Enter a value"));
b=int(input("Enter b value"));
print("Addition of a and b ",a+b);
print("Subtraction of a and b ",a-b);
print("Multiplication of a and b ",a*b);
print("Division of a and b ",a/b);
print("Remainder of a and b ",a%b);
print("Exponent of a and b ",a**b);
print("floor division of a and b ",a//b)

# tuple program
T = ("a", "b", "c,"e","f","g")
print("\n Created tuple is :",T)
print("\n Second letter is :",T[1])
print("\n From 3-6 letters  are :",T[3:6])
print("\n List of all items in Tuple :")
for x in T:
  print(x)
if "a" in T:
  print("\n Yes, 'a' is in the letter tuple")
print("\n Length of Tuple is :",len(T)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)"""



"Everthying is an object and all datatypes are implemented by the concepts of object where there is mp fixed size"
# Dictories and Lists


"""per_value = [900, 342, 542, 190]
sum(per_value)
per_value.append(39.99)
print(per_value)
len(per_value)
per_value
per_value[3]
per_value[2]
per_value[2] * 120
my_string = "Newbie"
len(my_string)
my_string[4] 

#dict
my_list = [1,2,3,4,5]
my_data = {"name": "Rakesh"}
my_data["name"]
my_data = {"name": "Rakesh", "location": "kenegri "}
my_data[0]
my_data.keys()
dict_keys(['name', 'location'])
list(my_data.keys())
['name', 'location']
list(my_data.keys())[0]
'name'
my_data.append({"occ": "coder"})
my_data["occ"] = "loader"
my_data
{'name': 'Rakesh', 'location': 'kenegri ', 'occ': 'loader'}
user_1 = {"name": "SRK"}
user_2 = {"name": "Tony Stark"}
my_users = [user_1, user_2]


#solved 10  hacker rank basic questions






