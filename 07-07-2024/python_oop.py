# 1. Introduction
# Object-Oriented Programming (OOP) is a programming paradigm based on the concept of objects.
# Objects are instances of classes, which can contain data (attributes) and functions (methods) to manipulate that data.
# OOP aims to model real-world entities and solve problems by creating objects that interact with each other.

# 2. General OOP vs Python OOP
# While the core concepts of OOP (such as encapsulation, inheritance, and polymorphism) remain consistent across programming languages,
# the implementation varies. Python, being an object-oriented language, offers unique syntax and features for defining and manipulating classes and objects.

# 3. Class and Object
# A class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have.
# An object is an instance of a class, representing a specific entity with its own unique set of attribute values.

class MyClass:
    pass  # This is an empty class definition

obj = MyClass()  # Creating an instance (object) of the MyClass class

# 4. Data Members in Class

# A. Instance Variables
# Instance variables are attributes specific to each instance (object) of a class. They store data related to that particular instance.

class MyClass:
    def increment(self):
        if not hasattr(self, 'instance_var'):
            self.instance_var = 0
        self.instance_var += 1
        return self.instance_var

obj = MyClass()
print(obj.increment())  # Output: 1
print(obj.increment())  # Output: 2

# B. Class Variables
# Class variables are shared among all instances of a class. They are defined within the class but outside any instance methods.

class MyClass:
    class_var = 0  # Defining a class variable

    def increment(self):
        MyClass.class_var += 1

obj1 = MyClass()
obj2 = MyClass()

print(MyClass.class_var)  # Output: 0
obj1.increment()
print(MyClass.class_var)  # Output: 1
obj2.increment()
print(MyClass.class_var)  # Output: 2

# 5. Methods in Class

# A. Normal Methods
# Normal methods, also known as instance methods, have access to instance data through the self parameter.

class MyClass:
    def my_method(self):
        print("This is a normal method.")

obj = MyClass()
obj.my_method()  # Output: This is a normal method.

# B. Class Methods
# Class methods are bound to the class itself and take a class parameter cls as the first argument.

class MyClass:
    class_var = 0

    @classmethod
    def increment(cls):
        cls.class_var += 1

obj1 = MyClass()
obj2 = MyClass()

print(MyClass.class_var)  # Output: 0
obj1.increment()
print(MyClass.class_var)  # Output: 1
obj2.increment()
print(MyClass.class_var)  # Output: 2

# C. Static Methods
# Static methods are functions defined within a class but are not bound to any instance or the class itself.

class MathUtils:
    @staticmethod
    def is_even(num):
        return num % 2 == 0

    @staticmethod
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

print(MathUtils.is_even(4))  # Output: True
print(MathUtils.is_prime(7))  # Output: True

# 6. Special Methods

# A. __init__ Method
# The __init__ method initializes an object's attributes when an instance is created.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 25)
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 25

# B. __str__ Method
# The __str__ method defines the string representation of an object.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

person1 = Person("Alice", 25)
print(person1)        # Output: Alice (25)
print(str(person1))   # Output: Alice (25)

# C. __new__ Method
# The __new__ method is called before __init__ to create a new instance of a class.

class Person:
    def __new__(cls, *args, **kwargs):
        print("Creating a new instance of Person")
        return super(Person, cls).__new__(cls)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

person1 = Person("Alice", 25)
print(person1)  # Output: Creating a new instance of Person
                #         Alice (25)

# 7. Constructor and Destructor

# A. Constructor
# The constructor is a special method automatically called when an instance of the class is created.

class MyClass:
    def __init__(self):
        print("Constructor called")

obj = MyClass()  # Output: Constructor called

# B. Destructor
# The destructor (__del__ method) is called when an object is deleted.

class MyClass:
    def __del__(self):
        print("Destructor called")

obj = MyClass()
del obj  # Output: Destructor called

# C. Constructor without Arguments
# A class can have a constructor without any arguments to initialize attributes.

class MyClass:
    def __init__(self):
        self.data = 0

obj = MyClass()
print(obj.data)  # Output: 0

# D. Constructor with Arguments
# Constructors can take arguments to initialize object attributes.

class MyClass:
    def __init__(self, value):
        self.data = value

obj = MyClass(10)
print(obj.data)  # Output: 10

# E. Constructor with Default Arguments
# Constructors can have default arguments.

class MyClass:
    def __init__(self, value=0):
        self.data = value

obj1 = MyClass()
print(obj1.data)  # Output: 0

obj2 = MyClass(20)
print(obj2.data)  # Output: 20

# 8. Methods with Arguments

# A. Methods with Multiple Arguments
# Methods can take multiple arguments besides self.

class MyClass:
    def my_method(self, arg1, arg2):
        print(f"Arguments: {arg1}, {arg2}")

obj = MyClass()
obj.my_method(10, 20)  # Output: Arguments: 10, 20

# B. Passing Objects as Arguments
# You can pass objects as arguments to methods.

class MyClass:
    def __init__(self, value):
        self.data = value

    def update(self, other):
        self.data += other.data

obj1 = MyClass(10)
obj2 = MyClass(20)

obj1.update(obj2)
print(obj1.data)  # Output: 30

# C. Returning Objects from Methods
# Methods can return objects.

class MyClass:
    def __init__(self, value):
        self.data = value

    def increment(self):
        self.data += 1
        return self

obj = MyClass(10)
obj = obj.increment()
print(obj.data)  # Output: 11

# D. Method Overloading
# Method overloading allows a class to have multiple methods with the same name but different parameters.

class MyClass:
    def my_method(self, arg1, arg2=0):
        print(f"arg1: {arg1}, arg2: {arg2}")

obj = MyClass()
obj.my_method(10)  # Output: arg1: 10, arg2: 0
obj.my_method(10, 20)  # Output: arg1: 10, arg2: 20

# 9. Data Encapsulation
# Encapsulation bundles data and methods within a single unit, hiding internal details from the outside world.

class MyClass:
    def __init__(self):
        self.__private_var = 0  # Private instance variable

    def get_private_var(self):
        return self.__private_var

    def set_private_var(self, value):
        self.__private_var = value

obj = MyClass()
print(obj.get_private_var())  # Output: 0

obj.set_private_var(10)
print(obj.get_private_var())  # Output: 10

# 10. Data Abstraction
# Abstraction exposes only the essential features of an object while hiding the unnecessary details.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Private attribute

    def get_salary(self):
        return self.__salary

emp = Employee("Alice", 50000)
print(emp.get_salary())  # Output: 50000

# 11. Inheritance

# A. Single Inheritance
# Single inheritance allows a class to inherit from a single parent class.

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()  # Output: Animal speaks
dog.bark()   # Output: Dog barks

# B. Multiple Inheritance
# Multiple inheritance allows a class to inherit from multiple parent classes.

class A:
    def method_A(self):
        print("Method A")

class B:
    def method_B(self):
        print("Method B")

class C(A, B):
    pass

c = C()
c.method_A()  # Output: Method A
c.method_B()  # Output: Method B

# C. Multilevel Inheritance
# Multilevel inheritance involves a class inheriting from another class that is also a derived class.

class Animal:
    def speak(self):
        print("Animal speaks")

class Mammal(Animal):
    def run(self):
        print("Mammal runs")

class Dog(Mammal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()  # Output: Animal speaks
dog.run()    # Output: Mammal runs
dog.bark()   # Output: Dog barks

# D. Hierarchical Inheritance
# Hierarchical inheritance involves multiple derived classes inheriting from a single base class.

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

dog = Dog()
dog.speak()  # Output: Animal speaks
dog.bark()   # Output: Dog barks

cat = Cat()
cat.speak()  # Output: Animal speaks
cat.meow()   # Output: Cat meows

# 12. Polymorphism

# A. Operator Overloading
# Operator overloading allows customizing the behavior of operators for user-defined classes.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print(v3)  # Output: (6, 8)

# B. Method Overriding
# Method overriding allows a derived class to provide a specific implementation of a method already defined in its base class.

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

animal = Animal()
dog = Dog()

animal.speak()  # Output: Animal speaks
dog.speak()     # Output: Dog barks

# 13. Abstract Classes and Interfaces

# A. Abstract Classes
# Abstract classes cannot be instantiated and are designed to be subclassed.
# They can contain abstract methods that must be implemented by subclasses.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()  # Output: Dog barks

# B. Interfaces
# Python does not have explicit support for interfaces like some other languages.
# Instead, abstract base classes (ABCs) are used to achieve similar functionality.

# 14. Example Class

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

my_car = Car('audi', 'a4', 2016)
print(my_car.get_descriptive_name())  # Output: 2016 Audi A4
my_car.update_odometer(23)
my_car.read_odometer()  # Output: This car has 23 miles on it.
my_car.increment_odometer(100)
my_car.read_odometer()  # Output: This car has 123 miles on it.
