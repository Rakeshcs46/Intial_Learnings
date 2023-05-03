# # # # # # # oops in python
# Abstraction
from abc import ABC, abstractmethod

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0





def get_make(self):
    return self.make


def get_model(self):
    return self.model


def get_year(self):
    return self.year


def get_speed(self):
    return self.speed


def accelerate(self):
    self.speed += 10


def brake(self):
    if self.speed >= 10:
        self.speed -= 10
    else:
        self.speed = 0
    # Sure, here's an example of Object-Oriented Programming (OOP) in Python:

    # python
    # class Car:


def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.speed = 0


def get_make(self):
    return self.make


def get_model(self):
    return self.model


def get_year(self):
    return self.year


def get_speed(self):
    return self.speed


def accelerate(self):
    self.speed += 10


def brake(self):
    if self.speed >= 10:
        self.speed -= 10
    else:
        self.speed = 0


# # In this example, we have defined a class called Car which represents a car object. The __init__ method is the constructor method that initializes the object with the specified make, model, and year. The speed attribute is initialized to 0.
# We have also defined several methods that allow us to get the make, model, year, and speed of the car object. The accelerate method increases the speed of the car by 10, while the brake method decreases the speed by 10, but sets the speed to 0 if it is less than 10.
my_car = Car("Toyota", "Corolla", 2020)

my_car.accelerate()
print(my_car.get_speed())  # Output: 10

my_car.brake()
print(my_car.get_speed())  # Output: 0


# This is example of how OOP can be implemented in Python.


# # # # #inheritance

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species


def make_sound(self):
    print("Generic animal sound")


class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Cat")
        self.breed = breed

    def make_sound(self):
        print("Meow")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Woof")





class Vehicle(ABC):

    def start(self):
        pass


@abstractmethod
def stop(self):
    pass


class Car(Vehicle):
    def start(self):
        print("Starting car")


def stop(self):
    print("Stopping car")


class Bike(Vehicle):
    def start(self):
        print("Starting bike")

    def stop(self):
        print("Stopping bike")


# polymorphism
class Calculator:
    def add(self, x, y):
        return x + y

    def add(self, x, y, z):
        return x + y + z


my_calculator = Calculator()

print(my_calculator.add(2, 3))  # Output: TypeError: add() missing 1 required positional argument: 'z'
print(my_calculator.add(2, 3, 4))


class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


my_account = BankAccount("1234567890", 5000)

print(my_account.__balance)
print(my_account.get_balance())

my_account.__balance = 10000  # This doesn't actually change the balance because the attribute is private
print(my_account.get_balance())

my_account.deposit(2000)
print(my_account.get_balance())

my_account.withdraw(3000)
print(my_account.get_balance())

my_account.withdraw(5000)
# In this example, we have defined a class called BankAccount that represents a bank account. The __init__ method initializes the account number and balance, but the attributes are private because they are prefixed with two underscores. The deposit and withdraw methods modify the balance, but they also check to make sure that the balance doesn't become negative. The get_balance method returns the current balance.
