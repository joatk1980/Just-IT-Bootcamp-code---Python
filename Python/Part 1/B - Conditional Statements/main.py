# Python Part 1B - Conditional Statements

# Formatting Variables

format_output = "\033[47m\033[30m"

format_reset = "\033[0m"


# Formatted Message - Signify Start of Output

print(f"{format_output}---START---{format_reset}")


# ! Operators:

# * Before we look at some examples we need to be aware of operators

# * Again the concept is the same as we have seen in JavaScript

# * Most operators in Python are syntactically similar to JavaScript


# ! We have 4 main types of operator to consider:

# * Mathematical Operators - (+, -, *, / etc...)

# * Assignment Operators - (=, +=, -= etc...)

# * Comparison Operators - (==, !=, >, <, >=, <=)

# * Logical Operators - (and, or, not, |)

# TODO: Full List of Operators:

# https://www.programiz.com/python-programming/operators


# ! If Statement:

# * As we have seen previously in JavaScript, an If Statement executes a block of code if a condition is met


# * Example: An If Statement to check if a number is greater than 100

#
num2 = 89 #int(input("Enter a value:"))
num3 = 200
num = 101
# if num > num2: # 100:
#     print(f"{num} is greater than {num2}")
# else:
#     print(f"{num2} is greater than {num}")

#
if num > num2 or num < num3: # 100:
    print(f"{num} is greater than {num2} but less than {num3}")
elif num>= num3 and num <= 450:
    print(f"{num} is greater than {num3} but less than or equal to 450")
else:
    print(f"Some value")

    print(not(num==10))
    print(num != )


# ! Syntax: Very Similar to JavaScript
# ? What differences do you notice?
# * No (parentheses) around our condition
# * Colon ':' after our condition
# * Body of statement is indented rather than wrapped in {curly's}




# ! Indentation: is VERY important in Python

# * Think of it the same as {curly's} around a code block

# * It indicates that the code belongs together


# ! If Else Statement:

# ? If we wanted to an 'else' block to our example how would we do it?

#

score = int(input("Enter score: "))

if score- > 100 or score <0:
    #create a variable called grade and assign it a value "invalid Entry"
    grade = "Invalid Entry"

elif score>75 and score <=100:
    #reassign grade variable with new value
    grade = "A"

elif score >=60 and score <=74:
    grade = "B"

elif score >=50 and score <=59:
    grade = "C"

else:
    grade = "U"

print(f"You have scored {score} and your grade is {grade}")                

#


# ! Remember indentation - 'else' should be on the same level as 'if'

# * Colon ':' after our 'else'

# * Followed by our indented 'else' block




# ! If Elif Else Statement:

# * Working with an 'else if' block in Python has one main difference to note

# * Rather than adding an 'else if' block the syntax is 'elif' to reduce characters

#

num = 11
#

password = "python"
user_name = "coder21"

your_user_name = input("Enter your username:")
your_password =  input("Enter your password:")


if user_name == your_user_name and password == your_password:
    print(f"Welcome {your_user_name}")

elif user_name != your_user_name and password == your_password:
     print(f"Sorry your username {your_user_name} is invalid") 

elif user_name == your_user_name and password != your_password:
     print(f"Sorry your password {your_password} is invalid")     

else: 
     print(f"Sorry your username {your_user_name} and /or password {your_password} is invalid")   


#nesting - block of code in block of code - this is if statement in and if statement

userpass = "pass"

if user_name == "pass":
    user_age = int(input("Enter your age"))
    if user_age == 21:
        print(f"You have provided a valid user pass {user_pass} and you have met the age requirement {user_age}")
    else:
        print(f"You have provided a valid user pass {user_pass} but failed to meet the age requirement {user_age}")    
else:
    print("Invalid user pass provided")    
#

# ! Remember indentation - 'elif' should be on the same level as 'if' and 'else'

# * Colon ':' after our 'elif' condition

# * Followed by our indented 'elif' block




# ! Match Statement:

# * A Match is the equivalent to a Switch statement in JavaScipt

# * Useful for more complex comparisons or checking against multiple cases


# * An Example Match Statement to check the day of the week and print a related message

#

day = "Monday"

match day:
    case "Monday":
        print("Start of the work week")
    case "Friday":
        print("End of the work week") 
    case "Saturday" | "Sunday":
        print("Its the weekend") 
    case _:
         print("A day in the week")        


#
# case is basically the conditions you meet or dont meet 
# case _  -the underscore picks up anything else - wildcard 


# ! Remember indentation 

# * We use Match rather than Switch

# * We also don't need any 'break' keyword

# ! NOTE: The default case is represented by '_'



# Formatted Message - Signify Start of Output

print(f"{format_output}---END---{format_reset}")


# ! STUDENT TASKS ! 

"""

Python  Python Part 1B - Tasks:

1: Create your own examples of the following Condtional Statements to famliarise yourself with the syntax:


- If Statement

age = 18

if age >= 18:
    print("Your are an adult.")

- If/Else Statement

age = 18

if age = 18:
    print("You are an adult.")
else:
    print("You are a minor.")    

- If/Elif/Else Statement

age = 16

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are underage.")   
else:
    print("You are a minor")     



- Match Statement

error_code = 150

match error_code:
        case 150:
            print("User error")
        case 175:
            print("Error not found")  
        case 190:
            print("Server error")   
        case _:  
            print("Unknown Status code")     


# case_  - catches any values that dont match the other cases 
# The match statement is great for simplifying complex if-elif-else structures when checking for multiple conditions.


2: Research the 'and' and 'or' operators in Python and put together some example implementations using multiple conditions.


## and and or operators are used to combine conditional statements

'and' - both conditions must be true for the whole expression to be true

'or' - at least one condition must be true for the whole expression to be true

##example of 'and'

age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive")
else:
    print("You cannot drive")

#if - both conditions are true i.e age equal to or above 18 and has a license then they can drive, if not then they cannot drive  


##example of 'or'

day = "Saturday"
is_weekend = True

if day == "Saturday" or is_weekend:
    print("Stay in bed")
else:
    print("Get up lazy bones!") 


##combine 'and' and 'or'

age = 20
has_license = False
an_emergency = True

if (age >= 18 and has_license) or an_emergency:
    print("You can drive in this situation.")
else:
    print("You cannot drive.")


3: Research and create a 'Nested If Statement' to check whether a number is 'positive' or 'negative' and print the result to the console, the statement should also account for the possibility of the number being '0'.

number = float(input("Enter a number: "))

if number >= 0:   ##outer if statement
    if number == 0: ##Inner if statement
        print("Number is zero")
    else:
        print("The number is positive")
else:
        print("The number is negative")    

##outer if statement checks if the number is greater than or equal to zero
# if it is then the inner if checks that the number is exactly zero and prints "The number is zero"
# Otherwise it prints "The number is positive"            


4: Utilise 'input()' to obtain a students test-score (0-100), using a conditional statement assign the the student with the appropriate grade and print the result the conosle:

score = int(input("Enter your test score: "))

if score > 100 or score < 0:
    print("Invalid score. Please enter a score between 0 and 100.")
else:
    if score >= 90 and score <= 100:
        grade = "A"
    elif score >= 80 and score <= 89:
        grade = "B"
    elif score >= 70 and score <= 79:
        grade = "C"
    elif score >= 60 and score <= 69:
        grade = "D"
    else:
        grade = "F"

    print(f"You have scored {score} and your grade is {grade}")

      




- 90-100: "A"

- 80-89: "B"

- 70-79: "C"

- 60-69: "D"

- 00-59: "F"


Stretch Task: 




If you manage to complete all of the relevant tasks, feel free to experiment with further implementations or do some pre-reading on Lists and Loops in Python ahead of tomorrow's session.






"""