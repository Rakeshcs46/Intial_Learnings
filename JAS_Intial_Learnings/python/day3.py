# itertools is a built-in Python module that provides a collection of tools for working with iterators. Here are some common functions from itertools with brief explanations:

# count(start=0, step=1): Returns an infinite iterator that starts at start and increments by step on each iteration.

# cycle(iterable): Returns an infinite iterator that cycles through the elements of iterable.

# repeat(elem, n=None): Returns an iterator that repeats elem n times. If n is None, the iterator repeats indefinitely.

#  chain(*iterables): Returns a single iterator that combines the elements from multiple iterables in order.

# zip_longest(*iterables, fillvalue=None): Returns an iterator that aggregates the elements from multiple iterables. Unlike the built-in zip function, zip_longest continues until the longest iterable is exhausted, and any missing values are filled in with fillvalue.

#  islice(iterable, start, stop[, step]): Returns a slice of an iterator. start, stop, and step work like the corresponding slice arguments for lists.

#  tee(iterable, n=2): Returns n independent iterators that yield the same elements from iterable.

# example 
import itertools

def fibonacci():
   a, b = 0, 1
   yield a 
   yield b 
 
      
while True:
    a, b = b, a + b
yield b 

fib = fibonacci()
fibonacci_numbers = itertools.islice(fib, 10)

for num in fibonacci_numbers:
    print(num)

fib1, fib2 = itertools.tee(fibonacci())
next(fib2)
fibonacci_pairs = zip(fib1, fib2)
for a, b in itertools.islice(fibonacci_pairs, 10):
   print(f"{a} + {b} = {a + b}")



# # # #control strcutures in python 

x  = 5
if x > 0:
   print("x is positive")

#If-else statement
x = -5
if x > 0:
     print("x is positive")
else:
   print("x is not positive")

 #If-elif-else statement
m = 0
if m > 0:
     print("x is positive")
elif m < 0:
     print("x is negative")
else:
   print("x is zero")

#While loop
i = 0
while i < 10:
    print(i)



#iterating over a list 

my_list = [1, 2, 3, 4, 5]

for item in my_list:
   print(item)

my_list = [1, 2, 3, 4, 5]

# Traverse the list using an index variable
for i in range(len(my_list)):
    print(my_list[i])
