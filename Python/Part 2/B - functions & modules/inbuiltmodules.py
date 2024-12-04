#used to import modules not readily available to us
#import the random module 

import random
#return random inteer in range [a,b] including both end points
random_number = random.randint(1,10)
print(random_number)

#import the random module and assign it an alias
import random as r 

#return random float values between 0-1 (decimals?)
random_float = r.random()
print(random_float)

test = r.choice()


#google whether python has a module to do what you want 