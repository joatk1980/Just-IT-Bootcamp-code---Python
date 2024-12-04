This is Part 3A

# Python Part 3a - Tuples, Sets, Dictionaries
# Formatting Variables

format_output = "\033[47m\033[30m"

format_reset = "\033[0m"

# Formatted Message - Signify Start of Output

print(f"{format_output}---START---{format_reset}")

# ! Tuple:

# * Think of a Tuple like a set list that cannot be changed (immutable)

# * Syntax wise just replace the square brackets with parentheses
#
            0           1       2           3           4
fruits = ("apple", "orange", "strawberry", "grapes", "banana")

#
# * If we print the Tuple you will see it looks very similar to a list
# Tuples are faster to use than a list 
# Write protected and cannot be changed (data structure that doesnt need to be changed)

#
print(fruits)
#

# ! Tuple: Order
# * Like a list each item is indexed
# ? With what we know about lists how would we print "Orange"?

#
print(fruits[0])
print(fruits[1])
print(fruits[2])
#

# * The order of items in our Tuple cannot be changed, neither can the data itself
#

fruits[1] = "Mango"
print(fruits) 
#this will throw an error as you cannot update tuple

#

# ! Trying to update a Tuple:
# * If we try to update our Tuple, we get an error
# * To access the length of the tuple we can use len()

#

print(f"The number of items in our tuple {len(fruits)}") #will return length of items

# 

# ! Iterating over a Tuple:

# ? How do we think we would iterate over a tuple?

# * We can use a for loop #everything that has a beginning and an end - i.e a number of items - iterate/loop over items inside a tuple data structure
#
for a_fruit in fruits:
    print(a_fruit)
#
# * Tuples are most useful for read-only data
# * We can also store Tuples in Sets and Dictionaries


# ! Set:
# * A Set is an unordered collection of unique elements
# * Syntax wise it is similar to a Tuple but with {curly's}
# opposite of tuple and list as unordered and removes duplicate values 

#fruits = ("apple", "orange", "strawberry", "grapes", "banana", "orange")
#

days_of_week = {"mon", "tues", "wed", "thur", "fri", "sat", "sun"}
#
# * Lets print our set
print(days_of_week)

# will print items in random order 
# use it to get rid of duplicate values 


# * Notice how our order of our set is not how as we defined
# * If run our code a few more times we will see the order changes
# * This is because a set is unordered


# ! Sets with duplicate values:
# * Sets do not allow duplicate data
# * For example lets add another "Monday" to the end of our set and print it
#
print()

#
# * Notice that only one instance of "Monday" is included
# * This is because a set will automatically remove duplicates


# ! Set: Intersection, Difference and Union: 

# * To demonstrate futher functionality with sets lets make another

# * We will create a Set named 'weekend'

# * We will also remove our duplicate

days_of_week = {"mon", "tues", "wed", "thur", "fri", "sat", "sun"}
weekend = {"sat", "sun"}

print(f"Common days: {days_of_week.intersection(weekend)}") #brings back common days in both sets

#

# ! Set: Intersection:

# * When working with multiple sets we can find common elements
# * This is known as the intersection of the sets
# * Lets look for the intersection of our examples
# * We do this by referncing one of our sets and using 'intersection()'
# * The argument we pass to this method is the set we want to compare
#

print(days_of_week & weekend)

#

# * Notice that our result is "Saturday" and "Sunday"
# * The alternate syntax for this an ampersand '&'
# * We place the '&' between the sets we want the intersection of

#
print(f"The week {days_of_week}")
print(f"The weekend {weekend}")

#

# ! Set: Difference:
# * The opposite of an intersection is a difference
# * This returns us the elements NOT present in both sets
# * Using the same idea we can replace the 'intersection()' method...
# * ...with the 'difference()' method
#

print(f"Days not in the week: {days_of_week.difference(weekend)}")

#
# * Alternatively we can replace the '&' with '-'

print(days_of_week - weekend)

days_of_weeks = {"mon", "tues", "wed", "thur", "fri"}
weekend = {"sat", "sun", "mon"}

print(f"Days not in the weekend: {weekend.difference(days_of_weeks)}")
# first argument is being called and looked at first i.e. weekend is looked at first 

# ! Set: Union:
# * If we wanted to merge two sets we can use the 'union()' method
# * Or use the single bar '|' between the two sets
#
print(f"The entire week: {days_of_week.union(weekend)}")
week = days_of_week | weekend
print(week)
#

# ! STUDENT TASK:

# * Python Dictionaries - Music Playlist Task (PDF Brief)


# Formatted Message - Signify Start of Output

print(f"{format_output}---END---{format_reset}")


 
