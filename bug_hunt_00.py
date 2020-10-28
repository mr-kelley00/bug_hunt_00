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

mult_operator = input("What is the correct operator for multiplication?  Type it and then press enter.\n")

if mult_operator == "*":
    print("Ok, you're smart.\n")
    new_num = y * z
    print(f"y times z equals {new_num}.\n")
else:
    while mult_operator != "*":
        print("What is so hard about this?  If you don't know it, look it up!\n")
        mult_operator = input("What is the correct operator for multiplication?  Type is and then press enter.\n")

print("Next, I am going to count to a random number between 1 and 100.\n  If the number is divisible by two, print it on the screen.\n")
num_even = 0
num_odd = 0

for idx in range(random.randint(1, 100)):
    if idx % 2 == 0:
        print(f"{idx} is divisible by two!\n")
        time.sleep(0.5)
        num_even += 1
    else:
        print(f"{idx} is not divisible by two!\n")
        num_odd += 1
        
print(f"There were {num_even} even numbers in the range.\n")
print(f"There were {num_odd} odd numbers in the range.\n")
time.sleep(2)

while z > 0:
    print("The wheels on the bus go 'round and 'round.  The wheels on the bus go 'round and 'round, all through the town!\n")
    print(f"z is {z}.\n")
    time.sleep(0.5)
    z += -1

print(f"If this printed on the screen, you found and squashed all of the bugs!  The secret code is {x}{y + 1}{z + 2}.\n")
