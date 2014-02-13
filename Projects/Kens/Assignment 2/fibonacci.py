# Assignment 2: Write a Python script that generates the nth sequence
# of the Fibonacci numbers. The script will take exactly one command
# line argument for n.
# filename : fibonacci.py
# Author: Garth
import sys
# Things to do:
#   First: dummy guard. Cant allow input that is not a non-negative digit.as
#   Next: Ask for input if they enter something funky at the command line
#

get_number = int(sys.argv[1])# Grab your argument
is_int = type(get_number)

#if get_number == ""
   # print("This script requires a single non negative digit. Please try again")
    #exit()
#else

if  is_int != int:
    print("This script requires a single non negative digit. Please try again")
    exit()
# need to add devinsive coding


fib_numbers = [0,1] # create a list
    if get_number == 1:
    return 1
    else get_number == 0:
        return 0

for i in range(get_number): #just learned range! It gives me all the numbers!
    # Grab the index i and the next index (i + 1) and add those beezys!
    fib_numbers.append(fib_numbers[i] + fib_numbers[i+1])
print fib_numbers #print the list!
