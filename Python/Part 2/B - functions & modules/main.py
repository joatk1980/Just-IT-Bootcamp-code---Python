This is Part 2B

# Python Part 2b -Functions and Modules

# Formatting Variables

format_output = "\033[47m\033[30m"

format_reset = "\033[0m"

# Formatted Message - Signify Start of Output

print(f"{format_output}---START---{format_reset}")

# ! Functions:
# * As discussed, functions are blocks of code that can be reused throughout our program
# * Exactly the same as we have seen with JavaScript but with different syntax.

# * Basic Example (Greeting Function):

# use the def keyword to define the function called greeting
def greeting():
    # body of the function/code to be executed
    print("Hello World")

#call the function greeting
greeting()

def greetings():
    name = "user"
    greet = input("Enter Greetings:  ")
    print(f"{greet} {name}")
greetings()

#! Quick Task
#Create a function with 3 variables 
#
def greet_person(name, age, city):  #defines function name to take 3 parameters
        print(f"Hello, {name}! You are {age} years old and live in {city}.")

greet_person("Jo", 44, "Gloucester")  #calls function with the arguments which are passed into the parameters.      
#
#

# * Think of it like this, replace 'function' with 'def' and indent rather than add {curly's}

# * We now have our function, but in order for it to run we need to call it

# ? How would we call our function?

greet_person("Jo", 44, "Gloucester")
#

# ! Parameters and Arguments:

# ? What are arguments and parameters and how do they differ?

# * Again, we have seen arguments and parameters before, the concept does not change

# ! Parameter(s) - Defined with the function, placeholder for data passed to the function

# ! Argument(s) - Passed to the function when calling it, fulfilling the parameter(s)

# * Parameters are defined in the parentheses following our function name

# * Lets look at an example function that defines 'name' as our parameter

#
def greet_by_name(name): #parameter name is a placeholder(variable)
    print(f"Hello {name}")

greet_by_name("Lucy") #pass hardcoded string value
greet_by_name(290) #pass hardcoded integer value
arg_value = "James" #declare a variable with a string value to be used as an argument
arg_value2 = input("Enter a value: ")
arg_list3 = ["HTML", "CSS", "Javascript"]
arg_list4 = [1,2,3,4,5,6]
greet_by_name(arg_value) #pass a variable that holds a string value
greet_by_name(arg_value2)
greet_bu_name(arg_list3)

user = "" #is a parameter
print(f"The user is: {user}")    
user = "Jane" #passing a value(atgument) to the parameter which is a variable 
print(f"The user is: {user}") 
#
#parameter can not be empty
#function has nothing until it is called 
#what data you put into the function dictates what the data type is 


# * If we call this function without passing an argument we get an error

# ? How would we call this function and supply a name as our argument?

# * We supply the data to our argument in the parentheses of our function call

# greet_by_name()
# greeting()
#

# * Our 'greet_by_name' example used 1 parameter, lets look at how we can work with multiple

# * If we define an 'add' function with parameters of 'a' and 'b':

#define the function with multiple parameters

def multiply(a,b):
    print(a * b)

#call the function with multiple arguments    
multiply(12,34)


arg1 = int(input("Enter a value:  "))
arg1 = int(input("Enter a value:  "))
multiply(arg1, arg2)

# * Our params are seperated by commas and we can work with 'a' and 'b' in our function
# * In this example our function will print the sum of the numbers passed as our args
multiply(1)
multiply(2,3,4) # ned to ensure 3 parameters are being put in, called ie multiply(a,b,c)

# ! Default Arguments:

# * Another concept we have seen before in JS, we can set default arguments with functions

def greet_user(message = "Hello"):
    print(f"{message}")

greet_user()    #uses default values and dont use an argument

#
greet_user("Goodbye") # overwrites default value by entering an argument

# * Here we have created a 'greet_user' function with defualt args set for our params

# ? If we call our function without passing arguments what will happen? 

def greet_a_user(msg = "Hello", user_name = "James"):
    print(f"{msg} {user_name}")

greet_a_user()
greet_a_user("Yo")
greet_a_user("Dave")

greet_a_user(user_name = "Dave")
greet_a_user(msg="Dancing")
#

# * With no arguments passed, our default arguments are supplied to the function

# ? What do you think would happen if we just passed one argument?



# * By defualt our single argument will be supplied to our first parameter

# * Meaning if we just supply a name to our function we get 'name User'



# * To get around this we can use a 'keyword argument' and reference the parameter
# * When calling the function we can reference the parameter name and supply a value

#* means arguments, can put any amount of arguments in parameter - removes limits

def add_nums(*numbers):
    print(sum(numbers))

#call the function with multiple arguments because of definition the * followed by a parameter
add_nums(1,2)
add_nums(1,2,12,45,67,89,1234)   #adds these numbers 

val1 = int(input("Enter a value: "))
val2 = int(input("Enter a value: "))
val3 = int(input("Enter a value: "))
add_nums(val1,val2,val3)

# * I want to take a look at '*args' or "Starguments"

# ! DISCLAIMER: Starguments is not an official technical term

# ! simply a name I came up with to help teach the concept




# ! *args "Starguments":

# * *args allow a function to take any number of arguments




# * For example lets say we wanted to write a function that calculates the...

# * ...sum of the numbers passed to it, no matter how many numbers are passed




# * When defining our params a pass an asterisk(star) '*' followed by our param name

# * In this case 'nums'

# * Our function then prints the result of the sum function with 'nums' as the arg

def add_nums(*numbers):
    print(sum(numbers))

#call the function with multiple arguments because of definition the * followed by a parameter
add_nums(1,2)
add_nums(1,2,12,45,67,89,1234) 

# * Now when we call our function we can pass as many numbers as we like
add_nums(1,2) #result 3
add_nums(1,2,12,45,67,89,1234) #result 1450

# ? Think about JavaScript functions, if I wanted to do something with the result...

# ? ...of our function other than print it to the console, what would we need to do?

# ! Return Statement

# * To return a value from a function we need to use 'return'

# * This is no different to what we have seen with JavaScript

# Can add a return statement to function instead of or in addition to using print.    
# Return function allows the function to return the sum of numbers 

def add_nums(*numbers):
    return sum(numbers)

result1 = add_nums(1,2)    
result2 = add_nums(1,2,12,45,67,89,1234)

print(result1) #3
print(result2) #1450

#instead of printing the sum inside the function, return the sum with return sum(numbers) this allows the result to be used elsewhere in the program

#results are stored in result1 and result2 which can then be printed or used in further calcs

# ? How do you think we would print the result of our function now?

# * To print the result of our function we need to call our function in a print function

 print(sum(numbers))

# * We can also store the result in a variable and print the variable

print(result1) #3
print(result2) #1450


# ! Modules

# * As discussed earlier, modules in Python can be used to compartmentalise our code

# * We can create modules of our own but to introduce the concept we will look at...

# * ...an example of a module built-in to Python




# ! 'random' module:

# * To import a module we use the 'import' keyword followed by the module name




#

import random

#




# * We can also rename a module on import and provide it a different reference




#

# import random as r

#




# * For demo purposes we will stick with 'random'

# * Now we have imported the module we have access to its functions such as random()

# * 'random.random()' will provide us with a random float between 0-1




#

random_float = ''

#




# * Similar to 'math.random()' in JS

# * However, if we want to generate an integer between a range it is much simpler

# * We can use 'random.randint(a,b)' and pass the range as the argument




#

random_num = ''

#




# ! STUDENT TASKS ! 

"""

Python Part 2b - Tasks:

1: Write functions that meet the following criteria in order to familiarize yourself with how they work:

- A function that uses input to obtain a user's name and returns a string greeting them by their name.

def get_greeting():
    user_name = input("Please enter your name: ")
    greeting = (f"Hello, {user_name}!")
    return greeting

greeting_message = get_greeting()
print(greeting_message)

or

def get_greeting():
    user_name = input("Please enter your name:")
    return f"Hello, {user_name}!"

print(get_greeting())    

or

def get_greeting():
    user_name = input("Please enter your name: ")
    return "Hello, {}!".format(user_name)

print(get_greeting())    

- A function with parameters of 'name' and 'age' that returns a string containing the 'name' and 'age' supplied to it as arguments. Set a default argument of 'unknown' for 'age'.

def create_greeting(name, age="unknown"):

    return f"Hello, {name}! Your age is {age}."

print(create_greeting("Jo", 44))
print(create_greeting("Sid"))    



- A function that uses input to obtain a users name and age and checks whether or not the user is over the age of 18. If the user is over the age of 18, return a string containing their name advising that their sign-up has been successful. If a user is under
 the age of 18, return a string containing their name and age advising that they are unable to register due to their age.

def check_registration():
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))

    if age > 18:
        return f"Welcome {name}! Your sign-up has been successful!"
    else:
        return f"Sorry {name}, as you are {age}, you are under 18 and therefore unable to sign up"    

registration_message = check_registration()
print(registration_message)



2: Create your own custom module containing the functions from Task 1:

- Create a file named 'my_functions.py'.

- Import your file as a module into a 'main.py' file.

- Use all 3 of the created functions from the module in your 'main.py' file.


https://www.programiz.com/python-programming/modules




3: Familiarise yourself with Scope in Python:


https://www.programiz.com/python-programming/global-local-nonlocal-variables



Stretch Task: 


Guess the Number V2: Write a function called 'guess_the_number' that starts the game when called.
 

Use the random module to generate a random number between 1 and 100. Each turn the user should guess a number, feedback to the user whether their guess is too high, too low or correct. The game should continue until the user guesses the correct number.
 




Additional Challenges:




https://www.hackinscience.org/exercises/




https://www.practicepython.org/




"""

#Python modules

#A file containing a set of functions you want to include in your application
#To create a module just save the code you want in a file with the file extension .py
#can then use the module created by using the import statement

#eg;
# def greeting(name):
#     print("Hello," + name)

# import mymodule
# mymodule.greeting("Jonathan")    

# How to use Math module 
# Python has a built in module that you can use for mathematical tasks
#Math module has a set of methods and constrants - many many many!
#methods in the module accept int, float, and complex numbers

#Random Module 
#Python has a built-in module that you can use to make random numbers.
#The random module has a set of methods (long list - w3schools)

