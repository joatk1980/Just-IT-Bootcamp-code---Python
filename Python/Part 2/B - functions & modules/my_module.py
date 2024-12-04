#Purposefully Create custom modules from my_modules.py and use it when you want 
#proof of concept modules usually have a lot more functionality in them

def func1():
    print("Hello")

def add(a,b):
    return a + b

def func2():
    name = input("Enter your name: ")
    return f"Hello {name}"

#only execute the function(s) if this file is run directly and prevent the automatic execution of functions when this file is imported into another file if the function(s) are not called - will only run from this page not if imported

#Will only call this code if calling it from the main file not importing and running it from another file - keeps control of your code and the module
if __name__ == "__main__"
    func1() 
    print(add(12,12)) #must call within a print statement


    add("My name is","Jo")

