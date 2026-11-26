## Python Programs

## Types of Functions and Anonymous Function (Lambda)
In Python, a function is a block of reusable code that performs a specific task. Instead of writing the same code repeatedly, we can define a function and call it whenever required.

Python functions are mainly classified into different types.
1. Types of Functions in Python
Python functions are broadly divided into two main categories:
1. Built-in Functions
2. User-defined Functions
A. Built-in Functions
Built-in functions are predefined functions available in Python. We can use them directly without defining them.

Examples:
Function	 |  Purpose
print()	   |   Displays output
input()    |  Accepts user input
len()	     |  Returns length
type()	   |   Returns data type
max()	     |   Returns maximum value
min()	     |  Returns minimum value
sum()	     |  Returns sum of values

Example:
name = "Python Programming"

print(name)
print(len(name))
print(type(name))

B. User-defined Functions
User-defined functions are functions created by programmers using the def keyword to perform a particular task.

def function_name():
    # statements

function_name()

Ex : 
def addition():
    a = 10
    b = 20
    print("Addition:", a + b)

addition()

Types of User-defined Functions
User-defined functions can be classified into four types based on arguments and return values.

1. Function without arguments and without return value
   def greet():
    print("Hello Python")

greet()
2. Function with arguments and without return value
def addition(a, b):
    print("Addition:", a + b)

addition(10, 20)


3. Function without arguments and with return value
   def addition():
    a = 10
    b = 20
    return a + b

result = addition()
print("Addition:", result)

4. Function with arguments and with return value
   def addition(a, b):
    return a + b

result = addition(10, 20)
print("Addition:", result)
<hr>
<hr>

2. Anonymous Function (Lambda Function)
An anonymous function is a function without a name.

In Python, anonymous functions are created using the lambda keyword. Lambda functions are used to perform small and simple operations in a single line.

Syntax
lambda arguments: expression

- lambda – Keyword used to create an anonymous function.
- arguments – Values passed to the function.
- expression – Operation performed by the function.
  
Example 1: Addition using Lambda
add = lambda a, b: a + b

print(add(10, 20))

3. Difference Between Normal Function and Lambda Function
Normal Function	                  |    Lambda Function
Uses def keyword                  |    Uses lambda keyword
Has a function name	              |    Anonymous function (no declared name)
Can contain multiple statements	  |    Contains a single expression
Uses return to return a value	    |    Returns the expression result automatically
Suitable for complex tasks	      |    Suitable for small tasks

4. Advantages of Lambda Functions
  1. Reduces the amount of code.
  2. Makes simple operations easier.
  3. Does not require the def keyword.
  4. Returns values automatically.
  5. Useful with functions like map(), filter() and sorted().

<hr>
<hr>

## Modules: Module basic usage, Creating, importing modules.

## 1. What is a Module in Python?
A module in Python is a file containing Python code such as functions, variables, and classes that can be reused in other Python programs.
In simple words, a module is a Python file (.py) that helps us organize and reuse code.

Example: We can create one module for mathematical operations and use its functions in another Python program.

## Advantages of Modules
1. Code reusability.
2. Easy to maintain programs.
3. Reduces code duplication.
4. Makes programs organized.
5. Helps divide large programs into smaller files.

## 2. Types of Modules in Python
Python modules are mainly classified into two types:
1. Built-in Modules
2. User-defined Modules

Example 1: Math Module
import math

print(math.sqrt(25))
print(math.factorial(5))
print(math.pi)

**3. Creating a Module in Python**
We can create our own module by creating a Python file (.py) containing variables and functions.

Example: Creating a module
Step 1: Create a Python file named mymodule.py.
Step 2: Write the following code inside mymodule.py.

File: mymodule.py
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

name = "Python"

Here, we have created a module named mymodule containing two functions and one variable.

**4. Importing a Module in Python**
The import keyword is used to include a module in another Python program so that we can use its functions and variables.

Step 1: Create another Python file named main.py in the same folder.

Step 2: Write the following code.

File: main.py
import mymodule

print(mymodule.addition(10, 20))
print(mymodule.subtraction(20, 10))
print(mymodule.name)

**Explanation:**
- import mymodule imports the created module.
- mymodule.addition(10, 20) calls the addition function.
- mymodule.subtraction(20, 10) calls the subtraction function.
- mymodule.name accesses the variable.

5. Different Ways of Importing Modules
   A. Import Entire Module
         import math
         print(math.sqrt(16))
   
   B. Import Specific Function
    We can import only a particular function from a module using from and import.
     from math import sqrt
      print(sqrt(25))

   C. Import Module Using Alias
    We can give a shorter name to a module using the as keyword.(as => alias)
         import math as m
          print(m.sqrt(36))
   
   D. Import All Functions
    We can import all public names from a module using *.
       from math import *
        print(sqrt(25))
        print(factorial(5))

6. Difference Between Module and Function
Module	                                      |        Function
A Python file containing reusable code.      	|      A block of code performing a specific task.
Has .py extension.	                          |      Defined using def or lambda.
Can contain multiple functions and variables. |   	Performs a particular operation.
Imported using import.	                      |     Called using its name.

Quick Revision for Exams
Term	              |    Meaning
Module	            |    A Python file containing reusable code.
import	            |   Used to import a module.
from	              |  Used to import specific items from a module.
as	                | Used to give an alias to a module or imported item.
Built-in Module     |  	Module already available in Python.
User-defined Module |  	Module created by the programmer.

A module is a Python file containing functions, variables, and classes that can be reused in other programs. We use the import keyword to import modules in Python.

<hr>
<hr>

## **Python Package**

1. What is a Package in Python?
A package in Python is a collection of related modules organized inside a directory (folder).

In simple words:
- A Module is a Python file (.py) containing functions, variables and classes.
- A Package is a folder containing multiple related Python modules.
  
Packages help us organize large Python projects into smaller and manageable parts.
Advantages of Packages
1. Organizes modules properly.
2. Makes code reusable.
3. Avoids confusion in large projects.
4. Makes programs easier to maintain.
5. Helps manage large applications.

2. Difference Between Module and Package

<img width="811" height="236" alt="image" src="https://github.com/user-attachments/assets/5ff5e46b-12c1-422a-ae9b-e1413d5558eb" />


3. Creating a Package in Python
Let's understand how to create a simple package.

Step 1: Create a folder named mypackage.
Step 2: Inside mypackage, create a file named __init__.py.
Step 3: Create two Python files inside the package.
- addition.py
- subtraction.py

<hr>
<hr>

## Python Namespace Packages

1. What is a Namespace Package in Python?
A namespace package in Python is a special type of package that allows multiple directories to contribute modules to the same package.
In simple words, a namespace package allows us to combine modules from different folders under one common package name without requiring an __init__.py file.
Namespace packages are useful when a large project is divided into multiple folders or different developers work on separate parts of the same package.

## Advantages of Namespace Packages
Allows multiple directories to share one package name.
Does not require an __init__.py file.
Makes large projects easier to organize.
Supports modular application development.
Allows different developers to maintain separate parts of a package.

<img width="810" height="277" alt="image" src="https://github.com/user-attachments/assets/2a602cc5-d7dd-401e-8653-1fcd49405bf8" />

4. Creating a Namespace Package
Let's understand namespace packages with a simple example.
Suppose we have two different folders containing modules with the same package name.

Folder Structure:

<img width="525" height="322" alt="image" src="https://github.com/user-attachments/assets/30c58e36-8a98-4bf5-8c13-ac09ed3b0f78" />

Here, both folders contain a package directory named mypackage.

Python can treat these two directories as parts of one namespace package.
4. Writing Code in Namespace Package Modules
  Step 1: Create module1.py inside part1/mypackage/.
  def greet():
    print("Hello from Module 1")

  Step 2: Create module2.py inside part2/mypackage/.
    def welcome():
    print("Welcome from Module 2")

  Step 3: Create main.py in the PythonProject folder.
    import sys
    sys.path.extend(["part1", "part2"])
    from mypackage.module1 import greet
    from mypackage.module2 import welcome
    greet()
    welcome()


5. How to Check a Namespace Package?
We can use the __path__ attribute to check the directories associated with a namespace package.
import sys

sys.path.extend(["part1", "part2"])

import mypackage

print(list(mypackage.__path__))

Possible Output:
['.../part1/mypackage', '.../part2/mypackage']

6. Real-World Use of Namespace Packages
Namespace packages are useful in large Python applications where different developers or teams maintain separate modules.

For example:
- company.sales – Sales-related modules.
- company.accounts – Account-related modules.
- company.reports – Reporting-related modules.
These modules can be distributed across different directories or Python distributions while sharing the same top-level namespace, company.

<img width="977" height="317" alt="image" src="https://github.com/user-attachments/assets/e2791b8b-f746-4891-8d81-972b41c19626" />

## Decorators and Generators

What is a Decorator?
A decorator in Python is a function that takes another function as an argument and adds extra functionality to it without changing its original code.

In simple words, a decorator is used to modify or extend the behaviour of an existing function.

Example: Suppose we have a function that displays a welcome message. We want to display an additional message before and after executing that function. We can use a decorator.

Basic Syntax

def decorator_function(original_function):
    def wrapper():
            # Additional functionality
            original_function()
        return wrapper

@decorator_function
def my_function():
    print("Hello Python")

my_function()

Here:
- decorator_function is the decorator.
- original_function is the function passed to the decorator.
- wrapper() adds extra functionality.
- @decorator_function applies the decorator.

Example 1: Simple Decorator

def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@my_decorator
def greet():
    print("Hello Python")

greet()

Explanation:
1. my_decorator() takes the greet() function as an argument.
2. wrapper() executes additional statements.
3. func() calls the original greet() function.
4. @my_decorator applies the decorator to greet().

Example 2: Decorator with Arguments
A decorator can also work with functions that accept arguments.
def my_decorator(func):
    def wrapper(name):
        print("Welcome!")
        func(name)
    return wrapper

@my_decorator
def greet(name):
    print("Hello", name)


greet("Pankaj")

Example 3: Decorator Without @ Symbol
We can also apply a decorator without using the @ symbol.
def decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper


def greet():
    print("Hello Python")


result = decorator(greet)

result()

Advantages of Decorators
1. Adds extra functionality to existing functions.
2. Avoids modifying original function code.
3. Promotes code reusability.
4. Reduces code duplication.
5. Helps with logging, authentication and execution time calculation.
Real-Life Uses of Decorators
- Authentication and authorization.
- Logging function execution.
- Measuring execution time.
- Caching results.
- Checking user permissions.

<hr>
<hr>


## Generators in Python

What is a Generator?
A generator in Python is a special type of function that returns values one at a time using the yield keyword instead of returning all values at once.
In simple words, a generator produces values one by one whenever required, rather than storing all values in memory.
Generators are useful when working with large amounts of data because they can save memory.

Difference Between return and yield
<img width="832" height="213" alt="image" src="https://github.com/user-attachments/assets/ad7164cf-320e-43ff-adbc-2d2619876f8f" />

Example 1: Simple Generator
def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


for value in my_generator():
    print(value)

Explanation:
1. def my_generator() defines a generator function.
2. yield produces one value at a time.
3. The function pauses after each yield.
4. The for loop requests the next value.
5. After the last value, the generator stops.

