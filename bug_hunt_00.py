# Bug Hunt 00 -- <Your Name Here> <Time> <Date>.
# Your assignment is to read this code carefully and fix any Syntax Errors you find.

import random
import time

rand_num = random.randint(1, 100) # Generate a random number between 1 and 100.  

player_name = input("What is your name?  Please type your name and press enter.\n")
print(f"Welcome to the Bug Hunt #00 activity {player_name}!\n")
time.sleep(2)

# Declare and initalize x, y, and z. 
x = -1
y = 0
z = 1

print(f"Right now, x is {x}, y is {y}, and z is {z}.\n")
time.sleep(2)

num_add = int(input("What number should I add to x to make it equal to 5?\n"))
x += num_add

if x == 5:
    print("Ok, you can do basic addition.  That's good.\n")
else:
    while x != 5:
        print(f"{x} is NOT 5.  Can you not add?\n")
        x = -1
        num_add = int(input("What number should I add to x to make it equal to 5?\n"))
        x += num_add    
time.sleep(2)

print("Thank you for helping me with x.  Next thing I need to do is multiply y and z together.\n")
time.sleep(2)

mult_operator = input("What is the correct operator for multiplication?\n")
