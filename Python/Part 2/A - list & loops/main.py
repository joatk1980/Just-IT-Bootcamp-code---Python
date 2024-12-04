This is Part 2 A

# Python Part 2a - Lists and Loops

# Formatting Variables

format_output = "\033[47m\033[30m"

format_reset = "\033[0m"

# Formatted Message - Signify Start of Output

print(f"{format_output}---START---{format_reset}")

# ! Lists

# * Lists in Python can be thought of like Arrays in JavaScript

# * Think of it as just a different name, the same principles apply:

# * Ordered, Indexed, Mutable, Allow Duplicates

# ? If you were to guess how would we create a list?

#

#index      0           1       2           3
languages = ["HTML", "CSS", "Javascript", "Python"] # collection - holds a list of multi items

language = "HTML" #holds a single item

#
# * Same as JavaScript just no variable declaration keyword as we have seen

# *
print(languages)

# ? How would we access an item in our list? Say we wanted to print "CSS"?

#remember index starts at 0

print(languages[0])
#to access index position 1
print(languages[1])
print(languages[2])
print(languages[3])
#
#will result in index error as out of rang
print(languages[4])
#

# * Remember the index starts from 0 NOT 1

# ! Negative Indexing

# * Python supports negative indexing meaning 'list[-1]' references the last item

#

print(f"\nUsing negative value(s) to access items in a list: {languages[-1]}")

print(languages[-1])

#

# ? With the last item being [-1] how would we access "HTML" using negative indexing?

#

print(f"\nUsing negative value(s) to access items in a list: {languages[-4]}")

#

# * Think of negative indexing like counting from right to left - starting from 1

# ! Updating / Changing List Items

# * We can amend list items by referencing an index and assigning a new value

# * Lets replace "Python" with "SQL"
#
print(f"\nOld list:{languages}")
languages[3] = "SQL"
print(f"\nUpdated list:{languages}")

#

# ! List Methods

# * As we have seen with Arrays, Lists also have methods

# RESOURCE: https://www.programiz.com/python-programming/methods/list

# ! Remove an Item

# * To remove an item from a list we can use 'remove()'

# * We pass an argument of the item we wish to remove NOT the index

# * If we wanted to remove "SQL" from our list we would do so with:
#

languages.remove("SQL")
print(f"\nRemoved and item from the list:{languages}")

# 

# * If the item cannot be found we receive an error

#
#Adds item to the end of the list 
languages.append("Python")
print(f"\nAppend an item to the list:{languages}")

# 
# ! Add / Append an Item

# * To add an item to the end of a list we can use 'append()'
# * We pass an argument of the item we wish to append
# * Lets add "Python" back to our list
#
#Insert item to a certain position in list
languages.insert(3, "SQL")
print(f"\nInsert an item to the list:{languages}")

#after a variable do a dot and it will give you your options i.e num.
#

num1= 10

# ! Familiarise yourself with the additional list methods

# * There will be an oppurtunity to experiment later on in the session

# ! Number of Items in a list

# * To find the number of items in a list in Python we have the 'len()' function
# * Think of it like the .length property in JavaScript
# * We pass the list name as an argument to the function
#

nums = [1,2,3,4,5,6,7,8,9,10]
print(f"{len(nums)}") #number of items from numbers list 
# result 10


print(f"{len(languages)}") #number of items from languages list
print(f"{len(language)}") #number of items from language string
print(f"{language[0]}")
print(f"{language[1]}")
print(f"{language[2]}")
print(f"{language[3]}")
#
#HTML
#result would be 4
#H
#T
#M
#L

# ! Loops

# * Python is no different than JavaScript or any other programming language
# * When we need to iterate over a sequence we use a loop

# ! For Loop - List

# * As mentioned earlier in the session a for loop in Python works the same as in JavaScript

# * The syntax however is more similar to a For of loop in JavaScript
# * Lets say we wanted to print our list of languages

#
#most efficient way to do this
for a_language in languages: 
   # a_language[0] = "HTML"
   # a_language[1] = "CSS"
   # a_language[2] = "Javascript"
   # a_language[3] = "SQL"
   # a_language[4] = "Python"
    print(a_language)

print(f"\nManually access each element/items from the list\n{languages}")
print(f"{languages[0]}")
print(f"{languages[1]}") 
print(f"{languages[2]}")
print(f"{languages[3]}") 
print(f"{languages[4]}")  
#
#

# ! REMEMBER 'i' is just a reference it could be anything

# * With a Python for loop we are not incrementing or checking against length
# * So our reference in this case 'i' does not hold a numeric value
# * It simply references the item in the list each iteration

#
for a_character in language:
    print(a_character)
# result H T M L

#
# ! For Loop - String

# * We can also iterate over a string
#

string = "Example"
#
# * Again our 'i' is simply a reference

for i in string:
    print(i)

#
#

# ! For Loop - Range

# * In Python if we wish to loop over a sequence of numbers we can use 'range()'

# * The number of iterations is defined by what we pass as an argument to the function

#
print("Range\n")
for aNumber in range(10):
    print(aNumber)

#
print("Range with a plus operator to get the actual value\n")
for aNumber in range(10):
    print(aNumber+1)

#investigate:range(start, stop[, step]) -> range object    

# * Remember we start our count from 0

# ? If I wanted to iterate from 1-5 rather than 0-4 how do we think we would do that?
#
#

# ! While Loop

# * We have seen these before, a loop that will repeat until a condition is met to end it

# ! Remember: No Autosave! 

# * Be mindful of infinite loops that will run forever if conditions are not met

# * Basic Example:
#

print("While loop with a start and stop value\n")
num = 1

#
while num <=5:
    print(num)
    num = num + 1
    # or
    #num+=1
#
# * Num starts at 1 is printed and increases by one each time until we reach 5

# ! Break Statement:

# * A 'break' statement allows us to terminate a loop immediately regardless of the condtition
# * Lets look at an example of a loop that will run until you tell it to "Stop"

#user_input =''
keep_looping = True


#while True:
while keep_looping:
    user_input = input("I will keep asking for input until you tell me to stop:").lower()

    #if user_input.lower() == "stop":
    if user_input == "stop":
            print(f"{user_input}\nI will stop")
            break #ends the loop if condition where value = stop is met

#user will need to type stop to end the loop
#

# ! STUDENT TASKS ! 

"""
Python Part 2a - Tasks:

1: Create your own examples of the following For Loops to familiarize yourself with the syntax:

- For Loop (List): Write a for loop that prints each item in a list

my_list = ["Cheese", "Bread", "Butter"]

for item in my_list:
    print(item)

#result 
# Cheese
# Bread
# Butter   


w3schools example:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#result
# apple
# banana
# cherry  

- For Loop (String): Write a for loop that prints each character in a string

my_string = "Hello"

for letter in my_string:
    print(letter)

#result
# H
# e
# l
# l
# o    


- For Loop with Range: Write a for loop that prints numbers 1 to 10 using the range function

The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number. (w3schools)

for num in range(1,11):
    print(num)

#this would print 1-10 as index starts at 0

#result
#1
#2
#3
#4
#5
#6
#7
#8
#9
#10


or 

x = range(6)
for n in x:
    print (n)

#result
# 0
# 1
# 2
# 3
# 4
# 5   


w3schools example:

thislist = ["apple", "banana", "cherry"] #defines list with 3 elements
for i in range(len(thislist)): #returns number of elements in this list, 3 #range generates seq of numbers starting from 0 up to not inc 3

    print(thislist[i]) #i takes the loop variable to take the values of 0,1,2 as the loop progresses #prints the element at position i

 #result
 # apple -- first iteration i=0 prints apple
 # banana -- i=1
 # cherry -- i=2   



2: Create your own examples of the following While Loops to familiarize yourself with the syntax and the 'break' and 'continue' keywords:




- Basic While Loop: Write a while loop that prints numbers from 1 to 10.

w3schools def: With the while loop we can execute a set of statements as long as a condition is true. -- Note: remember to increment i, or else the loop will continue forever.


#initialise variable
num = 1

#while loop to print numbers from 1 to 10
while num <= 10:
    print(num)
    num += 1 #increment num by 1 after each iteration

 #loop continues as long as num is less than or equal to 10
 # each iteration the current value of num is printed and num is then incremented by 1 num +=1

 #result
 1  
 2
 3
 4
 5
 6
 7
 8
 9
 10



- While Loop with Break: Implement a 'break' statement in a while loop that prints numbers from 1 to 10 and stops when it reaches 5.

w3schools def: With the break statement we can stop the loop even if the while condition is true

num = 1

#while loop to print numbers from 1 to 10, but stop at 5
while num <= 10:
    print(num)

    if num == 5:  #stop loop when num is 5
        break  #break statement terminates the loop

    num += 1  #increment num by 1


#result only numbers 1 to 5 would be printed    
#1
#2
#3
#4
#5




- While Loop with Continue: Research the 'continue' statement and implement it in a while loop that prints numbers from 1 to 10, but skips printing the number 5.

w3 schools def: The continue keyword is used to end the current iteration in a for loop (or a while loop), and continues to the next iteration.

num = 1

#while loop to print numbers from 1 to 10, but skip 5
while num <= 10:
    if num == 5:  #skip iteration when number is 5
        num += 1
        continue  #skip the rest of the loop for this iteration

    print(num)
    num += 1  #increment by 1

#result
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10    




https://www.programiz.com/python-programming/break-continue




3: Research list methods and experiment with them, putting together some example implemntations:

https://www.programiz.com/python-programming/methods/list

# w3schools:
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# append() - adds element to end of list 
fruits = ["apple", "orange", "kiwi"]
fruits.append("strawberry")
print(fruits)

#result ["apple", "orange", "kiwi", "strawberry"]


#insert() - adds element to specified position
            0       1           2
fruits = ["apple", "orange", "kiwi"]
fruits.insert(1, "strawberry")
print(fruits)

            0           1           2       3
#result:  ["apple", "strawberry", "orange", "kiwi"]
# inserts strawberry into position 1

remove() - Removes the first occurrence of an element.
fruits = ["apple", "strawberry", "orange", "kiwi"]
fruits.remove("strawberry")
print(fruits)

#result: ["apple", "orange", "kiwi"]

pop() - Removes and returns the element at the specified position (or the last element if no index is specified).
fruits = ["apple", "strawberry", "orange"]
fruits.pop(1)
print(fruits)

#result: ['apple', 'orange']

last_fruit = fruits.pop()  # Removes the last element
print(last_fruit)  

#result: 'orange'

clear() - Removes all elements from the list.
fruits = ["apple", "strawberry", "orange"]
fruits.clear()
print(fruits)
# result: []

index() - Returns the index of the first occurrence of an element.

            0           1              2
fruits = ["apple", "strawberry", "orange"]
index_of_cherry = fruits.index("orange")
print(index_of_orange)
# Output: 2

count() - Returns the number of occurrences of an element in the list.

fruits = ["apple", "banana", "cherry", "apple"]
apple_count = fruits.count("apple")
print(apple_count)
# result: 2

sort() - Sorts the list in ascending order.

numbers = [3, 1, 4, 1, 5, 9]
numbers.sort()
print(numbers)
# result: [1, 1, 3, 4, 5, 9]


Stretch Task: 

Guess the Number: Store a number between 1 and 10 in a variable. Write a while loop that asks the user to input a guess, the game should continue until the user inputs a correct guess.

num = 7  #number user needs to guess 
keep_looping = True  ##loop continues to run as long as variable remains True

while keep_looping:
    user_input = int(input("Please enter number guess between 1-10:"))  #convert input to an integer
    if user_input == 7:
        print(f"{user_input}\nloop stopped")
        break

#starts while loop which runs contiuosly as keep_looping set to True and keeps repeating until break statement encountered
# int converts user input (as string) into an integer and stored in user_input variable
# checks if user_input matches the variable 
# if correct guess made then the 'if' block executes and break statement breaks the loop and exit it immediately - if guess not correct loop goes around again and asks user for another input 








"""
