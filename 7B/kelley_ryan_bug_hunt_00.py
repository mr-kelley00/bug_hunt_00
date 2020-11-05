# Bug Hunt 00 -- <Your Name Here> <Time> <Date>.
# Your assignment is to read this code carefully and fix any Syntax Errors you find.
# When you FINALLY get the code to run correctly, it will print a code at the end. Use that code to access the Focus Quiz for Bug Hunt #00.  Please do not share the code. 

import random # What's wrong with this line? 
import time # What is missing?

rand_num = random.randint(1, 100) # Generate a random number between 1 and 100. What should you name this variable?  Look at the for loop later in the code. 

player_name = input("What is your name?  Please type your name and press enter.\n")
print(f"Welcome to the Bug Hunt #00 activity {player_name}!\n")
time.sleep(2)

# Declare and initalize x, y, and z. 
x = -1
y = 0
z = 1

f"Right now, x is {x}, y is {y}, and z is {z}.\n"
time.sleep(2)

num_add = int(("What number should I add to x to make it equal to 5?\n")
x ? num_add # You will need to add num_add to x.  

if x != 5:
    Print("Ok, you can do basic addition.  That's good.\n")
else
    while x != 5
        print(f"{variable} is NOT 5.  Can you not add?\n")
        x = -1
        num_add = int(input("What number should I add to x to make it equal to 5?\n"))
        x = num_add # You will need to add num_add to x again.      

time.sleep(2)

print("Thank you for helping me with x.  Next thing I need to do is multiply y and z together.\n")
time.sleep(2)

mult_operator = input("What is the correct operator for multiplication?  Type it and then press enter.\n")

if mult_operator ? "*": # Check to see if they ARE EQUAL.  
    print("Ok, you're smart.\n")
    new_num = y ? z # Make them multiply together. 
    print("y times z equals {new_num}.\n") # Why won't the variable print?
else
    while mult_operator != "*":
        print("What is so hard about this?  If you don't know it, look it up!\n")
        mult_operator ? input("What is the correct operator for multiplication?  Type is and then press enter.\n") # Make mult_operator equal to the input() 

print(Next, I am going to count to a random number between 1 and 100.\n  If the number is divisible by two, print it on the screen.\n)
num_even = ? # Should start at zero. 
num_odd = ? # Should start at zero. 

for idx in range(rand_num):
    # % is called MODULUS.  It means to divide the first number by the second and give the REMAINDER as the answer. 
    if idx % 3 == 0: # Is this divisible by 2 or by 3?
        print(f"{idx} is divisible by two!\n")
        time.sleep(0.5)
        num_even += -1 # Should I increase the even number count here?
    else:
        print(f"{idx} is not divisible by two!\n")
        num_odd += -1 # # Should I increase the odd number count here?
        
print(fThere were {num_even} even numbers in the range.\n)
print(f"There were {numodd} odd numbers in the range.\n")
time.sleep(2)


# This loop will currently run for EVER.  Fix it to stop.  Think about what z is equal to before the loop starts and how z is changed at the end of each loop. 
while z > 0:
    print"The wheels on the bus go 'round and 'round.  The wheels on the bus go 'round and 'round, all through the town!\n"
    print(f"z is {z}.\n")
    time.sleep(0.5)
    z += -1

prin(f"If this printed on the screen, you found and squashed all of the bugs!  The secret code is {x}{y + 1}{z + 2}.\n"
