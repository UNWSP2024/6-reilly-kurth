#Reilly Kurth
#2/28/2025

import random

#set min and max


def randDice():
    #get first and second number
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    print("The first dice is", roll1)
    print("The second dice is", roll2)
    # find sum
    return roll1  + roll2

#display end result
rollsadded = randDice()
print("The total of your dice rolls is", rollsadded)