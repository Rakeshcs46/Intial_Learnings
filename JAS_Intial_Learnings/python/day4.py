#dictionaries in python 

new_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(new_dict["key1"])
new_dict["key4"] = "value4"

# Remove a key-value pair from the dictionary
del new_dict["key3"]

# Get a list of keys in the dictionary
keys_list = list(new_dict.keys())

# Get a list of values in the dictionary
values_list = list(new_dict.values())


#mergee dict
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
print(dict1)

#Dictionary comprehension:
squares = {x: x*x for x in range(1,6)}
print(squares)

#Nested dictionaries:
students = {
    'me': {'age': 25, 'gender': 'male'},
    'u': {'age': 27, 'gender': 'female'}
}
print(students['me']['u'])


#Sorting a dictionary by value:

prices = {'apple': 0.5, 'banana': 0.25, 'orange': 0.75}
sorted_prices = sorted(prices.items(), key=lambda x: x[1])
print(sorted_prices)


#count frequency
fruits = ['apple', 'banana', 'orange', 'apple', 'banana', 'grape']
fruit_counts = {}
for fruit in fruits:
    if fruit in fruit_counts:
        fruit_counts[fruit] += 1
    else:
        fruit_counts[fruit] = 1
print(fruit_counts)

#removing duplicates 
# Removing duplicates from a list using a dictionary
num = [1, 2, 3, 4, 3, 2, 1, 5, 6, 7, 6]
unique_num = list(dict.fromkeys(num))
print(unique_num)


#maps in python 
nums = (1, 2, 3, 4, 5, 6, 7) 
print("Original list: ", nums)
result = map(lambda x: x + x + x, nums) 
print("\nTriple of said list numbers:")
print(list(result))

strings = ['hello', 'world', 'python']
lengths = map(len, strings)
print(list(lengths))  # output: [5, 5, 6]