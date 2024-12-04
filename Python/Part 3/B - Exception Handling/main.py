This is Part 3B

# Python Part 3B - Exception Handling

# Formatting Variables

format_output = "\033[47m\033[30m"

format_reset = "\033[0m"

# Formatted Message - Signify Start of Output

print(f"{format_output}---START---{format_reset}")

# ! Built-In Exceptions:

# * Exceptions are basically errors
# * Python has some built-in error detection that we can make use of

# * Lets look at the example from the presentation
# * We want to write a function that takes 2 numbers from the user and divides...
# * ... the first number by the second number

#
def divide_1():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {round(result)}") #round number
    print(f"The result of {num1} divided by {num2} is: {result}") #dont round number

#
# * On a basic level this function works fine
#

divide_1()

#
#ZeroDivisionError

# * But if we test it's robustness we can easily break it
# * Lets say someone passes a character that is not a number
# * Or if someone tries to divide by '0'




#

# divide_1()

#




# * We can handle this error with exceptions

# ! try...except Block:

# * 'try:' is followed by the code we would like to run

# * 'except:' must follow try as this is how we handle our exceptions

# * Think of the except block like a conditional

# * If there is an error, we need to do this

def divide_2():
    try: #try is followed by the code we would like to run
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is: {round(result)}") #round number
        print(f"The result of {num1} divided by {num2} is: {result}") #dont round number

#Allows us to handle any unforseen errors (and python inbuilt errors) and return a useful error message
    except  ZeroDivisionError:
        print("You attempted to divide by zero")



# ! ValueError

# * In this case the exception we're checking for is "ValueError"

# * When we encounter an invalid value we can return an error message 

  except ValueError:
        print("You must enter an Integer Value")  



# ! ZeroDivisionError:

# * When user tries to divide by zero we can handle this error
def divide_2():
    try: #try is followed by the code we would like to run
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is: {round(result)}") #round number
        print(f"The result of {num1} divided by {num2} is: {result}") #dont round number

#Allows us to handle any unforseen errors (and python inbuilt errors) and return a useful error message
    except  ZeroDivisionError:
        print("You attempted to divide by zero")



# ! except Exception:

# * Allows us to handle any unforseen errors and return a useful error message
try: #try is followed by the code we would like to run
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is: {round(result)}") #round number
        print(f"The result of {num1} divided by {num2} is: {result}") #dont round number

#Allows us to handle any unforseen errors (and python inbuilt errors) and return a useful error message
    except  ZeroDivisionError:
        print("You attempted to divide by zero")

    except ValueError:
        print("You must enter an Integer Value")  

    except Exception as e:
        print(f"An error has occurred: {e}")


# ! Finally:

# * Our finally block runs regardless of whether or not an error occurs

# * Finally blocks are useful for running cleanup actions such as disconnecting from a server
#
def divide_2():
    try: #try is followed by the code we would like to run
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is: {round(result)}") #round number
        print(f"The result of {num1} divided by {num2} is: {result}") #dont round number

#Allows us to handle any unforseen errors (and python inbuilt errors) and return a useful error message
    except  ZeroDivisionError:
        print("You attempted to divide by zero")

    except ValueError:
        print("You must enter an Integer Value")  

    except Exception as e:
        print(f"An error has occurred: {e}") #the system will then tell you the system error - we can put this if we aren't sure what error is going to come up, not specific to any error.   Exception is baseline error for all errors on system. Deal with error if know it specifically or use if Exception if unsure, but could then tailor error handling based on what errors come up

    finally:
        print("Operation completed")   #last block to show operation has worked and that this is the last block run 

#error handling stops programme from breaking             

#
divide_2()
#




#




# ! STUDENT TASK:




# * Python Exceptions - Music Playlist Task Extension (PDF Brief)






# Formatted Message - Signify Start of Output

print(f"{format_output}---END---{format_reset}")
