# write program that

# lets user type in integer that keeps calling collatz
# (convert input value to integer otherwise it will be string value)
#have it repeat function until it winds up as 1. - got this part to work

import sys

def collatz(number): 
    while number != 1:  
        if number % 2 == 0:
            number = number //2
        elif number % 2 == 1:
            number = 3 * number + 1
        print(number)   
try:
    collatz(int(input(' please enter positive or negative number:  ')))

except ValueError:
    print('Entry invalid. You must enter an integer')
except KeyboardInterrupt:
    sys.exit()