# Python Python Part 1a - Introduction

'format_output = "\033[47m\033[30m"'

# \033: This is the escape character, represented by the octal code 033. It signals the start of an escape sequence.

# [47m: This sets the background color of the text. The code 47 corresponds to a white background.

# [30m: This sets the text (foreground) color. The code 30 corresponds to black text.

# So, format_output is a sequence of escape codes that, when printed in a terminal
 

# that supports ANSI escape codes, will format the output with black text on a white background.


'format_reset = "\033[0m"'


# \033[0m: This is a reset code that clears all previously set text formatting, returning the text to the terminal's
 

# default appearance (usually white or light text on a black or dark background, but this can vary).

# These escape codes are commonly used in scripts and programs to make terminal output more readable by highlighting

# important information or categorizing different types of output with colors.



# Formatting Variables

format_output = "\033[47m\033[30m"

format_reset = "\033[0m"


# Formatted Message - Signify Start of Output

print(f"{format_output}---START---{format_reset}")



# ! 'print()' - Is the equivalent to console.log in JavaScript

# * This will print the string "Hello World" to the console


#

print("Hello World") 

#


# ? How do we run the file to see our output? 

# ! We have 2 options

# * Press the play button in the top right of our VS Code workspace

#  or

# * Open our terminal in the CORRECT DIRECTORY and run: "python filename.py"


# ! Similar to console.log(), print() will evaluate the argument and print the result

# * For Example: We can complete mathematical operations


# 

print(2+2)

# 


# * We can also seperate arguments with a comma

# 

print("The answer to 3 x 3", 3 * 3)
print("The answer to 3 x 3", 3 * 3, "\nTest", "\n", 12344)
#back slash n \n prints answer in a new line

# 


# ? What happens if we try to add quote marks to a string in our print function? 

# * For example if you wanted to write "My name is "name""

# 

#print("My name is "Christian"")

# 


# * Notice we encounter an error - Python tries to help but isn't correct

# ! In order to write "illegal" characters we need to use an "escape character"

# * Backslash + Quote '\"' allows us to escape our string and use our quote marks


# 
print("My name is \'Christian'")
print("My name is \"Christian\"")
print('My name is "Christian"')

# 


# ? Thinking back to JavaScript do we remember what a variable is?

# * Aside from syntax there is no difference - Just a label / box for our data


# ! Python Varaiables are delcared without a keyword - no 'let'/'const' equivalent

#

greeting = "Good Morning"

#

# * Meaning we can now access our string by referencing our variable

#

print(greeting)

#

# ? How do you think we would assign a new value to the variable? 

# * Similar to JavaScript, in Python we simply reference the variable and reassign

#

greeting = "Good Afternoon"

print(greeting)

#

# ? As there is no keyword you may be wondering how we declare constants? 

# ! In Python constants are delcared by a practice and are not a seperate type of variable

# * To indicate a constant we would declare a variable in capital letters

#

NAME = "Python Constant"

print("This is the initial constant value\n", NAME)

#

# ! NOTE the value can still be reassigned

# * However the rule is if the variable is capitalised DO NOT reassign value


# Constant Variable do not reassign with new value - do not change constant value

NAME = "New Value (EXAMPLE ONLY: Never update a constant!)"

print("This constant value has been updated\n", NAME)

#


# ! snake_case - Previously when working with JavaScript we have used camelCase

# ! to differentiate between the languages we will be using snake_case instead

# * Seperate variables with more than 1 word in their name with underscore

# * This follows python convention and also helps you not confuse PY with JS


#Snake case variable type declaration

multi_word_variable = "This is python"

print(multi_word_variable)

#Camel notation/case to create a variable 
camelVariable = "camelCase"
print(camelVariable)

firstNumber = 12
second_number = 10


# ! We will introduce Python specific data types later this week

# * For now lets look at ones we are familiar with

# * String - Series of characters contained in quote marks - single '' or double ""

#

string = "Characters between speech marks"

#

# * Integer - A whole number

#

integer = 5

#

# * Float - Decimal place number

# ! Text changes colour as a float is technically a class (advanced topic)


#

float = 1.5

#

# * Boolean - True or False

# ! Must start with a capital T or F

#

boolean = True

#


# ! By using 'type()' we can check the data type and in JavaSript it is typeof


#

print(type(string))

print(type(integer))

print(type(float))

print(type(boolean))

#


# ! fSTRING - Think of Template Literals/Strings in JavaScript

# * By passing 'f' before our string we are able to inject variable values

# * Simply wrap the variable in curlys '{}' and the value will take its place


#

day = "Monday"
date = "16/09/2024"
number = 1
float_variable = 12.6
myBool = True

print("Today is", day, "It is sunny")
print("Today is" + day + "It is the first working day")
print("Today is", day, "and it is" + str(number))

print(f"Today is {day}, {number} test {myBool} and it is {date} and float value = {float_variable}")

#


# Formatted Message - Signify End of Output

print(f"{format_output}---END---{format_reset}")


# ! STUDENT TASKS ! 

"""

Python Part 1a - Tasks:




1: Create a variable "name" and assign a string containing your first name as its value, then print the variable to the console.

name = "Jo";
print (name)


2: Update the value of your "name" variable to contain your full name. Create 2 more variables named "age" and "city" and assign them your age as a number and your city of residence as a string. Finally, print an f{string} to the console of a sentence containing
 the name, age and city information. eg: "My name is Dave, I'm 25 and live in London"

name = "Jo Atkins"
age = "44"
city = "Gloucester"

sentence = f"My name is {name}, I'm {age} and I live in {city}."
print(sentence)


3: Research the 'input()' function and utilise it to store a users name in a "user_name" variable.
## input function gets input from the user 

user_name = input("Please enter your name:")
user_age = input("Please enter your age:")
user_city = input("Please enter your city:")

print(f"Hello, my name is {user_name}, I am {user_age} years old, and I live in {user_city}.")




4: Utilise 'input()' to obtain a users age and city, then print an f{string} containing the user data, similar to Task 2.

user_name

print(f"Hello, my name is {user_name}, I am {user_age} years old, and I live in {user_city}.")


Stretch Tasks: 




1: Use input to obtain 2 numbers from a user, once obtained add the 2 numbers provided together and print the result to the console.
 
number1 = int(input("Please enter your first number"))
number2 = int(input("Please enter your second number"))

result = number1 + number2

print(f"The result of the sum is {result}")

#int () is integer - whole number
#float () is decimal


(TIP: Think about data types and type conversion...)


2: Research Python's built in methods and string methods. Experiment with them to familiarise yourself with what Python can do natively.

Built-In Methods (Functions): 

https://www.programiz.com/python-programming/methods/built-in


abs() - returns absolute value of a number 
i.e. 
number = -20
absolute_number = abs(number)
print(absolute_number)
# output: 20


all() - function returns True if all elements in the given iterable are truthy, If not return False

#check if all elements are true
result = all(boolean_list)
print(result)

#Output: True

any() - checks if any element of an iterable is True 
boolean_list = ['True', 'False', 'True']

# check if any element is true
result = any(boolean_list)
print(result)

# Output: True

ascii() - replaces non -printable character with its corresponding ascii value and returns it

text = 'Pythön is interesting'

# replace ö with its ascii value
print(ascii(text))    # Output: 'Pyth\xf6n is interesting' 

bin()
converts integer to binary string
The bin() method converts a specified integer number to its binary representation and returns it.

number = 15

# convert 15 to its binary equivalent 
print('The binary equivalent of 15 is', bin(number))

# Output: The binary equivalent of 15 is 0b1111

list() - creates a list in python
The list() constructor converts an iterable (dictionary, tuple, string etc.) to a list and returns it.

text = 'Python'

# convert string to list
text_list = list(text)
print(text_list)

# check type of text_list
print(type(text_list))

# Output: ['P', 'y', 't', 'h', 'o', 'n']
#         <class 'list'> 

len()
The len() function returns the length (the number of items) of an object.

languages = ['Python', 'Java', 'JavaScript']

length = len(languages)

print(length)  # Output: 3








String Methods (Functions): 

https://www.programiz.com/python-programming/methods/string


capitalize() Converts first character to Capital Letter

sentence = "i love PYTHON"

# converts first character to uppercase and others to lowercase
capitalized_string = sentence.capitalize()

print(capitalized_string)

# Output: I love python

count() - The count() method returns the number of occurrences of a substring in the given string.

message = 'python is popular programming language'

# number of occurrence of 'p'
print('Number of occurrence of p:', message.count('p'))

# Output: Number of occurrence of p: 4

find() - The find() method returns the index of first occurrence of the substring (if found). If not found, it returns -1.

message = 'Python is a fun programming language'

# check the index of 'fun'
print(message.find('fun'))

# Output: 12

format() - The format() reads the type of arguments passed to it and formats it according to the format codes defined in the string.





"""




and in part 1,  folder B, copy and paste this code below in a file called main.py.



