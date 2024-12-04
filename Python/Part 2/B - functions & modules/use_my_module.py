#can write code in another file in vscode and then look to import this - i.e my_module and import this code 

#import and use custom modules from file my_module

import my_module
import random

myAdd = my_module.add(100,200)
print(myAdd)


print(my_module.add(5,12))
#need to add parameters otherwise you will get an error


my_module.func1() #do not call inside a print statement as called directly 

#print(f"This {greetings} is from my_module")

my_module.func1()