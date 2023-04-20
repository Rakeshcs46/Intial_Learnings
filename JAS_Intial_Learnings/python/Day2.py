#days2  today mainly foucused on the the concepts such as itertools function and methods and oops

'''Itertools is module in python which mainly gives  fuctions which we use in the programming world the main fucnc of itertools
 is used reduce problem statements and to use the libraray tools approach problem in a faster scale '''


import itertools
colors  = ['red' , ' green ', 'blue']
sizes = ['small', 'medium ', 'large']
materials  = ['cotton', ' wool ', 'silk']
combinations = itertools.product(colors, sizes, materials)
for combination  in combinations:
    print(combination)
## will give out possbile combination  from the given list

'''def naive_grouper(inputs, n):
        num_groups = len(inputs) // n
        return [tuple(inputs[i * n:(i + 1) * n]) for i in range(num_groups)]'''



##functions and  objects
''' def function(arguments):


    body of the function
    return the return value or expression
class my_class:

    def method1(self):
        return "Hello World"
    def method2(self, methodToRun):
        result = methodToRun()
        return result


def func2(text):
    return text.upper()

def func3(text):
    return text.lower()

def func1(func):
    res = func("Hello World")
    print(res)

#funtion calls
func1(func2)
func1(func3) 

obj = my_class()
#method1 is passed as an argument
print(obj.method2(obj.method1))

def accumulate(iterable, func=operator.add, *, initial=None):
    total = initial
    if initial is None:
        try:
            total = next(it)
        except StopIteration:
            return
    yield total
    for element in it:
        total = func(total, element)
        yield total
         Keyword def: This is the keyword used to say that a function will be defined now, and the next word that is there, is the function name.

Function name: This is the name that is used to identify the function. The function name comes after the def keyword. Function names have to be a single word. PEP8, which is a style guide for Python, recommends that in case multiple words are used, they should be in lowercase and they should be separated with an underscore. In the example above, add_two_numbers is the parameter name.
parameter list: Parameter list are place holders that define the parameters that go into the function. The parameters help to generalise the transformation/computation/task that is needed to be done. In Python, parameters are enclosed in parentheses. In the example above, the parameters are num1and num2. You can pass as many parameters as needed to a function.
Function docstrings: These are optional constructs that provide a convenient way for associated documentation to the corresponding function. Docstrings are enclosed by triple quotes 
Function returns: Python functions returns a value. You can define what to return by the return keyword. In the example above, the function returns result. In case you do not define a return value, the function will return None.'''

""" oops concepts 

class Dog:
 
    # class attribute
    attr1 = "mammal"
 
    # Instance attribute
    def __init__(self, name):
        self.name = name
 
# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
 
# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))
 
# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))



class Dog:
 
    # class attribute
    attr1 = "mammal"
 
    # Instance attribute
    def __init__(self, name):
        self.name = name
         
    def speak(self):
        print("My name is {}".format(self.name))
 
# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
 
# Accessing class methods
Rodger.speak()
Tommy.speak()"""

s =  '''mnopqr'''
i = ''' m '''''
while i in s:
   print('i', end= '' '')
