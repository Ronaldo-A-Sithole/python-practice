#global variables
z= "I am Ronaldo Alberto Sithole"

def my_function2():
    global z
    z = "I am a Python programmer"  
    print(z)


"""Python does not have a random() function to make a random number, 
but Python has a built-in module called random that can be used to make random numbers"""

import random
print(random.randint(1, 100))  # This will print a random integer between 1 and 100 (inclusive).